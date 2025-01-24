#!/bin/bash

# Install OpenSSH Server if not already installed
if ! dpkg -l | grep -q openssh-server; then
    sudo apt-get update
    sudo apt-get install -y openssh-server
fi

# Create required directory
sudo mkdir -p /run/sshd

# Setup SSH key authentication for vscode user
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# Copy all SSH files from mounted .ssh directory
if [ -d "${WORKSPACE_ROOT}/.devcontainer/.ssh" ]; then
    cp "${WORKSPACE_ROOT}/.devcontainer/.ssh/"* ~/.ssh/ 2>/dev/null || true
    chmod 600 ~/.ssh/*
    chmod 644 ~/.ssh/*.pub ~/.ssh/known_hosts 2>/dev/null || true
fi

# Start SSH daemon
sudo /usr/sbin/sshd

echo "SSH server has been set up and started"
