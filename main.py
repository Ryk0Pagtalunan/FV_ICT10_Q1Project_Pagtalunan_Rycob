from pyscript import display

store_name = "𝒞u𝒯𝕖a" #string
time_open = ["7:30 AM-", "8:30 PM"] #list
owner = "Rycob Pagtalunan" #string
yearfounded = 2025 #integer
has_delivery = (True) #boolean

item1 = "Seal Boba Tea" #string | Cookies n cream/Oreo Boba Tea
price1 = 90.0 #float
item2 = "Frog Boba Tea" #string | Matcha Boba Tea
price2 = 95.0 #float
item3 = "Dog Boba Tea" #string  | Mocha Boba Tea
price3 = 100.50 #float
item4 = "Cat Boba Tea" #string  | Classic Boba Tea
price4 = 85.0 #float

display(store_name, target= "storename")
display(owner, target="ownername")
display(yearfounded, target="yearfounded")

display(item1, target="name1")
display(item2, target="name2")
display(item3, target="name3")
display(item4, target="name4")
display(f"₱ {price1}", target="price1")
display(f"₱ {price2}", target="price2")
display(f"₱ {price3}", target="price3")
display(f"₱ {price4}", target="price4")

display(f"Opening Hours: {time_open}", target="time") 