class Hotel:
    def __init__(self, name, location, rating, capacity):
        self.name = name
        self.location = location
        self.rating = rating
        self.capacity = capacity
        self.rooms = []

    def check_availability(self):
        # Add code for checking room availability

        print("Room Availability Status:")
        for room in self.rooms:
            status = "Available" if room.is_available else "Occupied"
            print(f"Room {room.room_number}: {status}")

    def book_room(self, guest, room_type, check_in_date, check_out_date):
        reservations=[]
        # Add code for booking a room
        # For simplicity, let's assume you have a list of available rooms

        # Find an available room of the specified type
        available_room = None
        for room in self.rooms:
            if room.room_type == room_type and room.is_available:
                available_room = room
                break

        if available_room:
            # Update the room's availability
            available_room.update_availability(False)

            # Create a reservation
            reservation = Reservation(guest, available_room, check_in_date, check_out_date)

            # You may want to store the reservation in a list or database for future reference
            reservations.append(reservation)

            print(f"Room {available_room.room_number} is booked for {guest.name}.")
            return reservation
        else:
            print(f"No available {room_type} rooms.")
            return None


class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = True

    def update_availability(self, is_available):
        self.is_available = is_available


class Guest:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class Reservation:
    def __init__(self, guest, room, check_in_date, check_out_date):
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date


class Billing:
    def __init__(self, reservation, total_amount):
        self.reservation = reservation
        self.total_amount = total_amount

    def generate_invoice(self):
        # Add code for generating an invoice
        guest_name = self.reservation.guest.name
        room_number = self.reservation.room.room_number
        check_in_date = self.reservation.check_in_date
        check_out_date = self.reservation.check_out_date

        invoice = f"Invoice for {guest_name}:\n"
        invoice += f"Room Number: {room_number}\n"
        invoice += f"Check-In Date: {check_in_date}\n"
        invoice += f"Check-Out Date: {check_out_date}\n"
        invoice += f"Total Amount: ${self.total_amount}\n"

        print(invoice)