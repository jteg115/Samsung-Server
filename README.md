Samsung-Server
==============

Python Server that accepts connections and controls a Samsung Smart TV

Dependencies
	sudo pip install twisted

To Run
	update variables at the top of the script to reflect your IP
	'src = "XXX.XXX.X.XXX" # the IP of server'
	'dst = "XXX.XXX.X.XXX" # the IP of TV'

	Then run the following in the Samsung-Server directory
	'sudo python server.py'