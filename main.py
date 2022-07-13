import platform, socket, os, subprocess
from requests import get

os.system("cls")

# Machine Info
machine = platform.machine()
platform = platform.platform()


# Internet Info
ip = get('https://api.ipify.org').text
Internet_Citylocation = subprocess.check_output(f"curl ipinfo.io/{ip}/city", shell=False).decode('utf-8')
Internet_Countrylocation = subprocess.check_output(f"curl ipinfo.io/{ip}/country", shell=False).decode('utf-8')


# Print Data to Info

print("Machine Information: \n")

print(f"Machine: {machine}")
print(f"Platform: {platform}")

print("\nInternet Information: \n")

print(f"IP: {ip}")
print(f"Internet_CityLocation: {Internet_Citylocation}")
print(f"Internet_CountryLocation: {Internet_Countrylocation}")
