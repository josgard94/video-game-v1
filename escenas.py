"""Cada función resuelve una sola escena y devuelve su título."""

from jugador import Jugador
from item import crear
import acciones
import interfaz


def escena_sendero(jugador: Jugador) -> str:
    titulo = "El sendero de niebla"
    interfaz.titulo(titulo)
    interfaz.narrar(
        "La niebla abre un claro. Sobre una piedra hay un bastón que zumba "
        "al ritmo de tu pulso."
    )
    acciones.ofrecer_recogida(jugador, crear("baston"))
    return titulo


def escena_puente(jugador: Jugador) -> str:
    titulo = "El puente agrietado"
    interfaz.titulo(titulo)
    interfaz.narrar(
        "Un puente de tablas cruza el barranco. Abajo, el río ofrece un vado lento."
    )
    indice = interfaz.elegir(
        "¿Cómo cruzas?",
        [
            "Cruzar el puente con la capa bien cerrada",
            "Bajar al vado y caminar entre las piedras",
        ],
    )
    if indice == 0:
        _cruzar_puente(jugador)
    else:
        _cruzar_vado(jugador)
    return titulo


def _cruzar_puente(jugador: Jugador) -> None:
    dano, detalle = acciones.dano_mitigado(
        15,
        [(jugador.inventario.contiene("Capa de viaje"), 4, "la capa amortigua las astillas")],
    )
    interfaz.narrar("Una tabla cede y las astillas saltan.")
    if not acciones.aplicar_dano(jugador, dano, detalle.capitalize() + "."):
        return
    interfaz.narrar("Del otro lado, algo brilla enganchado en el pasamanos.")
    acciones.ofrecer_recogida(jugador, crear("amuleto"))


def _cruzar_vado(jugador: Jugador) -> None:
    interfaz.narrar("El agua te llega a las rodillas y el fondo resbala.")
    if not acciones.aplicar_dano(jugador, 8, "Te golpeas la espinilla contra una roca."):
        return
    interfaz.narrar("Entre las raíces de la orilla hay un frasco todavía sellado.")
    acciones.ofrecer_recogida(jugador, crear("savia"))


def escena_cueva(jugador: Jugador) -> str:
    titulo = "La cueva del eco"
    interfaz.titulo(titulo)
    interfaz.narrar(
        "El eco repite tu respiración. Una bandada de murciélagos cae desde la bóveda."
    )
    dano, detalle = acciones.dano_mitigado(
        24,
        [
            (jugador.inventario.contiene("Espada corta"), 6, "la espada corta el enjambre"),
            (
                jugador.inventario.contiene("Amuleto de guardia"),
                5,
                "el amuleto desvía los picotazos",
            ),
        ],
    )
    if not acciones.aplicar_dano(jugador, dano, detalle.capitalize() + "."):
        return titulo
    interfaz.narrar("Cuando se van, un cristal pulsa luz azul en un nicho.")
    acciones.ofrecer_recogida(jugador, crear("cristal"))
    acciones.ofrecer_curacion(jugador)
    return titulo


def escena_torre(jugador: Jugador) -> str:
    titulo = "La torre dormida"
    interfaz.titulo(titulo)
    interfaz.narrar(
        "La puerta cede. Un sello antiguo estalla en chispas en cuanto pisas el umbral."
    )
    dano, detalle = acciones.dano_mitigado(
        18,
        [
            (
                jugador.inventario.contiene("Amuleto de guardia"),
                5,
                "el amuleto absorbe parte del sello",
            )
        ],
    )
    if not acciones.aplicar_dano(jugador, dano, detalle.capitalize() + "."):
        return titulo
    interfaz.narrar("En el atril, un cuaderno espera una mano que sepa leerlo.")
    grimorio = crear("grimorio")
    acciones.ofrecer_recogida(jugador, grimorio)
    if jugador.inventario.contiene(grimorio.nombre):
        acciones.aplicar_curacion(
            jugador,
            10,
            "El grimorio reconoce a un mago y te devuelve un soplo de vida.",
        )
    acciones.ofrecer_curacion(jugador)
    return titulo
