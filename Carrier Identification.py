import phonenumbers
from phonenumbers import carrier, geocoder

phone_number = input("Enter your phone number in E.164 format (e.g., +233XXXXXXXXX): ")
ph_num = f"+233{phone_number}".strip()
parse_num = phonenumbers.parse(phone_number)

print("Country:", geocoder.description_for_number(parse_num, "en"))
print("Carrier:", carrier.name_for_number(parse_num, "en"))