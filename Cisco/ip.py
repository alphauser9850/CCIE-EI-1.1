import ipaddress

# Read IP address and prefix value from user
ip = input("Enter Network address: ")
prefix = int(input("Enter prefix value: "))

# Calculate subnet mask
subnet_mask = str(ipaddress.IPv4Network(ip + '/' + str(prefix)).netmask, False)

# Calculate network ID
network_id = str(ipaddress.IPv4Network(ip + '/' + str(prefix)).network_address,False)

# Calculate broadcast ID
broadcast_id = str(ipaddress.IPv4Network(ip + '/' + str(prefix)).broadcast_address,False)

# Calculate number of available IPs
num_ips = (2**(32 - prefix)) - 2

# Print subnet information
print("Subnet information:")
print("Subnet mask: " + subnet_mask)
print("Network ID: " + network_id)
print("Broadcast ID: " + broadcast_id)
print("Number of available IPs: " + str(num_ips))

