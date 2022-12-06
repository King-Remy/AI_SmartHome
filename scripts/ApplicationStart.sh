#!/bin/bash
##### Start http service

cd /home/app/SmartHome/
#####   Creating a service call SmartHome
sudo forever-service Install SmartHome -r app
##### start a service called SmartHome
sudo service SmartHome start