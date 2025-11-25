import time #This library add time in the code.
from Inventory import * #Impor my another archive in this for create a modular code.

def Menu():

    while True:

        print("Welcome to the national bookshop")
        print("What can you do:")
        print("1.Add new books \n2.Look the stock \n3.Update the stock \n4.Remove any book \n5.Vents of bookshop \n6.Watch the stast \n7.Exit of the inventory\n")

        try:
            Dec = int(input("Select any option: "))
            
            if Dec == 1:
                Add()
                input("Push ENTER to go back to the main menu\n")
            elif Dec == 2:
                Look()
                input("Push ENTER to go back to the main menu\n")
            elif Dec == 3:
                Update()
                input("Push ENTER to go back to the main menu\n")
            
            elif Dec == 4:
                Delete()
                input("Push ENTER to go back to the main menu\n")
            
            elif Dec == 5:
                vents()
                input("Push ENTER to go back to the main menu\n")

            elif Dec == 6:
                Math()
                input("Push ENTER to go back to the main menu\n")

            elif Dec == 7:  

                for timer in range(3, 0, -1):
                    print(f"\nClose the system: {timer}...")
                    time.sleep(1)
                print("\nThe system close.")
                break

            else:
                print("it doesn't a option")
        except ValueError:
            print("Invalid...")


Load()
Menu()
