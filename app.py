from flask import Flask, render_template, request, jsonify
import random
import string
import os

app = Flask(__name__)

def generate_password(length=12, use_upper=True, use_numbers=True, use_special=True):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['GET'])
def generate():
    length = int(request.args.get('length', 12))
    use_upper = request.args.get('use_upper', 'true').lower() == 'true'
    use_numbers = request.args.get('use_numbers', 'true').lower() == 'true'
    use_special = request.args.get('use_special', 'true').lower() == 'true'
    password = generate_password(length, use_upper, use_numbers, use_special)
    return jsonify(password=password)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

