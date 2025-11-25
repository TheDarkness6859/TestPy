# Gestión del inventario
# • Registrar, consultar, actualizar y eliminar productos. x
# • Cada producto debe tener: título, autor, categoría, precio, cantidad en stock. x

# Registro y consulta de ventas
# • Permitir registrar ventas de productos, asociando: cliente, producto vendido,
# cantidad, fecha y descuento (si aplica).
# • Validar stock disponible y actualizarlo automáticamente.

# Módulo de reportes
# • Mostrar el top 3 de productos más vendidos.
# • Generar reporte de ventas totales agrupado por autor.
# • Calcular ingreso neto y bruto (con y sin descuento).
import csv

# The main inventory of the code
inventory = []
# The inventory for the clients
Clients = []

ARCHIVO_CSV = "Inventario.csv"

def Save():
    with open(ARCHIVO_CSV, "w") as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Book","Author","Category","Price","Amount"])
        for Book in inventory:
            writer.writerow([Book["Book"], Book["Author"], Book["Category"], Book["Price"], Book["Amount"]])

def Load():
    global inventory
    try:
        with open(ARCHIVO_CSV, "r") as archivo:
            lector = csv.reader(archivo)
            next(lector)
            for fila in lector:
                if len(fila) == 5:
                    Book, Author, Category, Price, Amount = fila
                    inventory.append({
                        "Book": Book,
                        "Author": str(Author),
                        "Category": str(Category),
                        "Price": float(Price),
                        "Amount": int(Amount)
                    })
                    print(f"\n Data upload from {ARCHIVO_CSV}\n")
    except FileNotFoundError:
        print(f"\nDon't exist a {ARCHIVO_CSV}\n")

#Add the names of the books
def Book():
    try:
        while True:
            Name = str(input("Add a new book: ")).strip()
            if Name == "" or not Name.replace(" ", "").isalpha():
                print("The name can't be empty or has numbers")
                continue
            else:
                print(f"The book called: {Name} were added\n")
                return Name
    except ValueError:
        print("you can't do this")

#Add the name of the authors
def Name():
    while True:
        try:
            Owner = str(input("pelease add the author of the book: "))
            if Owner == "" or not Owner.replace(" ", "").isalpha():
                print("The name can't be empty or has numbers")
                continue
            else:
                print(f"The name of the author:{Owner} were added\n")
                return Owner
        except ValueError:
            print("you can't do this")

#Add the category of the books 
def Category():
    while True:
        try:
            Category = str(input("pelease add the category of the book: "))
            if Category == "" or not Category.replace(" ", "").isalpha():
                print("The category can't be empty or has numbers")
                continue
            else:
                print(f"The category: {Category} were added\n")
                return Category
        except ValueError:
            print("you can't do this")

#Add the price of the books
def Price():
    while True:
        try:
            Price = float(input("How much cost: "))
            if Price <= 0:
                print("It can't cost this, it's very hard")
                continue
            else:
                print("The price were added\n")
                return Price
        except ValueError:
            print("Impossible")

#Add the stock of the books
def Amount():
    while True:
        try:
            Stock = int(input("How much books have: "))
            if Stock <= 0:
                print("It can't possible")
            else:
                print(f"Alright, we have {Stock} in the stock\n")
                return Stock
        except ValueError:
            print("Holy moly, it's impossible")

#Add all the information in the inventory like a dictionary
def Add():
    global inventory
    while True:
        print("Alright, you can fill out the information: ")

        Books = Book()
        Authors = Name()
        Type = Category()
        Cost = Price()
        Stock = Amount()
        
        Shelving = {"Book": Books,
                    "Author": Authors,
                    "Category": Type,
                    "Price": Cost,
                    "Amount": Stock
        }
        
        inventory.append(Shelving)
        print(f"The book: {Books} were add to the shelving\n")
        Save()
        
        while True:
                Continue = str(input("Do you want continue add books (y/n)")).lower().strip()
                
                if Continue == "" or not Continue.replace(" ", "").isalpha():
                    print("The name can't be empty or has numbers.")
                    continue
                elif Continue == "y":
                    break
                elif Continue == "n":
                    return
                else:
                    print("Ingrese (y/n): ")

        

    

#Show the inventory of the bookshop
def Look():
    global inventory

    if not inventory:
        print("In our stock don't have nothing, sorry")
        return
    
    while True:
        try:
            Find = str(input("Please put the name of the book that you need: "))
            if Find == "" or not Find.replace(" ", "").isalpha():
                print("The name can't be empty or has numbers")
                continue
            else:
                print(f"The book called: {Find} were Find\n")
                break
        except ValueError:
            print("you can't do this")

    for Book in inventory:
        if Book["Book"] == Find:
            print(f"We have the book: {Book}")
            break

#Update the inevntory with new data
def Update():
    global inventory

    if not inventory:
        print("In our stock don't have nothing, sorry")
        return
    
    Find = False
    for Books in inventory:
        Update = str(input("Please put the name of the book that you want update: "))
        if Update == Books["Book"]:
            Find = True
            print(f"We have the book: {Books}")

            books = Book()
            Authors = Name()
            Type = Category()
            Cost = Price()
            Stock = Amount()

            Books["Book"] = books
            Books["Author"] = Authors
            Books["Category"] = Type
            Books["Price"] = Cost
            Books["Amount"] = Stock
            Save()
            print("book update correctly:")
            print(Books)
            break
    if not Find:
          print("In our stock don't have any book called that, sorry")


#Delete the books of the inventory
def Delete():
    global inventory

    if not inventory:
        print("In our stock don't have nothing, sorry")
        return
    
    while True:
        try:
            book = str(input("Please put the name of the book that you need delete: "))
            if book == "" or not book.replace(" ", "").isalpha():
                print("The name can't be empty or has numbers")
                continue
            else:
                print(f"The book called: {book} were Find")
                break
        except ValueError:
            print("you can't do this")

    encontrado = False

    for Book in inventory:
        if Book["Book"] == book:
            encontrado = True
            print(f": {Book}")

            Sure = input("¿you are sure that delete it? (y/n): ")

            if Sure.lower() == "y":
                inventory.remove(Book)
                print("Book delete correctly.")
            else:
                print("Delete of book cancel.")
            break
        Save()

    if not encontrado:
        print("This book doesn't exist in our bookshop")

#Identify the vents in the booshop with loops
def vents():
    global inventory
    for Book in inventory:
        if Book["Book"]:
            print(f"We have the book: {Book}")
            break

    while True:
        try:
            Name = str(input("Add the client: ")).strip()
            if Name == "" or not Name.replace(" ", "").isalpha():
                print("The name can't be empty or has numbers")
                continue
            else:
                print(f"The client is {Name}\n")
                break
        except ValueError:
            print("you can't do this")
    

        
    while True:
        try:
            for Book in inventory:
                Prod = str(input("pelease enter the name of the sale book : ")).strip()
                if Prod == "" or not Prod.replace(" ", "").isalpha():
                    print("The name can't be empty or has numbers")
                    continue
                elif Book["Book"] == Prod:
                    print(f"We have the book: {Book}")
                    break
                else:
                    continue
            break  
        except ValueError:
            print("you can't do this")  

    while True:
        try:
            for books in inventory:
                Stock = int(input("How much books do you sell: "))
                if Stock <= 0:
                    print("It can't possible")
                elif Prod == books["Book"]:
                    if Stock > 0 and Stock < books["Amount"]:
                        books["Amount"] -= Stock
                        print(f"incredible you can sell {Stock} books\n")
                        break
                    else:
                        print("We don't have the amounts of books\n")
            break
        except ValueError:
            print("Holy moly, it's impossible")

    while True:

        Date = str(input("What date do you sell it: ")).isalnum()

        if Date == True:
            print(f"OK the date is add correctly\n")
            break
        else:
            print("it's impossible")
            continue

    Vents = {"Client": Name,
                    "Book": Prod,
                    "Sell": Stock,
                    "Date": Date
        }

    Clients.append(Vents)
    print(f"The sell of: {Name} were add to the Clients\n")
    Save()
        
    while True:
            Continue = str(input("Do you want continue add sells (y/n)")).lower().strip()
            
            if Continue == "" or not Continue.replace(" ", "").isalpha():
                print("The name can't be empty or has numbers.")
                continue
            elif Continue == "y":
                break
            elif Continue == "n":
                return
            else:
                print("put (y/n)")

def Math():
    global inventory
    Total = sum(book["Amount"] * book["Price"] for book in inventory)
    Authors = max(inventory, key=lambda p: p["Author"])

    print(f"Stas of the inventory: \nThe gross total:{Total} \nThe author with more vents is: {Authors}")





    




