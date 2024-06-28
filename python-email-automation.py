import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587  # Port for TLS
SENDER_EMAIL = 'your_email@gmail.com'
SENDER_PASSWORD = 'your_app_password'  # Use the app password generated
RECIPIENT_EMAIL = 'recipient_email@example.com'

def create_email_content():
    current_date = datetime.datetime.now().strftime('%Y-%m-%d')
    subject = f'Daily Report for {current_date}'
    body_plain = f'This is the plain text version of the daily report for {current_date}.'
    body_html = f'''
    <html>
    <body>
        <h1>Daily Report for {current_date}</h1>
        <p>This is the HTML version of the daily report for {current_date}.</p>
    </body>
    </html>
    '''
    return subject, body_plain, body_html

def send_email(subject, body_plain, body_html):
    msg = MIMEMultipart('alternative')
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject

    part1 = MIMEText(body_plain, 'plain')
    part2 = MIMEText(body_html, 'html')
    msg.attach(part1)
    msg.attach(part2)

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, msg.as_string())
        server.quit()
        print('Email sent successfully.')
    except Exception as e:
        print(f'Failed to send email. Error: {e}')

if __name__ == '__main__':
    subject, body_plain, body_html = create_email_content()
    send_email(subject, body_plain, body_html)
