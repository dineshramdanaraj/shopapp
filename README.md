
# ShopApp - Online Poster Store

Welcome to ShopApp, an online poster store developed using Django! This project allows users to browse and purchase posters seamlessly, with integrated payment functionality via Instamojo. The website is powered by Django, utilizes SQLite for database storage, and is hosted on PythonAnywhere.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Database](#database)
- [Payment Gateway](#payment-gateway)
- [User Accounts](#user-accounts)
- [Rating and Reviews](#rating-and-reviews)
- [Order History and Returns](#order-history-and-returns)
- [Hosting](#hosting)
- [Contributing](#contributing)
- [License](#license)

## Features
- Browse a wide variety of posters
- Add posters to the shopping cart
- Secure and seamless payment process using Instamojo
- User authentication and authorization
- User registration and login
- User accounts for a personalized experience
- Rating system for posters
- Reviews for user feedback
- Order history for tracking past purchases
- Return option for eligible orders
- Admin panel for managing products, orders, and user accounts
- Responsive design for a great user experience across devices

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/shopapp.git
   cd shopapp
   
2. Create a virtual environment (optional but recommended):

```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
3. Install dependencies:

```bash

pip install -r requirements.txt
```
4.Apply database migrations:

```bash

python manage.py migrate
```
5.Create a superuser (admin):

```bash
python manage.py createsuperuser
Usage
```
6.Run the development server:

```bash
python manage.py runserver
```
Open your browser and visit http://127.0.0.1:8000/ to access the website.

Log in with the superuser credentials to access the admin panel.

Database
ShopApp uses SQLite as its database. You can manage the database using Django's admin panel or Django shell.

To make changes to the models, run:

```bash

python manage.py makemigrations
python manage.py migrate
```
Payment Gateway
ShopApp integrates with Instamojo for secure online payments. Make sure to configure your Instamojo API credentials in the settings.

User Accounts
Users can register and create accounts for a personalized shopping experience. The registration and login functionality are included.

Rating and Reviews
Users can rate posters and leave reviews, providing valuable feedback for other shoppers.

Order History and Returns
ShopApp keeps a record of users' order history, and eligible orders can be returned through a simple process.

Hosting
The website is hosted on PythonAnywhere. Follow their documentation for deploying Django projects.
