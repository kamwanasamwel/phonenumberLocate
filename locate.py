from phonenumbers import carrier
from phonenumbers import geocoder
import phonenumbers

number = "+254703733726"


ch_number = phonenumbers.parse(number, "KH")
print(geocoder.description_for_number(ch_number, "en"))

service_number = phonenumbers.parse(number, "KO")
print(carrier.name_for_number(service_number, "en"))
