#!/bin/bash

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

#vlc
snap install vlc

#balena etcher
curl -1sLf \
   'https://dl.cloudsmith.io/public/balena/etcher/setup.deb.sh' \
   | sudo -E bash
sudo apt update
sudo apt install balena-etcher-electron

#minecraft
curl -O https://launcher.mojang.com/download/Minecraft.deb

#steam
snap install steam