# 🏠 BT Real Estate - Django Web Application

A full-featured real estate website built with Django, featuring property listings, user authentication, and automated email notifications.

Visit here at btre.duckdns.org

## 🚀 Features

### Core Functionality
- **Property Listings**: Browse and search real estate properties
- **Advanced Search**: Filter by location, price, bedrooms, and keywords
- **User Authentication**: Register, login, and user dashboard
- **Contact System**: Inquiry forms with email notifications
- **Admin Panel**: Comprehensive backend management
- **Responsive Design**: Mobile-friendly Bootstrap interface

### Technical Features
- **Email Integration**: Gmail SMTP with automated notifications
- **Image Management**: Property photo galleries with lightbox
- **Pagination**: Efficient property listing pagination
- **Security**: Environment variables for sensitive data
- **Database**: PostgreSQL for production-ready data storage

## 🛠️ Technology Stack

- **Backend**: Django 5.0.4
- **Database**: PostgreSQL
- **Frontend**: HTML5, CSS3, Bootstrap 4, JavaScript
- **Email**: Gmail SMTP
- **Image Processing**: Pillow
- **Environment**: python-decouple for configuration

## 📋 Prerequisites

- Python 3.12+
- PostgreSQL
- Git
- Gmail account with App Password

## ⚡ Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/rahulbhattachan/django-real-estate-website.git
cd django-real-estate-website
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the project root:
```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True

# Database Settings
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=localhost

# Email Settings
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
```

### 5. Database Setup
```bash
# Create PostgreSQL database
createdb your_database_name

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser
```

### 6. Run the Application
```bash
python manage.py runserver
```

Visit `http://localhost:8000` to view the application.

## 📁 Project Structure

```
django_framework_website/
├── btre/                    # Main project directory
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL configuration
│   └── static/            # Static files (CSS, JS, images)
├── accounts/              # User authentication app
├── contacts/              # Contact form and email handling
├── listings/              # Property listings app
├── pages/                 # Static pages (home, about)
├── realtors/              # Realtor management app
├── templates/             # HTML templates
├── media/                 # User uploaded files
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (not in repo)
├── .gitignore            # Git ignore file
└── manage.py             # Django management script
```

## 🎨 Screenshots

### Home Page
- Featured property listings
- Advanced search functionality
- Responsive navigation

### Property Details
- High-resolution photo galleries
- Detailed property information
- Contact realtor functionality

### User Dashboard
- User inquiry history
- Account management
- Responsive design

## 📧 Email Configuration

### Gmail Setup
1. Enable 2-Factor Authentication on your Gmail account
2. Generate an App Password:
   - Google Account → Security → App passwords
   - Generate password for "Mail"
3. Use the 16-character app password in your `.env` file

### Email Features
- **Realtor Notifications**: Automatic emails when inquiries are submitted
- **Client Confirmations**: Thank you emails to prospective buyers
- **Admin Alerts**: Property inquiry notifications in admin panel

## 🔒 Security Features

- Environment variables for sensitive data
- CSRF protection
- User authentication and authorization
- Secure password validation
- Gmail App Password integration

## 🚀 Deployment

### Environment Variables for Production
```env
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
# Production database settings
# Production email settings
```

### Static Files
```bash
python manage.py collectstatic
```

## 🛠️ Admin Panel

Access the admin panel at `/admin/` with your superuser credentials:

- **Manage Properties**: Add, edit, delete listings
- **Realtor Management**: Manage realtor profiles
- **User Inquiries**: View and respond to contact forms
- **User Management**: Manage registered users

## 📱 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page with featured listings |
| `/listings/` | GET | All property listings |
| `/listings/<id>` | GET | Individual property details |
| `/listings/search` | GET | Search properties |
| `/accounts/register` | GET/POST | User registration |
| `/accounts/login` | GET/POST | User login |
| `/accounts/dashboard` | GET | User dashboard |
| `/contacts/contact` | POST | Submit inquiry |

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Rahul Bhattachan**
- GitHub: [@rahulbhattachan](https://github.com/rahulbhattachan)
- LinkedIn: [rahul-bhattachan](https://www.linkedin.com/in/rahul-bhattachan-b55472215/)
- Email: rahul.bhattachan@yahoo.com

## 🙏 Acknowledgments

- Django Documentation
- Bootstrap Framework
- PostgreSQL Community
- FontAwesome Icons
- Lightbox.js for image galleries

## 📞 Support

If you have any questions or run into issues, please:
1. Check the [Issues](https://github.com/rahulbhattachan/django-real-estate-website/issues) page
2. Create a new issue if your problem isn't already listed
3. Contact me directly via email

---

⭐ **Star this repository if you found it helpful!**