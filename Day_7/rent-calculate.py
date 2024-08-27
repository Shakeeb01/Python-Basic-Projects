rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food ordered = "))
electricity_bill = int(input("Enter the total of electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit rate = "))
total_persons = int(input("Enter the count of all perons in a room = "))

total_bill = electricity_bill * charge_per_unit

output = (food + rent + total_bill) // total_persons
total = food + rent + total_bill
print(f"Total amount is {total} .")
print(f"Each person will pay {output} .")