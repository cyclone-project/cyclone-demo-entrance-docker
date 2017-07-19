# cyclone-demo-entrance-docker
=====================================================

This is a demonstration for the integration of Entrance components, with the Federated Identity Provider of the project CYCLONE. It allows users to deploy an Entrance instance as a Service on Docker compatible systems. 
It consists of a preconfigured Entrance instance which includes two Python services a Key Exchange Service (KEX) and a Dashboard (web frontend. Furthermore a Java-based backend is involved and provided online on entrance2.snet.tu-berlin.de. The backend is responsable for the Attribute-based Encryption and exposes a REST-like API.
Login to the systems mainly requires to login into the Dashboard. The Dashboard uses Python Flask and bootstrap.io. The Cyclone Federation Provider integration is based on OpenIDconnect implementation http://pyoidc.readthedocs.io.


Docker
-----

Both services, Dashboard and KEX are availavle as docker-image on https://hub.docker.com/.

Usage
-----
To start a container with defaults, on the project root run:
``` 
docker-compose pull
docker-compose up -d 
```
Details
-------
[todo]
