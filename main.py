import os, requests, sys, colorama, json, time
from dotenv import load_dotenv
from termcolor import cprint

uname = os.getlogin()
welcome = f"\nWelcome, {uname}...\n"
github = "\nGithub: https://github.com/NError404F\n"
text = """

  ____   _____ _____ _   _ _______   _  _    ___  _  _   
 / __ \ / ____|_   _| \ | |__   __| | || |  / _ \| || |  
| |  | | (___   | | |  \| |  | |    | || |_| | | | || |_ 
| |  | |\___ \  | | | . ` |  | |    |__   _| | | |__   _|
| |__| |____) |_| |_| |\  |  | |       | | | |_| |  | |  
 \____/|_____/|_____|_| \_|  |_|       |_|  \___/   |_|  
"""

colorama.init()
load_dotenv()

# API KEYS
PHONE_VERIFICATION_API_KEY = os.getenv('PHONEVERAPIKEY')
ADDRESS_API_KEY = os.getenv('ADDRESSAPIKEY')

def phone_number_lookup():
   os.system("cls||clear")

   phone_number = input("Enter phone number to lookup with county code (ex +30 69...): ")

   response = requests.get(f"https://api.veriphone.io/v2/verify?phone={phone_number}&key={PHONE_VERIFICATION_API_KEY}")
   
   is_number_valid = response.json()['phone_valid']
   country = response.json()['country']
   country_code = response.json()['country_code']
   phone_type = response.json()['phone_type']
   carrier = response.json()['carrier']
   
   
   if is_number_valid == True:
      os.system("cls||clear")
      cprint('Number is valid', 'green')
      cprint(f'Phone number: {phone_number}\nCountry: {country}\nCountry code: {country_code}\nPhone type: {phone_type}\nCarrier: {carrier}\n', 'yellow')
   else:
      cprint('Number is invalid', 'red')
      os.system("timeout 3")
      main()

   os.system("pause")



def ip_lookup():
   os.system("cls||clear")

   ip_addr = input("Enter IP address to lookup: ")

   response = requests.get(f"http://ip-api.com/json/{ip_addr}")

   country = response.json()['country']
   country_code = response.json()['countryCode']
   region = response.json()['regionName']
   city = response.json()['city']
   zip = response.json()['zip']
   timezone = response.json()['timezone']
   isp = response.json()['isp']
   org = response.json()['org']

   try:
      os.system("cls||clear")
      cprint(f'IP: {ip_addr}\nCountry: {country}\nCountry code: {country_code}\nRegion: {region}\nCity: {city}\nZip code: {zip}\nTimezone: {timezone}\nISP: {isp}\nOrganization: {org}\n', 'yellow')
      os.system("pause")
   except:
      cprint("Couldn't find info on this IP address, it either doesn't exist or is invalid", 'red')
      os.system("timeout 3")



def address_lookup():
   os.system("cls||clear")
   country_code = input("Enter country code (ex. GR): ")
   address = input("Enter address (in Latin): ")
   postal_code = input("Enter postal code: ")

   url = "https://global-address.p.rapidapi.com/V3/WEB/GlobalAddress/doGlobalAddress"

   querystring = {"ctry":f"{country_code}","format":"json","a1":f"{address}","DeliveryLines":"Off", "postal":f"{postal_code}"}

   headers = {
	"X-RapidAPI-Key": f"{ADDRESS_API_KEY}",
	"X-RapidAPI-Host": "global-address.p.rapidapi.com"
   }

   response = requests.get(url, headers=headers, params=querystring)

   print(response.json())

   option = input("Do you want to save to a json file? [Y/N]: ")

   if option == "Y":
      f = open("address.json", "x")
      with open('address.json', 'w') as f:
         json.dump(response.json(), f)
   elif option == "N":
      main()
   else:
      cprint("Wrong option... Returning to main page", 'red')
      os.system("timeout 3")
      main()


   
   os.system("pause")



def main():
   os.system("cls||clear")
   os.system("title OSINT404 by Error404 ")
   cprint(text, 'green')

   for char in github:
      time.sleep(0.03)
      sys.stdout.write(char)
      sys.stdout.flush()
   time.sleep(1)
   
   for char in welcome:
      time.sleep(0.03)
      sys.stdout.write(char)
      sys.stdout.flush()
   time.sleep(1)

   cprint("\n[1] Phone number lookup\n[2] IP lookup\n[3] Address lookup\n", 'magenta')

   option = input(f"{uname}:~$ ")

   if option == "1":
      phone_number_lookup()
   if option == "2":
      ip_lookup()
   if option == "3":
      address_lookup()

while True:
   main()