import os

#update
os.system('sudo apt-get update')
os.system('sudo apt-get upgrade -y')

# download dockers
os.system('sudo apt-get remove docker docker-engine docker.io containerd runc')
os.system('sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common -y')
os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -')
os.system('sudo apt-key fingerprint 0EBFCD88')
os.system('sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"')
os.system('sudo apt-get update')
os.system('sudo apt-get install docker-ce docker-ce-cli containerd.io -y')
os.system('sudo docker run hello-world')

# download docker-compose

os.system('sudo curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose')
os.system('sudo chmod +x /usr/local/bin/docker-compose')
os.system('sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose')

