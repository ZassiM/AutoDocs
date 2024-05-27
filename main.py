import random
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# List of random search terms
search_terms = ['hello world', 'selenium python', 'today’s weather', 'best movies 2022', 'python examples']

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Go to the Google home page
driver.get("http://www.google.com")
time.sleep(2)  # Wait for 2 seconds after loading the page

# Accept all
driver.find_element(By.XPATH, "//div[text()='Accept all']").click()

# Find the search box element by its name attribute (update to the correct method for finding elements)
search_box = driver.find_element('name', 'q')

# Generate a random search term and enter it into the search box
random_search_term = random.choice(search_terms)
search_box.send_keys(random_search_term)
time.sleep(1)  # Wait for 1 second after typing the search term

# Hit Enter to submit the search
search_box.send_keys(Keys.RETURN)
time.sleep(2)  # Wait for 2 seconds to load the search results

# The browser will now display the search results for the random term
# Optionally, you can close the browser after a delay or after certain actions
# driver.quit()
