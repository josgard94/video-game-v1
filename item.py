"""Objetos que pueden entrar al inventario del mago."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Item:
    """Un objeto del mundo. La curación solo aplica si alguien lo bebe."""

    nombre: str
    descripcion: str
    categoria: str
    curacion: int = 0

    def es_consumible(self) -> bool:
        return self.curacion > 0


CATALOGO: dict[str, Item] = {
    "espada": Item(
        "Espada corta",
        "Hoja de acero. En la mano de un mago sigue cortando.",
        "arma",
    ),
    "pocion": Item(
        "Poción menor",
        "Frasco rojo. Restaura 30 puntos de vida.",
        "consumible",
        curacion=30,
    ),
    "capa": Item(
        "Capa de viaje",
        "Lana gruesa. Amortigua raspones y el viento del puente.",
        "equipo",
    ),
    "baston": Item(
        "Bastón de fresno",
        "Madera viva. Late cuando hay magia cerca.",
        "arma",
    ),
    "amuleto": Item(
        "Amuleto de guardia",
        "Piedra pulida que desvía parte de un golpe.",
        "equipo",
    ),
    "savia": Item(
        "Frasco de savia",
        "Savia dulce. Restaura 20 puntos de vida.",
        "consumible",
        curacion=20,
    ),
    "cristal": Item(
        "Cristal de maná",
        "Fragmento tibio. Un grimorio sabría qué hacer con él.",
        "reliquia",
    ),
    "grimorio": Item(
        "Grimorio de chispas",
        "Cuaderno de hechizos menores. Reconoce a un mago.",
        "reliquia",
    ),
}


def crear(clave: str) -> Item:
    """Devuelve una copia independiente del objeto catalogado."""
    try:
        origen = CATALOGO[clave]
    except KeyError as error:
        raise KeyError(f"No existe el objeto '{clave}'.") from error
    return Item(origen.nombre, origen.descripcion, origen.categoria, origen.curacion)
