from datetime import datetime


def get_time_based_category():
    hour = datetime.now().hour

    if 6 <= hour < 11:
        return "breakfast"
    elif 11 <= hour < 16:
        return "lunch"
    elif 16 <= hour < 19:
        return "snacks"
    else:
        return "drinks"


def get_popular_keywords():
    return [
        "dosa",
        "idli",
        "biryani",
        "coffee",
        "sandwich",
        "burger"
    ]