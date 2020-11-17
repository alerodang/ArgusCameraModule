# Argus Camera Module

This is camera module for the Argus application, designed to be installed in any device supporting docker and docker-compose platforms. 

## Install Docker and docker compose

``curl -sSL https://get.docker.com | sh``

``sudo usermod -aG docker [ user ]``

``sudo apt-get install -y libffi-dev libssl-dev``

``sudo apt-get install -y python3 python3-pip``

``sudo apt-get remove python-configparser``

``sudo pip3 install docker-compose``

## Executing Intructions
This is a docker compose project.

1. Put *run.jar* file in image-capturer-container/application (Information about how to get this jar file is in https://github.com/alerodang/ArgusCameraMotionDetection/blob/master/README.md) Note: Be sure to name the jar file as *run.jar*.
2. Once you have installed docker and docker-compose you can run ``docker-comnpose up`` command for starting the application.