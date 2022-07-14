import platform,  os
from requests import get
from pathlib import Path

os.system("cls")

# Machine Info
machine = platform.machine()
platform = platform.platform()


# Internet Info
ip = get('https://api.ipify.org').text
os.system(f"curl ipinfo.io/{ip}/city -o city.txt")
os.system(f"curl ipinfo.io/{ip}/country -o country.txt")
os.system(f"curl ipinfo.io/{ip}/region -o region.txt")

# Puts Data into Variables.

Internet_Citylocation = Path('country.txt').read_text()
Internet_Countrylocation = Path('city.txt').read_text()
Internet_Countryregion = Path('region.txt').read_text()

# Print Data to Info

print("Machine Information: \n")

print(f"Machine: {machine}")
print(f"Platform: {platform}")

print("\nInternet Information: \n")

print(f"IP: {ip}\n")
print(f"Internet_CityLocation: {Internet_Citylocation}")
print(f"Internet_CountryLocation: {Internet_Countrylocation}")
print(f"Internet_Countryregion: {Internet_Countryregion}")
