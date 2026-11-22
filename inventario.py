"""Colección ordenada de objetos del jugador."""

from item import Item


class Inventario:
    """Lista primaria de objetos. No conoce la vida ni la terminal."""

    def __init__(self, items: list[Item] | None = None) -> None:
        self._items: list[Item] = list(items or [])

    def agregar(self, item: Item) -> None:
        self._items.append(item)

    def quitar(self, item: Item) -> None:
        self._items.remove(item)

    def items(self) -> tuple[Item, ...]:
        return tuple(self._items)

    def contiene(self, nombre: str) -> bool:
        return any(item.nombre == nombre for item in self._items)

    def consumibles(self) -> tuple[Item, ...]:
        return tuple(item for item in self._items if item.es_consumible())

    def nombres(self) -> tuple[str, ...]:
        return tuple(item.nombre for item in self._items)
