# coding=utf-8
import sys

class Vehicle:
    def __init__(self, make, model, kilometres, mot):
        self.make = make
        self.model = model
        self.kilometres = kilometres
        self.mot = mot  # MOT is British English for TÜV

    def make_and_model(self):
        return self.make + " " + self.model


def display_vehicle_list(vehicles):
    for index, vehicle in enumerate(vehicles, 1):
        print "ID: " + str(index)
        print vehicle.make_and_model()
        print "Kilometres driven: " + vehicle.kilometres
        print "Last MOT was performed on: " + vehicle.mot
        print

    if not vehicles:
        print "You don't have any vehicles! Try entering a new vehicle."


def add_new_vehicle(vehicles):
    print "A new car will be added to the list."
    print
    make = raw_input("What is the make of car? ")
    model = raw_input("What model? ")
    kilometres = raw_input("How many kilometres has this vehicle been driven? ")
    mot = raw_input("Finally, when was the date of its last MOT? ")

    new_vehicle = Vehicle(make=make, model=model, kilometres=kilometres, mot=mot)
    vehicles.append(new_vehicle)

    print
    print new_vehicle.make_and_model() + " was added to the fleet."


def select_vehicle(vehicles):
    print "List of available vehicles:"
    for index, vehicle in enumerate(vehicles, 1):
        print str(index) + ": " + vehicle.make_and_model()

    natural_id = raw_input("Which vehicle should be edited? Enter its ID: ")
    try:
        car_select = int(natural_id) - 1  # User input ID matches list index number
    except:
        print "Please enter a valid ID number."

    while True:
        print
        print "Please choose one of these options:"
        print "1) Change number of kilometres driven"
        print "2) Change date of last MOT"
        print "3) Delete vehicle"
        print "4) Back"
        print

        option_select = raw_input("What would you like to do? Please enter the corresponding number: ")
        print

        if option_select == "1":
            edit_km(car_select, vehicles)
        elif option_select == "2":
            edit_mot(car_select, vehicles)
        elif option_select == "3":
            delete_vehicle(car_select, vehicles)
        elif option_select == "4":
            main()
        else:
            print "Please enter one of the numbers listed above."


def edit_km(car_select, vehicles):
    selected_car = vehicles[int(car_select)]
    updated_km = raw_input("Enter the new total km for %s " % selected_car.make_and_model())
    selected_car.kilometres = updated_km
    print "Total km driven for %s is now %s" % (selected_car.make_and_model(), updated_km)


def edit_mot(car_select, vehicles):
    selected_car = vehicles[int(car_select)]
    updated_mot = raw_input("Enter the new MOT date for %s " % selected_car.make_and_model())
    selected_car.mot = updated_mot
    print "New MOT date for %s is now set to %s" % (selected_car.make_and_model(), updated_mot)


def delete_vehicle(car_select, vehicles):
    selected_car = vehicles[int(car_select)]
    deleteconfirm = True
    while deleteconfirm == True:
        confirm = raw_input("Are you sure you want to delete the vehicle? (y/n) ").lower()
        if confirm == "y" or confirm == "yes":
            vehicles.remove(selected_car)
            print "Vehicle deleted."
            print
            main()
        elif confirm == "n" or confirm == "no":
            deleteconfirm = False
            continue
        else:
            print "Please enter (y)es or (n)o!"

def generate_file(vehicles):
    vehicle_file = open("vehicle_list.txt", "w+")
    for vehicle in vehicles:
        vehicle_file.write("%s %s, %s kilometres, last MOT %s\n" % (vehicle.make, vehicle.model, vehicle.kilometres, vehicle.mot))
    print "List of vehicles has been saved as vehicle_list.txt."
    print

    vehicle_file.close()

''' @Patrick: Hab hier Beispieleinträge außerhalb von main() generiert, da die Liste überschrieben wird, wenn main()
    durch meine Funktion select_vehicle() erneut aufgerufen wird. Das Problem ist, dass ich irgendwie meine Liste
    vehicles an main() weitergeben muss... Hab keine bessere Methode dafür gefunden als vehicles als global variable
    festzulegen - hast du eine bessere Lösung?'''

def populate_list():
    global vehicles
    example = Vehicle(make="DeLorean", model="DMC-12", kilometres="88", mot="26.10.1985")
    example2 = Vehicle(make="Ford", model="Falcon GT", kilometres="4000", mot="12.04.1979")
    example3 = Vehicle(make="Dodge", model="Monaco", kilometres="2000", mot="20.06.1980")
    vehicles = [example, example2, example3]


def main():
    print "Welcome to the Vehicle Manager!"
    while True:
        print
        print "Please choose one of these options:"
        print "1) Show all vehicles"
        print "2) Add a new vehicle to the list"
        print "3) Edit (km/MOT) or delete a vehicle"
        print "4) Generate a text file of the vehicle list"
        print "5) Exit the Vehicle Manager"
        print

        user_number = raw_input("What would you like to do? Please enter the corresponding number: ")
        print

        if user_number == "1":
            display_vehicle_list(vehicles)
        elif user_number == "2":
            add_new_vehicle(vehicles)
        elif user_number == "3":
            select_vehicle(vehicles)
        elif user_number == "4":
            generate_file(vehicles)
        elif user_number == "5":
            quitconfirm = True
            while quitconfirm == True:
                confirm = raw_input("Are you sure you want to quit? (y/n) ").lower()
                if confirm == "y" or confirm == "yes":
                    print "Now exiting the Vehicle Manager..."
                    sys.exit() # Break hat nicht funktioniert, laut debugger hat das Programm nach break nochmals main() durchgeführt... Ursache noch unklar
                elif confirm == "n" or confirm == "no":
                    quitconfirm = False
                    continue
                else:
                    print "Please enter (y)es or (n)o!"
        else:
            print "Please enter one of the numbers listed above."


if __name__ == "__main__":  # this means that if somebody ran this Python file, execute only the code below
    populate_list()
    main()
