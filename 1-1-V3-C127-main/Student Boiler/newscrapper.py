from selenium import webdriver 
from selenium.webdriver.common.by import By  
from bs4 import BeautifulSoup  
import time 
import pandas as pd 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC  
# import request module
import requests 

browser = webdriver.Chrome() 
new_planets_data = []  

def scrape_more_data(hyperlink):
        # Use request to get the hyperlink and store in page variable
        page = requests.get(hyperlink)
        # Create soup using BeautifulSoup
        soup = BeautifulSoup(browser.page.content , "html.parser")
        # Create empty temp_list
        temp_list = []
        # Create a list information_to_extract with text of each div for which information is needed
        information_to_extract = ["Light-Years From Earth", "Planet Mass", 
                                      "Stellar Magnitude", "Discovery Date"]

        # Run a for loop for each info_name in  information_to_extract
        for info_name in information_to_extract :
             # Add try block
            try : 
                # Get the value needed using find() and find_next() and append to temp_list
                value = soup.find('dive', text = info_name).find_next('span').text.strip()
                temp_list.append(value)
                
                # Add a except block
            except :
                temp_list.append('unknown') # Add Unknown to temp_list
            
        new_planets_data.append(temp_list) # append temp_list to new_planets_data
    
# Read the scrapped_data.csv in planet_df_1
df = pd.read_csv('crap_data.csv')
# Loop through each row 
for index,row in df.iterrows() :
     scrape_more_data(row['hyperlink'])
    # Print hyperlink
    
    # Call scrap_more_data and pass hyperlink
    
    # Print Data scrapping at hyperlink completed
    

headers = ["planet_type","discovery_date", "mass", "planet_radius", "orbital_radius", "orbital_period", "detection_method"]
new_planet_df_1 = pd.DataFrame(new_planets_data,columns = headers)
new_planet_df_1.to_csv('new_scraped_data.csv',index=True, index_label="id")