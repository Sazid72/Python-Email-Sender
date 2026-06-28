# Python Email Sender

## Description

This project is a Python-based command-line email sender that allows users to send plain text emails through Gmail. The application prompts the user to enter the sender's email address, recipient's email address, subject, and a multi-line message body before securely sending the email. I decided to build this project because I wanted to create something practical that combined several Python concepts into a single application. Instead of building another calculator or text-based game, I wanted to learn how real-world applications communicate with external services. Since email is one of the most common forms of digital communication, I thought building an email sender would be both useful and educational.

To develop this project, I used Python's `EmailMessage` class to construct the email, the `smtplib` module to communicate with Gmail's SMTP server, and the `ssl` module to establish a secure encrypted connection. I also used the `validators` library to verify that the sender's and recipient's email addresses were valid before attempting to send the email. To make the program more reliable, I organized the code into separate functions for validation and collecting the email body, and I implemented exception handling to catch authentication errors, network problems, and other unexpected exceptions so the program could display user-friendly messages instead of crashing.

One of the biggest challenges I faced was understanding how SMTP and SSL work together. Initially, I knew the code worked but did not understand the purpose of each module or how they communicated with Gmail's servers. Through research and experimentation, I learned that SMTP is responsible for sending emails while SSL encrypts the connection to keep the communication secure. Another challenge was implementing proper input validation and error handling. My initial validation function did not stop the program when invalid email addresses were entered, so I improved it by terminating the program when validation failed. Overall, this project strengthened my understanding of Python programming, modular design, networking concepts, secure communication, and exception handling while giving me experience building an application that performs a real-world task.

---

## Features

- Send plain text emails through Gmail
- Validate sender and recipient email addresses
- Secure SSL/TLS connection
- Multi-line email body input
- Handles authentication and connection errors gracefully
- Simple command-line interface

---

## Requirements

- Python 3.10 or later
- Gmail account
- Gmail App Password

Install the required package:

```bash
pip install -r requirements.txt
```

---

## Setup

1. Clone this repository.

```bash
git clone <repository-url>
cd <repository-folder>
```

2. Install the required dependencies.

```bash
pip install -r requirements.txt
```

3. Create a file named `password.py` in the project directory.

```python
pwd = "YOUR_GMAIL_APP_PASSWORD"
```

> **Note:** Use a Gmail App Password instead of your regular Gmail password.

---

## Usage

Run the program:

```bash
python project.py
```

The program will ask for:

- Sender email address
- Recipient email address
- Subject
- Email body (finish by pressing **Ctrl+D** on Linux/macOS or **Ctrl+Z** then **Enter** on Windows)

If authentication succeeds, the email will be sent securely through Gmail's SMTP server.

---

## Project Structure

```
.
├── main.py
├── password.py
├── requirements.txt
└── README.md
```

---

## Dependencies

- validators

The following modules are part of Python's standard library and do not require installation:

- email
- smtplib
- ssl
- sys

---

## License

This project is for educational purposes.

## Author
Md. Sazid Al Mafi
