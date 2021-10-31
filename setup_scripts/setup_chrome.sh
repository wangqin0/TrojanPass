# install chrome
sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add
sudo bash -c "echo 'deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main' >> /etc/apt/sources.list.d/google-chrome.list"
sudo apt -y update
sudo apt -y install google-chrome-stable

# install Xvfb (X virtual framebuffer): an in-memory display server
sudo apt update
sudo apt install -y unzip xvfb libxi6 libgconf-2-4
sudo apt install default-jdk

# download and setup chromedriver
# find your version at https://sites.google.com/chromium.org/driver/downloads
google-chrome --version
wget https://chromedriver.storage.googleapis.com/95.0.4638.17/chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
