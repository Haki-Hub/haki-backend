import requests
from flask import current_app

def get_wagtail_pages():
    api_url = f"{current_app.config['WAGTAIL_API_BASE_URL']}pages/"
    response = requests.get(api_url)
    return response
