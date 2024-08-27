import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch the news website
    url = 'https://news.google.com'
    response = requests.get(url)

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the news headlines
    headlines = soup.find_all('a', class_='DY5T1d')

    # Extract the text from the headlines
    news_headlines = [headline.text for headline in headlines]

    # Render the template with the news headlines
    return render_template('index.html', headlines=news_headlines)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
