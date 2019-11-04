def vailBookObject(BookObject):
    if "name" in BookObject and "price" in BookObject and "ISBN" in BookObject:
        return True
    else:
        return False


valid_object = {
    "name": "f",
    "price": 234,
    "ISBN": 3453
}

missing_name = {
    "price": 234,
    "ISBN": 3453}
missing_price = {"name": "f",
                 "ISBN": 3453}
missing_ISBN = {"name": "f",
                "price": 234}
empty_dictionary = {}