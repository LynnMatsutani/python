import requests
from flask import Flask
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def hello():
    load_url = "https://www.ymori.com/books/python2nen/test1.html"
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    return soup.find("title").text

@app.route('/good')
def good():
    name = "Good"
    return name

if __name__ == "__main__":
    app.run(debug=True)