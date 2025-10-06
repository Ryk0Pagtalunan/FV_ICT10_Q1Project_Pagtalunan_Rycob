from pyscript import display, document

def Restate(e):
    name = document.getElementById("name").value
    address = document.getElementById("address").value
    contactinfo = document.getElementById("contact").value
    seal = float(document.getElementById("seal").value) if document.getElementById("seal").checked else 0 # Seal Boba Tea: Cookies & Cream | Opera AI
    frog = float(document.getElementById("frog").value) if document.getElementById("frog").checked else 0 # Frog Boba Tea: Matcha | Opera AI
    dog = float(document.getElementById("dog").value) if document.getElementById("dog").checked else 0 # Dog Boba Tea: Mocha | Opera AI
    cat = float(document.getElementById("cat").value) if document.getElementById("cat").checked else 0 # Cat Boba Tea: Classic | Opera AI

    total = (seal + frog + dog + cat)

    msg1 = f"Order for: {name}" # Google AI
    msg2 = f"Address: {address}" # Google AI
    msg3 = f"Contact number: {contactinfo}" # Google AI
    msg4 = f"Total: ₱ {total}" # Google AI

    display(msg1, target="appear1", append=False)
    display(msg2, target="appear2", append=False)
    display(msg3, target="appear3", append=False)
    display(msg4, target="appear4", append=False)