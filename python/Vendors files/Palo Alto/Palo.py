from netmiko import ConnectHandler
import datetime
import os
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Define device information
device = {
    'device_type': 'paloalto_panos',
    'host': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}

# Define TFTP server information
tftp_server = '192.168.1.2'
tftp_folder = '/mnt/tftp/'

# Define hostname

# Connect to device and backup configuration
with ConnectHandler(**device) as conn:
    conn.enable()
    output = conn.send_command("show running")
    now = datetime.datetime.now()
    filename = f"{device['host']}_config_{now.strftime('%Y%m%d')}.txt"
    with open(f"{tftp_folder}{filename}", 'w') as f:
        f.write(output)


# Send email notification
from_email = 'saif@example.com'
to_email = 'nivedita@example.com'
smtp_server = 'smtp.example.com'
smtp_port = 587
smtp_username = 'me@example.com'
smtp_password = '  '


msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email

msg['Subject'] = 'Palo Alto Firewall Configuration Backup'
body = f"The configuration backup of {device['host']} has been completed and saved to {tftp_server}:{tftp_folder}{filename}."
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('sender_email_address', 'sender_email_password')

text = msg.as_string()
server.sendmail('sender_email_address', 'receiver_email_address', text)
server.quit()
