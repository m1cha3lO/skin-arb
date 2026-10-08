import os

import requests
from dotenv import load_dotenv

load_dotenv()

def get_listings():
    api_key = os.getenv("CSFLOAT_API_KEY")

    if not api_key:
        raise ValueError("CSFLOAT_API_KEY not found in .env")

    headers = {
        "Authorization": api_key
    }

    response = requests.get(
        "https://csfloat.com/api/v1/listings",
        headers=headers,
        timeout=10
    )

    response.raise_for_status()
    data = response.json()
    listings = []

    for api_listing in data["data"]:
        item = api_listing.get("item", {})
        if "wear_name" not in item:
            continue

        skin = {
            "marketplace": "csfloat",
            "listing_id": api_listing["id"],
            "name": item['market_hash_name'],
            "float": item['float_value'],
            "paint_seed": item["paint_seed"],
            "stattrak": item["is_stattrak"],
            "souvenir": item["is_souvenir"],
            "stickers": item.get("stickers", []),
            "price": api_listing["price"] / 100
        }
        if validate_listing(skin):
            listings.append(skin)

    return listings

def validate_listing(listing):
    required_fields = [
        "marketplace",
        "listing_id",
        "name",
        "float",
        "paint_seed",
        "stattrak",
        "souvenir",
        "stickers",
        "price"
    ]

    for field in required_fields:
        if field not in listing:
            return False

    if not isinstance(listing["name"], str):
        return False
    if not isinstance(listing["float"], (int, float)):
        return False
    if not 0 <= listing["float"] <= 1:
        return False
    if not isinstance(listing["price"], (int, float)):
        return False
    if listing["price"] < 0:
        return False
    return True