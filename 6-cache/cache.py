"""Module Cache"""


from typing import Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class Cache(Generic[K, V]):
    _items: dict[K, V]

    def __init__(self) -> None:
        self._items = {}

    def set(self, key: K, value: V) -> None:
        self._items[key] = value

    def get(self, key: K) -> V | None:
        return self._items.get(key)

    def keys(self) -> list[K]:
        return list(self._items.keys())

    def values(self) -> list[V]:
        return list(self._items.values())


hits = Cache[str, int]()
hits.set("home", 10)
hits.set("about", 3)
x = hits.get("home")          # x: int | None
paths = hits.keys()         # list[str]
counts = hits.values()      # list[int]

print(paths)
print(counts)

hits.set("contacts", "5")   # ❌ ошибка типов
hits.get(123)               # ❌ ошибка типов
