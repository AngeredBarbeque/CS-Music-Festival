#Nicholas, Aaron, Alex, and Yenesis Music Festival Project

#Alex Anderson, Music Festival Pseudocode



#store tickets function
def store_tickets():
    ticket_list = ['','','']
#have ticket types be equal to Seated, Vip, Grass
    remaining_options = ["seated", "vip", "grass"]


#have a while true loop, a placement for continues to go back to
    while True:
#ticket_type equals an input asking what they want to store, out of the ticket types, Tickets.
        try: 
            ticket_type = input("What ticket type do you want to store:", remaining_options[0], "or", remaining_options[1], "or", remaining_options[2])
        except:
            try:
                ticket_type = input("What ticket type do you want to store:", remaining_options[0], "or", remaining_options[1])
            except:
                print("You are now storing:", remaining_options[0], "tickets.")
                ticket_type = remaining_options[0]

#just making sure that they did a real ticket type
        if ticket_type != "seated" and ticket_type != "vip" and ticket_type != "grass":
            print("invalid input")
            continue

#have an input asking what is the amount of 1-day tickets of this type that were bought. 
        one_day_ticket_amount = input("What is the amount of 1-day tickets of this type that were bought?: ")

#have an input asking what is the amount of 2-day tickets of this type that were bought. 
        two_day_ticket_amount = input("What is the amount of 2-day tickets of this type that were bought?: ")

#combine ticket_type, one_day_tickets, and 2_day_tickets into a list
        type_tickets = [ticket_type, one_day_ticket_amount, two_day_ticket_amount]


#If ticket_type is equal to Seated have it be put in position 0 in ticket_list and remove Seated from ticket types
        if ticket_type == "seated":
            remaining_options.pop(remaining_options.index("seated"))
            ticket_list[0] = type_tickets

#If ticket_type is equal to VIP have it be put in position 1 in ticket_list and remove VIP from ticket types
        if ticket_type == "vip":
            remaining_options.pop(remaining_options.index("vip"))
            ticket_list[1] = type_tickets

#If ticket_type is equal to Grass have it be put in position 2 in ticket_list and remove Grass from ticket types
        if ticket_type == "grass":
            remaining_options.pop(remaining_options.index("grass"))
            ticket_list[2] = type_tickets

#If the ticket type is not equal to empty, continue back to the beginning of while true loop
        if remaining_options != []:
            continue



# edit tickets function
def edit_tickets():
# have a while true loop, a placement for continues to go back to
    while True:
# have ticket_type be equal to an input asking what they want to store out of Seated, Vip, or Grass Tickets.
        ticket_type = input("What ticket type do you want to change: seated, vip or grass")

#just making sure that they did a real ticket type
        if ticket_type != "seated" and ticket_type != "vip" and ticket_type != "grass":
            print("invalid input")
            continue

# have an input asking what amount of one-day tickets of this type were removed/added? 
        one_day_change_amount = input("What is the amount of 1-day tickets of this type that were removed/added?: ")
        
# If ticket_type is equal to Seated, have input be added to position 1 in position 0 of the ticket list
# If ticket_type is equal to VIP, have input be added to position 1 in position 1 the ticket list
# If ticket_type is equal to Grass, have input be added to position 1 in position 2 of the ticket list
# Input asking what amount of two-day tickets of this type were removed/added. 
# If ticket_type is equal to Seated, have input be added to position 2 in position 0 of the ticket list
# If ticket_type is equal to VIP, have input be added to position 2 in position 1 of the ticket list
# If ticket_type is equal to Grass, have input be added to position 2 in position 2 of the ticket list
# input asking if they want to change any other ticket amounts
# if the input is equal to yes, continue back to the beginning of while true loop
# Return ticket_list and go to the store_attendee function next


# store attendee function
# have total_seated_tickets equal to ticket_list(position 1 in position 0) + ticket_list(position 2 in position 0)
# have total_VIP_tickets equal to ticket_list(position 1 in position 1)+ ticket_list(position 2 in position 1)
# have total_grass_tickets equal to ticket_list(position 1 in position 2)+ ticket_list(position 2 in position 2) 
# have total_tickets equal to total_grass_tickets + total_VIP_tickets + total_seated_tickets 
# have attende_types equal to female, male
# have a while true loop, a placement for continues to go back to
# have gender_type be equal to an input asking if they want to store, out of the attende_types, attendees
# remove gender_type from attende_types
# have under_18 equal to an input asking what was the amount of (gender_type) ages 18 and under that went?
# have over_18 equal to an input asking what was the amount of (gender_type) ages 19-49 that went?
# have over_50 equal to an Input asking what was the amount of (gender_type) ages 50-79 that went?
# have age_list equal to the combination of all the age variables into a list
# have gender_seated_amount equal to an input asking what was the amount of Seated (gender_type).
# have gender_VIP_amount equal to an input asking what was the amount of VIP (gender_type).
# have gender_grass_amount equal to an input asking what was the amount of grass (gender_type).
# have area_amounts equal to gender_seated_amount, gender_VIP_amount, gender_grass_amount 
# if gender_type equals female: have total_female equal to area_amount[position 0] + area_amount[position 1] + area_amount[position 2]
# if gender_type equals male: have total_male equal to area_amount[position 0] + area_amount[position 1] + area_amount[position 2]
# if gender_type equals female: have attende_list[position 0] equal to total_female, area_amounts, age_list
# if gender_type equals male: have attende_list[position 1] equal to total_male, area_amounts, age_list
# If attende_types is not empty, continue back to beginning of while true loop
# if total_female + total_male > total_tickets, print that they had too many people and continue
# for number in range(attende_list[position 0][position 1][position 0]):
# input asking what the name of a woman in seated:
# add the input to position 0 in attende_names
# for number in range(attende_list[position 0][position 1][position 1]):
# input asking what is the name of a woman in VIP:
# add the input to position 1 in attende_names
# for number in range(attende_list[position 0][position 1][position 2]):
# input asking what is the name of a woman in the grass:
# add the input to position 2 in attende_names
# for number in range(attende_list[position 1][position 1][position 0]):
# input asking what is the name of a man in seated:
# add the input to position 3 in attende_names
# for number in range(attende_list[position 1][position 1][position 1]):
# input asking what is the name of a man in VIP:
# add the input to position 4 in attende_names
# for number in range(attende_list[position 1][position 1][position 2]):
# input asking what is the name of a man in the grass:
# add the input to position 5 in attende_names
# Return attende_list, total_tickets, and attende_names and go to artist management and then go to find artist function


# find_function
# have a while True loop, a placement for continues to go back to
# have an input asking if they are trying to find an artist, schedules, or attendees.

# Attendees
# have a while true loop, a placement for continues to go back to
# have an input that asks what the name of the attendee is.
# If the input is not in attende_names, continue back to beginning of while true loop
# If the name is in position 0 in attendee names: print that it is a seated female.
# If the name is in position 1 in attendee names: print that it is a VIP female.
# If the name is in position 2 in attendee names: print that it is a grass-located female.
# If the name is in position 3 in attendee names: print that it is a seated male.
# If the name is in position 4 in attendee names: print that it is a VIP male.
# If the name is in position 5 in attendee names: print that it is a grass-located male.

# Schedules
# have a while true loop, a placement for continues to go back to
# have an input asking what the name is of the schedule.
# If the input is not in scedules, continue back to beginning
# print schedule information

# Artists
# have a while true loop, a placement for continues to go back to
# have an input asking what the name of the artist is.
# If the input is not in artists, continue back to beginning of while true loop
# print artist information

# input asking if they want to find something else (yes or no)
# if yes, continue back to beginning of while true loop
# else, go to the main function

    
    
        
  
