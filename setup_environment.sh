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

echo "Manual steps required:"
echo "1. Copy the content of /etc/rancher/k3s/k3s.yaml"
echo "2. Create the secrets/my-custom.secrets file and include the line KUBECONFIG='<your-kube-config>'"
echo "3. Replace the <your-kube-config> string in the secrets/my-custom.secrets file with the copied content"
echo "4. Restart the raspberry pi"
