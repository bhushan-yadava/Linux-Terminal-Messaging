cat > terminal_messenger.sh << 'EOF'
#!/bin/bash

# 1. Send Email
echo "Hello from Linux terminal!" | mailx -s "Test Email" receiver@example.com

# 2. Send SMS/WhatsApp
python3 send_sms_whatsapp.py

# 3. Send Tweet
twurl -d "status=Hello from Linux terminal!" /1.1/statuses/update.json
EOF

chmod +x terminal_messenger.sh

# Run
./terminal_messenger.sh
