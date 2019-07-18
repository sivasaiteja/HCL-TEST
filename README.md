# HCL-TEST
Once the above project is cloned 
please run the docker commands inside the directory 

to create docker image run command
	docker build -t mac_ip .

to run the docker image with ipaddress
	docker run mac_ip [ip_address]

	for example: 
		docker run mac_ip 44:38:39:ff:ef:57

		the response for the above should be 'Cumulus Networks, Inc is the vendor company name for the following mac address 44:38:39:ff:ef:57'
