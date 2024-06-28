#!/bin/bash

# Make sure to modify /etc/pacman.conf to enable multilib
# (https://wiki.archlinux.org/title/official_repositories#Enabling_multilib)

# Config (MODIFY THESE BEFORE RUNNING SCRIPT)
nvidia_GPU = true # Only installs packages, make sure to follow https://wiki.hyprland.org/Nvidia/

# Get path of script file
script_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" &>/dev/null && pwd)

# Update all first
sudo pacman -Syu --noconfirm

# Install yay (AUR manager)
sudo pacman -S --needed base-devel git --noconfirm
git clone https://aur.archlinux.org/yay.git ~/yay
sh -c "cd ~/yay && makepkg -si"

# Install hyprland
yay -S hyprland-git --noconfirm
if [ "$nvidia_GPU" = true ]; then
	sudo pacman -S linux-headers --noconfirm
	sudo pacman -S nvidia-dkms --noconfirm
	sudo pacman -S nvidia-utils --noconfirm
	sudo pacman -S lib32-nvidia-utils --noconfirm
	sudo pacman -S egl-wayland --noconfirm
	sudo pacman -S libva-nvidia-driver --noconfirm
fi

# Install fonts
sudo pacman -S ttf-jetbrains-mono-nerd --noconfirm
sudo pacman -S ttf-nerd-fonts-symbols-mono --noconfirm
sudo pacman -S ttf-liberation --noconfirm
sudo pacman -S noto-fonts-emoji --noconfirm

# Install hyprland extra tools
sudo pacman -S mako --noconfirm
sudo pacman -S pipewire --noconfirm
sudo pacman -S wireplumber --noconfirm
sudo pacman -S polkit-gnome --noconfirm
sudo pacman -S qt5-wayland --noconfirm
sudo pacman -S qt6-wayland --noconfirm
sudo pacman -S wl-clipboard --noconfirm
yay -S hyprlock-git --noconfirm
yay -S hyprpaper-git --noconfirm
yay -S xdg-desktop-portal-hyprland-git --noconfirm

# Install extra packages
sudo pacman -S kitty --noconfirm
sudo pacman -S waybar --noconfirm
sudo pacman -S rofi-wayland --noconfirm
sudo pacman -S firefox --noconfirm
sudo pacman -S nemo --noconfirm
sudo pacman -S fastfetch --noconfirm
sudo pacman -S nwg-look --noconfirm
sudo pacman -S btop --noconfirm
sudo pacman -S steam --noconfirm
sudo pacman -S stow --noconfirm
sudo pacman -S grim --noconfirm
sudo pacman -S slurp --noconfirm
yay -S vesktop --noconfirm
yay -S visual-studio-code-bin --noconfirm
yay -S cava --noconfirm
yay -S cli-visualizer --noconfirm
yay -S bemoji --noconfirm

# Symlink all dotfiles
sh -c "cd $script_dir && stow ."

# Celebration!!!! and update all again
yay --noconfirm
