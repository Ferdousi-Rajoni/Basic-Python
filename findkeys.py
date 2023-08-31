key_location="chair"
locations=["garage","bedroom","living room","closet","chair","kitchen"]
for i in locations:
    if i==key_location:
        print("Key is found",i)
        break
    else:
        print("key is not found in",i)
        