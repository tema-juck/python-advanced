"""Slots Module"""
from dataclasses import dataclass
import sys


@dataclass
class User:
    name: str
    email: str
    password: str


@dataclass(slots=True)
class SlotUser:
    name: str
    email: str
    password: str


users = [User("Anton", "1@1.ru", "12345678") for i in range(100000)]
usersSlots = [SlotUser("Anton", "1@1.ru", "12345678") for i in range(10000)]

print(sys.getsizeof(users))
print(sys.getsizeof(usersSlots))
