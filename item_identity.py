def get_item_identity(listing):
    stickers = tuple(
        sorted(
            (
                sticker.get("slot"),
                sticker.get("stickerId")
            )
            for sticker in listing["stickers"]
        )
    )

    return (
        listing["name"],
        listing["stattrak"],
        listing["souvenir"],
    )