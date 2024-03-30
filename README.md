# SETTNIG UP, about this honeypot

## Set up cloud server (Akamai Linode) 
 Specyfication:
    OS: Debian 11   
    
   Region: Miami, FL, USA

## SSH settings:

Change port from 22 to other unprivileged port number, i.e. from 1024 to 65535, and avoid IANA registered service numbers.  
etc/ssh/sshd_config <- change it in this file, then restart ssh 
```bash
sudo systemctl restart ssh #restart 
sudo systemctl status ssh #checking the status
```

Now ssh works in a different port. Command to login: 
```
ssh <user>@<ipaddres> -p <port_nr>
```

## Install Python dependencies
    - sudo apt update #for refresh the list of available packages
    - sudo apt upgrade #for upgrade installed packages to the latest version
    - sudo apt-get install git python3-virtualenv libssl-dev libffi-dev build-essential libpython3-dev python3-minimal authbind virtualenv #it contains packages for python virtualenv and other important stuff

## Create new user
    - sudo adduser <username>
    - su <username>

## Download cowrie (in user)
   ```
    git clone https://github.com/cowrie/cowrie.git
   ```
   https://github.com/cowrie/cowrie?tab=readme-ov-file <== cowrie official repository   
   
   https://cowrie.readthedocs.io/en/latest/index.html <== cowrie documentation

## Setting up python virtual enviroment  
In /home/user/cowrie directory create an enviroment 
```
virtualenv cowrie-env
```
## Activate and install packages
    - source cowrie-env/bin/activate
    - pip install --upgrade pip
    - pip install --upgrade -r requirements.txt

## Enable telnet
   home/user/cowrie/etc/ <- in this localization are config file 'cowrie.cfg' and 'cowrie.cfg.dist'   
   
   To enable telnet create 'cowrie.cfg': 
   ```
   cp /etc/cowrie.cfg.dist cowrie.cfg
   ```
   Open file, find '[telnet]' and set 'enable = true'

## Port redirection   
(make it as a root)   
for ssh:   
```
sudo iptables -t nat -A PREROUTING -p tcp --dport 22 -j REDIRECT --to-port 2222
```
for telnet: 
```
sudo iptables -t nat -A PREROUTING -p tcp --dport 23 -j REDIRECT --to-port 2223
```
 ! to keep ssh server reachable, move the server to a diffrent port (step 2) !

## Start honeypot
    - bin/cowrie start
