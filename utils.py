import requests

BOARD = 'wg'

API_BOARD = 'http://a.4cdn.org/{0}/catalog.json'.format(BOARD)
API_THREAD = 'http://a.4cdn.org/{0}/thread/{1}.json'

IMG_SOURCE = 'http://i.4cdn.org/{0}/{1}'


def send_request(url):
    r = requests.get(url)
    return r.json()


def get_pages(page=None):
    json = send_request(API_BOARD)
    print len(json)
    if page is None:
        return [page for page in json]
    return json[page - 1]['threads']


def get_thread_urls(pages):
    urls = [str(thread['no']) for page in pages for thread in page['threads']]
    return urls


def get_pictures_urls(thread):
    json = send_request(API_THREAD.format(BOARD, str(thread)))
    urls = [IMG_SOURCE.format(BOARD, str(post['tim']) + post['ext'])
            for post in json['posts']if 'tim' in post
            if 'ext' in post if post['w'] > 700]
    return urls
