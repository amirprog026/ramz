
# Fernet Encryption/Decryption API


This project is a Flask-based API for encrypting and decrypting text using the Fernet encryption library. The API is secured by an API token and can be deployed using Docker. This guide provides instructions for setup, configuration, and usage.


## Structure
- app.py: Main Flask application file for API endpoints.
- conf.ini: Configuration file for storing constants like encryption keys and tokens.
- Dockerfile: Used to build the Docker image for the Flask API.
- Jenkinsfile: Pipeline configuration for CI/CD using Jenkins.
- requirements.txt: Python dependencies required to run the app.
- forms.py: Flask-WTF form for encrypting text via a web interface.
- templates/: Contains the HTML template (encrypt.html) for the encryption form UI.
- tests/: Contains unit tests for API functionality (optional).

## Prerequirements
- Prerequisites
- Python 3.9+
- Docker
- Jenkins (for CI/CD pipeline)
- Git

## Configuration
You need to make your own `conf.ini` file:
```
[APP]
KEY = your_32B_key(hex)  
TOKEN = your_api_token           
SECRET = your_secret_key        
```
## Guide
using `Guicorn` is suggested for production use.

to run the app you must write your own Dockerfile | docker-compose.yaml

```
curl -X POST http://127.0.0.1:5000/api/encrypt \
  -H "Authorization: Bearer your_api_token" \
  -H "Content-Type: application/json" \
  -d '{"text": "Your text to encrypt"}'

```

```
curl -X POST http://127.0.0.1:5000/api/decrypt \
  -H "Authorization: Bearer your_api_token" \
  -H "Content-Type: application/json" \
  -d '{"encrypted_text": "your_encrypted_text_here"}'

```
##Written By
## Acknowledgements

 - [Written By Amir Ahmadabadiha](https://ir.linkedin.com/in/amir-ahmadabadiha-259113175)
