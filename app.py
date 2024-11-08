from flask import Flask, request, jsonify, abort
from cryptography.fernet import Fernet
from functools import wraps
from forms import EncryptForm

app = Flask(__name__)
app.secret_key = 'your_secret_key'  

# Generate a Fernet key and use it to create a Fernet instance
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Set your API token
API_TOKEN = 'your_api_token'

# Decorator to check API token
def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token != f"Bearer {API_TOKEN}":
            abort(403, description="Forbidden: Invalid API Token")
        return f(*args, **kwargs)
    return decorated_function

# Route to encrypt text
@app.route('/api/encrypt', methods=['POST'])
@token_required
def encrypt_text():
    data = request.json.get("text")
    if not data:
        return jsonify({"error": "Text is required"}), 400
    encrypted_text = cipher_suite.encrypt(data.encode())
    return jsonify({"encrypted_text": encrypted_text.decode()}), 200

# Route to decrypt text
@app.route('/api/decrypt', methods=['POST'])
@token_required
def decrypt_text():
    data = request.json.get("encrypted_text")
    if not data:
        return jsonify({"error": "Encrypted text is required"}), 400
    try:
        decrypted_text = cipher_suite.decrypt(data.encode()).decode()
        return jsonify({"decrypted_text": decrypted_text}), 200
    except Exception as e:
        return jsonify({"error": "Invalid encrypted text"}), 400

# Encrypt web form route
@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt_form():
    form = EncryptForm()
    encrypted_result = None
    if form.validate_on_submit():
        text_to_encrypt = form.text.data
        encrypted_result = cipher_suite.encrypt(text_to_encrypt.encode()).decode()
    return render_template('encrypt.html', form=form, encrypted_result=encrypted_result)

if __name__ == '__main__':
    app.run(debug=True)
