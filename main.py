#Nicholas, Aaron, Alex, and Yenesis Music Festival Project

#--------------------------------------------------------Start of alex's code---------------------------------------------------------------------------
print("Welcomne to ticket and attende storage and change!")
print()

#store tickets function
def store_tickets():
    ticket_list = ['','','']
#have ticket types be equal to Seated, Vip, Grass
    remaining_options = ["seated", "vip", "grass"]


#have a while true loop, a placement for continues to go back to
    while True:
#ticket_type equals an input asking what they want to store, out of the ticket types, Tickets. 
        print("You are now storing", remaining_options[0], "tickets.")
        ticket_type = remaining_options[0]

#just making sure that they did a real ticket type
        if ticket_type != "seated" and ticket_type != "vip" and ticket_type != "grass":
            print("error")
            continue

#have an input asking what is the amount of 1-day tickets of this type that were bought. 
        try:
            one_day_ticket_amount = int(input("What is the amount of 1-day tickets of this type that were bought?: "))
        except:
            print("invalid input")
            continue

#have an input asking what is the amount of 2-day tickets of this type that were bought.
        try:
            two_day_ticket_amount = int(input("What is the amount of 2-day tickets of this type that were bought?: "))
        except:
            print("invalid input")
            continue

#combine ticket_type, one_day_tickets, and 2_day_tickets into a list
        type_tickets = [ticket_type, one_day_ticket_amount, two_day_ticket_amount]


#If ticket_type is equal to Seated have it be put in position 0 in ticket_list and remove Seated from ticket types
        if ticket_type == "seated":
            remaining_options.pop(remaining_options.index("seated"))
            ticket_list[0] = type_tickets

#If ticket_type is equal to VIP have it be put in position 1 in ticket_list and remove VIP from ticket types
        elif ticket_type == "vip":
            remaining_options.pop(remaining_options.index("vip"))
            ticket_list[1] = type_tickets

#If ticket_type is equal to Grass have it be put in position 2 in ticket_list and remove Grass from ticket types
        elif ticket_type == "grass":
            remaining_options.pop(remaining_options.index("grass"))
            ticket_list[2] = type_tickets

#If the ticket type is not equal to empty, continue back to the beginning of while true loop
        if remaining_options != []:
            continue
            
        return ticket_list



# edit tickets function
def edit_tickets(ticket_list):
# have a while true loop, a placement for continues to go back to
    while True:
# have ticket_type be equal to an input asking what they want to store out of Seated, Vip, or Grass Tickets.
        ticket_type = input("What ticket type do you want to change: seated, vip or grass?: ")

#just making sure that they did a real ticket type
        if ticket_type != "seated" and ticket_type != "vip" and ticket_type != "grass":
            print("invalid input")
            continue

# have an input asking what amount of one-day and two-day tickets of this type were removed/added? 
        try:
            one_day_change_amount = int(input("What is the amount of 1-day tickets of this type that were removed/added?: "))
        except:
            print("invalid input")
            continue

        try:
            two_day_change_amount = int(input("What is the amount of 2-day tickets of this type that were removed/added?: "))        
        except:
            print("invalid input")
            continue
            
# If ticket_type is equal to Seated, have inputs be added to position 1 and 2 in position 0 of the ticket list
        if ticket_type == "seated": 
            ticket_list[0][1] += one_day_change_amount
            ticket_list[0][2] += two_day_change_amount
            
# If ticket_type is equal to VIP, have inputs be added to position 1 and 2 in position 1 the ticket list
        elif ticket_type == "vip": 
            ticket_list[1][1] += one_day_change_amount
            ticket_list[1][2] += two_day_change_amount

# If ticket_type is equal to Grass, have inputs be added to position 1 and 2 in position 2 of the ticket list
        elif ticket_type == "grass": 
            ticket_list[2][1] += one_day_change_amount
            ticket_list[2][2] += two_day_change_amount

# input asking if they want to change any other ticket amounts
        change_ticket_amounts = input("type yes if you want to change any other ticket amounts: ")
        
# if the input is equal to yes, continue back to the beginning of while true loop
        if change_ticket_amounts == "yes":
            continue
        
# Return ticket_list and go to the store_attendee function next
        return ticket_list


        
# store attendee function
def store_attendee(ticket_list):
    attendee_list = ['','']
    attendee_names = [[],[],[],[],[],[]]
# have total_seated_tickets equal to ticket_list(position 1 in position 0) + ticket_list(position 2 in position 0)
    total_seated_tickets = ticket_list[0][1] + ticket_list[0][2]
    
# have total_VIP_tickets equal to ticket_list(position 1 in position 1)+ ticket_list(position 2 in position 1)
    total_vip_tickets = ticket_list[1][1] + ticket_list[1][2]

# have total_grass_tickets equal to ticket_list(position 1 in position 2)+ ticket_list(position 2 in position 2) 
    total_grass_tickets = ticket_list[2][1] + ticket_list[2][2]

# have total_tickets equal to total_grass_tickets + total_VIP_tickets + total_seated_tickets 
    total_tickets = [total_grass_tickets + total_vip_tickets + total_seated_tickets, total_grass_tickets, total_vip_tickets, total_grass_tickets]

# have attendeegenders equal to female, male
    attendee_genders = ["female", "male"]
# have a while true loop, a placement for continues to go back to
    while True:
# have gender_type be equal to an input asking if they want to store, out of the attendee_genders, attendees
        print("You are now storing", attendee_genders[0], "attendes.")
        gender_type = attendee_genders[0]
            
        if gender_type != "female" and gender_type != "male":
            print("invalid input")
            continue
            
# remove gender_type from attendee_genders
        if gender_type == "female":
            attendee_genders.pop(attendee_genders.index("female"))

        elif gender_type == "male":
            attendee_genders.pop(attendee_genders.index("male"))
        

# have under_18 equal to an input asking what was the amount of (gender_type) ages 18 and under that went?
        print("What is the amount of", gender_type, "ages 18 and under that went?: ")
        under_18 = input()
        try:
            under_18 = int(under_18)
        except:
            print("invalid input")
            continue
            
# have over_18 equal to an input asking what was the amount of (gender_type) ages 19-49 that went?
        print("What is the amount of", gender_type, "ages 18 to 49 that went?: ")
        over_18 = input()
        try:
            over_18 = int(over_18)
        except:
            print("invalid input")
            continue

# have over_50 equal to an Input asking what was the amount of (gender_type) ages 50-79 that went?
        print("what is the amount of", gender_type, "ages 50 and older that went?: ")
        over_50 = input()
        try:
            over_50 = int(over_50)
        except:
            print("invalid input")
            continue


# have age_list equal to the combination of all the age variables into a list
        age_list = [under_18, over_18, over_50]

# have gender_seated_amount equal to an input asking what was the amount of Seated (gender_type).
        print("what is the amount of seated", gender_type)
        gender_seated_amount = input()
        try:
            gender_seated_amount = int(gender_seated_amount)
        except:
            print("invalid input")
            continue

# have gender_VIP_amount equal to an input asking what was the amount of VIP (gender_type).
        print("what is the amount of vip", gender_type)
        gender_vip_amount = input()
        try:
            gender_vip_amount = int(gender_vip_amount)
        except:
            print("invalid input")
            continue

# have gender_grass_amount equal to an input asking what was the amount of grass (gender_type).
        print("what is the amount of grass seated", gender_type)
        gender_grass_amount = input()
        try:
            gender_grass_amount = int(gender_grass_amount)
        except:
            print("invalid input")
            continue

# have area_amounts equal to gender_seated_amount, gender_VIP_amount, gender_grass_amount 
        area_amounts = [gender_seated_amount, gender_vip_amount, gender_grass_amount]


# if gender_type equals female: have total_female equal to area_amount[position 0] + area_amount[position 1] + area_amount[position 2]
# if gender_type equals female: have attendee_list[position 0] equal to total_female, area_amounts, age_list
        if gender_type == "female":
            total_female_areas = area_amounts[0] + area_amounts[1] + area_amounts[2]
            attendee_list[0] = [total_female_areas, area_amounts, age_list]

# if gender_type equals male: have total_male equal to area_amount[position 0] + area_amount[position 1] + area_amount[position 2]
# if gender_type equals male: have attendee_list[position 1] equal to total_male, area_amounts, age_list
        elif gender_type == "male":
            total_male_areas = area_amounts[0] + area_amounts[1] + area_amounts[2]
            attendee_list[1] = [total_male_areas, area_amounts, age_list]

# If attendee_genders is not empty, continue back to beginning of while true loop
        if attendee_genders != []:
            continue

# if total_female + total_male > total_tickets, print that they had too many people and continue
        if total_female_areas + total_male_areas > total_tickets[0]:
            attendee_genders = ["female", "male"]
            print("You had not have more people then your total tickets amount!")
            continue


# for number in range(attendee_list[position 0][position 1][position 0]):
# input asking what the name of a woman in seated:
# add the input to position 0 in attendee_names
        for number in range(attendee_list[0][1][0]):
            person_name = input("What is the name of a woman in seated?: ")

            while True:
                try:
                    person_age = int(input("What is the age of that women?: "))
                except:
                    print("invalid input")
                    continue
                attendee_names[0] += [person_name, person_age]
                break

# for number in range(attendee_list[position 0][position 1][position 1]):
# input asking what is the name of a woman in VIP:
# add the input to position 1 in attendee_names
        for number in range(attendee_list[0][1][1]):
            person_name = input("What is the name of a woman in vip?: ")

            while True:
                try:
                    person_age = int(input("What is the age of that women?: "))
                except:
                    print("invalid input")
                    continue
                attendee_names[0] += [person_name, person_age]
                break

# for number in range(attendee_list[position 0][position 1][position 2]):
# input asking what is the name of a woman in the grass:
# add the input to position 2 in attendee_names
        for number in range(attendee_list[0][1][2]):
            person_name = input("What is the name of a woman in grass?: ")
            
            while True:
                try:
                    person_age = int(input("What is the age of that women?: "))
                except:
                    print("invalid input")
                    continue
                attendee_names[0] += [person_name, person_age]
                break
                
# for number in range(attendee_list[position 1][position 1][position 0]):
# input asking what is the name of a man in seated:
# add the input to position 3 in attendee_names
        for number in range(attendee_list[1][1][0]):
            person_name = input("What is the name of a man in seated?: ")
            
            while True:
                try:
                    person_age = int(input("What is the age of that man?: "))
                except:
                    print("invalid input")
                    continue
                attendee_names[0] += [person_name, person_age]
                break
                
# for number in range(attendee_list[position 1][position 1][position 1]):
# input asking what is the name of a man in VIP:
# add the input to position 4 in attendee_names
        for number in range(attendee_list[1][1][1]):
            person_name = input("What is the name of a man in vip?: ")
            
            while True:
                try:
                    person_age = int(input("What is the age of that man?: "))
                except:
                    print("invalid input")
                    continue
                attendee_names[0] += [person_name, person_age]
                break
                
# for number in range(attendee_list[position 1][position 1][position 2]):
# input asking what is the name of a man in the grass:
# add the input to position 5 in attendee_names
        for number in range(attendee_list[1][1][2]):
            person_name = input("What is the name of a man in grass?: ")
            
            while True:
                try:
                    person_age = int(input("What is the age of that man?: "))
                except:
                    print("invalid input")
                    continue
                attendee_names[0] += [person_name, person_age]
                break
                
# Return attendee_list, total_tickets, and attendee_names and go to artist management and then go to find artist function
        return attendee_list, total_tickets, attendee_names



# find_function
def find_function(attendee_names, artists, schedules):
# have a while True loop, a placement for continues to go back to
    while True:
# have an input asking if they are trying to find an artist, schedules, or attendees.
        what_find = input("Do you want to find an artist, schedule, or a attendee?: ")


# Attendees
        if what_find == "attendee":
# have a while true loop, a placement for continues to go back to
            while True:
# have an input that asks what the name of the attendee is.
                find_attendee = input("what is the name of the attendee?: ")


# If the input is not in attendee_names, continue back to beginning of while true loop
                if find_attendee not in attendee_names[0] and find_attendee not in attendee_names[1] and find_attendee not in attendee_names[2] and find_attendee not in attendee_names[3] and find_attendee not in attendee_names[4] and find_attendee not in attendee_names[5]:
                    print("There is nobody with that name")
                    continue

# If the name is in position 0 in attendee names: print that it is a seated female.
                if find_attendee in attendee_names[0]:
                    print("That is a female in a seated area.")
                    break

# If the name is in position 1 in attendee names: print that it is a VIP female.
                elif find_attendee in attendee_names[1]:
                    print("That is a female in vip area.")
                    break

# If the name is in position 2 in attendee names: print that it is a grass-located female.
                elif find_attendee in attendee_names[2]:
                    print("That is a female in the grass area.")
                    break

# If the name is in position 3 in attendee names: print that it is a seated male.
                elif find_attendee in attendee_names[3]:
                    print("That is a male in a seated area.")
                    break

# If the name is in position 4 in attendee names: print that it is a VIP male.
                elif find_attendee in attendee_names[4]:
                    print("That is a male in vip area.")
                    break

# If the name is in position 5 in attendee names: print that it is a grass-located male.
                elif find_attendee in attendee_names[5]:
                    print("That is a male in the grass area.")
                    break


# Schedules
        if what_find == "schedule":
# have a while true loop, a placement for continues to go back to
            while True:
# have an input asking what the name is of the schedule.
                    
                schedule_finder = input("What is the name of the schedule?: ")
                
# If the input is not in scedules, continue back to beginning
                schedule_found = False
                for item in schedules:
                    if schedule_finder == item[0]:
                        schedule_found = True

                if schedule_found == False:
                    print("That is not a schedule.")
                    continue
                
# print schedule information
                print("This is where schedule information would print.")
                break

# Artists
        if what_find == "artist":
# have a while true loop, a placement for continues to go back to
            while True:
# have an input asking what the name of the artist is.
                artist_finder = input("What is the name of the artist?: ")
                    
# If the input is not in artists, continue back to beginning of while true loop
                if artist_finder not in artists:
                    print("That artist is not here")
                    continue
                        
# print artist information
                print("This is where the artist information would print.")
                break

        if what_find != "artist" and what_find != "schedule" and what_find != "attende":
            print("invalid input")
            continue
            
# input asking if they want to find something else and to say yes if they do
        do_other_search = input("Say yes if you want to search for something else: ")
# if yes, continue back to beginning of while true loop
        if do_other_search == "yes":
            continue
# else, go to the main function
        break



def tickets_and_attende_function(schedules, artists):
    ticket_list = store_tickets()
    attendee_list, total_tickets, attendee_names = store_attendee(ticket_list)
    while True:
        do_what = input("Do you want to edit tickets (1) or search (2)?: ")

        if do_what == "1":
            ticket_list = edit_tickets(ticket_list)

        if do_what == "2":
            find_function(attendee_names, artists, schedules)

        do_again = input("say yes if you want to do somthing else: ")

        if do_again == "yes":
            continue
        
        return attendee_list, total_tickets, attendee_names, ticket_list
#------------------------------------------------------end of alex's code----------------------------------------------------------------------