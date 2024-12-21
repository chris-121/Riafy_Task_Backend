## Prerequisites

- Python 3.8+
- pip
- virtualenv (optional)
- Django 4.0+

## Setup Instructions

### 1. Clone the repository:

```bash
git clone https://github.com/chris-121/Riafy_Task_Backend.git
cd Riafy_Task_Backend
```

### 2. Create and activate a virtual environment (Optional):

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

### 3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Apply migrations:

```bash
python3 manage.py migrate
```

### 5. Run server:

```bash
python manage.py runserver
```
