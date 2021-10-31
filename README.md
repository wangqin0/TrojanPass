# TrojanPass

Tired of Trojan Check every day? You need this. TrojanPass will automate the process of wellness assessment and send the pass to your mailbox. 

You can use cron to schedule TrojanCheck, making your life easier. 

## What you need to have

- A USC account (SSO)
- A Gmail account with [App Passwords](https://support.google.com/accounts/answer/185833?hl=en), this is required for security concerns

## Deploy to Cloud

### Heroku (Recommend)

You need to verify your account (by adding a credit card)if you want to schedule a daily job. It should be okay if you only use heroku to run this project. 

First, in the project root, run `./heroku_deploy.sh`, then set environment variable by

```shell
heroku config:set TROJAN_PASS_NETID=<Your Net ID>
heroku config:set TROJAN_PASS_PASSWORD=<Your NetID password>
heroku config:set TROJAN_PASS_GMAIL_ACCOUNT=<Your Gmail Account>
heroku config:set TROJAN_PASS_GMAIL_PASSWORD=\<Your Gmail Password>
```

Last, deploy and trigger the build:
```shell
git add . && git commit -m "trigger deploy" && git push heroku main
```

### GitHub Actions

Fork this project, then add the following project [secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository):

- `TROJAN_PASS_NETID`
- `TROJAN_PASS_PASSWORD`
- `TROJAN_PASS_GMAIL_ACCOUNT`
- `TROJAN_PASS_GMAIL_PASSWORD`

You need to

1. enable repo `Action` (appear as in tabs above the repo name)
2. enable `Get Trojan Pass` Action
3. run it instantly or wait for the automation


## Quick Setup on Your Machine

On Ubuntu with bash:
```shell
git clone https://github.com/dqwert/TrojanPass.git
cd TrojanPass

# root privilege required
./scripts/setup_firefox.sh

# IMPORTANT: replace <>s with your info
`printf '\n# Trojan Pass\nexport TROJAN_PASS_NETID="<Your Net ID>"\nexport TROJAN_PASS_PASSWORD="<Your NetID password>"\nexport TROJAN_PASS_GMAIL_ACCOUNT="<Your Gmail Account>"\nexport TROJAN_PASS_GMAIL_PASSWORD="<Your Gmail Password>"\n' >> ~/.bash_profile

python3 main.py
```

Optional: setup crontab, see below.

## Project Setup

### Environment Variables

- set your system environment variables:
  - Unix
    - ZSH: `printf '\n# Trojan Pass\nexport TROJAN_PASS_NETID="<Your Net ID>"\nexport TROJAN_PASS_PASSWORD="<Your NetID password>"\nexport TROJAN_PASS_GMAIL_ACCOUNT="<Your Gmail Account>"\nexport TROJAN_PASS_GMAIL_PASSWORD="<Your Gmail Password>"\n' >> ~/.zshrc`
    - Bash: `printf '\n# Trojan Pass\nexport TROJAN_PASS_NETID="<Your Net ID>"\nexport TROJAN_PASS_PASSWORD="<Your NetID password>"\nexport TROJAN_PASS_GMAIL_ACCOUNT="<Your Gmail Account>"\nexport TROJAN_PASS_GMAIL_PASSWORD="<Your Gmail Password>"\n' >> ~/.bash_profile` (or `>> ~/.bashrc`)
    - Note: use `echo` in macOS and `printf` on Linux
    - For example, on macOS 11.6, suppose the NET ID is `wq`, password is `foo`, Gmail account is `wangqin0.me@gmail.com`, Gmail password is `fool` open the Terminal and execute `echo '\n# Trojan Pass\nexport TROJAN_PASS_NETID="wq"\nexport TROJAN_PASS_PASSWORD="foo"\nexport TROJAN_PASS_GMAIL_ACCOUNT="wangqin0.me@gmail.com"\nexport TROJAN_PASS_GMAIL_PASSWORD="fool"\n' >> ~/.zshrc` 
  - Windows
    - I don't use Windows, maybe you can take look at [about_Environment_Variables](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_environment_variables) in Microsoft Docs
  - Notice that `<>` is NOT in the actual command; for security concerns, please don't hard code your password into the program

### Install Prerequisites

#### Ubuntu 20.04

Firefox: `./setup_scripts/setup_firefox.sh`
Chrome: `./setup_scripts/setup_chrome.sh`

#### macOS

Download the browser and related chrome driver. Add the driver to path directory.  

### Run task

#### Linux with Xvfb

- Run once: `xvfb-run python3 <project root>/main.py` (for example: `xvfb-run python3 ~/TrojanPass/main.py`), note that you need to manually set environment variables in `crontab -e`
- Run every day: Execute `cron -e` in shell then add following line: `20 15 * * * cd <path to TrojanPass> && xvfb-run python3 main.py &> ~/TrojanPass.log`, this will run task at 7:00 am every day and log is saved to `~/TrojanCheck.log`

#### macOS

Inside project, run once: `python3 main.py`

## Acknowledgement

https://elements.heroku.com/buildpacks/gordiansoftware/heroku-integrated-firefox-geckodriver
