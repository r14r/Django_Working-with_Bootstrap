# Introduction

## Preperation

### Check Python Version

    $ python -m django --version

### Install Django

Read here: https://docs.djangoproject.com/en/2.2/topics/install/

    pip install django djangorestframework django-cors-headers

### Install Reqirements

    npm -g install yarn
    yarn add bootstrap jquery popper webpack webpack-cli

### Create a project

    $ django-admin startproject main

### Run Development Server

\$ python manage.py runserver

### Create app App

    cd main
    python manage.py startapp app

### Migrate database

    $ python manage.py migrate

### Deploy

    python setup.py sdist

### Install from Deploy Package

    pip install --user django-app/dist/django-app-0.1.tar.gz
