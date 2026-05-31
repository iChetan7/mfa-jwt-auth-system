
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
```

## 🧪 Local Setup

Follow these steps to run the project on your local machine.

### Prerequisites

- Python 3.8 or higher
- Git
- Google Authenticator app on your smartphone

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/iChetan7/mfa-jwt-auth-system.git
   cd mfa-jwt-auth-system
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. Open your browser and go to `http://127.0.0.1:5000`

## 👨‍💻 How to Use

1. **Create an Account**: Navigate to the Signup page, create a username and password. An account with **Admin** role will be created.
2. **Set up MFA**: After signup, a QR code will appear. Open Google Authenticator, scan the code, and complete the setup.
3. **Log in**: Use your username, password, and the 6-digit code from Google Authenticator.
4. **Access Dashboard**: Upon successful login, you'll be redirected to the Admin Dashboard to view protected data.
5. **Log out**: Click the logout button to invalidate your Refresh Token.

## 🚢 Deployment on Vercel

This project is configured for deployment on Vercel.

1. **Push code to GitHub**
2. **Create a New Project on Vercel** and import the GitHub repository.
3. **Configure Build Settings**:
   - **Build Command**: `pip install -r requirements.txt`
   - **Output Directory**: (leave blank)
4. **Deploy!**

> **Note**: The free tier of Vercel uses an **ephemeral file system**. For production databases, consider using a cloud-based PostgreSQL service like [Neon.tech](https://neon.tech).

## 🧩 API Endpoints

- `POST /register` – Create a new user
- `GET /mfa/qrcode?username=<username>` – Retrieve QR code for MFA setup
- `POST /login` – User login with password and OTP
- `GET /admin` – Admin-only protected data
- `POST /refresh` – Get a new Access Token using a Refresh Token
- `POST /logout` – Log out and blacklist the Refresh Token

## 🛡️ Security Features

- **Hashed Passwords** – Using Bcrypt.
- **MFA (TOTP)** – Adds a time-based second factor.
- **JWT with Expiry** – Access Tokens expire in 5 minutes.
- **Refresh Token Rotation** – Prevents indefinite session reuse.
- **Token Blacklisting** – Ensures logout is secure.

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## 📄 License

This project is open-source and available under the MIT License.

---

## ❓ Need Help?

If you encounter any issues or have questions, feel free to open an issue on GitHub.

Made with ❤️ by [Chaitanya Shekhar](https://github.com/iChetan7)
```
