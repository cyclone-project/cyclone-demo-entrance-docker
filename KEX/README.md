# Entrance-KEX

Key EXchange Service. A python service for storing secret ABE keys per user. This service enables different software clients (WebBrowser or e.g. a native Windows C# Client) to use the same secret ABE key. The clients have to use the OAuth 2 procotol to get the user-specific ABE key for a decryption.

Initialize the KEX service:
 	
	...$ cd src/
	.../src$ sudo python setup-database.py install 
	.../src$ sudo python setup.py install
	
Run the Service:
	
	.../src$ python run.py
	
Check whether a hidden ".kex" directory in your home folder exists.
