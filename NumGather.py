import pyfiglet
import phonenumbers
import areadatabase
from phonenumbers import carrier
from phonenumbers import geocoder
from pyfiglet import Figlet

pyfiglet.print_figlet("Num Gather",'banner')
print("This tool was made by H1DD3N_SH4D0W for SecHunt-OS")
print("\t\t\t Github Profile : https://github.com/mr-sh4n")

print("If indian Number : +91987456321")
number = input ("Enter your mobile number : ")
phone = phonenumbers.parse(number)
print("The country of this Phone number is : "+geocoder.description_for_number(phone, 'en'))
print("The ISP of the phone number is : "+carrier.name_for_number(phone,'en'))

areadatabase.find_area(number)
