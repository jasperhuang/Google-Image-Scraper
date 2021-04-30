# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
#Import libraries
from GoogleImageScrapper import GoogleImageScraper
import os

#Define file path
webdriver_path = os.getcwd()+"/webdriver/chromedriver"
image_path = os.path.normpath(os.getcwd()+"/photos/bush")

#Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]
# search_keys = [
#     "holly berries", "mistletoe berries", "jerusalem cherries",
#     "woody nightshade berries", "pokeweed berries", "ivy berries",
#     "yew berries", "virginia creeper berries"
# ]
# search_keys = [
#     "elderberries", "cloudberries", "huckleberries",
#     "gooseberries", "chokeberries", "saskatoon berries",
#     "salmonberries", "buffaloberries"
# ]
# search_keys = [
#     "holly berries", "mistletoe berries"
# ]

search_keys = ['european box plant']

# for different folders if you want to download actual images
# image_paths = []
# for key in search_keys:
#     image_paths.append(
#         os.path.normpath(
#             os.getcwd() + "/photos/" + key.replace(" ", "")
#         )
#     )

#Parameters
number_of_images = 200
headless = False
min_resolution=(0,0)
max_resolution=(2056,2056)

#Main program
for search_key in search_keys:
    print(search_key + " = " + image_path)
    image_scrapper = GoogleImageScraper(
        webdriver_path, image_path, search_key,
        number_of_images, headless, min_resolution,
        max_resolution
    )
    image_urls = image_scrapper.find_image_urls()
    # write all urls to a text file
    image_scrapper.save_image_textfile(
        write_path=image_path,
        file_name=search_key.replace(" ", ""),
        image_urls=image_urls
    )
    # image_scrapper.save_images(image_urls)