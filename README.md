# Stock Tracker (Internship Assignment - Parksons Graphics)

A Django-based inventory tracking web app with basic UI (Django admin).

## Features

- Add products with description and quantity
- Record transactions (stock movement)
- Track individual product-level quantity changes
- Django Admin interface for easy data management

## Tech Stack

- Python 3
- Django 4.x
- SQLite (for demo)

## How to Run Locally

```bash
git clone https://github.com/Adicoder24hr/stocktracker.git
cd stocktracker
python -m venv env
source env/bin/activate  # or `env\Scripts\activate` on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # create admin user
python manage.py runserver
