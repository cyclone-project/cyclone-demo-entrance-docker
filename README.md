# cyclone-demo-entrance-docker
=====================================================
This is a demonstration for the integration of Entrance components, with the Federated Identity Provider of the project CYCLONE. It allows users to deploy an Entrance instance as a Service on Docker compatible systems. 
It consists of a preconfigured Entrance instance which includes two Python services a Key Exchange Service and a Dashboard, Furthermore a Java backend is provided.
Login to the systems mainly requires to login to the Dashboard builds on top of Python Flask and bootstrap.io. The intgration bases on an OpenIDconnect Plugin for Flask https://github.com/puiterwijk/flask-oidc. 

Usage
-----
To start a container with defaults, on the project root run:
``` 
docker-compose build
docker-compose up -d 
```
Details
-------
To build the image... [todo]
