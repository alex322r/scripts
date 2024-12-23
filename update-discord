#!/bin/bash

# Update Discord

# discord url

discord_dir="/opt/Discord"
discord_version=$(cat $discord_dir/version.txt)
echo "Current Discord version: $discord_version"

# Get latest version
discord_url="https://discord.com/api/download?platform=linux&format=tar.gz"
echo "comprobando ultima version de $discord_url"
discord_latest_version=$(curl -I 'https://discord.com/api/download?platform=linux&format=tar.gz' 2>/dev/null | grep -oP '(?<=/)[0-9]+\.[0-9]+\.[0-9]+(?=/)'
)

# Check if the latest version is different from the current version
if [ "$discord_version" != "$discord_latest_version" ]; then
  echo "Updating Discord from $discord_version to $discord_latest_version"
  # Download the latest version
  wget -O /tmp/discord.tar.gz $discord_url
  # Extract the tarball
  tar -xvzf /tmp/discord.tar.gz -C /tmp/
  # Remove the old version
  sudo rm -rf $discord_dir
  # Move the new version to the correct directory
  sudo mv /tmp/Discord $discord_dir
  # Update the version file
  echo $discord_latest_version | sudo tee $discord_dir/version.txt
  echo "Discord updated successfully"
else
  echo "Discord is already up to date"
fi