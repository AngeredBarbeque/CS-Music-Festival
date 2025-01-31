#Nicholas, Aaron, Alex, and Yenesis Music Festival Project
stages = set({})
class Schedule:
    def __init__(self):
        self.schedule = []  # List to store time slot, artist, and stage tuples

    def create_schedule(self):
        # Create the schedule by allowing the user to input time slots
        num_slots = int(input("Enter the number of time slots you want to create: "))
        for _ in range(num_slots):
            time_slot = input("Enter a time slot (e.g., 10:00 AM): ")
            stage = input(f"Enter the stage for time slot {time_slot}: ")
            # Add time slot tuple with None for artist
            self.schedule.append((time_slot, None, stage))

    def assign_artist(self):
        # Assign an artist to a time slot, check for conflicts
        try:
            time_slot = input("Enter the time slot (e.g., 10:00 AM) to assign an artist: ")
            slot_found = False

            # Check if the time slot exists and is available
            for i, (slot, artist, stage) in enumerate(self.schedule):
                if slot == time_slot:
                    slot_found = True
                    if artist is None:
                        artist = input(f"Enter the artist name to assign to {time_slot} at {stage}: ")
                        self.schedule[i] = (slot, artist, stage)  # Update the tuple
                        print(f"Artist {artist} assigned to {time_slot} at {stage}.")
                        return
                    else:
                        print(f"Conflict! The time slot {time_slot} is already occupied by {artist}.")
                        return

            if not slot_found:
                print("This time slot does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def edit_schedule(self):
        # Allow the user to edit an existing schedule (change artist)
        try:
            time_slot = input("Enter the time slot (e.g., 10:00 AM) you want to edit: ")
            slot_found = False

            for i, (slot, artist, stage) in enumerate(self.schedule):
                if slot == time_slot:
                    slot_found = True
                    if artist is None:
                        print(f"No artist assigned to {time_slot}.")
                    else:
                        current_artist = artist
                        new_artist = input(f"Current artist for {time_slot} at {stage} is {current_artist}. Enter the new artist name: ")
                        self.schedule[i] = (slot, new_artist, stage)  # Update the tuple with new artist
                        print(f"Artist for {time_slot} at {stage} updated to {new_artist}.")
                    return

            if not slot_found:
                print("This time slot does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def view_schedule(self):
        # Display the current schedule
        if not self.schedule:
            print("No time slots created yet.")
            return
        print("Current Schedule:")
        for slot, artist, stage in self.schedule:
            artist_name = artist if artist else "No artist assigned"
            print(f"{slot} at {stage}: {artist_name}")

    def remove_schedule(self):
        # Remove the entire schedule
        try:
            confirmation = input("Are you sure you want to remove the entire schedule? (y/n): ")
            if confirmation.lower() == 'y':
                self.schedule.clear()  # Clear the schedule
                print("Schedule has been removed.")
            else:
                print("Schedule removal canceled.")
        except Exception as e:
            print(f"An error occurred while removing the schedule: {e}")

    def link_time_slots_to_artist_and_stage(self):
        # Link all time slots with artist and stage details
        try:
            if not self.schedule:
                print("No schedule exists to link.")
                return

            for i, (slot, artist, stage) in enumerate(self.schedule):
                if artist is None or stage is None:
                    print(f"Time slot {slot} is incomplete. It needs both artist and stage.")
                    # Optionally prompt for missing data
                    if artist is None:
                        artist = input(f"Enter artist for {slot}: ")
                    if stage is None:
                        stage = input(f"Enter stage for {slot}: ")
                    self.schedule[i] = (slot, artist, stage)  # Update the tuple with missing data
                    print(f"Time slot {slot} is now linked with artist {artist} and stage {stage}.")
        except Exception as e:
            print(f"An error occurred while linking the time slots: {e}")


# Main program flow
def schedule_management():
    schedule = Schedule()

    while True:
        print("\nMenu:")
        print("1. Create Schedule")
        print("2. Assign Artist to Time Slot")
        print("3. Edit Schedule")
        print("4. View Schedule")
        print("5. Remove Schedule")
        print("6. Link Time Slots to Artist and Stage")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            schedule.create_schedule()
        elif choice == '2':
            schedule.assign_artist()
        elif choice == '3':
            schedule.edit_schedule()
        elif choice == '4':
            schedule.view_schedule()
        elif choice == '5':
            schedule.remove_schedule()
        elif choice == '6':
            schedule.link_time_slots_to_artist_and_stage()
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the main program
if __name__ == "__main__":
    main()

    