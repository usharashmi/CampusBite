from app.database.connection import SessionLocal
from app.models.menu import Menu

db = SessionLocal()

items = [
    {"name": "Masala Dosa", "price": 50, "category": "breakfast"},
    {"name": "Idli", "price": 30, "category": "breakfast"},
    {"name": "Biryani", "price": 120, "category": "lunch"},
    {"name": "Coffee", "price": 20, "category": "drinks"},
]

for item in items:
    db.add(Menu(**item))

db.commit()
print("Seed data inserted!")