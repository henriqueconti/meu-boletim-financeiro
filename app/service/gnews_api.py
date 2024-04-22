import os
import requests
from retry import retry
from requests.exceptions import Timeout

api_url = os.getenv('GNEWS_API_URL')


@retry(Timeout)
def get_news_info() -> dict:
    try:
        response = requests.get(api_url)

        return response.json()
    except Timeout as e:
        raise e
    except Exception as e:
        print('Request API Error: ', str(e))
