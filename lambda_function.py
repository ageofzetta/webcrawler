import urllib3
from bs4 import BeautifulSoup as soup


def lambda_handler(event, context):
    url = event.get('url')
    http = urllib3.PoolManager()
    r = http.request('GET', url)

    page_soup = soup(r.data, "html.parser")
    meta_description = page_soup.find('meta', attrs={'name': 'description'})
    meta_title = page_soup.find('title')

    return {
        'statusCode': r.status,
        'metaDescription': meta_description.get('content'),
        'title': meta_title.string,
    }
