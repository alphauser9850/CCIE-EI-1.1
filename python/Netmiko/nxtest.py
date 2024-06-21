from netmiko import ConnectHandler
import datetime
import os

# Enter the details of the Palo Alto firewall
device = {
    "device_type": "paloalto_panos",
    'ip': '172.16.50.41',
    'username': 'Labnoc',
    'password': 'GroupWare95008',
}

# Connect to the device
net_connect = ConnectHandler(**device)

# Get the hostname of the device
hostname = net_connect.find_prompt().replace("(passive)>", "")

# Get the configuration
config = net_connect.send_command('show config running')

# Disconnect from the device
net_connect.disconnect()

# Create the file name with the hostname and the current date and time
now = datetime.datetime.now()
filename = f"{hostname}_conf_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"

# Save the configuration to a file
with open(filename, 'w') as f:
    f.write(config)

# Copy the file to the Windows machine
os.system(f"copy {filename} \\\\10.0.50.30\\C$\\Users\\adm-averma\\Documents\\Automation\\Backups\\Palo\\Pan1")

# Delete the file from the local directory
os.remove(filename)
