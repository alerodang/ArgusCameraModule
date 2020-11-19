# Argus Camera Module

This is a camera module for the Argus application, designed to be installed in any device supporting docker and docker-compose platforms. 

## Install Docker and docker-compose

``curl -sSL https://get.docker.com | sh``

``sudo usermod -aG docker [user]``

``sudo apt-get install -y python3 python3-pip``

``sudo pip3 install docker-compose``

## Configuration

Before installing a producer you should define a producer name and a producer secret in docker-compose.yml. Both configuration variables are required for adding a producer to the mobile app. 
- PRODUCER_NAME
- PRODUCER_SECRET

## Executing

1. Put *run.jar* file in image-capturer-container/application (Information about how to get this jar file is in https://github.com/alerodang/ArgusCameraMotionDetection/blob/master/README.md) Note: Be sure to name the jar file as *run.jar*.
2. Once you have installed docker and docker-compose you can run ``docker-compose up`` command for starting the application.
