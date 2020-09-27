#!/usr/bin/python3
import gspread
import os.path
import sys
from oauth2client.service_account import ServiceAccountCredentials
import pprint
from datetime import datetime

client_secret = 'credentials.json'

from oauth2client.service_account import ServiceAccountCredentials

# Google
gscope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
gcredentials = 'credentials.json'
gdocument = 'Рестораны'

def add_to_gsheet(message, data, text):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(gcredentials, gscope)
    gc = gspread.authorize(credentials)
    wks = gc.open(gdocument).sheet1
    wks.append_row(
        [datetime.now().strftime('%d.%m.%Y %H:%M:%S'), 'колонка1', 'колонка2', 'колонка3', 'колонка4'])
        
add_to_gsheet(1,2,3)