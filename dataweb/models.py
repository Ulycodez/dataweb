from django.db import models

# Create your models here.
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Website(db.Model):
    __tablename__ = 'websites'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    niche = db.Column(db.String, nullable=False)
    
    def __init__(self, name, niche):
        self.name = name
        self.niche = niche
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'niche': self.niche
        }

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    website_id = db.Column(db.Integer, db.ForeignKey('website.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    title = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    
    def __init__(self, website_id, customer_id, title, category):
        self.website_id = website_id
        self.customer_id = customer_id
        self.title = title
        self.category = category
    
    def serialize(self):
        return {
            'id': self.id,
            'website_id': self.website_id,
            'customer_id': self.customer_id,
            'title': self.title,
            'category': self.category
        }

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    website_id = db.Column(db.Integer, db.ForeignKey('website.id'), nullable=False)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    
    
    def __init__(self, account_id, website_id, first_name, last_name):
        self.account_id = account_id
        self.website_id = website_id
        self.first_name = first_name
        self.last_name = last_name
    
    def serialize(self):
        return {
            'id': self.id,
            'account_id': self.account_id,
            'website_id': self.website_id,
            'first_name': self.first_name,
            'last_name': self.last_name
        }

class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    website_id = db.Column(db.Integer, db.ForeignKey('website.id'), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    
    
    def __init__(self, website_id, username, password):
        self.website_id = website_id
        self.username = username
        self.password = password
    
    def serialize(self):
        return {
            'id': self.id,
            'website_id': self.website_id,
            'username': self.username
        }