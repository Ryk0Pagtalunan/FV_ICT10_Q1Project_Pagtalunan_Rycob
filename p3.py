from pyscript import display, document

contact = "Contact Us!"
msg1 = "~Where to Contact Us~"
location = "Our Location"
msg2 = "*123 Coffee Street Brewville, GH San Juan Philippines*" #to assign a message to the value msg2; I don't want to disclose my location, so I'll just copy the ones in the example same with the other bottom ones
phone = "Phone Numbers"
msg3 = f"""Main: (123) 456 - 7890 \n Mobile: (0912) 345 - 7689"""
mail = "Email Addresses"
msg4 = f"""info@CuTea.com \n support@CuTea.com \n careers@CuTea.com"""

display(contact, target="contactus")
display(msg1, target="msg1")
display(location, target="location")
display(msg2, target="msg2")
display(phone, target="phone")
display(msg3, target="msg3")
display(mail, target="email")
display(msg4, target="msg4")