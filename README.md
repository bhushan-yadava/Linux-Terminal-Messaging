# Linux Terminal Messaging

Send emails, SMS/WhatsApp messages, and Tweets directly from the **Linux terminal** using Python, Ruby, and CLI tools.  
This project demonstrates Linux automation, scripting, and API integration skills — perfect for DevOps, cloud, and automation roles.

## Features

- **Send Emails** via Python SMTP directly from terminal
- **Send SMS and WhatsApp messages** via Twilio API
- **Post Tweets** via Twitter API using Twurl
- Fully automated workflow using a bash script

## Prerequisites

- Linux system (Rocky Linux, Ubuntu, CentOS, etc.)
- Python 3
- Ruby and gem
- Git, curl, jq
- Twilio account (for SMS/WhatsApp)
- Twitter developer account (for API/Twurl)

## Installation

### Install dependencies:

sudo dnf update -y
sudo dnf install -y ruby ruby-devel python3 python3-pip git curl jq
sudo gem install twurl
pip3 install twilio requests


Usage
1. Send Email

Edit send_email.py with your email credentials:

python3 send_email.py

2. Send SMS / WhatsApp

Edit send_sms_whatsapp.py with your Twilio account SID, auth token, and phone numbers:

python3 send_sms_whatsapp.py

3. Send Tweet

Authorize Twurl with your Twitter API keys:

twurl authorize --consumer-key YOUR_CONSUMER_KEY --consumer-secret YOUR_CONSUMER_SECRET


Post a tweet:

twurl -d "status=Hello from Linux terminal!" /1.1/statuses/update.json

4. Automate All Actions

Use the bash automation script:

chmod +x terminal_messenger.sh
./terminal_messenger.sh

##Project Structure

Linux-Terminal-Messaging/
├── send_email.py
├── send_sms_whatsapp.py
├── terminal_messenger.sh
├── README.md

Notes

For Gmail SMTP, use App Passwords instead of your account password.

Twilio requires verified numbers for trial accounts.

Keep your API keys secure; do not commit them to GitHub.

Skills Demonstrated

Linux terminal scripting & automation

Python & Ruby programming

API integration (Twilio, Twitter)

End-to-end CLI-based project development
