# # Get user input for auditorium size
# num_rows = int(input("Enter number of rows: "))
# section1 = int(input("Enter number of seats in Section 1: "))
# section2 = int(input("Enter number of seats in Section 2: "))
# section3 = int(input("Enter number of seats in Section 3: "))

# total_seats = section1 + section2 + section3

# # Create seating layout with '-' for available seats
# auditorium = [["-" for _ in range(total_seats)] for _ in range(num_rows)]

# # Function to print seating with section separators
# def print_seating():
#     print("\nCurrent Seating Arrangement:")
#     for row in auditorium:
#         s1 = " ".join(row[:section1])
#         s2 = " ".join(row[section1:section1+section2])
#         s3 = " ".join(row[section1+section2:])
#         print(f"{s1}   |   {s2}   |   {s3}")

# # Function to book a seat
# def book_seat(row, seat):
#     if 0 <= row < num_rows and 0 <= seat < total_seats:
#         if auditorium[row][seat] == "-":
#             auditorium[row][seat] = "*"
#             print(f"Seat ({row+1}, {seat+1}) booked successfully!")
#         else:
#             print(f"Seat ({row+1}, {seat+1}) is already booked.")
#     else:
#         print("Invalid seat number. Please try again.")

# # User can book seats
# while True:
#     print_seating()
    
#     choice = input("\nDo you want to book a seat? (yes/no): ").lower()
#     if choice == "no":
#         break

#     try:
#         row = int(input(f"Enter row number to book (1 to {num_rows}): ")) - 1
#         seat = int(input(f"Enter seat number to book (1 to {total_seats}): ")) - 1
#         book_seat(row, seat)
#     except ValueError:
#         print("Please enter valid numbers.")

# # Final display
# print("\nFinal Auditorium Seating Arrangement:")
# print_seating()
# print("Booking process complete. Enjoy the show! 🎭")


# Get user input for auditorium size
num_rows = int(input("Enter number of rows: "))
section1 = 6
section2 = 10
section3 = 6

total_seats = section1 + section2 + section3

# Create seating layout with '-' for available seats
auditorium = [["-" for _ in range(total_seats)] for _ in range(num_rows)]

# Function to book a seat
def book_seat(row, seat):
    if 0 <= row < num_rows and 0 <= seat < total_seats:
        if auditorium[row][seat] == "-":
            auditorium[row][seat] = "*"
            print(f"Seat ({row+1}, {seat+1}) booked successfully!")
        else:
            print(f"Seat ({row+1}, {seat+1}) is already booked.")
    else:
        print("Invalid seat number. Please try again.")

# Function to display seating with section dividers
def display_seating():
    print("\nCurrent Seating Arrangement:")
    for row in auditorium:
        line = ""
        for i, seat in enumerate(row):
            if i == section1 or i == section1 + section2:
                line += "  "  # Add section separator
            line += f" {seat}"
        print(line)
# Helper function to get seat index from section and seat number
def get_seat_index(section, seat_in_section):
    if section == 1:
        if 1 <= seat_in_section <= section1:
            return seat_in_section - 1
    elif section == 2:
        if 1 <= seat_in_section <= section2:
            return section1 + seat_in_section - 1
    elif section == 3:
        if 1 <= seat_in_section <= section3:
            return section1 + section2 + seat_in_section - 1
    return -1  # Invalid


# User interaction loop
while True:
    display_seating()

    choice = input("\nDo you want to book a seat? (yes/no): ").lower()
    if choice == "no":
        break

    row = int(input(f"Enter row number to book (1 to {num_rows}): ")) - 1
    section = int(input("Enter section number to book (1, 2, or 3): "))
    if section == 1:
        max_seats = section1
    elif section == 2:
        max_seats = section2
    elif section == 3:
        max_seats = section3
    else:
        print("Invalid section. Please try again.")
        continue

    seat_in_section = int(input(f"Enter seat number in section {section} (1 to {max_seats}): "))
    seat_index = get_seat_index(section, seat_in_section)

    if seat_index == -1:

        print("Invalid seat number. Please try again.")
        continue

    book_seat(row, seat_index)


# Final display
print("\nFinal Auditorium Seating Arrangement:")
display_seating()
print("Booking process complete. Enjoy the show! 🎭")