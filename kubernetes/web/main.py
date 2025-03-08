from flask import Flask, render_template
import requests

app = Flask(__name__)

DOG_API_URL = "https://dog.ceo/api/breeds/image/random"

@app.route('/dog')
def home():
    # Fetch a random dog image
    response = requests.get(DOG_API_URL)
    data = response.json()
    dog_image_url = data["message"]  # Extract image URL

    return render_template('dog.html', dog_image_url=dog_image_url)

if __name__ == '__main__':
    app.run(debug=True)
