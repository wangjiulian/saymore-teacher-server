# SayMore Teacher API Server (Django)

A backend REST API service for English teachers on the SayMore platform, built with Django and Django REST framework.

## Overview

This server provides RESTful APIs for teacher-side functionality, such as managing schedules, classes, students, and teaching records.  
It serves as the backend for web and mini-program teacher clients in the SayMore ecosystem.

## Features

- **Authentication**: Login via SMS verification and JWT
- **Teacher Profile**: Manage personal info, teaching experience, and certifications
- **Course Management**: View, start, end, or cancel scheduled classes
- **Availability Settings**: Define weekly available teaching hours
- **Teaching Records**: Track completed sessions, hours, and compensation
- **Student Info**: View enrolled students and their progress

## Tech Stack

- **Framework**: Django 4.x
- **API Layer**: Django REST Framework (DRF)
- **Database**: PostgreSQL / MySQL / SQLite (via Django ORM)
- **Authentication**: JWT (via `djangorestframework-simplejwt`)
- **File Storage**: Local or Aliyun OSS (optional)
- **Docs**: Swagger / Redoc (via `drf-spectacular`)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-org/saymore-teacher-api.git
cd saymore-teacher-api
```

2. Set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure environment variables in `.env`:

```env
DJANGO_SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3
```

5. Apply migrations and create superuser:

```bash
python manage.py migrate
python manage.py createsuperuser
```

6. Run the server:

```bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/

## API Documentation

- Swagger UI: `/api/docs/`
- Redoc: `/api/redoc/`

## Testing

```bash
pytest
```

## Related Projects

- [SayMore Student Mini App](https://github.com/wangjiulian/saymore-mini)
- [SayMore Core Server](https://github.com/wangjiulian/saymore-server)

## License

MIT License © 2025 SayMore