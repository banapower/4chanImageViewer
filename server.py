from flask import Flask, render_template
from utils import get_pages, get_thread_urls, get_pictures_urls, BOARD
app = Flask(__name__)


@app.route('/')
def show_threads():
    urls = get_thread_urls(get_pages())
    return render_template('home.html', urls=urls, board=BOARD)


@app.route('/thread/<int:thread>')
def thread_page(thread):
    urls = get_pictures_urls(thread)
    return render_template('thread.html', board=BOARD, urls=urls)
