import time
import pandas as pd
import logging
import requests
import json
import os
from urllib.parse import urlparse
import streamlit as st

from urllib.parse import urlparse

def extract_domain_name(url):
    """
    A function to extract domain from an API link.
    
    Parameters:
        url : str
            URL of the API.
    
    Returns:
        str or None:
            Domain of the link if valid, else None.
    """
    
    # Ensure the URL has a scheme; if not, then prepend 'http://'
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    print(url)

    if domain:
        return domain
    else:
        return None

extract_domain_name("https://openlibrary.org/search.json?q=the+lord+of+the+rings")
# ------------------------------------------------------------------------------------

def Extracting_data(link, domain):
    """Function to extract data from an domain
    Params:
    ------
        domain(str) : domain name to extract data from
        size(int)(default=1) : size of the data to extract
    """

    try:
        logging.info(f"Trying to connect to {domain} and decoding to .json()!!")
        st.info(f"Trying to connect to {domain} and decoding to .json()!!")

        response = requests.get(link)
        response.raise_for_status()
        response_json = response.json()
    
    except requests.exceptions.JSONDecodeError as e:
        logging.error(f"Unable to decode json for {domain} data.")
        st.error(f"Unable to decode json for {domain} data.")

    
    except Exception as e:
        logging.error(f"An Error occured : {e}")
        st.warning(f"An Error occured : {e}")


    else:
        logging.info(f"Connection to {domain} and decoding to .json() is successful!!")
        st.info(f"Connection to {domain} and decoding to .json() is successful!!")
        

    sample_file_name = f"sample_json/{domain}_sample.json"
    raw_file_name = f"raw_json/{domain}_raw.json"

    try:
        logging.info(f"Trying to save {domain} data to sample directory!!")
        st.info(f"Trying to save {domain} data to sample directory!!")
        
        # # Trying to create a directory and if it exists do nothing (nothing means - don't raise fileExistsException)
        # if not os.path.exists("sample_json"):
        #     os.mkdir("sample_json")

        # st.write(response_json[0])

        # sample_file_name = f"sample_json/{domain}_sample.json"
        # with open(sample_file_name, "w") as file:
        #     json.dump(response_json[0], file)

        # Trying to create a directory and if it exists do nothing (nothing means - don't raise fileExistsException)
        if not os.path.exists("raw_json"):
            os.mkdir("raw_json")
        
        with open(raw_file_name, "w") as file:
            json.dump(response_json, file)

    except Exception as e:
        logging.error(f"An exception occured while saving data to {raw_file_name} : {e}!!!")
        st.error(f"An exception occured while saving data to {raw_file_name} :{e}!!!")
        return 

    else:
        logging.info(f"Data successfully saved in {raw_file_name}")
        st.info(f"Data successfully saved in {raw_file_name}")

    logging.info(f"Extraction for {domain} completed successfully!!!")
    st.write(f"Extraction for {domain} completed successfully!!!")

# Extracting_data("https://stephen-king-api.onrender.com/api/books","stephenking" )