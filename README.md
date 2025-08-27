# Django Social Website

A modern, responsive **Django Social Website** application with a polished UI.  
This is **Version 1**, featuring a simple design, improved search, and a cleaner layout.

---

## 🛠 Prerequisites

- Git (optional, for cloning)
- Redis
---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/Fakhrillo/Social_Website
cd Web-Blog
```

### 2. Configure environment variables

Copy the sample configuration and update values if needed:

```bash
cp .env.sample .env
```

By default, `.env.sample` contains settings for Django.

### 3. Build and start the services

```bash
uv sync
```

This will install the necessary dependencies,

```bash
uv run manage.py makemigrations
```
,

```bash
uv run manage.py migrate
```

,

```bash
uv run manage.py runserver
```


### 4. Create an admin user

```bash
uv run manage.py createsuperuser
```

---

## 📍 Access the App

- Main Page: [http://localhost:8000/account/](http://localhost:8000/account/)  
- Admin: [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## 📂 Project Structure

```
Social_Website/
│── account/             
│── actions/           
│── bookmarks/             
│── images/
│── media/
│── .env
│── .env.sample
│── manage.py
```

---

## 📝 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more details.
