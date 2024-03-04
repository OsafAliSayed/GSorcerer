# GSorcerer - GSoC Issue Finder

## Description
Gsorcerer lets you find issues and search GitHub codebases for the organizations coming every year. Here you can find all the GSoC organizations and their GitHub open issues(Usually Good first issues).

## Setup

To set up the project follow the given steps:
- clone this repo using ```git clone https://github.com/OsafAliSayed/GSorcerer.git```
- Enter the project directory ```cd GSorcerer```
- initialize a python environment ``` python -m venv venv ```
- start the environment ```venv/Scripts/activate``` for Windows or ```source venv/bin/activate``` for Linux-based OS.
- install dependencies ``` pip install -r requirements.txt ```
- Create migrations
  - ``` python manage.py makemigrations ```
  - ``` python manage.py migrate```
- Create super user to access admin panel ``` python manage.py createsuperuser ```
- Finally run the project using ``` python manage.py runserver ```


## Features

- GSorcerer lets you find/filter issues from organizations that come in GSoC
- You can then contribute to them easily by not having to go through GitHub repositories suitable for you.
- Find the organization and contribute by directly filtering from the site.
- Easy-to-use UI

## Screenshots
Here are some of the screenshots of the main project screens.

### Homepage: 

![image](https://github.com/OsafAliSayed/GSorcerer/assets/99737087/6890dc4d-8908-40f7-a6a1-34901ae13f5f)

### Issues page:

![image](https://github.com/OsafAliSayed/GSorcerer/assets/99737087/b097c6bf-704a-4b39-8a55-53b0f1887d46)

![image](https://github.com/OsafAliSayed/GSorcerer/assets/99737087/b26fb872-0ac5-4259-9ba3-8a8c82201ecd)

Make sure to star the repository if this helps you! 
