from flask import Flask, render_template, jsonify
import requests
import os
from dotenv import load_dotenv

# Will load viariables from .env file
# No need to hardcode API keys
load_dotenv()

API_URL = f'https://api.api-ninjas.com/v1/jokes?'
API_KEY = os.getenv("API_KEY")

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    joke = fetch_joke()
    return render_template("index.html", joke=joke)

# Make the API request
def fetch_joke():
    response = requests.get(API_URL, headers={'X-Api-Key': API_KEY})

    if response.status_code == requests.codes.ok:
        # Returns a joke
        return response.json()[0]["joke"]
    else:
        # If errors
        return jsonify({
            'error': response.status_code,
            'message': response.text
        }), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
