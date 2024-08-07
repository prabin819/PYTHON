with open("poem.txt","r") as f:
    poem = f.read()

print(poem)

if ('Twinkle' in poem):
    print("The poem contains Twinkle")
else:
    print("The poem does not contain Twinkle")