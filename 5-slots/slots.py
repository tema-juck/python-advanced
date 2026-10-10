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


before = tracemalloc.get_traced_memory()[0]
users = [User("Anton", "1@1.ru", "12345678") for _ in range(100000)]
users_mem = tracemalloc.get_traced_memory()[0] - before

before = tracemalloc.get_traced_memory()[0]
slot_users = [SlotUser("Anton", "1@1.ru", "12345678") for _ in range(100000)]
slot_users_mem = tracemalloc.get_traced_memory()[0] - before

print(f"User: {users_mem} byte")
print(f"UserSlots: {slot_users_mem} byte")
