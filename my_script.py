# Sample taken from pyStrich GitHub repository
# https://github.com/mmulqueen/pyStrich

import sys
import requests
import json


def get_mac_ip(macaddress):
	api_url_base = 'https://api.macaddress.io/v1/?'
	api_key_value = 'apiKey=' + 'at_uITxbwNJHNu1GLQJ7F889o4j5ypa6'
	final_url = api_url_base + api_key_value + '&output=json&search=' + mac_address
	try:
	    output = requests.get(final_url,timeout=3)
	    output.raise_for_status()
	except requests.exceptions.HTTPError as errh:
	    print ("Http Error:",errh)
	except requests.exceptions.ConnectionError as errc:
	    print ("Error Connecting:",errc)
	except requests.exceptions.Timeout as errt:
	    print ("Timeout Error:",errt)
	except requests.exceptions.RequestException as err:
	    print ("sorry, Some error happened",err)
	json_data = json.loads(output.text)
	if('error' in json_data):
		 print(json_data['error'])
	else:
		print(json_data['vendorDetails']['companyName'], "is the vendor company name for the following mac address" , macaddress)



if __name__ == '__main__':
	mac_address = sys.argv[1]
	get_mac_ip(mac_address)
	