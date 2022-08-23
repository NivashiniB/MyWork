class TicketBooking:

    def __init__(self, booking_id, flight_no, operation, seat_class, total_seats, meal_pref,seats,seats_booked,total_cost):
        self.booking_id = booking_id
        self.flight_no = flight_no
        self.operation = operation
        self.seat_class = seat_class
        self.total_seats = total_seats
        self.meal_pref = meal_pref
        self.seats = seats
        #self.status = status
        self.seats_booked = seats_booked
        self.total_cost = total_cost


class FlightDetails:

    def __init__(self, flight_no,operation,seat_class,total_seats,meal_pref,ec_fare,bc_fare,seats,flight_total_cost,total_cost,meal_seats):
        self.flight_no = flight_no
        self.operation = operation
        self.seat_class = seat_class
        self.total_seats = total_seats
        self.meal_pref = meal_pref
        self.ec_fare = ec_fare
        self.bc_fare = bc_fare
        self.seats = seats
        self.flight_total_cost = flight_total_cost
        self.total_cost = total_cost
        self.meal_seats = meal_seats

        if self.operation =='b':
            if self.meal_pref == 'y':
                self.meal_seats[self.seat_class].extend(self.seats[self.seat_class][:self.total_seats])
            self.seats[self.seat_class] = self.seats[self.seat_class][self.total_seats:]
            self.ec_fare = self.ec_fare+100
            self.bc_fare = self.bc_fare+200
            self.flight_total_cost += self.total_cost
            



def getTotalCost(operation, seat_class, total_seats, meal_pref,ec_fare,bc_fare):
    if operation == 'b':
        if seat_class == 'bc':
            total_cost = total_seats*bc_fare
        if seat_class == 'ec':
            total_cost = total_seats*ec_fare
        if meal_pref =='y':
            total_cost = total_cost + total_seats*200
    if operation == 'c':
        total_cost = total_seats*200
    return total_cost


#Driver
ec_fare = 1000
bc_fare = 2000
flight_details = {}
ticket_booking = {}
seats_booked ={"bc":[],"ec":[]}
meal_seats = {"bc":[],"ec":[]}
seats ={ "bc":[1,2,3,4,5,6],"ec":[7,8,9,10,11,12,13,14]}
while(1):
    booking_id = int(input("booking_id: "))
    flight_no = int(input("Flight No: "))
    operation = input("Booking/Cancellation (B/C): ").lower()
    if operation =='b':
        if flight_no not in flight_details:
            seats = { "bc":[1,2,3,4,5,6],"ec":[7,8,9,10,11,12,13,14]}
            meal_seats = {"bc":[],"ec":[]}
            ec_fare = 1000
            bc_fare = 2000
            flight_total_cost = 0
        else:
            seats = flight_details[flight_no].seats
            ec_fare = flight_details[flight_no].ec_fare
            bc_fare = flight_details[flight_no].bc_fare
            flight_total_cost = flight_details[flight_no].flight_total_cost
            meal_seats = flight_details[flight_no].meal_seats
       
        seat_class = input("Business or economy class (BC/EC): ").lower()
        print("Available seats in flight ",flight_no,":",seats)
        total_seats = int(input("Total seats: "))
        meal_pref = input("Meal preference (Y/N) : ").lower()
        seats_booked ={"bc":[],"ec":[]}
        seats_booked[seat_class] = seats[seat_class][:total_seats]
        print("Booked seats: ",seats_booked)

        total_cost = getTotalCost(operation, seat_class, total_seats, meal_pref,ec_fare,bc_fare)
        ftb = TicketBooking(booking_id, flight_no, operation, seat_class, total_seats, meal_pref,seats,seats_booked,total_cost)
        fd = FlightDetails(flight_no,operation,seat_class,total_seats,meal_pref,ec_fare,bc_fare,seats,flight_total_cost,total_cost,meal_seats)
        ticket_booking[booking_id] = ftb
        flight_details[flight_no] = fd

    elif operation == 'c':
        seats_booked = ticket_booking[booking_id].seats_booked
        seats = ticket_booking[booking_id].seats
        total_seats = ticket_booking[booking_id].total_seats
        flight_details[flight_no].flight_total_cost -= ticket_booking[booking_id].total_cost
        if ticket_booking[booking_id].meal_pref == 'y':
            for key in flight_details[flight_no].meal_seats:
                flight_details[flight_no].meal_seats[key] = sorted(list(set(flight_details[flight_no].meal_seats[key]) - set(seats_booked[key])))

        for key in seats:
            seats[key].extend(seats_booked[key])
            seats[key] = sorted(seats[key])
        ticket_booking[booking_id].seats_booked = []
        ticket_booking[booking_id].seats = seats

        ticket_booking[booking_id].total_cost = getTotalCost(operation,'',total_seats,'',0,0)
        flight_details[flight_no].flight_total_cost += ticket_booking[booking_id].total_cost
        ticket_booking[booking_id].operation = operation

    next_process = input("wanna proceed? ").lower()
    print("\n")
    if next_process == 'n':
        break

print("Booking Details")
print("***************\n")
for key in ticket_booking:
    print("Booking ID: ",ticket_booking[key].booking_id)
    print("Flight No: ",ticket_booking[key].flight_no)
    if ticket_booking[key].operation == 'b':
        print("seats: ",ticket_booking[key].seats_booked)
        print("Meal pref: ",ticket_booking[key].meal_pref)
    else:
        print("Cancelled")
    print("total cost: ",ticket_booking[key].total_cost)
    print("\n")
    
print("Flight Details")
print("**************\n")     
for key in flight_details:
    booked_seats = {"bc" : {}, "ec":{}}
    print("Summary of flight: ",key)
    for seat in flight_details[key].seats:
        if seat == "bc":
            booked_seats["bc"] = sorted(list({1,2,3,4,5,6} - set(flight_details[key].seats["bc"])))
        else:
            booked_seats["ec"] = sorted(list({7,8,9,10,11,12,13,14} - set(flight_details[key].seats["ec"])))
    print("Total seats available: ",flight_details[key].seats)
    print("Meal seats: ",flight_details[key].meal_seats)
    print("Total seats booked: ",booked_seats)
    print("Total cost : ",flight_details[key].flight_total_cost)
    print("\n")


























