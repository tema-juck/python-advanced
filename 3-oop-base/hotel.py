"""Hotel Module"""


from abc import ABC, abstractmethod


class Room(ABC):
    """Abstract class Room"""

    def __init__(self, room_number: int, base_price: float) -> None:
        self.room_number = room_number
        self.base_price = base_price

    @abstractmethod
    def get_price(self) -> float:
        """asdasdsad"""
        raise NotImplementedError


class CommonRoom(Room):
    """Common Room class"""

    def get_price(self) -> float:
        return self.base_price


class LuxuryRoom(Room):
    """Luxury Room class"""
    _price_multiplier = 1.5

    def get_price(self) -> float:
        return self.base_price * self._price_multiplier


class Booking:
    """Booking Room class"""

    def __init__(self, room: Room, start_date: str,
                 end_date: str, cancelled: bool = False):
        self.room = room
        self.start_date = start_date
        self.end_date = end_date
        self.cancelled = cancelled

    def cancel(self) -> None:
        """Cancel Booking"""
        self.cancelled = True


class Hotel:
    """Hotel class"""

    def __init__(self) -> None:
        self.rooms = []
        self.bookings = []

    def add_room(self, room: Room):
        """Add room at Hotel"""
        self.rooms.append(room)

    def book_room(self, room: Room, start_date: str, end_date: str):
        """Book the Room"""
        booking = Booking(room, start_date, end_date)
        self.bookings.append(booking)

    def cancel_booking(self, booking: Booking):
        """Cancel the Booking"""
        booking.cancel()

    def show_booked_rooms(self) -> list[Booking]:
        """Show booked rooms"""
        booked_rooms = []

        for booking in self.bookings:
            if not booking.cancelled:
                booked_rooms.append(booking)

        return booked_rooms

    def show_available_rooms(self, start_date: str, end_date: str) -> list[Room]:
        """show availble rooms"""
        available_rooms = []

        for room in self.rooms:
            is_available = True

            for booking in self.bookings:
                if (
                    booking.room == room
                    and not booking.cancelled
                    and start_date < booking.end_date
                    and end_date > booking.start_date
                ):
                    is_available = False
                    break

            if is_available:
                available_rooms.append(room)

        return available_rooms


hotel = Hotel()

room1 = CommonRoom(101, 100)
room2 = LuxuryRoom(102, 100)

hotel.add_room(room1)
hotel.add_room(room2)

print(room1.get_price())  # 100
print(room2.get_price())  # 150

print(hotel.rooms)

hotel.book_room(
    room1,
    "2026-10-10",
    "2026-10-15"
)

print(hotel.show_booked_rooms())

available = hotel.show_available_rooms(
    "2026-10-12",
    "2026-10-14"
)

print(available)

for room in available:
    print(room.room_number)

available = hotel.show_available_rooms(
    "2026-10-16",
    "2026-10-20"
)

for room in available:
    print(room.room_number)

booking = hotel.bookings[0]

hotel.cancel_booking(booking)

print(booking.cancelled)

print(hotel.show_booked_rooms())

available = hotel.show_available_rooms(
    "2026-10-12",
    "2026-10-14"
)

print(available)
