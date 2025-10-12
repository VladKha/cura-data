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
