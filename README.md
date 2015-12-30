ModemRestart
============

A short python script for restarting the Motorola SB6121 Cable Modem (Hardware Version 5.0 Firmware Name: SB_KOMODO-1.0.6.14-SCM01-NOSH)

This may or may not work for other models depending on their embedded webserver.

The script checks connectivty by sending GET requests to Google. If the internet is down the script will pull all the status and log information from the modem and write them into a single file named incident<datetime>.hmtl and restart the modem.
 

Installation
------------

The following assumes Ubuntu 14.04 64-bit

### Install pip

```
sudo apt-get install python-pip
sudo pip install -U pip
```

### Setup Virtualenv

```
sudo pip install virtualenv
virtualenv venv
source venv/bin/activate
```

### Install script requirements

```
pip install -r requirements.txt
```


### Start the script
```
python restart.py &
```
