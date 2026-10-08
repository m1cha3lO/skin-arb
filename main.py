from csfloat import get_listings
from item_identity import get_item_identity

listings = get_listings()
print(f"Retrieved {len(listings)} listings.")
print()

for item in listings[:5]:
    print("Listing")
    print("-" * 40)

    print(f"Marketplace: {item['marketplace']}")
    print(f"ID: {item['listing_id']}")
    print(f"Name: {item['name']}")
    print(f"Float: {item['float']:.6f}")
    print(f"Paint Seed: {item['paint_seed']}")
    print(f"StatTrak: {item['stattrak']}")
    print(f"Souvenir: {item['souvenir']}")
    print(f"Stickers: {len(item["stickers"])}")
    print(f"Price: ${item['price']:.2f}")

    print(f"Identity: {get_item_identity(item)}")
    print()