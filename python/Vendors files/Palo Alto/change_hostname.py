import panos 
from panos import firewall
from panos import device


host = "192.168.63.105"
user = "admin"
password = "Alpha123"



fw = panos.firewall.Firewall(host,user,password)

name = panos.firewall.Firewall.set_hostname(self, "new_hostname")
name.create()
print("Creating Rule ......")
fw.commit(sync=True)

