from xml.dom.minidom import Element
import panos
from panos.panorama import Panorama
from panos.firewall import Firewall


fw = Firewall('10.0.0.1', 'admin','Alpha123') 


Element_response = fw.op('show system info')

