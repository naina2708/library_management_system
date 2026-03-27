# 📚 Library Management System

## 📌 Project Overview

This is a **Library Management System** built using **Django**.
It allows users to issue and return books/movies, while the admin manages inventory and tracks transactions.

---

## 🚀 Features

### 👤 User Features

* User Login & Registration
* View available Books & Movies
* Search by Book Name or Author
* Issue Book/Movie
* Return Book/Movie
* Fine calculation for late returns
* View issued items (My Books)

---

### 🛠️ Admin Features

* Add / Update / Delete Books & Movies
* Auto-generate unique codes (e.g., SCB000001)
* Track all transactions
* Manage users and memberships

---

## 📊 Business Rules Implemented

* Due Date = Issue Date + 15 days
* Fine = ₹10 per day after due date
* Fine must be paid before return
* Membership options: 6 months, 1 year, 2 years
* Book & Movie handled in same system
* Search requires at least one field

---

## 🧱 Tech Stack

* Backend: Django (Python)
* Frontend: HTML, Bootstrap
* Database: SQLite

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/library-system.git
cd library-system
```

### 2️⃣ Install Dependencies

```bash
pip install django
```

### 3️⃣ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

### 5️⃣ Run Server

```bash
python manage.py runserver
```

---

## 🔑 Default Users (for testing)

| Role  | Username | Password |
| ----- | -------- | -------- |
| Admin | naina     | sahu     |
| User  | user     | user     |

---

## 🌐 URLs

* User Login: http://127.0.0.1:8000/
* Dashboard: http://127.0.0.1:8000/home/
* My Books: http://127.0.0.1:8000/mybooks/
* Admin Panel: http://127.0.0.1:8000/admin/

---

## 🧪 Testing Features

* Add books from Admin panel
* Issue & return items
* Modify issue date to test fine
* Search functionality

---

## 📸 Screenshots

(Add screenshots here if needed)

---

## 🎯 Future Improvements

* Advanced UI dashboard
* Online fine payment integration
* Email notifications
* REST API support

---

## 👩‍💻 Author

Naina Sahu
