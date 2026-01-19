# 🔗 URL Shortener API

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/FastAPI-Backend-black?style=for-the-badge&logo=flask">
  <img src="https://img.shields.io/badge/RESTful-API-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite">
  <img src="https://img.shields.io/badge/SQLModel-ORM-green?style=for-the-badge">
</p>

<p align="center">
  <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExOTJ6ZWwxMHF1aDN2YWp2NzNtcmF5NjlvZ3RvNTVhaGswaHN3eGFwNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/loXfQtPqLxGmbLs9h2/giphy.gif" alt="gif" height="505" width="300"/>
</p>


A simple RESTful URL shortening service built with **FastAPI** and **SQLModel**.

This project is designed as a **learning-focused backend system** that demonstrates:
- Clean service-layer architecture
- Proper separation of concerns
- RESTful API design
- URL redirection with access statistics

No authentication. No overengineering. Just correct backend fundamentals.


## 🚀 Features

- Create short URLs
- Retrieve original URLs
- Update existing short URLs
- Delete short URLs
- Redirect short URLs (with access count tracking)
- Fetch access statistics for a short URL


## 🧠 Architecture Overview

The project follows a **layered design**:

- routes → HTTP / API layer
- services → Business logic
- storage → Database operations
- models → Data models
- utils → Pure helper functions


Key rule:
> **Only the redirect endpoint increments access counts.**


## 🛠 Tech Stack

- **Python**
- **FastAPI**
- **SQLModel**
- **SQLite** (default, easily replaceable)
- **Bruno** (for API testing)


## 📂 Project Structure
```
├── main.py # App entry point
├── routes.py # API routes
├── services.py # Business logic
├── storage.py # DB operations
├── models.py # Data models
├── db.py # Database engine
├── utils.py # Helpers (shortcode generator, URL validation)
├── errors.py # Domain-level errors
├── schemas.py # Request schemas
├── URL Shortner/ # Bruno tests
├── designs.txt # Helper Designs
├── .gitignore
└── README.md
```

## 🏁 Final Note

This project is not about shortening URLs.

It’s about:
- Thinking in layers
- Writing predictable services
- Designing APIs that don’t lie


