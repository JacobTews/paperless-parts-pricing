import os
import requests
import pandas as pd
import pyodbc
from sqlalchemy import create_engine, text, exc, engine
from sqlalchemy.engine.url import URL
from datetime import datetime, timedelta
import time
import copy
from math import ceil

def load_config():
    return {
        "api_token": os.environ["API_TOKEN"],
        "NIM_portal_token": os.environ["NIM_PORTAL_TOKEN"],
        "MWCDC_connection": {
            "username": os.environ["DB_USERNAME"],
            "password": os.environ["DB_PASSWORD"],
            "host": os.environ["DB_HOST"],
            "database": os.environ["DB_NAME"],
            "driver": os.environ["DB_DRIVER"]
        }
    }

def setup_environment(config):
    # API Setup
    P3_API_TOKEN = config['api_token']
    P3_BASE_URL = 'https://api.paperlessparts.com'
    P3_HEADERS = {
        'Authorization': f'API-Token {P3_API_TOKEN}',
        'Content_Type': 'application/json'
    }

    NIM_API_TOKEN = config['NIM_portal_token']
    NIM_BASE_URL = 'https://api.norfolkiron.com/CustomerPortal_Test'
    NIM_HEADERS = {
        "x-api-key": NIM_API_TOKEN,
        'Content_Type': 'application/json',
    }

    NIM_PRICE_URL = NIM_BASE_URL + '/api/prices/stock'

    # DB Connection
    connectionInfo = config['MWCDC_connection']
    MWCDC_URL_OBJECT = engine.url.URL.create(
        'mssql+pyodbc',
        username=connectionInfo['username'],
        password=connectionInfo['password'],
        host=connectionInfo['host'],
        database=connectionInfo['database'],
        query={"driver": connectionInfo['driver']}
    )

    session = requests.Session()
    session.verify = False

    return {
        "P3_BASE_URL": P3_BASE_URL,
        "P3_HEADERS": P3_HEADERS,
        "NIM_HEADERS": NIM_HEADERS,
        "NIM_PRICE_URL": NIM_PRICE_URL,
        "MWCDC_URL_OBJECT": MWCDC_URL_OBJECT,
        "session": session
    }

def main(input_int):
    config = load_config()
    env = setup_environment(config)

    # Replace this block with your actual logic
    print(f"Received input: {input_int}")
    return {"message": "Script ran successfully", "input": input_int}
