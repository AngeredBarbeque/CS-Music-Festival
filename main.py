#Nicholas, Aaron, Alex, and Yenesis Music Festival Project
def store_tickets():
  remaining_options = ["seated,", "vip,", "grass"]
  while True:
    try: 
      ticket_type = input("What ticket type do you want to store,", remaining_options[0], remaining_options[1], "or", remaining_options[2])
    except:
      try:
        ticket_type = input("What ticket type do you want to store,", remaining_options[0], "or", remaining_options[1])
      except:
        ticket_type = input("You are now storing,", remaining_options[0], "tickets.")
    
        
  
