cat > send_sms_whatsapp.py << 'EOF'
from twilio.rest import Client

client = Client("YOUR_TWILIO_ACCOUNT_SID", "YOUR_TWILIO_AUTH_TOKEN")

# Send SMS
sms = client.messages.create(
    body="Hello from Linux terminal!",
    from_="+917004152715",  # Your Twilio number
    to="+919876543210"       # Receiver number
)

# Send WhatsApp
wa = client.messages.create(
    body="Hello from WhatsApp Linux terminal of Bhushan!",
    from_="whatsapp:+917004152715",  # Twilio sandbox
    to="whatsapp:+919876543210"
)

print("SMS sent with SID:", sms.sid)
print("WhatsApp sent with SID:", wa.sid)
EOF

# Run
python3 send_sms_whatsapp.py
