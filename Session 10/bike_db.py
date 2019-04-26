import pymongo

client = pymongo.MongoClient("mongodb+srv://longbruce:sBrsBYehmstUAQM1@cluster0-gv7w3.mongodb.net/test?retryWrites=true")
db = client.test


def all_bikes(): 
    return list(db.bikes.find({}))

def add_bike(model, price, image, year):
    db.bikes.insert_one({"model": model, 'price':price,'image_url':image, 'year': year})
