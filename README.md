# 🛡️ BarredList - Professional Venue Management System



**BarredList** is a professional incident reporting and banned customer management system designed for venue security teams.  
It enables staff to create, view, and manage incident reports while fostering collaboration through comments and reactions.

🔗 **Live Site:** [https://barredlist-fae77b6e4587.herokuapp.com/](https://barredlist-fae77b6e4587.herokuapp.com/)

---

## 🧭 Table of Contents
- [Design & Planning](#-design--planning)
- [Database Diagram](#-database-diagram)
- [Features](#-features)
- [Authentication & Authorization](#-authentication--authorization)
- [Technologies Used](#-technologies-used)
- [Testing](#-testing)
- [Bugs](#-bugs)
- [Deployment](#-deployment)
- [Credits](#-credits)
- [Acknowledgments](#-acknowledgments)

---

## 🎨 Design & Planning

### 👥 User Stories

#### As a **Venue Staff Member**
- View and understand incident reports  
- Create an account and log in securely  
- Comment on reports (add, edit, delete)  
- React to reports (Helpful, Not Helpful, Urgent, Resolved)

#### As a **Venue Manager**
- Approve comments before publication  
- Manage user accounts and permissions  
- View reaction analytics on reports  

#### As a **Site Administrator**
- Full CRUD control over all content  
- Manage users, posts, and comments via Django Admin  

---

### 🧩 Wireframes
<img width="771" height="635" alt="wireframes" src="https://github.com/user-attachments/assets/1241bf72-ceb5-44e7-a134-7102ad9bf751" />



### ⚙️ Agile Methodology
This project followed **Agile** practices using **GitHub Projects** (Kanban board).

**Key Agile Practices:**
- User stories with acceptance criteria  
- Sprint planning and reviews  
- Iterative development cycles  
- Regular testing & feedback  
- Story point estimation  
- Labels for priority (Must/Should/Could Have)

> _Screenshots of GitHub Kanban board and iterations would appear here._

---

### ✍️ Typography
| Type | Font Family |
|------|--------------|
| Primary | 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif |
| Secondary | 'Arial', sans-serif |
| Brand | Lato |

Clean, modern typography ensures readability and a professional aesthetic.

---

### 🎨 Colour Scheme

| Purpose | Color | Hex |
|----------|--------|-----|
| Primary | Dark Blue-Gray | `#2c3e50` |
| Secondary | Red | `#e74c3c` |
| Accent | Orange | `#f39c12` |
| Success | Green | `#27ae60` |
| Warning | Yellow | `#f1c40f` |
| Background | Light Gray | `#f8f9fa` |



---

## 🧱 Database Diagram

**Models Overview:**

**User (Django built-in)**  
Handles authentication and permissions.

**Post**
- `title`, `slug`, `author`, `featured_image`, `content`, `excerpt`  
- `created_on`, `updated_on`, `status` (Draft/Published)

**Comment**
- `post`, `author`, `body`, `approved`, `created_on`

**Reaction**
- `post`, `user`, `reaction_type`, `created_on`  
- Unique constraint: `(post, user)`

**About**
- `title`, `profile_image`, `content`, `updated_on`

**CollaborateRequest**
- `name`, `email`, `message`, `read`

> _ERD diagram image would be placed here._

---

## 🌟 Features

### 🧭 Navigation
- Fixed top navbar with responsive design  
- Dynamic links for authenticated/anonymous users  
- Active state highlights  

### 📜 Footer
Includes branding, copyright, and social links.

### 🏠 Home Page
- Hero section with branding and stats  
- Report cards with title, author, date, and reactions  
- Pagination with full navigation controls  

---

## 🧰 CRUD Functionality

| Action | Feature | Description |
|--------|----------|-------------|
| Create | Register, comment, react | Add user content and feedback |
| Read | View posts and comments | Accessible to all users |
| Update | Edit own comments | User control over contributions |
| Delete | Remove own comments | Maintain content accuracy |

---

## 🔐 Authentication & Authorization

**Authentication:**  
- `django-allauth` for registration/login  
- Secure password hashing  
- Password reset functionality  

**Authorization Levels:**
| Role | Access |
|------|--------|
| Anonymous | View only |
| Authenticated | Comment & react |
| Comment Author | Edit/delete own comments |
| Admin | Full CRUD control |

**Security Measures:**
- CSRF protection  
- Session-based authentication  
- Secure password storage  

---

## ⚙️ Technologies Used

### 🖥️ Backend
- **Django 5.2.6**  
- **Python 3.x**

### 🗄️ Database
- **PostgreSQL (production)**  
- **SQLite (development)**

### 🎨 Frontend
- HTML5, CSS3, JavaScript  
- Bootstrap 5.3.2  
- Cloudinary (media)  
- django-crispy-forms + crispy-bootstrap5  

### 🧰 Admin Tools
- django-summernote  
- Django Admin Interface  

### 🚀 Deployment
- **Heroku** (live hosting)  
- **Gunicorn**, **WhiteNoise** for static serving  

### 🧪 Development
- Git, GitHub, VS Code  

---

## 🧪 Testing

### ⚡ Performance
Tested using **Google Lighthouse** for desktop & mobile.  
<img width="916" height="875" alt="image" src="https://github.com/user-attachments/assets/af3cf88e-6246-4a81-aae5-b0bde4dfb337" />



### 🌍 Browser Compatibility
✅ Chrome  
✅ Firefox  
✅ Safari  
✅ Edge  

### 📱 Responsiveness
- Fully responsive grid system  
- Optimized for mobile, tablet, and desktop  

---

## 🧩 Code Validation

| Type | Tool | Status |
|------|------|---------|
| HTML | W3C Validator | ✅ Passed |

<img width="1879" height="579" alt="html pass" src="https://github.com/user-attachments/assets/54485e7d-0546-4f68-9755-39a41087272f" />


| CSS | W3C Validator | ✅ Passed, With 1, boostrap error. (Doesnt effect Performance) |

> _Validation screenshots can be added here._
<img width="1887" height="462" alt="css validator - `1 bootstrap error" src="https://github.com/user-attachments/assets/d26e64c1-9660-4aa3-a261-d7ec6130e027" />

---

## 🧠 Manual Testing

| User Story | Test | Result |
|-------------|------|--------|
| View reports | Visit homepage | ✅ |
| View details | Click “View Report” | ✅ |
| Register | Create account | ✅ |
| Comment | Add/edit/delete | ✅ |
| React | Submit reaction | ✅ |
| Pagination | Navigate pages | ✅ |



---

## 🐛 Bugs

| ID | Issue | Solution | Status |
|----|--------|-----------|--------|
| 1 | Comment edit form not populating | Passed instance to form | ✅ Fixed |
| 2 | Pagination too small on mobile | Adjusted CSS | ✅ Fixed |
| 3 | Large image load times | Cloudinary optimization | ✅ Fixed |
| 4 | CSRF token missing in AJAX | Added token handling | ✅ Fixed |

---

## 🚀 Deployment

### 1️⃣ GitHub Setup
- Use Code Institute template  
- Create new repo: `barredlist`  
- Open workspace in Gitpod  

### 2️⃣ Heroku Setup
- Create app: `barredlist-fae77b6e4587`  
- Add PostgreSQL database  
- Add config vars:  
  - `DATABASE_URL`  
  - `SECRET_KEY`  
  - `CLOUDINARY_URL`  
  - `PORT=8000`

### 3️⃣ Final Deployment
```bash
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
