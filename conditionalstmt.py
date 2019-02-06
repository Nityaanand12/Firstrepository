#7. Take the input from the user for(Total number of people, total number of buses, Number of seats for bus, adjust factor). Based on four inputs
#Decide whether there is sufficient buses or not and give solution for how many extra buses required.

Total_no_of_people = int(input("Enter no of people: "))
Total_no_of_buses = int(input("Enter no of buses: "))
no_of_seats_in_buses = int(input("Enter no of seats in buses: "))
adjust_factor = float(input("Enter no of people can adjust per seat: "))
Total_no_seats = Total_no_of_buses*no_of_seats_in_buses*adjust_factor
if Total_no_of_people > Total_no_seats:
    print("Buses are not sufficient")
    no_of_people_left = (Total_no_of_people - Total_no_seats)
    if no_of_people_left > no_of_seats_in_buses:
        buses_required = no_of_people_left/no_of_seats_in_buses
        if buses_required != round(buses_required):
            buses_required = round(buses_required)+1
            print(f"{buses_required} buses are required")
        else:
            print(f"{buses_required} buses are required")
    else:
        print("One extra bus is required")
else:
    print("buses are sufficient")