# 🎓 University Calendar

<div align="center">

![Django](https://img.shields.io/badge/Django-5.1.4-green?style=for-the-badge&logo=django)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightblue?style=for-the-badge&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

**A comprehensive academic calendar management system for universities, featuring festival information, event tracking, and email notifications.**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Project Structure](#-project-structure) • [API Endpoints](#-api-endpoints) • [Contributing](#-contributing)

</div>

---

## 📋 Overview

University Calendar is a Django-based web application designed to help students and faculty manage academic events, track important dates, and stay informed about festivals and holidays throughout the year. The system provides a user-friendly interface for creating, updating, and organizing calendar events with email notifications.

## ✨ Features

### 🔐 Authentication System
- **User Registration** - Secure sign-up with email verification
- **User Login** - Email-based authentication
- **Session Management** - Persistent login sessions

### 📅 Calendar Management
- **Add Events** - Create custom events with titles, dates, and descriptions
- **Event Categories** - Organize events by type (Holiday, Exam, Lecture, Other)
- **Update Events** - Modify existing events
- **Delete Events** - Remove unwanted events
- **View Events** - Browse all personal calendar events
- **Categorized View** - Filter events by upcoming, current, and completed

### 📧 Email Notifications
- **Event Reminders** - Automatic email notifications when new events are created
- **SMTP Integration** - Gmail SMTP configuration for reliable email delivery

### 🎉 Festival Information
Comprehensive festival pages organized by month:

| Month | Festivals |
|-------|-----------|
| **January** | New Year, Guru Gobind Singh Jayanti, Bhogi, Sankranti, Kanuma, Swami Vivekananda Jayanti, Netaji Bose Jayanti, Republic Day |
| **February** | Valentine's Day, Shivaji Jayanti, Maha Shivaratri |
| **March** | Holi, Ugadi, Ramzan |
| **April** | Ram Navami, Mahavir Jayanti, Ambedkar Jayanti, Good Friday, Easter |
| **May** | Tagore Jayanti, Mother's Day, Buddha Purnima |
| **June** | Bakrid, Kabir Jayanti, Father's Day |
| **July** | Muharram |
| **August** | Friendship Day, Raksha Bandhan, Independence Day, Janmashtami, Ganesh Chaturthi |
| **September** | Onam, Teacher's Day, Durga Puja |
| **October** | Vijaya Dashami, Gandhi Jayanti, Diwali |
| **November** | Children's Day |
| **December** | Christmas |

### 📊 Academic Timetables
- Multiple timetable views for different schedules
- Responsive table layouts

## 🛠 Technology Stack

| Technology | Purpose |
|------------|---------|
| **Django 5.1.4** | Backend Framework |
| **Python 3.x** | Programming Language |
| **SQLite3** | Database |
| **HTML5/CSS3** | Frontend Templates |
| **Django Templates** | Template Engine |
| **Django Haystack** | Search Functionality |
| **Whoosh** | Search Backend |

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/chidwilash17/UniversityCalendar.git
cd UniversityCalendar
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install django
pip install django-haystack
pip install whoosh
```

### Step 4: Configure Environment Variables
Create a `.env` file in the project root (optional but recommended):
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Step 5: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 7: Run the Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

## 🚀 Usage

### User Registration
1. Navigate to the homepage
2. Fill in username, email, and password
3. Submit the registration form
4. Login with your credentials

### Creating Events
1. Login to your account
2. Navigate to the calendar page
3. Click "Add Event"
4. Fill in event details (title, date, type, description)
5. Submit to save and receive email notification

### Viewing Festival Information
1. Access timetable pages to see festival listings
2. Click on any festival to view detailed information

## 📁 Project Structure

```
UniversityCalendar/
├── 📂 core/                    # Django project configuration
│   ├── __init__.py
│   ├── settings.py             # Project settings
│   ├── urls.py                 # Main URL routing
│   ├── wsgi.py                 # WSGI configuration
│   └── asgi.py                 # ASGI configuration
│
├── 📂 calendar_app/            # Main Django application
│   ├── __init__.py
│   ├── admin.py                # Admin panel configuration
│   ├── apps.py                 # App configuration
│   ├── forms.py                # Form definitions
│   ├── models.py               # Database models
│   ├── views.py                # View functions
│   ├── urls.py                 # App URL routing
│   ├── tasks.py                # Background tasks
│   ├── tests.py                # Unit tests
│   │
│   ├── 📂 static/              # Static files (CSS, Images)
│   │   ├── calendar.css
│   │   ├── login.css
│   │   ├── register.css
│   │   └── 📂 images/
│   │
│   ├── 📂 templates/           # HTML templates
│   │   ├── calendar.html
│   │   ├── login.html
│   │   ├── register.html
│   │   ├── event_details.html
│   │   ├── update_event.html
│   │   ├── categorized_events.html
│   │   └── 📂 festivals/       # Festival pages by month
│   │       ├── 📂 jan/
│   │       ├── 📂 feb/
│   │       ├── 📂 march/
│   │       ├── 📂 april/
│   │       ├── 📂 may/
│   │       ├── 📂 june/
│   │       ├── 📂 august/
│   │       ├── 📂 sept/
│   │       ├── 📂 oct/
│   │       └── 📂 nov/
│   │
│   └── 📂 migrations/          # Database migrations
│
├── 📂 staticfiles/             # Collected static files
├── db.sqlite3                  # SQLite database
├── manage.py                   # Django management script
└── README.md                   # Project documentation
```

## 🔌 API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/` | User registration page |
| GET/POST | `/login_view/` | User login page |

### Calendar Events
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/calander/` | View calendar with events |
| POST | `/add_event/` | Create a new event |
| GET | `/get_events/` | Fetch all user events (JSON) |
| GET/POST | `/update_event/<id>/` | Update an event |
| POST | `/delete_event/<id>/` | Delete an event |
| GET | `/event_details/<id>/` | View event details |
| GET | `/categorized_events/` | View categorized events |

### Festival Pages
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tables/` | January-March festivals |
| GET | `/tables2/` | April-June festivals |
| GET | `/tables3/` | July-September festivals |
| GET | `/tables4/` | October-December festivals |
| GET | `/<festival_name>/` | Individual festival page |

## 📊 Database Schema

### CalendarEvent Model
```python
class CalendarEvent(models.Model):
    title = CharField(max_length=200)
    date = DateField()
    event_type = CharField(choices=['holiday', 'exam', 'lecture', 'other'])
    description = TextField(blank=True)
    user_email = EmailField()
    user = ForeignKey(User)
    created_at = DateTimeField(auto_now_add=True)
```

## 🔧 Configuration

### Email Settings
Configure SMTP settings in `settings.py`:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

> ⚠️ **Security Note**: Never commit email credentials to version control. Use environment variables instead.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Coding Standards
- Follow PEP 8 style guidelines
- Write meaningful commit messages
- Add comments for complex logic
- Update documentation as needed

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Chidwilash**
- GitHub: [@chidwilash17](https://github.com/chidwilash17)

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap for UI components
- The open-source community

---

<div align="center">

**⭐ Star this repository if you found it helpful!**

Made with ❤️ for the university community

</div>
