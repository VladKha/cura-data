"""Gradio demo for running data error detection."""
import re
import time
import json
from typing import Any
from urllib.parse import urljoin, urlparse

import gradio as gr
import requests
from bs4 import BeautifulSoup, NavigableString

from advanced_w_instructor import find_wikipedia_errors_advanced_2


def download_web_page(url):
    """
    Download any web page and return both the HTML and parsed soup.
    """
    try:
        # Validate URL
        if not url.startswith(('http://', 'https://')):
            return None, "<p style='color: red;'>Please enter a valid URL starting with http:// or https://</p>"

        # Download the page
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Parse with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Get the base URL for resolving relative links
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

        # Fix all relative URLs to absolute URLs
        for tag in soup.find_all(['a', 'link'], href=True):
            tag['href'] = urljoin(url, tag['href'])

        for tag in soup.find_all(['img', 'script'], src=True):
            tag['src'] = urljoin(url, tag['src'])

        for tag in soup.find_all(['source', 'video', 'audio', 'embed'], src=True):
            tag['src'] = urljoin(url, tag['src'])

        # Fix srcset attributes for responsive images
        for tag in soup.find_all(srcset=True):
            srcset_parts = []
            for part in tag['srcset'].split(','):
                part = part.strip()
                if part:
                    url_part = part.split()[0]
                    rest = ' '.join(part.split()[1:])
                    absolute_url = urljoin(url, url_part)
                    srcset_parts.append(f"{absolute_url} {rest}".strip())
            tag['srcset'] = ', '.join(srcset_parts)

        # Add base tag to help with any remaining relative URLs
        if soup.head:
            base_tag = soup.new_tag('base', href=url)
            soup.head.insert(0, base_tag)

        # Add custom style to ensure good visibility
        if soup.head:
            style_tag = soup.new_tag('style')
            style_tag.string = """
                body {
                    background-color: white !important;
                    color: black !important;
                    margin: 0;
                    padding: 0;
                }
            """
            soup.head.append(style_tag)

        return soup, None

    except requests.Timeout:
        return None, "<p style='color: red;'>Error: Request timed out. The page took too long to load.</p>"
    except requests.RequestException as e:
        return None, f"<p style='color: red;'>Error downloading page: {str(e)}</p>"
    except Exception as e:
        return None, f"<p style='color: red;'>Error processing page: {str(e)}</p>"


def soup_to_iframe(soup):
    """Convert BeautifulSoup object to iframe HTML."""
    import html
    import time
    full_html = str(soup)

    # Add cache buster
    cache_buster = f"<!-- Updated: {time.time()} -->"
    full_html = cache_buster + full_html

    # Properly escape for srcdoc
    escaped_html = html.escape(full_html, quote=True)

    iframe_html = f'''
    <iframe 
        srcdoc="{escaped_html}" 
        style="width: 100%; height: 800px; border: 1px solid #ccc;" 
        sandbox="allow-same-origin allow-scripts"
        key="{time.time()}"
    ></iframe>
    '''
    return iframe_html


def inject_styles_and_script(soup):
    """Inject error highlighting styles and tooltip script into the soup object."""
    style_block = """
.error-highlight {
    position: relative;
    background-color: rgba(255, 87, 87, 0.3) !important;
    color: inherit !important;
    text-decoration: none !important;
    border-bottom: 2px solid rgba(220, 20, 60, 0.9) !important;
    cursor: help !important;
    transition: background-color 0.2s ease;
    padding: 2px 4px;
    border-radius: 3px;
    display: inline !important;
}
.error-highlight:hover,
.error-highlight:focus {
    background-color: rgba(255, 87, 87, 0.6) !important;
}

/* Tooltip styles */
#error-tooltip-container {
    display: none;
    position: fixed;
    z-index: 10000;
    background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
    border: 2px solid #dc3545;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
    max-width: 500px;
    min-width: 350px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    font-size: 14px;
    line-height: 1.6;
    color: #212529;
    pointer-events: none;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
}

.tooltip-header {
    font-size: 16px;
    font-weight: 700;
    color: #dc3545;
    margin-bottom: 16px;
    padding-bottom: 12px;
    border-bottom: 2px solid #fee;
    display: flex;
    align-items: center;
    gap: 8px;
}

.tooltip-header::before {
    content: "⚠️";
    font-size: 20px;
}

.tooltip-section {
    margin-bottom: 16px;
}

.tooltip-section:last-child {
    margin-bottom: 0;
}

.tooltip-label {
    font-weight: 700;
    color: #495057;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
    display: block;
}

.tooltip-content {
    color: #212529;
    background: #f8f9fa;
    padding: 10px 12px;
    border-radius: 6px;
    border-left: 3px solid #dc3545;
}

.tooltip-content div {
    margin: 4px 0;
}

.tooltip-fix {
    background: #d4edda;
    border-left-color: #28a745;
    color: #155724;
    font-weight: 500;
}

.tooltip-references {
    margin-top: 8px;
}

.tooltip-references a {
    display: block;
    color: #007bff;
    text-decoration: none;
    padding: 6px 10px;
    margin: 4px 0;
    background: #e7f3ff;
    border-radius: 4px;
    font-size: 12px;
    word-break: break-all;
}

.tooltip-references a:hover {
    background: #cce5ff;
    text-decoration: underline;
}

.tooltip-references a::before {
    content: "🔗 ";
    margin-right: 4px;
}
"""

    script_block = """
(function() {
    console.log('Tooltip script loaded');
    
    // Function to initialize everything
    function init() {
        console.log('Initializing tooltips');
        
        // Create tooltip container
        var tooltipContainer = document.createElement('div');
        tooltipContainer.id = 'error-tooltip-container';
        document.body.appendChild(tooltipContainer);
        console.log('Tooltip container created');
        
        // Add event listeners to all error highlights
        var highlights = document.querySelectorAll('.error-highlight');
        console.log('Found ' + highlights.length + ' highlights');
        
        highlights.forEach(function(highlight) {
            highlight.addEventListener('mouseenter', function() {
                console.log('Mouse entered highlight');
                var errorDataStr = this.getAttribute('data-error');
                if (errorDataStr) {
                    try {
                        var errorData = JSON.parse(errorDataStr);
                        showTooltip(errorData, tooltipContainer);
                    } catch(e) {
                        console.error('Error parsing JSON:', e);
                    }
                }
            });
            
            highlight.addEventListener('mouseleave', function() {
                hideTooltip(tooltipContainer);
            });
        });
    }
    
    function showTooltip(errorData, container) {
        console.log('Showing tooltip', errorData);
        var html = '<div class="tooltip-header">' + escapeHtml(errorData.error_short_summary || 'Error') + '</div>';
        
        if (errorData.why_wrong) {
            html += '<div class="tooltip-section">';
            html += '<span class="tooltip-label">Why it\\'s wrong</span>';
            html += '<div class="tooltip-content">';
            var lines = errorData.why_wrong.split('\\n');
            lines.forEach(function(line) {
                line = line.trim().replace(/^[-•]\\s*/, '');
                if (line) {
                    html += '<div>' + escapeHtml(line) + '</div>';
                }
            });
            html += '</div></div>';
        }
        
        if (errorData.suggested_fix) {
            html += '<div class="tooltip-section">';
            html += '<span class="tooltip-label">Suggested Fix</span>';
            html += '<div class="tooltip-content tooltip-fix">' + escapeHtml(errorData.suggested_fix) + '</div>';
            html += '</div>';
        }
        
        if (errorData.references && errorData.references.length > 0) {
            html += '<div class="tooltip-section">';
            html += '<span class="tooltip-label">References</span>';
            html += '<div class="tooltip-references">';
            errorData.references.forEach(function(ref) {
                html += '<a href="' + escapeHtml(ref) + '" target="_blank" rel="noopener noreferrer">' + escapeHtml(ref) + '</a>';
            });
            html += '</div></div>';
        }
        
        container.innerHTML = html;
        container.style.display = 'block';
    }
    
    function hideTooltip(container) {
        container.style.display = 'none';
    }
    
    function escapeHtml(text) {
        var div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
    
    // Wait for body to exist
    if (document.body) {
        init();
    } else if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        // Fallback: wait a bit and try again
        setTimeout(init, 100);
    }
})();
"""

    if soup.head:
        style_tag = soup.new_tag('style')
        style_tag.string = style_block
        soup.head.append(style_tag)

        script_tag = soup.new_tag('script')
        script_tag.string = script_block
        soup.head.append(script_tag)
    else:
        # If no head, create one
        head = soup.new_tag('head')
        style_tag = soup.new_tag('style')
        style_tag.string = style_block
        head.append(style_tag)

        script_tag = soup.new_tag('script')
        script_tag.string = script_block
        head.append(script_tag)

        if soup.html:
            soup.html.insert(0, head)


def wrap_text_in_element(element, start_idx, end_idx, wrapper_tag, soup):
    """
    Wrap text from start_idx to end_idx within an element's text content.
    This handles text that may span multiple child nodes.
    """
    current_pos = 0
    nodes_to_process = []

    # Collect all text-containing children
    for child in element.descendants:
        if isinstance(child, NavigableString) and child.parent.name not in ['script', 'style']:
            text_len = len(str(child))
            nodes_to_process.append({
                'node': child,
                'start': current_pos,
                'end': current_pos + text_len,
                'text': str(child)
            })
            current_pos += text_len

    # Find which nodes overlap with our target range
    affected_nodes = []
    for node_info in nodes_to_process:
        if node_info['end'] > start_idx and node_info['start'] < end_idx:
            affected_nodes.append(node_info)

    if not affected_nodes:
        return False

    # If it's a single node, do simple replacement
    if len(affected_nodes) == 1:
        node_info = affected_nodes[0]
        node = node_info['node']
        text = node_info['text']

        local_start = start_idx - node_info['start']
        local_end = end_idx - node_info['start']

        before = text[:local_start]
        matched = text[local_start:local_end]
        after = text[local_end:]

        # Insert elements in order
        if before:
            node.insert_before(NavigableString(before))

        node.insert_before(wrapper_tag)
        wrapper_tag.string = matched

        if after:
            wrapper_tag.insert_after(NavigableString(after))
        node.extract()
        return True

    # Multiple nodes - wrap them all
    first_node_info = affected_nodes[0]
    last_node_info = affected_nodes[-1]

    # Split first node
    first_node = first_node_info['node']
    local_start = start_idx - first_node_info['start']
    before_text = first_node_info['text'][:local_start]
    first_matched = first_node_info['text'][local_start:]

    # Split last node
    last_node = last_node_info['node']
    local_end = end_idx - last_node_info['start']
    last_matched = last_node_info['text'][:local_end]
    after_text = last_node_info['text'][local_end:]

    # Insert before first node
    if before_text:
        first_node.insert_before(NavigableString(before_text))
    first_node.insert_before(wrapper_tag)

    # Add matched text to wrapper
    if first_matched:
        wrapper_tag.append(NavigableString(first_matched))

    # Move middle nodes into wrapper
    for node_info in affected_nodes[1:-1]:
        wrapper_tag.append(NavigableString(node_info['text']))

    # Add last matched text
    if last_matched and len(affected_nodes) > 1:
        wrapper_tag.append(NavigableString(last_matched))

    # Add after text
    if after_text:
        wrapper_tag.insert_after(NavigableString(after_text))

    # Remove original nodes
    for node_info in affected_nodes:
        node_info['node'].extract()

    return True


def highlight_errors_in_soup(soup, errors: list[dict[str, Any]]):
    """Highlight errors by searching in combined text content."""
    if not errors:
        print("No errors to highlight")
        return

    print(f"\n=== STARTING HIGHLIGHTING FOR {len(errors)} ERRORS ===")

    # Inject styles and script first
    inject_styles_and_script(soup)

    # Find main content area
    content_area = (
        soup.find('div', {'id': 'mw-content-text'}) or
        soup.find('div', {'class': 'mw-parser-output'}) or
        soup.find('article') or
        soup.find('main') or
        soup.body or
        soup
    )

    print(f"Content area: {content_area.name if hasattr(content_area, 'name') else 'soup'}")

    # Get all the text content
    full_text = content_area.get_text()
    print(f"Full text length: {len(full_text)}")

    for idx, err in enumerate(errors):
        error_phrase = err.get("error_phrase", "")
        error_short_summary = err.get("error_short_summary", "")
        suggested_fix = err.get("suggested_fix", "")

        if not error_phrase:
            continue

        print(f"\n--- Error {idx + 1}: '{error_phrase[:80]}...' ---")

        # Create a regex pattern that allows flexible whitespace
        pattern_parts = [re.escape(word) for word in error_phrase.split()]
        pattern = r'\s+'.join(pattern_parts)

        # Find in the full text
        match = re.search(pattern, full_text, re.IGNORECASE)

        if not match:
            print(f"✗ Not found in full text")
            continue

        print(f"✓ Found at position {match.start()}-{match.end()}")

        # Create wrapper span with error data as JSON attribute
        wrapper_span = soup.new_tag('span')
        wrapper_span['class'] = 'error-highlight'
        wrapper_span['data-error-idx'] = str(idx)

        # Store error data as JSON in data attribute
        error_json = json.dumps({
            'error_short_summary': error_short_summary,
            'why_wrong': err.get('why_wrong', ''),
            'suggested_fix': suggested_fix,
            'references': err.get('references', [])
        })
        wrapper_span['data-error'] = error_json

        # Wrap the text
        success = wrap_text_in_element(content_area, match.start(), match.end(), wrapper_span, soup)

        if success:
            print(f"  ✓ Successfully highlighted")
        else:
            print(f"  ✗ Failed to wrap text")

    print("\n=== HIGHLIGHTING COMPLETE ===\n")


def run_analysis(
    url: str,
    progress: gr.Progress = gr.Progress(track_tqdm=False),
) -> tuple[str, dict[str, Any], str]:
    progress(0, desc="Loading page...")
    soup, error = download_web_page(url)

    if error:
        return error, {}, "Failed to load page"

    progress(0.15, desc="Running error detection (this may take a while)...")
    start_time = time.perf_counter()
    try:
        analysis = find_wikipedia_errors_advanced_2(url)
    except Exception as exc:
        raise gr.Error(f"Analysis failed: {exc}") from exc

    elapsed = time.perf_counter() - start_time
    progress(0.9, desc="Highlighting errors in page...")

    # Handle both dict and object responses
    if hasattr(analysis, 'model_dump'):
        analysis_dict = analysis.model_dump(mode="json")
    elif hasattr(analysis, 'dict'):
        analysis_dict = analysis.dict()
    else:
        analysis_dict = analysis

    errors = analysis_dict.get("errors", [])
    num_errors = len(errors)

    # Highlight errors in the soup
    highlight_errors_in_soup(soup, errors)

    # Convert to iframe
    highlighted_html = soup_to_iframe(soup)

    progress(1.0, desc="Complete!")

    status = f"Found {num_errors} potential issue(s) in {elapsed:.1f}s."
    if num_errors == 0:
        status = f"No issues found in {elapsed:.1f}s."

    return highlighted_html, analysis_dict, status


with gr.Blocks(title="CuraData", theme=gr.themes.Ocean()) as demo:
    gr.Markdown("""
    <h1 style='text-align: center'>CuraData</h1>
    <p style='text-align: center; font-size: 16px; color: #666; margin: 20px 0;'>
        Paste a URL and run the data error detector
    </p>
    """)

    url_input = gr.Textbox(
        label="URL",
        placeholder="https://simple.wikipedia.org/wiki/Tartar_sauce",
        value="https://simple.wikipedia.org/wiki/Tartar_sauce",
    )

    gr.Markdown("### Examples:")
    gr.Markdown("""
- (Simple) Wikipedia:
    - `https://simple.wikipedia.org/wiki/Tartar_sauce`
    - `https://simple.wikipedia.org/wiki/Non-steroidal_anti-inflammatory_drug`
    - `https://simple.wikipedia.org/wiki/Bruce_Lee`
- Investopedia: `https://www.investopedia.com/terms/i/inflation.asp`
- News sites, blogs, documentation sites, etc.
""")

    analyze_button = gr.Button("Find Errors", variant="primary")

    page_content = gr.HTML(label="Page Content")
    detected_errors = gr.JSON(label="Detected Issues")
    status_message = gr.Markdown(label="Status")

    analyze_button.click(
        run_analysis,
        inputs=url_input,
        outputs=[page_content, detected_errors, status_message],
    )


if __name__ == "__main__":
    demo.launch()