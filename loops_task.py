items = []
counter = 0
total = 0.0
while True:
    user_inp = input('item (enter "done" when finished): ')
    if user_inp.lower() == "done":
        break
    price = input("price: ")
    quan = input("quantity: ")
    items.append({"item_name":user_inp, "price":price, "quantity":quan})

print("-"*20)
print("receipt")
print("-"*20)


for item in items:
    print((item["quantity"]+" " + item["item_name"] +" "+ "{:.3f}" + "KD").format(float(item["price"])*float(item["quantity"])))
    total += float(item["quantity"])*float(item["price"])

print("-"*20)
print("total: %.3f" % total)
