# ECHO LOG | Neural Terminal 🧠💻

A high-performance, aesthetically driven "Memory Bank" designed for developers to index code snippets, project logs, and hardware logic with absolute privacy.

![Status: Live](https://img.shields.io/badge/Status-Live-38bdf8?style=for-the-badge)
![Tech: Django](https://img.shields.io/badge/Built_With-Django-092e20?style=for-the-badge&logo=django)
![UI: Neon Glassmorphism](https://img.shields.io/badge/UI-Cyber_Dark-38bdf8?style=for-the-badge)

---

## 🛠 Project Overview
**EchoLog** is a secure, personal vault for developers. It bridges the gap between hardware engineering and web development, allowing users to store everything from **Arduino** logic to **Django** templates in a centralized, searchable "Neural Terminal."

### Key Features
- **Privacy Vault:** Multi-user authentication ensures that each user's memory bank is strictly isolated.
- **Cyber-Dark UI:** Custom CSS featuring glassmorphism, 3D interactive cards, and neon syntax highlighting.
- **Advanced CRUD:** Secure implementation of Create, Read, Update, and Purge (Delete) logic.
- **Smart Filtering:** Complex search for instant retrieval of project scraps based on title, tag, or content.

---

## 🚀 Tech Stack
- **Backend:** Python (Django 5.0+)
- **Database:** PostgreSQL (Production) / SQLite (Development)
- **Frontend:** Bootstrap 5, CSS3 Variables, Prism.js (Syntax Highlighting)
- **Deployment:** Render (Automated Continuous Deployment)

---

## 📂 Featured Implementation Examples
This terminal is utilized to track high-level engineering and narrative projects:
* **DuskLight:** An adaptive bio-rhythmic nightlight project featuring LDR sensitivity and non-blocking "breathing" LED logic.
* **Echoes of Itihaas:** Interactive narrative simulation of Indian epics (Mahabharata/Ramayana) — *SIH 2025 Waitlisted Idea*.
* **Luna Vision:** Vision-based engineering project roadmap for 2025.

---

## ⚙️ Quick Start (Local Setup)

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Likhitha987/EchoLog_Project.git](https://github.com/Likhitha987/EchoLog_Project.git)
   cd EchoLog_Project

2. **Initialize Environment & Dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt

3. **Database Migration & Superuser:**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser

4. **Run the Terminal:**
   ```bash
   python manage.py runserver
   
---

Access at http://127.0.0.1:8000

---
🛡 Security & Architecture


Ownership Logic: The Scrap model is filtered by request.user at the database level, preventing cross-user data leaks.

CSRF Protection: Secure form handling for all "Purge" and "Initialize" actions.

Production Readiness: Configured with WhiteNoise for static files and dj-database-url for cloud database scaling.


