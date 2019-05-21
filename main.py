from flask import Flask, Response
import requests
import os
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():
    response = requests.get("http://unkno.com/")

    soup = BeautifulSoup(response.content, "html.parser")
    return soup.find("div", id="content").getText().strip()


def latinize(text):
    payload = {'input_text': text}
    response = requests.post('https://hidden-journey-62459.herokuapp.com/piglatinize/',
                             data=payload)

    return response.url


@app.route('/')
def home():
    fact = get_fact()
    address = latinize(fact)
    html = f'<a href="{address}">{address}</a>'
    return Response(html, mimetype="text/html")


if __name__ == '__main__':
    port = os.environ.get("PORT", 8080)
    app.run(host='0.0.0.0', port=port)

