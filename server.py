from flask import Flask, render_template, abort
from utils import get_pages, get_thread_urls, get_pictures_urls
app = Flask(__name__)


@app.route('/<string:board>/')
def show_threads(board):
    urls = get_thread_urls(get_pages(board))
    if urls is not None:
        return render_template('home.html', urls=urls, board=board)
    else:
        return render_template('404.html', board=board)


@app.route('/<string:board>/thread/<int:thread>')
def thread_page(board, thread):
    urls = get_pictures_urls(thread, board)
    if urls is not None:
        return render_template('thread.html', board=board, urls=urls)
    else:
        return render_template('404.html', thread=thread)
