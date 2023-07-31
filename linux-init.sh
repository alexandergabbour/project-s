#!/usr/bin/env bash

#ask user if they want to perform the update/upgrade process

#update & upgrade repos
sudo apt update && sudo apt upgrade

#git
sudo apt install git

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~optional~apps~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#signal - taken from -> https://signal.org/download/linux/
wget -O- https://updates.signal.org/desktop/apt/keys.asc | gpg --dearmor > signal-desktop-keyring.gpg
cat signal-desktop-keyring.gpg | sudo tee /usr/share/keyrings/signal-desktop-keyring.gpg > /dev/null
echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/signal-desktop-keyring.gpg] https://updates.signal.org/desktop/apt xenial main' |\
  sudo tee /etc/apt/sources.list.d/signal-xenial.list
sudo apt update && sudo apt install signal-desktop

#vscode
snap install --classic code

#spotify
snap install spotify

#discord
snap install discord