# 🔐 MFA-JWT-Auth-System

A production-ready **Multi-Factor Authentication (MFA)** system built with Flask. This project adds a strong layer of security by combining **JWT tokens** with **Time-based One-Time Passwords (TOTP)** using the Google Authenticator app.

## 🚀 Live Demo

Check out the live application:[mfa-jwt-auth-system-git-main-galgotias-s-projects.vercel.app](https://mfa-jwt-auth-system-galgotias-s-projects.vercel.app/)

## ✨ Key Features

- **Multi-Factor Authentication (MFA)** – Adds an extra layer of security with TOTP using Google Authenticator.
- **JWT-based Authentication** – Issues short-lived Access Tokens (5 minutes) and Refresh Tokens (7 days).
- **Role-Based Access Control (RBAC)** – Differentiates between "Admin" and "User" roles for protected endpoints.
- **Secure Token Refresh** – Automatically obtains new Access Tokens using a Refresh Token.
- **Logout & Blacklisting** – Invalidates Refresh Tokens upon logout for better security.
- **Modern Web UI** – Features a sleek, responsive design for the login and signup process.
- **Deployed on Vercel** – Hosted on a serverless platform for global access.

## 🛠️ Technologies Used

- **Python** & **Flask** – Backend framework.
- **JWT** (`PyJWT`) – For generating and verifying JSON Web Tokens.
- **TOTP** (`pyotp`) – For Time-based One-Time Password generation and verification.
- **SQLite** – Lightweight database for user data and blacklisted tokens.
- **HTML/CSS/JS** – For the frontend interface.
- **Vercel** – For deployment as serverless functions.

## 📂 Project Structure

```text
.
├── api/               # Vercel serverless function entry point
├── static/            # CSS and images
├── templates/         # HTML files (landing page, login/signup, dashboard)
├── app.py             # Main Flask application
├── auth.py            # JWT and MFA logic
├── database.py        # Database initialization and helpers
├── requirements.txt   # Python dependencies
├── vercel.json        # Vercel deployment configuration
└── README.md          # Project documentation
