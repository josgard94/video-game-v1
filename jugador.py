"""El personaje jugador: un mago con vida e inventario."""

from inventario import Inventario
from item import Item, crear


class Jugador:
    """Estado del mago. Las escenas cambian este estado; no imprimen desde aquí."""

    def __init__(self, nombre: str, inventario: Inventario) -> None:
        self.nombre = nombre
        self.clase = "Mago"
        self.vida_maxima = 100
        self.vida = self.vida_maxima
        self.inventario = inventario

    def recibir_dano(self, cantidad: int) -> int:
        aplicado = min(self.vida, max(0, cantidad))
        self.vida -= aplicado
        return aplicado

    def recuperar_vida(self, cantidad: int) -> int:
        antes = self.vida
        self.vida = min(self.vida_maxima, self.vida + max(0, cantidad))
        return self.vida - antes

    def recoger(self, item: Item) -> None:
        self.inventario.agregar(item)

    def usar(self, item: Item) -> int:
        if not item.es_consumible():
            raise ValueError(f"{item.nombre} no se puede beber.")
        curado = self.recuperar_vida(item.curacion)
        self.inventario.quitar(item)
        return curado

    def sigue_en_pie(self) -> bool:
        return self.vida > 0


def crear_mago(nombre: str) -> Jugador:
    """Arma al mago con el inventario primario: espada, poción y capa."""
    primario = Inventario(
        [
            crear("espada"),
            crear("pocion"),
            crear("capa"),
        ]
    )
    return Jugador(nombre, primario)
