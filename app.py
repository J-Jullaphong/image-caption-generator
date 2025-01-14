from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get the API URL and token from environment variables
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-base"
headers = {"Authorization": f"Bearer {os.getenv('HUGGINGFACE_API_KEY')}"}

# Set the upload folder from environment variables
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER', 'static/uploads')
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


def get_caption(response):
    if isinstance(response, list) and len(response) > 0:
        return response[0].get('generated_text', 'Error: No caption was generated.')
    return 'Error: No caption was generated.'


def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return get_caption(response.json())


@app.route('/', methods=['GET', 'POST'])
def index():
    caption = None
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            caption = query(filepath)

    return render_template('index.html', caption=caption)


if __name__ == '__main__':
    app.run(debug=True)
