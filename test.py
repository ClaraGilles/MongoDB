from pymongo import MongoClient

client = MongoClient("mongodb://mongoadmin:mongopassword@localhost:27017")

# Select or create a database
db = client['delivery_app']

# Insert a document into the collection
# Collection 1: Restaurants
restaurants = db['restaurants']

restaurant_data = [
    {
        "_id": 1,
        "name": "La Table Gourmande",
        "address": {
            "street": "12 Rue de Rivoli",
            "city": "Paris",
            "postal_code": "75001",
            "country": "France"
        },
        "phone": "+33 1 40 00 00 00",
        "cuisine": "French",
        "rating": 4.7
    },
    {
        "_id": 2,
        "name": "Sushi World",
        "address": {
            "street": "5th Avenue",
            "city": "New York",
            "postal_code": "10001",
            "country": "USA"
        },
        "phone": "+1 212 555 1234",
        "cuisine": "Japanese",
        "rating": 4.5
    }
]

restaurants.insert_many(restaurant_data)

# Collection 2: Menus
menus = db['menus']
menu_data = [
    {
        "restaurant_id": restaurants.find_one({"name": "La Table Gourmande"})["_id"],
        "items": [
            {"dish_name": "Foie Gras", "price": 25.00, "category": "Starter"},
            {"dish_name": "Coq au Vin", "price": 32.50, "category": "Main"},
            {"dish_name": "Tarte Tatin", "price": 12.00, "category": "Dessert"}
        ]
    },
    {
        "restaurant_id": restaurants.find_one({"name": "Sushi World"})["_id"],
        "items": [
            {"dish_name": "Miso Soup", "price": 3.50, "category": "Starter"},
            {"dish_name": "Salmon Nigiri", "price": 15.00, "category": "Main"},
            {"dish_name": "Green Tea Mochi", "price": 7.00, "category": "Dessert"}
        ]
    }
]
menus.insert_many(menu_data)
db.menus.insert_many(menu_data)


# Collection 3: Dishes (individual dishes information)
dishes = db['dishes']
dish_data = [
    {"name": "Foie Gras", "ingredients": ["Duck liver", "Butter", "Salt"], "calories": 450},
    {"name": "Coq au Vin", "ingredients": ["Chicken", "Wine", "Mushrooms"], "calories": 600},
    {"name": "Tarte Tatin", "ingredients": ["Apples", "Sugar", "Butter"], "calories": 300},
    {"name": "Miso Soup", "ingredients": ["Miso paste", "Tofu", "Seaweed"], "calories": 60},
    {"name": "Salmon Nigiri", "ingredients": ["Salmon", "Rice", "Soy Sauce"], "calories": 150},
    {"name": "Green Tea Mochi", "ingredients": ["Rice flour", "Green tea", "Sugar"], "calories": 200}
]
dishes.insert_many(dish_data)

# Collection 4: Orders (customer orders)
orders = db['orders']
order_data = [
    {
        "customer_name": "Alice",
        "restaurant_id": restaurants.find_one({"name": "La Table Gourmande"})["_id"],
        "items_ordered": [
            {"dish_name": "Foie Gras", "quantity": 1},
            {"dish_name": "Coq au Vin", "quantity": 1}
        ],
        "total_price": 57.50,
        "order_date": "2023-09-30",
        "status": "Delivered"
    },
    {
        "customer_name": "Bob",
        "restaurant_id": restaurants.find_one({"name": "Sushi World"})["_id"],
        "items_ordered": [
            {"dish_name": "Salmon Nigiri", "quantity": 2},
            {"dish_name": "Miso Soup", "quantity": 1}
        ],
        "total_price": 33.50,
        "order_date": "2023-09-29",
        "status": "Pending"
    }
]
orders.insert_many(order_data)

# Collection 5: Reviews (customer reviews)
reviews = db['reviews']
review_data = [
    {
        "restaurant_id": restaurants.find_one({"name": "La Table Gourmande"})["_id"],
        "customer_name": "Alice",
        "rating": 5,
        "comment": "Fantastic experience! The Coq au Vin was exceptional."
    },
    {
        "restaurant_id": restaurants.find_one({"name": "Sushi World"})["_id"],
        "customer_name": "Bob",
        "rating": 4,
        "comment": "Great sushi, but the wait was a bit long."
    }
]
reviews.insert_many(review_data)

# Collection 6: Delivery Drivers (information about delivery personnel)
drivers = db['drivers']
driver_data = [
    {"name": "Luna", "vehicle_type": "Bicycle", "license_plate": "FR-1234-BX", "phone": "+33 6 12 34 56 78"},
    {"name": "Tom", "vehicle_type": "Motorcycle", "license_plate": "NY-5678-ZT", "phone": "+1 555 987 6543"}
]
drivers.insert_many(driver_data)
