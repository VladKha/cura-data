from dotenv import load_dotenv
load_dotenv()

from inconsistency_detection.claire_agent import InconsistencyAgent
from inconsistency_detection.utils.report_rendering import render_inconsistency_report
import asyncio
import time

agent = InconsistencyAgent(
	"gpt-5", # gpt-5-mini
    reasoning_effort="high", # low
    model_provider='openai', # azure_openai
	num_results_per_query=3,
)

passage = """
Reese's Pieces - Wikipedia

[Jump to content](#bodyContent)

Main menu

Main menu

move to sidebar
hide

Navigation

* [Main page](/wiki/Main_Page "Visit the main page [z]")
* [Contents](/wiki/Wikipedia:Contents "Guides to browsing Wikipedia")
* [Current events](/wiki/Portal:Current_events "Articles related to current events")
* [Random article](/wiki/Special:Random "Visit a randomly selected article [x]")
* [About Wikipedia](/wiki/Wikipedia:About "Learn about Wikipedia and how it works")
* [Contact us](//en.wikipedia.org/wiki/Wikipedia:Contact_us "How to contact Wikipedia")

Contribute

* [Help](/wiki/Help:Contents "Guidance on how to use and edit Wikipedia")
* [Learn to edit](/wiki/Help:Introduction "Learn how to edit Wikipedia")
* [Community portal](/wiki/Wikipedia:Community_portal "The hub for editors")
* [Recent changes](/wiki/Special:RecentChanges "A list of recent changes to Wikipedia [r]")
* [Upload file](/wiki/Wikipedia:File_upload_wizard "Add images or other media for use on Wikipedia")
* [Special pages](/wiki/Special:SpecialPages)

[![](/static/images/icons/wikipedia.png)

![Wikipedia](/static/images/mobile/copyright/wikipedia-wordmark-en.svg)
![The Free Encyclopedia](/static/images/mobile/copyright/wikipedia-tagline-en.svg)](/wiki/Main_Page)

[Search](/wiki/Special:Search "Search Wikipedia [f]")

Search

Appearance

* [Donate](https://donate.wikimedia.org/?wmf_source=donate&wmf_medium=sidebar&wmf_campaign=en.wikipedia.org&uselang=en)
* [Create account](/w/index.php?title=Special:CreateAccount&returnto=Reese%27s+Pieces "You are encouraged to create an account and log in; however, it is not mandatory")
* [Log in](/w/index.php?title=Special:UserLogin&returnto=Reese%27s+Pieces "You're encouraged to log in; however, it's not mandatory. [o]")

Personal tools

* [Donate](https://donate.wikimedia.org/?wmf_source=donate&wmf_medium=sidebar&wmf_campaign=en.wikipedia.org&uselang=en)
* [Create account](/w/index.php?title=Special:CreateAccount&returnto=Reese%27s+Pieces "You are encouraged to create an account and log in; however, it is not mandatory")
* [Log in](/w/index.php?title=Special:UserLogin&returnto=Reese%27s+Pieces "You're encouraged to log in; however, it's not mandatory. [o]")

Pages for logged out editors [learn more](/wiki/Help:Introduction)

* [Contributions](/wiki/Special:MyContributions "A list of edits made from this IP address [y]")
* [Talk](/wiki/Special:MyTalk "Discussion about edits from this IP address [n]")

Contents
--------

move to sidebar
hide

* [(Top)](#)
* [1
  Overview](#Overview)
* [2
  Variations](#Variations)
* [3
  Production](#Production)
* [4
  *E.T. the Extra-Terrestrial*](#E.T._the_Extra-Terrestrial)
* [5
  Product line expansion](#Product_line_expansion)
* [6
  Partnership](#Partnership)
* [7
  See also](#See_also)
* [8
  References](#References)
* [9
  External links](#External_links)

Toggle the table of contents

Reese's Pieces
==============

4 languages

* [Bahasa Indonesia](https://id.wikipedia.org/wiki/Reese%27s_Pieces "Reese's Pieces – Indonesian")
* [Русский](https://ru.wikipedia.org/wiki/Reese%E2%80%99s_Pieces "Reese’s Pieces – Russian")
* [Suomi](https://fi.wikipedia.org/wiki/Reese%E2%80%99s_Pieces "Reese’s Pieces – Finnish")
* [Türkçe](https://tr.wikipedia.org/wiki/Reese%27s_Pieces "Reese's Pieces – Turkish")

[Edit links](https://www.wikidata.org/wiki/Special:EntityPage/Q2358537#sitelinks-wikipedia "Edit interlanguage links")

* [Article](/wiki/Reese%27s_Pieces "View the content page [c]")
* [Talk](/wiki/Talk:Reese%27s_Pieces "Discuss improvements to the content page [t]")

English

* [Read](/wiki/Reese%27s_Pieces)
* [Edit](/w/index.php?title=Reese%27s_Pieces&action=edit "Edit this page [e]")
* [View history](/w/index.php?title=Reese%27s_Pieces&action=history "Past revisions of this page [h]")



Tools

Tools

move to sidebar
hide

Actions

* [Read](/wiki/Reese%27s_Pieces)
* [Edit](/w/index.php?title=Reese%27s_Pieces&action=edit "Edit this page [e]")
* [View history](/w/index.php?title=Reese%27s_Pieces&action=history)

General

* [What links here](/wiki/Special:WhatLinksHere/Reese%27s_Pieces "List of all English Wikipedia pages containing links to this page [j]")
* [Related changes](/wiki/Special:RecentChangesLinked/Reese%27s_Pieces "Recent changes in pages linked from this page [k]")
* [Upload file](//en.wikipedia.org/wiki/Wikipedia:File_Upload_Wizard "Upload files [u]")
* [Permanent link](/w/index.php?title=Reese%27s_Pieces&oldid=1315284476 "Permanent link to this revision of this page")
* [Page information](/w/index.php?title=Reese%27s_Pieces&action=info "More information about this page")
* [Cite this page](/w/index.php?title=Special:CiteThisPage&page=Reese%27s_Pieces&id=1315284476&wpFormIdentifier=titleform "Information on how to cite this page")
* [Get shortened URL](/w/index.php?title=Special:UrlShortener&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FReese%2527s_Pieces)
* [Download QR code](/w/index.php?title=Special:QrCode&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FReese%2527s_Pieces)

Print/export

* [Download as PDF](/w/index.php?title=Special:DownloadAsPdf&page=Reese%27s_Pieces&action=show-download-screen "Download this page as a PDF file")
* [Printable version](/w/index.php?title=Reese%27s_Pieces&printable=yes "Printable version of this page [p]")

In other projects

* [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Reese%27s_Pieces)
* [Wikidata item](https://www.wikidata.org/wiki/Special:EntityPage/Q2358537 "Structured data on this page hosted by Wikidata [g]")

Appearance

move to sidebar
hide

From Wikipedia, the free encyclopedia

Peanut butter candy

Reese's Pieces

|  |  |
| --- | --- |
| [Reese's Pieces, current design](/wiki/File:Reese%27s_Pieces_Bag.png "Reese's Pieces, current design") [Reese's Pieces candies](/wiki/File:Reese%27s_Pieces_(3394360433).jpg "Reese's Pieces candies") Reese's Pieces consists of bite-sized pieces of candy filled with a peanut butter center in a crunchy shell. | |
| Type | [Confectionery](/wiki/Confectionery "Confectionery") |
| Inventor | [The Hershey Company](/wiki/The_Hershey_Company "The Hershey Company") |
| Inception | September 1978; 47 years ago (1978-09) |
| Manufacturer | [The Hershey Company](/wiki/The_Hershey_Company "The Hershey Company") |
| Current supplier | [The Hershey Company](/wiki/The_Hershey_Company "The Hershey Company") |
| Models made | Standard candy, Mini candies, baking chips |
| Website | [hersheyland.com/reeses-pieces/](https://www.hersheyland.com/products/reeses-pieces-peanut-butter-candy-9-9-oz-bag.html) |

**Reese's Pieces** are a [peanut butter](/wiki/Peanut_butter "Peanut butter") [candy](/wiki/Candy "Candy") manufactured by [The Hershey Company](/wiki/The_Hershey_Company "The Hershey Company"); they are [oblate spheroid](/wiki/Oblate_spheroid "Oblate spheroid") in shape and covered in candy shells that are colored yellow, orange, or brown. They can be purchased in plastic packets, cardboard boxes, or cup-shaped travel containers.

Overview
--------

[[edit](/w/index.php?title=Reese%27s_Pieces&action=edit&section=1 "Edit section: Overview")]

The candy was introduced to the US market first in September 1978.[[1]](#cite_note-1)[[2]](#cite_note-2) Shortly after, Reese's Pieces were introduced to the [Canada](/wiki/Canada "Canada") market in 1980.[[3]](#cite_note-3)
The then relatively new product became very popular with the 1982 release of *[E.T. the Extra-Terrestrial](/wiki/E.T._the_Extra-Terrestrial "E.T. the Extra-Terrestrial")*, in which the candy is featured.[[4]](#cite_note-sweet-4)

Reese's Pieces were introduced in the UK in 1996,[[5]](#cite_note-5) but are produced in the US.[[6]](#cite_note-6)

Reese's Pieces are a [product extension](/wiki/Brand_extension "Brand extension") of the [Reese's Peanut Butter Cups](/wiki/Reese%27s_Peanut_Butter_Cups "Reese's Peanut Butter Cups") line; they were designed to capitalize on the success of the chocolate-covered peanut butter cups, though unlike the cups, they have no chocolate.[[7]](#cite_note-7)

Variations
----------

[[edit](/w/index.php?title=Reese%27s_Pieces&action=edit&section=2 "Edit section: Variations")]

Reese's Pieces has been included in many Reese's and Hershey's products since its introduction. Below is a list of available products that contain Reese's Pieces, from the candy pieces being stuffed inside of existing chocolate bar variations to bags of baking chip mixes.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*]

Products containing Reese's Pieces

| Product | Description | Sizes | Ingredients | Nutrition value | Year introduced |
| --- | --- | --- | --- | --- | --- |
| Reese's Pieces | A peanut butter candy in bite-size pieces containing Reese's peanut butter wrapped in a crunchy shell | * standard size * bag * box | [Sugar](/wiki/Sugar "Sugar"), partially defatted [peanuts](/wiki/Peanut "Peanut"), [hydrogenated vegetable oil](/wiki/Hydrogenated_vegetable_oil "Hydrogenated vegetable oil") [palm kernel oil](/wiki/Palm_kernel_oil "Palm kernel oil"), [soybean oil](/wiki/Soybean_oil "Soybean oil"), [corn syrup](/wiki/Corn_syrup "Corn syrup") Solids, [dextrose](/wiki/Dextrose "Dextrose") Contains 2% Less of: [corn syrup](/wiki/Corn_syrup "Corn syrup"), palm kernel oil, salt, confectioner's glaze, [modified corn starch](/wiki/Modified_corn_starch "Modified corn starch"), [lecithin soy](/w/index.php?title=Lecithin_soy&action=edit&redlink=1 "Lecithin soy (page does not exist)"), artificial [colorants](/wiki/Food_colorant "Food colorant") [yellow 6](/wiki/Sunset_Yellow_FCF "Sunset Yellow FCF") lake, [yellow 5](/wiki/Yellow_5 "Yellow 5") lake, [red 40](/wiki/Red_40 "Red 40") lake, [blue 1](/wiki/Blue_1 "Blue 1") lake, [vanillin](/wiki/Vanillin "Vanillin"), [artificial flavor](/wiki/Artificial_flavor "Artificial flavor"), [carnauba wax](/wiki/Carnauba_wax "Carnauba wax"), milk[[8]](#cite_note-8) | Reese's Pieces  | Nutritional value per 38 g | | | --- | --- | | [Energy](/wiki/Food_energy "Food energy") | 836.8 kJ (200.0 kcal) | |  | | | **[Carbohydrates](/wiki/Carbohydrate "Carbohydrate")** | 25 g | | [Sugars](/wiki/Sugar "Sugar") | 21 g | | [Dietary fibre](/wiki/Dietary_fiber "Dietary fiber") | 0 g | |  | | |  | | | **[Fat](/wiki/Fat "Fat")** | 9 g | | [Saturated](/wiki/Saturated_fat "Saturated fat") | 8 g | | [Trans](/wiki/Trans_fat "Trans fat") | 0 g | |  | | |  | | | **[Protein](/wiki/Protein_(nutrient) "Protein (nutrient)")** | 4 g | | | Vitamins and minerals | | | --- | --- | |  | | |  | | | **[Vitamins](/wiki/Vitamin "Vitamin")** | **Quantity** **%DV**† | | [Vitamin A equiv.](/wiki/Vitamin_A "Vitamin A") | 0% 0 μg | | [Vitamin C](/wiki/Vitamin_C "Vitamin C") | 0% 0 mg | |  | | |  | | | **[Minerals](/wiki/Mineral_(nutrient) "Mineral (nutrient)")** | **Quantity** **%DV**† | | [Calcium](/wiki/Calcium_in_biology#Humans "Calcium in biology") | 0% 0 mg | | [Iron](/wiki/Human_iron_metabolism "Human iron metabolism") | 22% 4 mg | | [Sodium](/wiki/Sodium_in_biology "Sodium in biology") | 2% 45 mg | |  | | | | | †Percentages estimated using [US recommendations](/wiki/Reference_Daily_Intake#Daily_Values "Reference Daily Intake") for adults,[[9]](#cite_note-FDADailyValues-9) except for potassium, which is estimated based on expert recommendation from the [National Academies](/wiki/National_Academies_of_Sciences,_Engineering,_and_Medicine "National Academies of Sciences, Engineering, and Medicine")[[10]](#cite_note-NationalAcademiesPotassium-10) Source: [[1]](https://smartlabel.hersheys.com/00034000114801-0010) | | | 1978[[11]](#cite_note-11) |
| Reese's Pieces Peanut | The original Reese's Pieces candies with the inclusion of peanuts. | * bag | Sugar, Peanuts, Partially Defatted Peanuts, Hydrogenated Vegetable Oil (Palm Kernel And Soybean Oil), Corn Syrup Contains 2% Or Less Of: Dextrose, Artificial Color (Yellow 5 Lake, Yellow 6 Lake, Red 40 Lake, Blue 1 Lake), Palm Kernel Oil, Confectioner's Glaze, Cornstarch, Modified Cornstarch, Salt, Lecithin (Soy), Carnauba Wax, Vanillin (Artificial Flavor), Milk. [[12]](#cite_note-12) | Reese's Pieces Peanut Butter with Peanut  | Nutritional value per 100 g (3.5 oz) | | | --- | --- | | [Energy](/wiki/Food_energy "Food energy") | 510 kcal (2,100 kJ) | |  | | | **[Carbohydrates](/wiki/Carbohydrate "Carbohydrate")** | 56 g | | [Sugars](/wiki/Sugar "Sugar") | 46 g | |  | | |  | | | **[Fat](/wiki/Fat "Fat")** | 28 g | | [Saturated](/wiki/Saturated_fat "Saturated fat") | 15 g | | [Trans](/wiki/Trans_fat "Trans fat") | 0.0 g | |  | | |  | | | **[Protein](/wiki/Protein_(nutrient) "Protein (nutrient)")** | 13 g | | | Vitamins and minerals | | | --- | --- | |  | | |  | | | **[Vitamins](/wiki/Vitamin "Vitamin")** | **Quantity** **%DV**† | | [Vitamin A equiv.](/wiki/Vitamin_A "Vitamin A") | 0% 0 μg | | [Vitamin C](/wiki/Vitamin_C "Vitamin C") | 0% 0 mg | |  | | |  | | | **[Minerals](/wiki/Mineral_(nutrient) "Mineral (nutrient)")** | **Quantity** **%DV**† | | [Calcium](/wiki/Calcium_in_biology#Humans "Calcium in biology") | 0% 0 mg | | [Iron](/wiki/Human_iron_metabolism "Human iron metabolism") | 10% 1.8 mg | | [Sodium](/wiki/Sodium_in_biology "Sodium in biology") | 7% 154 mg | |  | | | | |  | | | **Other constituents** | **Quantity** | | [Cholesterol](/wiki/Cholesterol "Cholesterol") | 0.0 mg | |  | | | †Percentages estimated using [US recommendations](/wiki/Reference_Daily_Intake#Daily_Values "Reference Daily Intake") for adults,[[9]](#cite_note-FDADailyValues-9) except for potassium, which is estimated based on expert recommendation from the [National Academies](/wiki/National_Academies_of_Sciences,_Engineering,_and_Medicine "National Academies of Sciences, Engineering, and Medicine")[[10]](#cite_note-NationalAcademiesPotassium-10) Source: [[2]](https://www.nutritionix.com/i/reeses/reeses-pieces-peanuts/56dba4c0e93ea7e63d8111e0) | | | 1980s[[13]](#cite_note-13) |
| Reese's Mini Pieces Baking Chips | Mini Reese's Pieces peanut butter candy for baking | * bag | Sugar, Partially Defatted Peanuts, Hydrogenated, Vegetable Oil, Palm Kernel Oil, Soybean Oil, Corn Syrup Solids, Dextrose Contains 2% or Less of: Palm Kernel Oil, Corn Syrup, Artificial Color, Yellow 6 Lake, Yellow 5 Lake, Red 40 Lake, Blue 1 Lake, Cornstarch, Salt, Confectioner's Glaze, Lecithin, Modified Cornstarch, Carnauba Wax, Vanillin (ARTIFICIAL FLAVOR), Milk [[14]](#cite_note-14) | Reese's Pieces Minis Peanut Butter Candies  | Nutritional value per 15 g | | | --- | --- | | [Energy](/wiki/Food_energy "Food energy") | 292.88 kJ (70.00 kcal) | |  | | | **[Carbohydrates](/wiki/Carbohydrate "Carbohydrate")** | 10 g | | [Sugars](/wiki/Sugar "Sugar") | 8 g | | [Dietary fibre](/wiki/Dietary_fiber "Dietary fiber") | 0 g | |  | | |  | | | **[Fat](/wiki/Fat "Fat")** | 3.5 g | | [Saturated](/wiki/Saturated_fat "Saturated fat") | 3 g | | [Trans](/wiki/Trans_fat "Trans fat") | 0 g | |  | | |  | | | **[Protein](/wiki/Protein_(nutrient) "Protein (nutrient)")** | 2 g | | | Vitamins and minerals | | | --- | --- | |  | | |  | | | **[Vitamins](/wiki/Vitamin "Vitamin")** | **Quantity** **%DV**† | | [Vitamin A equiv.](/wiki/Vitamin_A "Vitamin A") | 0% 0 μg | | [Vitamin D](/wiki/Vitamin_D "Vitamin D") | 0% 0 μg | |  | | |  | | | **[Minerals](/wiki/Mineral_(nutrient) "Mineral (nutrient)")** | **Quantity** **%DV**† | | [Calcium](/wiki/Calcium_in_biology#Humans "Calcium in biology") | 1% 10 mg | | [Iron](/wiki/Human_iron_metabolism "Human iron metabolism") | 2% 0.3 mg | | [Potassium](/wiki/Potassium_in_biology "Potassium in biology") | 1% 40 mg | | [Sodium](/wiki/Sodium_in_biology "Sodium in biology") | 1% 15 mg | |  | | | | | †Percentages estimated using [US recommendations](/wiki/Reference_Daily_Intake#Daily_Values "Reference Daily Intake") for adults,[[9]](#cite_note-FDADailyValues-9) except for potassium, which is estimated based on expert recommendation from the [National Academies](/wiki/National_Academies_of_Sciences,_Engineering,_and_Medicine "National Academies of Sciences, Engineering, and Medicine")[[10]](#cite_note-NationalAcademiesPotassium-10) Source: [[3]](https://smartlabel.hersheys.com/00034000141289-0012) | | | 2003[[15]](#cite_note-15) |
| Reese's Baking Cups and Reese's Pieces Candy | A mixture of mini Reese's Pieces peanut butter candies and mini Reese's Peanut Butter cups for baking | * bag | Milk Chocolate, Sugar, Cocoa Butter, Chocolate, Skim Milk, Milk Fat, Lactose, Lecithin, PGPR, Sugar, Partially Defatted Peanuts, Peanuts, Hydrogenated Vegetable Oil, Palm Kernel Oil, Palm Oil, Soybean Oil, Dextrose, Corn Syrup Solids Contains 2% or Less of: Cocoa Butter, Palm Kernel Oil, Salt, Corn Syrup, Confectioner's Glaze, Lecithin, Modified Cornstarch, Artificial Color, Yellow 6 Lake, Yellow 5 Lake, Red 40 Lake, Blue 1 Lake, PGPR, Vanillin (ARTIFICIAL FLAVOR), Carnauba Wax, TBHQ (Preservative), Citric Acid (TO MAINTAIN FRESHNESS)[[16]](#cite_note-16) | Reese's Baking Cups and Reese's Pieces Candy  | Nutritional value per 15 g | | | --- | --- | | [Energy](/wiki/Food_energy "Food energy") | 58.5289 kJ (13.9887 kcal) | |  | | | **[Carbohydrates](/wiki/Carbohydrate "Carbohydrate")** | 9 g | | [Sugars](/wiki/Sugar "Sugar") | 8 g | | [Dietary fibre](/wiki/Dietary_fiber "Dietary fiber") | 0 g | |  | | |  | | | **[Fat](/wiki/Fat "Fat")** | 4 g | | [Saturated](/wiki/Saturated_fat "Saturated fat") | 2.5 g | | [Trans](/wiki/Trans_fat "Trans fat") | 0 g | |  | | |  | | | **[Protein](/wiki/Protein_(nutrient) "Protein (nutrient)")** | 1 g | | | Vitamins and minerals | | | --- | --- | |  | | |  | | | **[Vitamins](/wiki/Vitamin "Vitamin")** | **Quantity** **%DV**† | | [Vitamin A equiv.](/wiki/Vitamin_A "Vitamin A") | 0% 0 μg | | [Vitamin D](/wiki/Vitamin_D "Vitamin D") | 0% 0 μg | |  | | |  | | | **[Minerals](/wiki/Mineral_(nutrient) "Mineral (nutrient)")** | **Quantity** **%DV**† | | [Calcium](/wiki/Calcium_in_biology#Humans "Calcium in biology") | 1% 10 mg | | [Iron](/wiki/Human_iron_metabolism "Human iron metabolism") | 2% 0.4 mg | | [Potassium](/wiki/Potassium_in_biology "Potassium in biology") | 2% 45 mg | | [Sodium](/wiki/Sodium_in_biology "Sodium in biology") | 1% 25 mg | |  | | | | | †Percentages estimated using [US recommendations](/wiki/Reference_Daily_Intake#Daily_Values "Reference Daily Intake") for adults,[[9]](#cite_note-FDADailyValues-9) except for potassium, which is estimated based on expert recommendation from the [National Academies](/wiki/National_Academies_of_Sciences,_Engineering,_and_Medicine "National Academies of Sciences, Engineering, and Medicine")[[10]](#cite_note-NationalAcademiesPotassium-10) Source: [[4]](https://smartlabel.hersheys.com/00034000445530-0010) | | | 2018[[17]](#cite_note-17) |

Production
----------

[[edit](/w/index.php?title=Reese%27s_Pieces&action=edit&section=3 "Edit section: Production")]

[![](//upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Respcsinside.jpg/250px-Respcsinside.jpg)](/wiki/File:Respcsinside.jpg)

A yellow Reese's Piece cut in half, showing the peanut butter inside

In the 1970s, the candies were produced by [The Hershey Company](/wiki/The_Hershey_Company "The Hershey Company") using panning machines that had been used to make [Hershey-ets](/wiki/Hershey-ets "Hershey-ets"), a chocolate-filled candy that had been discontinued. The candy was first called "PBs" and was later rechristened as Reese's Pieces.[[18]](#cite_note-18) Designers wanted a peanut-flavored candy but had problems with the filling. Original plans called for filling the candy shells with peanut butter, but the oil leaked out into the shell, leaving it soft, rather than crunchy.[*[citation needed](/wiki/Wikipedia:Citation_needed "Wikipedia:Citation needed")*]

The developer of the project turned the problem over to a team of outside scientists, who created a peanut-flavored [penuche](/wiki/Penuche "Penuche") filling.[[19]](#cite_note-19) More experimentation was needed to determine the correct thickness of the shell. Finally, the colors of the candy coating were designed to coordinate with the color of the Reese's package. The color distribution goal is 50% orange, 25% brown, and 25% yellow.[[20]](#cite_note-20)

*E.T. the Extra-Terrestrial*
----------------------------

[[edit](/w/index.php?title=Reese%27s_Pieces&action=edit&section=4 "Edit section: E.T. the Extra-Terrestrial")]

In 1982, the [Mars](/wiki/Mars,_Incorporated "Mars, Incorporated") candy bar company rejected a [product placement](/wiki/Product_placement "Product placement") offer for the inclusion of its key product [M&M's](/wiki/M%26M%27s "M&M's") in the [Steven Spielberg](/wiki/Steven_Spielberg "Steven Spielberg") film, *[E.T. the Extra-Terrestrial](/wiki/E.T._the_Extra-Terrestrial "E.T. the Extra-Terrestrial")*. Hershey accepted an offer for use of Reese's Pieces in the movie, and with the film's blockbuster success its product sales dramatically increased, perhaps as much as 300%.[[21]](#cite_note-21)

Product line expansion
----------------------

[[edit](/w/index.php?title=Reese%27s_Pieces&action=edit&section=5 "Edit section: Product line expansion")]

In 2010, The Hershey Company expanded the *Pieces* line to include [York Peppermint Pattie](/wiki/York_Peppermint_Pattie "York Peppermint Pattie") Pieces, [Hershey's Special Dark](/wiki/Hershey%27s_Special_Dark "Hershey's Special Dark") Pieces, and [Almond Joy](/wiki/Almond_Joy "Almond Joy") Pieces.[[22]](#cite_note-22) [Hershey's Milk Chocolate with Almonds](/wiki/Hershey_bar "Hershey bar") Pieces became the fourth expansion of this line in 2012.[[23]](#cite_note-23)

Partnership
-----------

[[edit](/w/index.php?title=Reese%27s_Pieces&action=edit&section=6 "Edit section: Partnership")]

[Chicago Sky](/wiki/Chicago_Sky "Chicago Sky") player [Angel Reese](/wiki/Angel_Reese "Angel Reese") became an official brand ambassador for Reese's Pieces, after fans' enthusiasm for the idea.[[24]](#cite_note-24) Angel Reese's fans are known as Reese's Pieces.[[25]](#cite_note-25) The most notable creations were the customized basketball jersey with Reese's Pieces colors and her Chicago Sky number, and Angel Reese appearing on the Reese's Puffs cereal box.[[26]](#cite_note-26) Senior brand manager Melissa Blette stated Reese was chosen for her personality and excited fanbase, in addition to her name.[[27]](#cite_note-27) Blette reported that Reese's sales exceeded expectations.[[28]](#cite_note-28)
"""

passage = """
Non-steroidal anti-inflammatory drugs (often shortened to NSAIDs) are drugs that have analgesic or fever-reducing properties, but that are not based on steroids. Higher doses of such drugs can also be used to fight inflammation. Such drugs are special as they are not narcotic, that is they don't induce sleep. Well-known examples of such drugs are aspirin, diclofenac and ibuprofen.
"""

passage = """
Tartar sauce (tartare in the United Kingdom and Australia) is a mayonnaise-based sauce. It is often served as a condiment with seafood dishes.[1] It is like mayonnaise, but with a few more ingredients such as pickles, onions, capers, lemon juice and parsley.

The word Tartar is a Turkic word. It is believed to be named after the Tatar people.
"""

# passage = (
#     "Title: Haruki Murakami > Biography\n\n"
#     "Haruki Murakami (村上 春樹, Murakami Haruki; born January 12, 1949[1]) is a Japanese writer. "
#     "His novels, essays, and short stories have been best-sellers in Japan and internationally."
# ),

async def main():
    reports = await agent.analyze_passage_for_inconsistencies(
        passage=passage
    )

    for report in reports:
        if report.verdict != 'consistent':
            render_inconsistency_report(report)

if __name__ == "__main__":
    start_time = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start_time
    print(f"Request duration: {elapsed:.2f} seconds")
# INFO     Extracted 6 claims from passage 'Tartar sauce (tartare in  agent.py:106
#          the United Kingdom and Australia) is a mayonnaise-based'
# INFO     Generated inconsistency reports for 6 claims               agent.py:117
# ───────────────────────────── Inconsistency Report ─────────────────────────────
# ╭─────────────────────────────────── Claim ────────────────────────────────────╮
# │ The word 'Tartar' is a Turkic word.                                          │
# ╰──────────────────────────────────────────────────────────────────────────────╯
# ╭────────────────────────── Claim Was Extracted From ──────────────────────────╮
# │                                                                              │
# │ Tartar sauce (tartare in the United Kingdom and Australia) is a              │
# │ mayonnaise-based sauce. It is often served as a condiment with seafood       │
# │ dishes.[1] It is like mayonnaise, but with a few more ingredients such as    │
# │ pickles, onions, capers, lemon juice and parsley.                            │
# │                                                                              │
# │ The word Tartar is a Turkic word. It is believed to be named after the Tatar │
# │ people.                                                                      │
# │                                                                              │
# ╰──────────────────────────────────────────────────────────────────────────────╯
#                                 ╭── Verdict ───╮
#                                 │ INCONSISTENT │
#                                 ╰──────────────╯
# ╭──────────────────────────────────── Why? ────────────────────────────────────╮
# │ Sources indicate that the Western form “Tartar” does not originate as a      │
# │ Turkic word. The Oxford English Dictionary (via the Tatars etymology) notes  │
# │ that the form “Tartar” has its origins in either Latin or French, entering   │
# │ Western languages from Turkish and Persian forms of “tatar”; the extra ‘r’   │
# │ in Western usage was likely added due to association with Tartarus [1].      │
# │ Separately, “Tatars” are Turkic peoples, and “Tatar” is the ethnonym         │
# │ connected to them [2].                                                       │
# │                                                                              │
# │ Thus, while the term ultimately refers to the Turkic Tatars, the specific    │
# │ word “Tartar” is a Westernized form shaped by Latin/French and an            │
# │ association with Greek “Tartarus,” not a Turkic word itself [1][14].         │
# ╰──────────────────────────────────────────────────────────────────────────────╯
# ╭──────────────── How the Claim Could Be Reworded for Clarity ─────────────────╮
# │ Revise to distinguish between the ethnonym “Tatar” and the Western form      │
# │ “Tartar.” For example: “The sauce’s name ultimately traces to the ethnonym   │
# │ ‘Tatar’ (a Turkic people); the Western spelling ‘Tartar’ is a Latin/French   │
# │ form, likely influenced by association with ‘Tartarus.’”                     │
# ╰──────────────────────────────────────────────────────────────────────────────╯
# ───────────────────────── Passages that Were Looked At ─────────────────────────
# ┌─────────────────────────── [1] Tatars > Etymology ───────────────────────────┐
# │ Further information: Tatarstan and Tartary Tatar became a name for           │
# │ populations of the former Golden Horde in Europe, such as those of the       │
# │ former Kazan, Crimean, Astrakhan, Qasim, and Siberian Khanates. The form     │
# │ Tartar has its origins in either Latin or French, coming to Western European │
# │ languages from Turkish and the Persian (tātār, "mounted messenger"). From    │
# │ the beginning, the extra r was present in the Western forms and according to │
# │ the Oxford English Dictionary this was most likely due to an association     │
# │ with Tartarus. The Persian word is first recorded in the 13th century in     │
# │ reference to the hordes of Genghis Khan and is of unknown origin; according  │
# │ to the Oxford English Dictionary it is "said to be" ultimately from tata.    │
# │ The Arabic word for Tatars is تتار. Tatars themselves wrote their name as    │
# │ تاتار or طاطار. Ochir (2016) states that Siberian Tatars and the Tatars      │
# │ living in the territories between Asia and Europe are of Turkic origin,      │
# │ acquired the appellation Tatar later, and do not possess ancestral           │
# │ connection to the Mongolic Nine Tatars, whose ethnogenesis involved Mongolic │
# │ people as well as Mongolized Turks who had been ruling over them during the  │
# │ 6–8th centuries. Pow (2019) proposes that Turkic-speaking peoples of         │
# │ Cumania, as a sign of political allegiance, adopted the endonym Tatar of     │
# │ their Mongol conquerors, before ultimately subsuming the latter culturally   │
# │ and linguistically. Some Turkic peoples living within the Russian Empire     │
# │ were named Tatar, although not all Turkic peoples of Russian Empire were     │
# │ referred to as Tatars (for instance, this name was never used in relation to │
# │ the Yakuts, Chuvashes, Sarts and some others). Some of these populations     │
# │ used and keep using Tatar as a self-designation, others do not. Kipchak      │
# │ groups Kipchak–Bulgar branch or "Tatar" in the narrow sense Volga Tatars     │
# │ Astrakhan Tatars Lipka Tatars Kipchak–Cuman branch Crimean Tatars Karachays  │
# │ and Balkars: Mountain Tatars Kumyks: Daghestan Tatars Kipchak–Nogai branch:  │
# │ Dobrujan Tatars Nogais: Nogai Tatars Siberian Tatars Siberian branch:        │
# │ Altaians: Altai Tatars, including the Tubalar or Chernevo Tatars Chulyms or  │
# │ Chulym Tatars Khakas: Yenisei Tatars (also Abakan Tatars or Achin Tatars),   │
# │ still use the Tatar designation Shors: Kuznetsk Tatars Oghuz branch          │
# │ Azerbaijanis: Caucasus Tatars (also Transcaucasia Tatars or Azerbaijan       │
# │ Tatars) The term is originally not just an exonym, since the Polovtsians of  │
# │ Golden Horde called themselves Tatar. It is also an endonym to a number of   │
# │ peoples of Siberia and Russian Far East, namely the Khakas people (тадар,    │
# │ tadar).                                                                      │
# └──────────────────────────────────────────────────────────────────────────────┘
# ┌───────────────────────────────── [2] Tatars ─────────────────────────────────┐
# │ Umbrella term for different Turkic ethnic groups in Asia and Europe Not to   │
# │ be confused with Tartar. Ethnic group                                        │
# │                                                                              │
# │                                                                              │
# │   татарлар tatarlar تاتارلار> Total population                               │
# │  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━      │
# │   Volga Tatars                                                               │
# │   Regions with significant populations                                       │
# │   Russia                                                                     │
# │   Ukraine (incl. population in Crimea and Crimean Tatars)                    │
# │   Uzbekistan                                                                 │
# │   Kazakhstan                                                                 │
# │   Turkey                                                                     │
# │   Afghanistan                                                                │
# │   Turkmenistan                                                               │
# │   Kyrgyzstan                                                                 │
# │   Azerbaijan                                                                 │
# │   Romania                                                                    │
# │   United States                                                              │
# │   Belarus                                                                    │
# │   France                                                                     │
# │   Switzerland                                                                │
# │   China                                                                      │
# │   Canada                                                                     │
# │   Poland                                                                     │
# │   Bulgaria                                                                   │
# │   Finland                                                                    │
# │   Japan                                                                      │
# │   Australia                                                                  │
# │   Czech Republic                                                             │
# │   Estonia                                                                    │
# │   Latvia                                                                     │
# │   Lithuania                                                                  │
# │   Iran                                                                       │
# │   Languages                                                                  │
# │   Kipchak languages                                                          │
# │   Religion                                                                   │
# │   Predominantly Sunni Islam with Eastern Orthodox minority                   │
# │   Related ethnic groups                                                      │
# │   Other Turkic peoples, especially other speakers of Kipchak languages       │
# │                                                                              │
# │                                                                              │
# │ Share of Tatars in regions of Russia, 2010 census "Tatar" (/ˈtɑːtərz/        │
# │ TAH-tərz) is an umbrella term for different Turkic ethnic groups bearing the │
# │ name "Tatar" across Eastern Europe and Asia. Initially, the ethnonym Tatar   │
# │ possibly referred to the Tatar confederation. That confederation was         │
# │ eventually incorporated into the Mongol Empire when Genghis Khan unified the │
# │ various steppe tribes. Historically, the term Tatars (or Tartars) was        │
# │ applied to anyone originating from the vast Northern and Central Asian       │
# │ landmass then known as Tartary, a term which was also conflated with the     │
# │ Mongol Empire itself. More recently, however, the term has come to refer     │
# │ more narrowly to related ethnic groups who refer to themselves as Tatars or  │
# │ who speak languages that are commonly referred to as Tatar. The largest      │
# │ group amongst the Tatars by far are the Volga Tatars, native to the          │
# │ Volga-Ural region (Tatarstan and Bashkortostan) of European Russia, who for  │
# │ this reason are often also known as "Tatars" in Russian. They compose 53% of │
# │ the population in Tatarstan. Their language is known as the Tatar language.  │
# │ As of 2010, there were an estimated 5.3 million ethnic Tatars in Russia.     │
# │ While also speaking languages belonging to different Kipchak sub-groups,     │
# │ genetic studies have shown that the three main groups of Tatars (Volga,      │
# │ Crimean, Siberian) are apparently unrelated, and thus their formation        │
# │ occurred independently of one another. However, it is possible that all      │
# │ Tatar groups have at least partially the same origin, mainly from the times  │
# │ of the Golden Horde. Many noble families in the Tsardom of Russia and        │
# │ Russian Empire had Tatar origins.                                            │
# └──────────────────────────────────────────────────────────────────────────────┘
# ┌───────────────────── [3] Tartar > People and languages ──────────────────────┐
# │ Tartar, someone from Tartary, the historical central Asian region populated  │
# │ by Manchus, Mongols, Turks, and others Tatars, a Turkic ethnic group native  │
# │ to present-day Russia and Ukraine Tatar language                             │
# └──────────────────────────────────────────────────────────────────────────────┘
# ┌───────────────────────── [4] Tartar sauce > History ─────────────────────────┐
# │ Tartar sauce is named for steak tartare (and thus ultimately named for the   │
# │ Tatars), with which it was commonly served in 19th century France. Recipes   │
# │ for tartar sauce have been found in English-language cookbooks dating to the │
# │ mid-19th century, including a recipe in Modern Cookery for Private Families  │
# │ in 1860. It was also popular in Hungary in the late 19th century.            │
# └──────────────────────────────────────────────────────────────────────────────┘
# ┌───────────── [5] Steak tartare > History > Origins of the name ──────────────┐
# │ Main article: Hamburg steak In the early 20th century, what is now generally │
# │ known as "steak tartare" was called steak à l'Americaine in Europe. One      │
# │ variation on that dish included serving it with tartar sauce; the 1922       │
# │ edition of Escoffier's Le Guide Culinaire defines "Steak à la tartare" as    │
# │ "steak à l'Americaine" made without egg yolk, served with tartar sauce on    │
# │ the side. "Steak à la tartare" (literally meaning "served with tartar        │
# │ sauce") was later shortened to "steak tartare" Over time, the distinction    │
# │ between steak à l'Americaine and its tartar-sauce variant disappeared. The   │
# │ 1938 edition of Larousse Gastronomique describes steak tartare as raw ground │
# │ beef served with a raw egg yolk, without any mention of tartar sauce. "À la  │
# │ tartare" or simply "tartare" can still mean "served with tartar sauce" for   │
# │ some dishes, mostly fried fish. At the same time, the name "tartare" is also │
# │ sometimes applied to other dishes of raw meats or fish, such as tuna         │
# │ tartare, introduced in 1975 by the restaurant Le Duc in Paris.               │
# └──────────────────────────────────────────────────────────────────────────────┘
# ┌───────────────────────────── [6] Steak tartare ──────────────────────────────┐
# │ Starter dish composed of finely chopped raw meat "Tartare" redirects here.   │
# │ For the sauce, see Tartar sauce.                                             │
# │                                                                              │
# │                                                                              │
# │   ---                ---                                                     │
# │  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━                   │
# │   Course             Main course                                             │
# │   Place of origin    France                                                  │
# │   Main ingredients   Raw beef                                                │
# │   Variations         Tartare aller-retour                                    │
# │   Cookbook           Steak tartare   Media: Steak tartare                    │
# │                                                                              │
# │                                                                              │
# │ Steak tartare in the French Quarter of San Francisco Steak tartare or tartar │
# │ steak is a French dish of raw ground (minced) beef. It is usually served     │
# │ with onions, capers, parsley or chive, salt, pepper, Worcestershire sauce,   │
# │ and other seasonings, often presented separately, to be added to taste. It   │
# │ is commonly served topped with a raw egg yolk. It is similar to the          │
# │ Levantine kibbeh nayyeh, the Turkish çiğ köfte, the German Mett and the      │
# │ Korean yukhoe. The name tartare is sometimes generalized to other raw meat   │
# │ or fish dishes. In France, a less-common variant called tartare aller-retour │
# │ is a mound of mostly raw ground meat lightly seared on both sides.           │
# └──────────────────────────────────────────────────────────────────────────────┘
# ┌─────────────────────── [7] Tartarus (disambiguation) ────────────────────────┐
# │ Tartarus refers to a deity and place in Greek mythology. Tartarus may also   │
# │ refer to: Tartarus, a Greek New Testament word used for Hell (in Christian   │
# │ belief), derived from the pagan Greek use. Tartaros, a Norwegian black metal │
# │ solo project by Charmand Grimloch aka Joachim Rygg. Tartarus (spider), a     │
# │ genus of spiders in the family Stiphidiidae. Tartarus, the Latin name of the │
# │ river Tartaro-Canalbianco in Italy. HMS Tartarus, the name of three ships of │
# │ the Royal Navy and one planned one. Tartarus (DC Comics), a group of DC      │
# │ comic book supervillains. Tartarus, a character in the Halo universe.        │
# │ Tartarus Press, a limited edition publishing house. Tartaros, a dark guild   │
# │ from the anime/manga Fairy Tail. Tartarus, a 2005 film by Dave Wascavage.    │
# │ Tartarus/Tarterus, an evil Outer Plane in Dungeons & Dragons In other usage: │
# │ A fictional "hottest point" of the sun in the novel Seven Ancient Wonders. A │
# │ fictional planet in the computer game Warhammer 40,000: Dawn of War. A       │
# │ fictional planet in the Stargate SG-1 universe. The artificial person        │
# │ creation and maintenance arcology in Appleseed media. The name of the tower  │
# │ which is one of the primary locations in the video game Persona 3. The name  │
# │ of the landship piloted by Malkuthian colonel Jade Curtiss in the PS2 and    │
# │ 3DS video game Tales of the Abyss. The location villains are sent to in the  │
# │ cartoon series My Little Pony. The gate is guarded by Cerberus. A software   │
# │ backup program, for use in Unix and Unix-like environments such as Linux and │
# │ FreeBSD. The name of a special prison for villains in the anime/manga series │
# │ My Hero Academia. Topics referred to by the same term                        │
# └──────────────────────────────────────────────────────────────────────────────┘
# ┌─────────────────────────────── [8] Tartarian ────────────────────────────────┐
# │ Look up in Wiktionary, the free dictionary. Tartarian may be the adjective   │
# │ form of: Tartarus, a place in the underworld of Greek mythology Tartary, a   │
# │ historic name for much of Central and Northern Asia Tatars, several Turkic   │
# │ groups Tatar languages, several Turkic languages with the name               │
# └──────────────────────────────────────────────────────────────────────────────┘
# ┌────────────────────────── [9] Tartar > Other uses ───────────────────────────┐
# │ Tartar (horse), a racehorse Commander Tartar, the antagonist of the Splatoon │
# │ 2 Octo Expansion Dental tartar or calculus, hardened dental plaque Tartar    │
# │ Sauce, a swear word for SpongeBob SquarePants Wayne State Tartars, now       │
# │ called the Warriors Tartarus, in Greek mythology, a place in the underworld  │
# │ Tartarium, a middle age expensive fabric also known as Cloth of Tars         │
# └──────────────────────────────────────────────────────────────────────────────┘
# ┌───────────────────────────── [10] Tartar > Food ─────────────────────────────┐
# │ Steak tartare, a meat dish made from raw ground (minced) beef or horsemeat   │
# │ Tartar sauce, a condiment primarily composed of mayonnaise and finely        │
# │ chopped capers Cream of Tartar, the culinary name for potassium bitartrate,  │
# │ a dry, powdery, acidic byproduct of fermenting grapes into wine              │
# └──────────────────────────────────────────────────────────────────────────────┘
# ┌───────────────────── [11] Calculus (dental) > Etymology ─────────────────────┐
# │ The word comes from Latin calculus 'small stone', from calx 'limestone,      │
# │ lime', probably related to Greek χάλιξ chalix 'small stone, pebble, rubble', │
# │ which many[who?] trace to a Proto-Indo-European root for 'split, break up'.  │
# │ Calculus was a term used for various kinds of stones. This spun off many     │
# │ modern words, including calculate ('use stones for mathematical purposes'),  │
# │ and calculus, which came to be used, in the 18th century, for accidental or  │
# │ incidental mineral buildups in human and animal bodies, like kidney stones   │
# │ and minerals on teeth. Tartar, on the other hand, originates in Greek as     │
# │ well (tartaron), but as the term for the white encrustation inside casks     │
# │ (a.k.a. potassium bitartrate, commonly known as cream of tartar). This came  │
# │ to be a term used for calcium phosphate on teeth in the early 19th century.  │
# └──────────────────────────────────────────────────────────────────────────────┘
# ┌──────────────────── [12] Calculus (medicine) > Etymology ────────────────────┐
# │ The word comes from Latin calculus "small stone", from calx "limestone,      │
# │ lime", probably related to Greek χάλιξ chalix "small stone, pebble, rubble", │
# │ which many trace to a Proto-Indo-European language root for "split, break    │
# │ up". Calculus was a term used for various kinds of stones. In the 18th       │
# │ century it came to be used for accidental or incidental mineral buildups in  │
# │ human and animal bodies, like kidney stones and minerals on teeth. Human     │
# │ gallstones, all removed from one patient. Grid scale 1 mm. Calculus          │
# │ developed from an arrowhead                                                  │
# └──────────────────────────────────────────────────────────────────────────────┘
# ┌────────────────────────── [13] Tartus > Etymology ───────────────────────────┐
# │ The name derives from Ancient Greek: Αντιάραδος, romanized: Anti-Arados      │
# │ (Antarados or Anti-Aradus, meaning "The town facing Aradus). In Latin, its   │
# │ name became Tortosa. The original name survives in its Arabic form as Ṭarṭūs │
# │ (Arabic: طَرْطُوس), from which the French Tartous and English Tartus derive.    │
# └──────────────────────────────────────────────────────────────────────────────┘
# ┌──────────────────── [14] Tartary > Geography and history ────────────────────┐
# │ Knowledge of Manchuria, Siberia and Central Asia in Europe prior to the 18th │
# │ century was limited. The entire area was known simply as "Tartary" and its   │
# │ inhabitants "Tartars". In the early modern period, as understanding of the   │
# │ geography increased, Europeans began to subdivide Tartary into sections with │
# │ prefixes denoting the name of the ruling power or the geographical location. │
# │ Thus, Siberia was Great Tartary or Russian Tartary, the Crimean Khanate was  │
# │ Little Tartary, Manchuria was Chinese Tartary, and western Central Asia      │
# │ (prior to becoming Russian Central Asia) was known as Independent Tartary.   │
# │ By the seventeenth century, however, largely under the influence of Catholic │
# │ missionary writings, the word "Tartar" came to refer to the Manchus and the  │
# │ lands they ruled as "Tartary". European opinions of the area were often      │
# │ negative, and reflected the legacy of the Mongol invasions that originated   │
# │ from this region. The term originated in the wake of the widespread          │
# │ devastation spread by the Mongol Empire. The adding of an extra "r" to       │
# │ "Tatar" was suggestive of Tartarus, a Hell-like realm in Greek mythology. In │
# │ the 18th century, conceptions of Siberia or Tartary and its inhabitants as   │
# │ "barbarous" by Enlightenment-era writers tied into contemporary concepts of  │
# │ civilization, savagery and racism. More positive opinions were also          │
# │ expressed by Europeans. Some saw Tartary as a possible source of spiritual   │
# │ knowledge lacking in contemporary European society. In Five Years of         │
# │ Theosophy, edited by the Theosophist and scholar G.R.S. Mead, the polymath   │
# │ and "seer" Emanuel Swedenborg is quoted as having advised, "Seek for the     │
# │ Lost Word among the hierophants of Tartary, China, and Tibet."               │
# └──────────────────────────────────────────────────────────────────────────────┘
# ┌─────────────────────── [15] Tartarus (spider) > Names ───────────────────────┐
# │ The genus name is derived from Tartarus, a place in the underworld of Greek  │
# │ mythology, even lower than Hades. All four species take their common names,  │
# │ and the specific epithet, from the caves in which they were first collected. │
# │ Tartarus murdochensis and Tartarus thampannensis are both commonly called    │
# │ Murdoch sink cave spider, Tartarus nurinensis is also known as the Nurina    │
# │ cave spider.                                                                 │
# └──────────────────────────────────────────────────────────────────────────────┘
# ┌──────────────── [16] Greek underworld > Geography > Tartarus ────────────────┐
# │ In some Greek sources Tartarus is another name for the underworld (serving   │
# │ as a metonym for Hades), while in others it is a completely distinct realm   │
# │ separate from the underworld. Hesiod most famously describes Tartarus as     │
# │ being as far beneath the underworld as the earth is beneath the sky. Like    │
# │ Hades, it too is so dark that the "night is poured around it in three rows   │
# │ like a collar round the neck, while above it grows the roots of the earth    │
# │ and of the unharvested sea." The most famous inhabitants of Tartarus are the │
# │ Titans; Zeus cast the Titans along with his father Cronus into Tartarus      │
# │ after defeating them. Homer wrote that Cronus then became the king of        │
# │ Tartarus. According to Plato's Gorgias (c. 400 BC), souls are judged after   │
# │ death and Tartarus is where the wicked received divine punishment. Tartarus  │
# │ is also considered to be a primordial force or deity alongside entities such │
# │ as the Earth, Night, and Time.                                               │
# └──────────────────────────────────────────────────────────────────────────────┘
# ┌────────────────────────── [17] Tzatziki > History ───────────────────────────┐
# │ Tarator was the name of a dish made of ground walnuts and vinegar in the     │
# │ Ottoman Empire. Dishes of various preparations in the region, including      │
# │ dips, salads, and sauces, acquired the name. In the Levant, tarator is a     │
# │ sauce based on tahini, while in Turkey and the Balkans it came to mean a     │
# │ combination of yogurt and cucumbers, sometimes with walnuts. It has become a │
# │ traditional part of meze.                                                    │
# └──────────────────────────────────────────────────────────────────────────────┘
# ┌───────────────────────────── [18] Ğ > Tatar use ─────────────────────────────┐
# │ The Turkic Tatar language is written mostly in Cyrillic, but a Latin-based   │
# │ alphabet is also in use. In the Latin alphabet, ğ represents /ʁ/, the voiced │
# │ uvular fricative. In Cyrillic, Tatar uses г for both g and ğ without         │
# │ distinction. Tatar ğ / г is the Arabic ghayn غ. In Arabic words and names    │
# │ where there’s an ayin ع, Tatar adds the ghayn instead (عبد الله, ʻAbd Allāh, │
# │ ’Abdullah; Tatar: Ğabdulla, Габдулла; Yaña imlâ: غابدوللا /ʁabdulla/). In    │
# │ the Mishar Tatar Dialect, ğ is not pronounced, and thus, a word like şiğır   │
# │ (شعر, шигыр, "poem") is şigır or şiyır for Mishars (who in Finland use the   │
# │ Latin alphabet).                                                             │
# └──────────────────────────────────────────────────────────────────────────────┘
# ┌──────────────────────────────── [19] Tartary ────────────────────────────────┐
# │ Historical term for northern and central Asia Not to be confused with        │
# │ Tatarstan, Strait of Tartary, or Tărtăria. Map of independent Tartary (in    │
# │ yellow) and Chinese Tartary (in violet), in 1806. Tartary (Latin: Tartaria;  │
# │ French: Tartarie; German: Tartarei; Russian: Тартария, romanized: Tartariya) │
# │ or Tatary (Russian: Татария, romanized: Tatariya) was a blanket term used in │
# │ Western European literature and cartography for a vast part of Asia bounded  │
# │ by the Caspian Sea, the Ural Mountains, the Pacific Ocean, and the northern  │
# │ borders of China, India and Persia, at a time when this region was largely   │
# │ unknown to European geographers. The active use of the toponym (place name)  │
# │ can be traced from the 13th to the 19th centuries. In European sources,      │
# │ Tartary became the most common name for Central Asia that had no connection  │
# │ with the real polities or ethnic groups of the region; until the 19th        │
# │ century, European knowledge of the area remained extremely scarce and        │
# │ fragmentary. In modern English-speaking tradition, the region formerly known │
# │ as Tartary is usually called Inner Asia or Central Eurasia. Much of this     │
# │ area consists of arid plains, the main nomadic population of which in the    │
# │ past was engaged in animal husbandry. Ignorance surrounding Tartary's use as │
# │ a place name has spawned conspiracy theories including ideas of a "hidden    │
# │ past" and "mud floods". Such theories assert that Tartary (or the "Tartarian │
# │ Empire") was a lost civilization with advanced technology and culture. This  │
# │ ignores the well-documented history of Asia, which Tartary refers to. In the │
# │ present day, the Tartary region spans from central Afghanistan to northern   │
# │ Kazakhstan, as well as areas in present Mongolia, China and the Russian Far  │
# │ East in "Chinese Tartary".                                                   │
# └──────────────────────────────────────────────────────────────────────────────┘
#
# Request duration: 487.93 seconds