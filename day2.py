# # Initialize sections with one row each
# a = [[0 for _ in range(5)]]
# b = [[0 for _ in range(10)]]
# c = [[0 for _ in range(5)]]

# while True:
#     section = input("Enter which section you want (a/b/c): ").lower()
#     row = int(input("Enter row number : "))  # Only row 0 is defined
#     column = int(input("Enter column number: "))

#     if section == 'a' and 0 <= column < 5:
#         a[row][column] = 1
#     elif section == 'b' and 0 <= column < 10:
#         b[row][column] = 1
#     elif section == 'c' and 0 <= column < 5:
#         c[row][column] = 1
#     else:
#         print("Invalid section or seat number.")
#         continue

#     # Display current seating
#     rowa = "".join(str(v) for v in a[0])
#     rowb = "".join(str(v) for v in b[0])
#     rowc = "".join(str(v) for v in c[0])
#     print(f"A: {rowa}  B: {rowb}  C: {rowc}")

#     # Ask if user wants to continue
#     more = input("Do you want to book another seat? (yes/no): ").lower()
#     if more != 'yes':
#         break

# print(" Booking complete!")







# Define 5 rows for each section
# a = [[0 for _ in range(5)] for _ in range(5)]   # Section A: 5x5
# b = [[0 for _ in range(10)] for _ in range(5)]  # Section B: 5x10
# c = [[0 for _ in range(5)] for _ in range(5)]   # Section C: 5x5

# while True:
#     section = input("Enter which section you want (a/b/c): ").lower()
#     row = int(input("Enter row number (0–4): "))
#     column = int(input("Enter column number: "))

#     if section == 'a' and 0 <= row < 5 and 0 <= column < 5:
#         a[row][column] = 1
#     elif section == 'b' and 0 <= row < 5 and 0 <= column < 10:
#         b[row][column] = 1
#     elif section == 'c' and 0 <= row < 5 and 0 <= column < 5:
#         c[row][column] = 1
#     else:
#         print("Invalid section or seat number.")
#         continue

#     # Display seating
#     print("\nCurrent Seating:")
#     print("Section A:")
#     for r in a:
#         print(" ".join(str(seat) for seat in r))
#     print("Section B:")
#     for r in b:
#         print(" ".join(str(seat) for seat in r))
#     print("Section C:")
#     for r in c:
#         print(" ".join(str(seat) for seat in r))

#     # Continue?
#     more = input("\nDo you want to book another seat? (yes/no): ").lower()
#     if more != 'yes':
#         break

# print("✅ Booking complete!")






# # Define 5 rows for each section
# a = [[0 for _ in range(5)] for _ in range(5)]   # Section A: 5x5
# b = [[0 for _ in range(10)] for _ in range(5)]  # Section B: 5x10
# c = [[0 for _ in range(5)] for _ in range(5)]   # Section C: 5x5

# while True:
#     section = input("Enter which section you want (a/b/c): ").lower()
#     row = int(input("Enter row number (0–4): "))
#     column = int(input("Enter column number: "))

#     if section == 'a' and 0 <= row < 5 and 0 <= column < 5:
#         a[row][column] = 1
#     elif section == 'b' and 0 <= row < 5 and 0 <= column < 10:
#         b[row][column] = 1
#     elif section == 'c' and 0 <= row < 5 and 0 <= column < 5:
#         c[row][column] = 1
#     else:
#         print("Invalid section or seat number.")
#         continue

#     # Display seating with column headers
#     print("\nCurrent Seating:")

#     print("\nSection A:")
#     print("   " + " ".join(str(i) for i in range(5)))  # Column header
#     for idx, r in enumerate(a):
#         print(f"{idx}  " + " ".join(str(seat) for seat in r))

#     print("\nSection B:")
#     print("   " + " ".join(str(i) for i in range(10)))  # Column header
#     for idx, r in enumerate(b):
#         print(f"{idx}  " + " ".join(str(seat) for seat in r))

#     print("\nSection C:")
#     print("   " + " ".join(str(i) for i in range(5)))  # Column header
#     for idx, r in enumerate(c):
#         print(f"{idx}  " + " ".join(str(seat) for seat in r))

#     # Continue?
#     more = input("\nDo you want to book another seat? (yes/no): ").lower()
#     if more != 'yes':
#         break

# print("✅ Booking complete!")












a=[[]]
b=[[]]
c=[[]]
for i in range(5):
    a[0].append(0)
for i in range(10):
    b[0].append(0)
for i in range(5):
    c[0].append(0)
section=str(input("Enter which section you want: "))
row=int(input("Enter row number: "))
column=int(input("Enter column number: "))
seat=f"{section}[{row}][{column}]"
print(seat)
if 'a' in seat:
    a[0][row]=1
elif 'b' in seat:
    b[0][row]=1
elif 'c' in seat:
    c[0][row]=1
else:
    print("choose the correct seat")
rowa="".join(str(v) for v in a[0])
rowb="".join(str(v) for v in b[0])
rowc="".join(str(v) for v in c[0])
print(f"{rowa} {rowb} {rowc}")