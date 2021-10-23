# TrojanPass

## Project Setup

### Environment Variables

- set your system environment variables:
  - Unix
    - ZSH: `echo '\n# Trojan Pass\nexport TROJAN_PASS_NETID="<Your Net ID>"\nexport TROJAN_PASS_PASSWORD="<Your NetID password>"\nexport TROJAN_PASS_GMAIL_ACCOUNT="<Your Gmail Account>"\nexport TROJAN_PASS_GMAIL_PASSWORD="<Your Gmail Password>"' >> ~/.zshrc`
    - Bash: `echo '\n# Trojan Pass\nexport TROJAN_PASS_NETID="<Your Net ID>"\nexport TROJAN_PASS_PASSWORD="<Your NetID password>"\nexport TROJAN_PASS_GMAIL_ACCOUNT="<Your Gmail Account>"\nexport TROJAN_PASS_GMAIL_PASSWORD="<Your Gmail Password>"' >> ~/.bash_profile`
    - For example, on macOS 11.6, suppose the NET ID is `wq`, password is `foo`, Gmail account is `wangqin0.me@gmail.com`, Gmail password is `fool` open the Terminal and execute `echo '\n# Trojan Pass\nexport TROJAN_PASS_NETID="wq"\nexport TROJAN_PASS_PASSWORD="foo"\nexport TROJAN_PASS_GMAIL_ACCOUNT="wangqin0.me@gmail.com"\nexport TROJAN_PASS_GMAIL_PASSWORD="fool"' >> ~/.zshrc` 
  - Windows
    - Not sure
  - Notice that `<>` is NOT in the actual command; for security concerns, please don't hard code your password into the program

### Install Prerequisites

```shell
# install Xvfb (X virtual framebuffer): an in-memory display server
sudo apt update
sudo apt install -y unzip xvfb libxi6 libgconf-2-4
sudo apt install default-jdk

# install chrome 
sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
sudo bash -c "echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google-chrome.list"
sudo apt -y update
sudo apt -y install google-chrome-stable

# download and setup chromedriver
# find your version at https://sites.google.com/chromium.org/driver/downloads
google-chrome --version
wget https://chromedriver.storage.googleapis.com/95.0.4638.17/chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
```

## Further Automation

### Use Cron

