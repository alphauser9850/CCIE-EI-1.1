import panos 
from panos import firewall
from panos import policies 


host = "192.168.63.101"
user = "admin"
password = "Alpha123"

def main():
    params = {
        "name" : "Test_Rule",
        "description": "This is a test Nat policy"
    }

    fw = panos.firewall.Firewall(host,user,password)
    rulebase = panos.policies.Rulebase()
    fw.add(rulebase)

    newRule = panos.policies.NatRule(**params)
    fw.add(newRule)

    print("Creating a new Nat Rule")
    newRule.create()
    print("Done!!!!!")
    fw.commit(sync=True)

    print("Done!!")


if __name__ == " __main__":

    if len(sys.argv) != 1:
        print(__doc__)
    else:
        main()