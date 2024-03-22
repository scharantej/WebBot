
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

chat_gpt_api_key = 'YOUR_CHAT_GPT_API_KEY'
chat_gpt_api_url = 'https://generativelanguage.googleapis.com/v1beta2/models/text-bison-001:generateText?key={}'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/build', methods=['POST'])
def build():
    prompt = request.form['prompt']
    headers = {'Content-Type': 'application/json'}
    data = {'prompt': {'text': prompt}, 'maxTokens': 1000}
    response = requests.post(
        chat_gpt_api_url.format(chat_gpt_api_key), json=data, headers=headers)
    website_spec = response.json()
    return render_template('preview.html', website_spec=website_spec)

@app.route('/preview')
def preview():
    website_spec = request.args.get('website_spec')
    return render_template('preview.html', website_spec=website_spec)

if __name__ == '__main__':
    app.run(debug=True)
