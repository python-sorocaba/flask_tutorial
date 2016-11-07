provision: install-python-remote
	@ansible-playbook provision.yml -v --ask-become-pass

deploy:	
	@ansible-playbook deploy.yml --ask-become-pass

all:
	@ansible-playbook provision.yml deploy.yml --ask-become-pass 

step:
	@ansible-playbook provision.yml deploy.yml --ask-become-pass --step

ping:
	@ansible all -i secret/hosts -m ping

install-ansible-local:
	@sudo apt-get install ansible sshpass

install-python-remote:
	@ansible all -i secret/hosts -m raw -a 'apt-get update && apt-get install -y python' -b --ask-sudo-pass
