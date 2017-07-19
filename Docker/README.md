# User guide:
This folder contains all you need to setup Entrance using Docker, 
Tested on Ubuntu 16.04. with:
- docker version 17.03.0-ceer (community edition)
- docker-compose version 1.11.2,

# Build the docker containers with:
sudo docker-compose build

The sources are fetched from: 

Dashboard/Frontend and KeyExchange (KEX) services
- https://github.com/SNET-Entrance/Entrance-UM
- https://github.com/SNET-Entrance/Entrance-KEX

Backend (not yet dockerized  - comming soon!)
- https://github.com/SNET-Entrance/Entrance-Backend

# Start docker containers with:
sudo docker-compose up -d


# Stop docker containers with:
sudo docker-compose kill

# Get the log
sudo docker-compose logs -f

# Optional: jump into the "frontend" or "kex" container:  

sudo docker-compose exec frontend /bin/bash

sudo docker-compose exec kex /bin/bash 

# Webinterfaces are available on:
- localhost:5000 (Dashboard/Frontend GUI)
- localhost:5001 (KeyExchange (kex) GUI)

# A test user is already preconfigured:
Testuser:Test1234

# Using an edugain account for login:
 After
 
 1st. defining a login/password for a SMTP server in config/default.py
 
 2nd. creating a local account using your edugain-ready email address,
 
 you can log into the Dashboard using your edugain credentials. Trigger the edugain login by clicking on the Cyclone logo at the login page.

# Data mapping between docker and your host system:
The docker container's "/root/.entrance" folder is mapped to the ./data/entrance folder of your host machine. 
This means adding content to the Dashboard (fit-file upload) will appear in ./data/entrance/ of your local machine.
Hereby "." represents the folder where you executed "docker-compose up -d". 

# Backend
The backend consists of the 'Entrance service' and the 'Vanish Core' and 'Vuze Vanish Backend'. 
Both Vanish components can be downloaded from https://vanish.cs.washington.edu/download.html - check their licence agreement!
The 'Entrance service' ist available here https://github.com/SNET-Entrance/Entrance-Backend.
Using docker automatically fetches, compiles and starts the Entrance-Backend. In order to distribute keys using the DHT, Vansih needs to be downloaded manually. The Vanaish files should be copied into the empty Docker folder called "vanish".
