# DeshGhure 🇧🇩

DeshGhure is a travel and exploration web application focused on Bangladesh. It helps users discover beautiful destinations, explore different divisions, and create a personalized travel experience.

## Overview

Bangladesh has many hidden travel destinations, but people often struggle to find organized information in one place. DeshGhure solves this by providing a structured and interactive platform where users can:

- explore destinations by division
- view travel spots with details
- plan trips and maintain a travel bucket list

This project is built as part of a full-stack Django learning journey.

## Features

### Destination Exploration
- Browse travel destinations across Bangladesh
- Division-based navigation system
- Clean and modern UI

### Interactive Map (Planned / In Progress)
- Clickable map of Bangladesh divisions
- Hover effects for better UX

### Travel Details
- View information about each destination
- Images and descriptions of places

### Bucket List (Planned)
- Save favorite destinations
- Track places you want to visit

### User System (Optional / Future)
- User registration and login
- Personalized travel experience

## Tech Stack

### Backend
- Django
- Django ORM

### Frontend
- HTML
- CSS
- Tailwind CSS
- JavaScript

### Database
- SQLite (development)
- PostgreSQL (planned for production)

## Project Structure

```

DeshGhure/
│
├── deshghure/          # main Django project
├── destinations/       # app for managing destinations
├── templates/          # HTML templates
├── static/             # CSS, JS, images
├── media/              # uploaded images
├── db.sqlite3
└── manage.py

````

## Installation

### 1. Clone the Repository

```bash id="clone01"
git clone https://github.com/AsifIqbal011/DeshGhure.git
cd DeshGhure
````

### 2. Create Virtual Environment

```bash id="venv01"
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```

### 3. Install Dependencies

```bash id="install01"
pip install -r requirements.txt
```

### 4. Run Migrations

```bash id="migrate01"
python manage.py makemigrations
python manage.py migrate
```

### 5. Run Server

```bash id="run01"
python manage.py runserver
```

Open browser:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Demo Video

Click below to watch the project demo:

<p align="center">
  <a href="https://www.youtube.com/watch?v=1X2ZwsSt95U">
    <img src="https://img.youtube.com/vi/1X2ZwsSt95U/0.jpg" width="700">
  </a>
</p>

## Future Improvements

* AI-based travel recommendation system
* Weather integration for destinations
* Hotel and transport suggestions
* Mobile responsive enhancements
* Full user authentication system
* Review and rating system

## Use Case

DeshGhure is useful for:

* travelers exploring Bangladesh
* students learning Django projects
* tourism-related applications

It provides a centralized platform to discover and plan trips efficiently.


## Author

Asif Iqbal
GitHub: [https://github.com/AsifIqbal011](https://github.com/AsifIqbal011)

```
