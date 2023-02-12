
# What is this?

Python App to create Webex calling local gateway configuration for CUBE IOS based device. While webex calling supports 3rd party SIP devices as local gateway, this app helps to create the configuration for CUBE IOS based device only.

# What is Webex Calling Local Gateway?
Refer help.webex.com/en-us/8z0x0x/Local-Gateway-Configuration-for-Cisco-CUBE for more details.

# What is CUBE?
Refer https://www.cisco.com/c/en/us/products/collateral/unified-communications/unified-border-element/white_paper_c11-731493.html for more details.

# What modes of local gateway are supported?
This app supports the following modes of local gateway:
1. Local Gateway with SIP Trunk in registration-based mode.
2. Local Gateway with SIP Trunk in certificate-based mode.

# How to use it?
A docker based python app to create Webex calling local gateway configuration for CUBE IOS based device. In order to use this app, you need to have docker installed on your machine.
Please refer to the following link for docker installation: https://docs.docker.com/get-docker/

After installing docker, you can use the following commands to build and run the docker image.

To build the docker image, run the following command from the root of the project:
```
 docker build -t python-app .
```
To run the docker image, run the following command from the root of the project:

```
 docker run -i python-app
```