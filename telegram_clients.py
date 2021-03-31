#!/usr/bin/python3.8
import json
import requests
import datetime, time
from config import *


url = f'https://api.telegram.org/bot{token_bot}/getUpdates'
r = requests.get(url)
todos = json.loads(r.text)
json.dumps(todos)

update_id_list = []

for i in todos['result']:
    if 'edited_message' in i or 'message' in i:
        if 'edited_message' in i:
            update_id = i['update_id']
            chat_id = i['edited_message']['chat']['id']
            chat_name = i['edited_message']['chat']['title']
            message = i['edited_message']['text']
            nick_name = i['edited_message']['from']['username']
            datetime_message = i['edited_message']['date']
            time_message = datetime.datetime.utcfromtimestamp(datetime_message).time()
            date_message = datetime.datetime.utcfromtimestamp(datetime_message).date()
            print(f"{update_id} : {chat_name} : {chat_id} : {time_message} : {date_message} - {message} - {nick_name}")
        else:
            update_id = i['update_id']
            chat_id = i['message']['chat']['id']
            chat_name = i['message']['chat']['title']
            message = i['message']['text']
            nick_name = i['message']['from']['username']
            datetime_message = i['message']['date']
            time_message = datetime.datetime.utcfromtimestamp(datetime_message).time()
            date_message = datetime.datetime.utcfromtimestamp(datetime_message).date()
            print(f"{update_id} : {chat_name} : {chat_id} : {time_message} : {date_message} - {message} - {nick_name}")


