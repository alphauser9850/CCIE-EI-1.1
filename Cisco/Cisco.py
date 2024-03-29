# Importing necessary libraries gfg
from netmiko import ConnectHandler
import datetime

# Defining the device details
device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.58',
    'username': 'saif',
    'password': 'test',
    'secret': 'enable',
}


# Establishing the SSH connection to the router
ssh_conn = ConnectHandler(**device)
ssh_conn.enable()

# Getting the current date and time
now = datetime.datetime.now()
date_time = now.strftime("%Y-%m-%d_%H-%M-%S")

# Defining the TFTP server details
tftp_server = '192.168.1.129'

# Sending the backup configuration file to the TFTP server
output = ssh_conn.send_command('copy running-config tftp://'+tftp_server+'/running-config_'+date_time+'.txt')
print(output)

# Closing the SSH connection
ssh_conn.disconnect()
