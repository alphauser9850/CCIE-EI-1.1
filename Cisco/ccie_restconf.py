import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

host = 'devnetsandboxiosxe.cisco.com'
port = '443'
username = 'admin'
password = 'C1sco12345'

url = "https://{}:{}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface".format(host,port)

headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.get(url, auth=(username, password),headers=headers,verify=False)
jsondata = response.json()

print("-" * 100)
print("{:<45} {:<30} {:<30}".format("Interface", "Ingress Octets", "Egress Octets"))
print("-" * 100)

for interface in jsondata['Cisco-IOS-XE-interfaces-oper:interface']:
    if interface['oper-status'] == "if-oper-state-ready" and interface['interface-type'] == "iana-iftype-ethernet-csmacd":
        interface_name = interface['name']
        in_octets = interface['statistics']['in-octets']
        out_octets = interface['statistics']['out-octets']
        print("{:<45} {:<30} {:<30}".format(interface_name, in_octets, out_octets))
