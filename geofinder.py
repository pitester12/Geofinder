#original code by pitester12
#code that pairs well with the camhacker that gives you lon-lat location Btw, a 11 year old wrote this.
import time
from geopy.geocoders import Nominatim
from random import randint
import os
# importing requests module
import requests

os.system("clear")
 
# initializing URL
url = "https://www.google.com"
timeout = 10
try:
    # requesting URL
    request = requests.get(url,
                           timeout=timeout)
    time.sleep(1)
    print("testing Internet...")
    time.sleep(1)
    print("\033[1;32;40mInternet is on")
    print("\033[0;37;40m  ")
    time.sleep(1)
    os.system("clear")
 
# catching exception
except (requests.ConnectionError,
        requests.Timeout) as exception:
    print("testing internet")
    time.sleep(1)
    print("\033[1;31;40minternet is off")
    time.sleep(1)
    input("\033[0;37;40mPress Enter to end the program >> ")
    os.system("clear")
    quit()
 
os.system("clear")
#How to use:
#
#sudo apt-install geopy
#python3 geofinder.py
#there you have it!
#insert your longitude and then your latitude
#keep on finding!
print(" example: 40.7128 -74.0060 (New York city) ")
print(" ")
print("             ██████╗ ███████╗ ██████╗ ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗")
print("            ██╔════╝ ██╔════╝██╔═══██╗██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗")
print("            ██║  ███╗█████╗  ██║   ██║█████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝")
print("            ██║   ██║██╔══╝  ██║   ██║██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗")
print("            ╚██████╔╝███████╗╚██████╔╝██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║")
print("             ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝")
print(" ")
print("                   type in longitude and then latitude and then find location!")
print("                                          _____ ")
print("                                      ,-:` \;',`'-, ")
print("                                    .'-;_,;  ':-;_,'.")
print("                                   /; 📍 '/   ,  _`.-\ ")
print("                                  | '`. (`     /` ` \`| ")
print("                                  |:.  `\`-.   \_ 📍 /| ")
print("                                  |     ( 📍`,  .`\ ;'| ")
print("                                   \     | .'     `-'/ ")
print("                                    `.   ;/        .' ")
print("                                      `'-._____.-' ")
print("                              Original Code By: Pi Tester 12, ")
print(" ")
def fake_loading_bar():
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(randint(1,2))
    print()

def get_location_info(latitude, longitude):
    geolocator = Nominatim(user_agent="location_finder")
    location = geolocator.reverse(f"{latitude}, {longitude}")
    return location.address


def main():
    latitude = input("Enter latitude: (press enter to continue) ")
    longitude = input("Enter longitude: (press enter to continue) ")
    print("Wait, Geofinder is Fetching location information", end="", flush=True)
    start_time = time.time()
    fake_loading_bar()
    address = get_location_info(latitude, longitude)
    os.system("clear")
    print(f"Address: {address}")
    print(" ")

    end_time = time.time()
    duration = end_time - start_time
    print("Geofinder took", duration, "seconds, Address located.")

if __name__ == "__main__":
    main()

print(" ")
print(" ")
print(" Thank you for using Geofinder 🌎            ") 
print("                                            😄")
print("              I'm on top of the world! -> --■--")
print("                                          _/_\__ ")
print("             Geofinder                ,-:` \;',`'-, ")
print("           found location           .'-;_,;  ':-;_,'.")
print("                                   /; 📍 '/   ,  _`.-\ ")
print("               (•ᴗ•)              | '`. (`     /` ` \`| ")
print("                                  |:.  `\`-.   \_ 📍 /| ")
print("                                  |     ( 📍`,  .`\ ;'| ")
print("                                   \     | .'     `-'/ ")
print("                                    `.   ;/        .' ")
print("                                      `'-._____.-' ")
print(" ")
input("Press Enter to end the program >> ")
os.system("clear")

