import sys
import panos 
from panos import firewall
from panos import policies




HOSTNAME = "192.168.63.105"
USERNAME = "admin"
PASSWORD = "Alpha123"


def main():

    parmas = {
        "name": "Block ssh",
        "description": "Prevent ssh usage",
        "fromzone": "any",
        "tozone": "any",
        "application": "ssh",
        "action": "deny",
        "log_end": True,
    }


    fw = panos.firewall.firewall()
    rulebase = panos.policies.Rulebase()
    fw.add(rulebase)

    new_rule = panos.policies.SecurityRule(**parmas)
    rulebase.add(new_rule)

    print("Creating Rule ......")
    fw.commit(sync=True)

    print("Done Boss, I just created a Rule for you")

