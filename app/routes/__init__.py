from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#Protection Cross Site Request Forgery(CSRF)
app.secret_key = '32e3cea25294cca16cbb4401a83f86be' # Application secret key
#Database configuratio
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:antony2002@localhost/hakidb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # {{{{{{{{{{{{{{{{{{{{{{{{{{ SECURITY PARAMETERS}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

# # Set X-Frame-Options header to deny framing
# @app.after_request
# def set_xframe_options(response):
#     response.headers['X-Frame-Options'] = 'DENY'
#     return response

# # Set Strict-Transport-Security header to enforce HTTPS
# @app.after_request
# def set_strict_transport_security(response):
#     response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
#     return response

# # Set X-Content-Type-Options header to prevent MIME-sniffing
# @app.after_request
# def set_xcontent_type_options(response):
#     response.headers['X-Content-Type-Options'] = 'nosniff'
#     return response

# # {{{{{{{{{{{{{{{{{{{{{{{{{{{ END OF SECURITY PARAMETERS }}}}}}}}}}}}}}}}}}}}}}}}}}}
db = SQLAlchemy(app)

# Import models after initializing db
from app.models import Category, Post, Resource
#Importing routes.py
from app import routes


""" This file consists of imports and configurations that are needed to run the for the first time."""