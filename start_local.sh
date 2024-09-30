#!/bin/bash

set -e

sudo apt update
sudo apt install -y ansible sshpass
echo "deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main" | sudo tee -a /etc/apt/sources.list
sudo apt install dirmngr -y
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
sudo apt update
sudo apt install -y ansible
ansible --version

ansible-playbook infrastructure/playbooks/prerequisites.yaml
