from netmiko import ConnectHandler
import datetime
import os

# Enter the details of the switch
device = {
    'device_type': 'cisco_nxos',
    'ip': '172.16.50.3',
    'username': 'admin',
    'password': 'admin@123',
    'secret': 'Admin@123',
}

# Connect to the device
net_connect = ConnectHandler(**device)

# Get the hostname of the device
hostname = net_connect.send_command('show run | i hostname').split()[1]

# Get the configuration
config = net_connect.send_command('show running-config')

# Disconnect from the device
net_connect.disconnect()

# Create the file name with the hostname and the current date and time
now = datetime.datetime.now()
filename = f"{hostname}_conf_{now.strftime('%Y-%m-%d_%H-%M-%S')}.txt"

# Save the configuration to a file
with open(filename, 'w') as f:
    f.write(config)

# Copy the file to the Windows machine
import os
os.system(f"copy {filename} \\\\10.0.50.30\\C$\\Users\\adm-averma\\Documents\\Automation\\Backups\\Nexus\\Nexus2")

# Delete the file from the local directory
os.remove(filename)
