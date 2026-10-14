def format_price(price):
    return f"₹{price}"


def calculate_total(items):
    return sum(item["price"] * item.get("qty", 1) for item in items)