import sys, os, django


sys.path.append("E:/CMPE165/crunchy/crunchy") #here store is root folder(means parent).

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crunchy.settings")
django.setup()

from hotels.models import Hotel
import csv

with open('hotel_db.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # The header row values become your keys
        name = row['Name'].strip()
        city = row['City'].strip()
        address = row['Address'].strip()
        phone = row['Phone'].strip()
        rating = row['Rating'].strip()
        price = row['Price'].strip()
        images = row['Photo Urls'].strip()

        new_hotel = Hotel(name = name, city= city, address= address, phone = phone, rating = rating, price = price,
                          images = images)
        print(new_hotel.name)
        print(new_hotel.city)
        new_hotel.save()
