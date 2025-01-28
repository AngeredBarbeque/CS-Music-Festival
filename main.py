#Nicholas, Aaron, Alex, and Yenesis Music Festival Project
#TURN THIS INTO A SET AND FIGURE THAT OUT
stages = set(())

def stage_display():
    print(stages)
    #CHANGE THIS TO BE PRETTIER


def add_stage():
    while True:
        stage = []
        equipment = set(())
        stage_name = input("What do you want to name the stage?:\n")
        equip_amount = input("How many seperate pieces of equipment does this stage have?:\n")
        try:
            equip_amount = int(equip_amount)
        except:
            print("Please enter a number.\n")
            i -= 1
            continue
        for i in range(equip_amount):
            equipment.append(input("Please enter a piece of equipment:\n"))
        stage.append(stage_name)
        stage.append(equipment)
        print(stage, '\n')
        return stage

stages.add(add_stage())
stages.add("Test")
print(stages)