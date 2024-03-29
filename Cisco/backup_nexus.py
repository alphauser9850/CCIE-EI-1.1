from netmiko import ConnectHandler
import datetime
import os
import subprocess
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Enter the details of the switch
device = {
    'device_type': 'cisco_nxos',
    'ip': '192.168.1.58',
    'username': 'saif',
    'password': 'test',
    'secret': 'enable',
}

# Connect to the switch and enter enable mode
net_connect = ConnectHandler(**device)
net_connect.enable()

# Get the hostname of the switch
hostname = net_connect.find_prompt().replace('#', '')

# Get the current date
date = datetime.datetime.now().strftime('%Y-%m-%d')

# Define the filename for the backup file
filename = f'{hostname}-{date}.cfg'

# Backup the configuration to local disk
output = net_connect.send_command('show running-config')
with open(filename, 'w') as file:
    file.write(output)

# Send the backup file to TFTP server
tftp_server = '192.168.1.129'
tftp_path = '/C:/Users/deshm/OneDrive/Backup'
subprocess.call(['tftp', '-v', tftp_server, '-c', f'put {filename} {tftp_path}/{filename}'])

# Disconnect from the switch
net_connect.disconnect()

print('Backup completed successfully.')

