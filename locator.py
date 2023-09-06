import phonenumbers

from phonenumbers import geocoder,timezone,carrier

num=input("enter num with +_ _:")

phone=phonenumbers.parse(num)

time =timezone.time_zones_for_number(phone)

loc=geocoder.description_for_number(phone,'en')

car=carrier.name_for_number(phone,'en')


print(phone)
print(time)
print(loc)
print(car)
