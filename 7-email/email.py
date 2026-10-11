"""Email Module"""

import asyncio
from random import uniform


async def send_email(user: str) -> None:
    await asyncio.sleep(uniform(0.3, 0.8))
    print(f"Email sent to {user}")


async def send_bulk(users: list[str]) -> None:
    emails = [
        send_email(user) for user in users
    ]
    await asyncio.gather(*emails)


async def main():
    users = ["alice", "bob", "carol", "dave", "eve"]
    await send_bulk(users)

asyncio.run(main())
