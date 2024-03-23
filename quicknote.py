#!/usr/bin/python3
from dotenv import load_dotenv
import os
import sys
import requests

load_dotenv('/home/maxhuppertz/Documents/Personal/Coding/Notion Scirpt/notion_script/.env')
database_id = os.getenv('DATABASE_ID')
database_name = os.getenv('DATABASE_NAME')
secret_key = os.getenv('SECRET_KEY')

URL_BASE = "https://api.notion.com/v1/pages"

thoughts = sys.argv[1:]


def create_request_body(note):
    request_body = {
        "parent": {
        "type": "database_id",
        "database_id": database_id,
        },
        "properties": {
            database_name: {
                "type": "title",
                "title": [{
                    "type": "text", "text": {
                        "content": note
                    }
                }]
            }
        }
    }
    return request_body


def send_note(request_body):
    headers = {
        "Authorization": "Bearer " + str(secret_key),
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }
    response = requests.post(URL_BASE, headers=headers, json=request_body)

    if response.status_code != 200:
        print("Error sending the note to Notion (status code: " + str(response.status_code) + ")")
        print(response.text)


for thought in thoughts:
    request_body = create_request_body(thought)
    send_note(request_body)
