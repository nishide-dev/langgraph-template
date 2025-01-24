#!/bin/bash

# Get the directory where the script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Create .devcontainer/.ssh directory if it doesn't exist
DEVCONTAINER_SSH_DIR="${PROJECT_ROOT}/.devcontainer/.ssh"
mkdir -p "$DEVCONTAINER_SSH_DIR"

# Copy authorized_keys to .devcontainer/.ssh
if [ -f "$HOME/.ssh/authorized_keys" ]; then
    cp "$HOME/.ssh/authorized_keys" "$DEVCONTAINER_SSH_DIR/"
    chmod 600 "$DEVCONTAINER_SSH_DIR/authorized_keys"
else
    echo "Warning: $HOME/.ssh/authorized_keys not found"
    echo "Please make sure you have SSH keys set up for authentication"
    exit 1
fi

echo "SSH configuration has been set up successfully"
echo "You can now build/rebuild your devcontainer"
