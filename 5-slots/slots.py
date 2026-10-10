"""Slots Module"""
from dataclasses import dataclass
import tracemalloc

tracemalloc.start()


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

users_mem = tracemalloc.get_traced_memory()

usersSlots = [SlotUser("Anton", "1@1.ru", "12345678") for i in range(100000)]

users_slots_mem = tracemalloc.get_traced_memory()

print(f"User: {users_mem} byte")
print(f"UserSlots: {users_slots_mem} byte")
