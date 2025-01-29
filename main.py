#Nicholas, Aaron, Alex, and Yenesis Music Festival Project
stages = set({})

#Prints the stages in a visually appealing way.
def stage_display(stages):
    stage_num = 1
    #Runs through every item in the list of stages.
    for i in stages:
        #For each item in stages, this will print the stage and its number, and then loop thorugh the stage printing all the equipment.
        print(f"\nStage {stage_num}: {i[0]}\nEquipment:")
        stage_num += 1
        for item in i:
            if type(item) is tuple:
                for equipment in item:
                    print(equipment)

#A function that allows you to add a stage to the stage list.
def add_stage():
    while True:
        stage = []
        equipment = []
        stage_name = input("\nWhat do you want to name the stage?:\n")
        equip_amount = input("\nHow many seperate pieces of equipment does this stage have?:\n")
        try:
            equip_amount = int(equip_amount)
        except:
            print("\nPlease enter a number.\n")
            continue
        #Adds a piece of equipment to the stage repeated as many times as requested.
        for i in range(equip_amount):
            equipment.append(input("\nPlease enter a piece of equipment:\n"))
        #converts the lists to tuples so they aren't mutable and can be added to a set
        equipment = tuple(equipment)
        stage.append(stage_name)
        stage.append(equipment)
        stage = tuple(stage)
        return stage

#Removes a stage
def remove_stage():
    while True:
        stage = input("\nWhat is the name of the stage you would like to remove?\n")
        for i in stages:
            if stage in i[0].split():
                return i
        print("Sorry, couldn't find that item in your list.")
        break

#"changes" a stage by removing the stage and adding a new one.
def change_stage():
    while True:
        stage = input("\nWhat is the name of the stage you would like to change?\n")
        for i in stages:
            if stage in i[0].split():
                stages.remove(i)
                stage = []
                equipment = []
                stage_name = input("\nWhat do you want to rename the stage?:\n")
                equip_amount = input("\nHow many seperate pieces of equipment do you want this stage to have?:\n")
                try:
                    equip_amount = int(equip_amount)
                except:
                    print("\nPlease enter a number.\n")
                    continue
                #Adds a piece of equipment to the stage repeated as many times as requested.
                for i in range(equip_amount):
                    equipment.append(input("\nPlease enter a piece of equipment:\n"))
                #converts the lists to tuples so they aren't mutable and can be added to a set
                equipment = tuple(equipment)
                stage.append(stage_name)
                stage.append(equipment)
                stage = tuple(stage)
                return stage
        #Exits the function if you entered a non-existent item
        print("Sorry, couldn't find that item in your list.")
        break
        
#Allows the user to access all other functions
def venues(stages):
    print("Welcome to venue management!")
    while True:
        print("Your venues currently look like this:")
        stage_display(stages)
        choice = input("Would you like to\n1:Add a stage\n2:Remove a stage\n3:Edit a stage\n4:Exit to main interface\nChoose:\n")
        if choice == '1':
            try:
                stages.add(add_stage())
            except:
                pass
        elif choice == '2':
            try:
                stages.remove(remove_stage())
            except:
                pass
        elif choice == '3':
            #Checks to avoid adding a non-existent item to the stages list
            isNull = change_stage()
            try:
                isNull[0]
            except:
                pass
            else:
                stages.add(isNull)
        elif choice == '4':
            #main()
            break
        else:
            print("Sorry, enter 1, 2, 3, or 4 to continue.")
            continue

#Allows the user to access the other functions
def main(stages):
    print("Hello! Welcome to your music festival management system!")
    while True:
        #Currently does not link to other functions
        choice = input("What would you like to do?\n1:Manages Artists\n2:Manage Schedules\n3:Manage Venue\n4:Manage Tickets\n5:Search for something\n6:Leave\nChoose:\n")
        if choice == '1':
            #artists()
            break
        elif choice == '2':
            #schedules()
            break
        elif choice == '3':
            venues()
        elif choice == '4':
            #tickets()
            break
        elif choice == '5':
            #search()
            break
        elif choice == '6':
            print("Goodbye!")
            exit()
        else:
            print("Sorry, please enter 1, 2, 3, 4, 5, or 6.")
venues(stages)