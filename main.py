from password import pwd
from email.message import EmailMessage
import validators
import ssl
import smtplib
import sys

def main():
    email_sender = input("Enter sender email address: ").strip()
    validate(email_sender)
    password = pwd

    email_receiver = input("Enter receiver email address: ").strip()
    validate(email_receiver)

    subject = input("Subject: ").strip()
    body = get_mail_body()

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
        print("Email sent!")
    except smtplib.SMTPAuthenticationError:
        print("Authentication failed. Check your email and app password.")
    except OSError:
        print("Could not connect to Gmail. Check your internet connection.")
    except Exception as e:
        print(f"Unexpected error: {e}")


def get_mail_body():
   lines = []
   print("Email body:")
   print("(press Ctrl+D on Linux/macOS or Ctrl+Z then Enter on Windows when finished)")
   while True:
       try:
           line = input()
           lines.append(line)
       except EOFError:
           break
   return "\n".join(lines)

def validate(email):
   if not validators.email(email):
       sys.exit("Invalid email address. Try again with a valid email.")
   
if __name__ == '__main__':
   main()
