import requests

API_BOARD = 'http://a.4cdn.org/{0}/catalog.json'
API_THREAD = 'http://a.4cdn.org/{0}/thread/{1}.json'
IMG_SOURCE = 'http://i.4cdn.org/{0}/{1}'


def send_request(url):
    try:
        r = requests.get(url)
        return r.json()
    except ValueError:
        return None


def get_pages(board, page=None):
    json = send_request(API_BOARD.format(board))
    if json is not None:
        if page is None:
            return [page for page in json]
        return json[page - 1]['threads']
    else:
        return None


def get_thread_urls(pages):
    if pages is not None:
        urls = [str(thread['no']) for page in pages
                for thread in page['threads']]
        return urls
    else:
        return None


def get_pictures_urls(thread, board, min_pic_width=0, min_pic_height=0):
    json = send_request(API_THREAD.format(board, str(thread)))
    if json is not None:
        urls = [IMG_SOURCE.format(board, str(post['tim']) + post['ext'])
                for post in json['posts'] if 'tim' in post
                if 'ext' in post if post['w'] > min_pic_width
                if post['h'] > min_pic_height]
        return urls
    else:
        return None
