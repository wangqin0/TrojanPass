# TrojanPass

## Project Setup

### Environment Variables

- set your system environment variables:
  - Unix
    - ZSH: `printf '\n# Trojan Pass\nexport TROJAN_PASS_NETID="<Your Net ID>"\nexport TROJAN_PASS_PASSWORD="<Your NetID password>"\nexport TROJAN_PASS_GMAIL_ACCOUNT="<Your Gmail Account>"\nexport TROJAN_PASS_GMAIL_PASSWORD="<Your Gmail Password>"' >> ~/.zshrc`
    - Bash: `printf '\n# Trojan Pass\nexport TROJAN_PASS_NETID="<Your Net ID>"\nexport TROJAN_PASS_PASSWORD="<Your NetID password>"\nexport TROJAN_PASS_GMAIL_ACCOUNT="<Your Gmail Account>"\nexport TROJAN_PASS_GMAIL_PASSWORD="<Your Gmail Password>"' >> ~/.bash_profile` (or `>> ~/.bashrc`)
    - Note: use `echo` in macOS and `printf` on Linux
    - For example, on macOS 11.6, suppose the NET ID is `wq`, password is `foo`, Gmail account is `wangqin0.me@gmail.com`, Gmail password is `fool` open the Terminal and execute `echo '\n# Trojan Pass\nexport TROJAN_PASS_NETID="wq"\nexport TROJAN_PASS_PASSWORD="foo"\nexport TROJAN_PASS_GMAIL_ACCOUNT="wangqin0.me@gmail.com"\nexport TROJAN_PASS_GMAIL_PASSWORD="fool"' >> ~/.zshrc` 
  - Windows
    - I don't use Windows, maybe you can take look at [about_Environment_Variables](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables) in Microsoft Docs
  - Notice that `<>` is NOT in the actual command; for security concerns, please don't hard code your password into the program

### Install Prerequisites

#### Ubuntu 20.04

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

#### macOS 11.6

Download the chrome and related chrome driver. Add the driver to path directory.  

### Run task

#### Linux with Xvfb

- Run once: `xvfb-run python3 <project root>/main.py` (for example: `xvfb-run python3 ~/TrojanPass/main.py`), note that you need to manually set environment variables in `crontab -e`
- Run every day: Execute `cron -e` in shell then add following line: `0 7 * * * xvfb-run python3 <project root>/main.py`, this will run task at 7:00 am every day

#### macOS 11.6

Run once: `python3 <project root>/main.py`
