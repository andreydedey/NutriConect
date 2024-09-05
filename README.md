﻿# NutriConnect

Welcome! This guide will help you set up and run your Django project locally.

## Prerequisites

Before you begin, make sure you have the following installed on your system:
- Python 3.7 or later
- pip (Python package manager)
- Virtualenv (recommended)
- Git

  ## Step-by-Step Instructions
  First, clone the project repository from GitHub or your preferred source:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

  Create a Virtual Environment
```bash
python -m venv venv
```

Activate the virtual environment:
- On Windows:
```bash
python -m venv venv
```

- On macOS and Linux:
```bash
source venv/bin/activate
```

Install Dependencies
```bash
pip install -r requirements.txt
```

Set Up the Dabase
```bash
python manage.py migrate
```

Run the Development Server
```bash
python manage.py runserver
```
