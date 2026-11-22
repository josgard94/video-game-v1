"""Efectos de una decisión: daño, recogida y curación."""

from jugador import Jugador
from item import Item
import interfaz

UMBRAL_CURACION = 80


def dano_mitigado(base: int, factores: list[tuple[bool, int, str]]) -> tuple[int, str]:
    """Resta protección al daño base y describe qué objetos intervinieron."""
    dano = base
    razones: list[str] = []
    for activo, reduccion, razon in factores:
        if activo:
            dano -= reduccion
            razones.append(razon)
    detalle = ", ".join(razones) if razones else "sin protección de tu equipo"
    return max(0, dano), detalle


def aplicar_dano(jugador: Jugador, cantidad: int, motivo: str) -> bool:
    """Aplica daño, lo anuncia y devuelve si el mago sigue en pie."""
    antes = jugador.vida
    aplicado = jugador.recibir_dano(cantidad)
    interfaz.narrar(f"{motivo} Pierdes {aplicado} puntos de vida ({antes} → {jugador.vida}).")
    if jugador.sigue_en_pie():
        return True
    interfaz.narrar("Caes al suelo. La magia se apaga y la partida termina.")
    return False


def aplicar_curacion(jugador: Jugador, cantidad: int, motivo: str) -> None:
    antes = jugador.vida
    recuperado = jugador.recuperar_vida(cantidad)
    interfaz.narrar(
        f"{motivo} Recuperas {recuperado} puntos de vida ({antes} → {jugador.vida})."
    )


def ofrecer_recogida(jugador: Jugador, item: Item) -> None:
    """Pregunta en la terminal si el objeto encontrado entra al inventario."""
    interfaz.narrar(f"Encuentras un item: {item.nombre}. {item.descripcion}")
    if interfaz.confirmar(f"¿Quieres recoger este item: {item.nombre}?"):
        jugador.recoger(item)
        interfaz.narrar(f"Guardas {item.nombre} en el inventario.")
        return
    interfaz.narrar(f"Dejas {item.nombre} donde estaba.")


def ofrecer_curacion(jugador: Jugador) -> None:
    """Ofrece beber un consumible cuando la vida quedó por debajo del umbral."""
    if jugador.vida >= jugador.vida_maxima or jugador.vida > UMBRAL_CURACION:
        return
    opciones = list(jugador.inventario.consumibles())
    if not opciones:
        interfaz.narrar("No te quedan frascos para beber.")
        return
    if not interfaz.confirmar(
        f"Tienes {jugador.vida} puntos de vida. ¿Quieres beber un consumible?"
    ):
        interfaz.narrar("Guardas los frascos para después.")
        return

    if len(opciones) == 1:
        elegido = opciones[0]
    else:
        indice = interfaz.elegir(
            "¿Cuál bebes?",
            [f"{item.nombre} (+{item.curacion} vida)" for item in opciones],
        )
        elegido = opciones[indice]

    antes = jugador.vida
    curado = jugador.usar(elegido)
    interfaz.narrar(
        f"Bebes {elegido.nombre}. Recuperas {curado} puntos de vida ({antes} → {jugador.vida})."
    )
