#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Create .devcontainer/.ssh directory if it doesn't exist
DEVCONTAINER_SSH_DIR="${PROJECT_ROOT}/.devcontainer/.ssh"
mkdir -p "$DEVCONTAINER_SSH_DIR"

# Copy SSH keys and config
if [ -f "$HOME/.ssh/authorized_keys" ]; then
    cp "$HOME/.ssh/authorized_keys" "$DEVCONTAINER_SSH_DIR/"
    chmod 600 "$DEVCONTAINER_SSH_DIR/authorized_keys"
else
    echo "Warning: $HOME/.ssh/authorized_keys not found"
fi

# Copy GitHub SSH keys if they exist
for key in id_rsa id_ed25519; do
    if [ -f "$HOME/.ssh/$key" ]; then
        cp "$HOME/.ssh/$key" "$DEVCONTAINER_SSH_DIR/"
        cp "$HOME/.ssh/$key.pub" "$DEVCONTAINER_SSH_DIR/"
        chmod 600 "$DEVCONTAINER_SSH_DIR/$key"
        chmod 644 "$DEVCONTAINER_SSH_DIR/$key.pub"
    fi
done

# Copy SSH config if it exists
if [ -f "$HOME/.ssh/config" ]; then
    cp "$HOME/.ssh/config" "$DEVCONTAINER_SSH_DIR/"
    chmod 600 "$DEVCONTAINER_SSH_DIR/config"
fi

# Copy known_hosts if it exists
if [ -f "$HOME/.ssh/known_hosts" ]; then
    cp "$HOME/.ssh/known_hosts" "$DEVCONTAINER_SSH_DIR/"
    chmod 644 "$DEVCONTAINER_SSH_DIR/known_hosts"
fi

echo "SSH configuration has been set up successfully"
echo "You can now build/rebuild your devcontainer"
