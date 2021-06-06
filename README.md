<<<<<<< HEAD
# Shiopa-Backend-DjangoRestFramework
Siopa is an ecommerce application built on Django Rest Framework
=======
# Shiopa DRF Backend

## Quick Setup

Make sure you have **Python 3.x** installed and **the latest version of pip** *installed* before running these steps.

Clone the repository using the following command

```bash
git clone https://github.com/Techminate/Shiopa-Backend-DRF.git
# After cloning, move into the directory having the project files using the change directory command
cd Shiopa-Backend-DRF
```
Create a virtual environment where all the required python packages will be installed

```bash
# Use this on Windows
python -m venv env
# Use this on Linux and Mac
python -m venv env
```
Activate the virtual environment

```bash
# Windows
.\env\Scripts\activate
# Linux and Mac
source env/bin/activate
```
Install all the project Requirements
```bash
pip install -r requirements.txt
```
-Apply migrations

```bash
# apply migrations and create your database
python manage.py migrate

# Create a user with manage.py
python manage.py createsuperuser
```

Run the development server

```bash
# run django development server
python manage.py runserver

```

Default Admin User

```bash
# Username : admin
# Email: admin@email.com
# Password: Password

```

