# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 11:02:06 2020

@author: OHyic

"""
# Import libraries
import os
import concurrent.futures
from random import randint
from GoogleImageScraper import GoogleImageScraper
from patch import webdriver_executable


def worker_thread(search_key, number_of_images, headless, min_resolution, max_resolution, keep_filenames):
    image_scraper = GoogleImageScraper(
        webdriver_path, image_path, search_key, number_of_images, headless, min_resolution, max_resolution)
    image_urls = image_scraper.find_image_urls()
    image_scraper.save_images(image_urls, keep_filenames)

    # Release resources
    del image_scraper


# Define file path
webdriver_path = os.path.normpath(os.path.join(
    os.getcwd(), 'webdriver', webdriver_executable()))
image_path = os.path.normpath(os.path.join(os.getcwd(), 'photos'))

# Add new search key into array ["cat","t-shirt","apple","orange","pear","fish"]

# Parameters
# Keep original URL image filenames

# Run each search_key in a separate thread
# Automatically waits for all threads to finish
# Removes duplicate strings from search_keys


def execute(
        search_key="Нападай",
        number_of_images=10,
        headless=True,
        min_resolution=(0, 0),
        max_resolution=(9999, 9999),
        max_missed=1000,
        number_of_workers=1,
        keep_filenames=False):
    worker_thread(open("./russian.txt", "r").readlines()[randint(0, 1532629)], number_of_images, headless,
                  min_resolution, max_resolution, keep_filenames)
