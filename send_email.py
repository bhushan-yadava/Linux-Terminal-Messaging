cat > send_email.py << 'EOF'
import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Hello from Linux terminal!")
msg['Subject'] = "Test Email"
msg['From'] = "byadava999@gmail.com"
msg['To'] = "bhushany999@gmail.com"

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login("byadava999@gmail.com", "your_password")
    server.send_message(msg)

print("Email sent successfully!")
EOF

# Run
python3 send_email.py
