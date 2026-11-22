"""Orquesta la partida: crear al mago, recorrer escenas y cerrar."""

from jugador import Jugador, crear_mago
import escenas
import interfaz


ESCENAS = (
    escenas.escena_sendero,
    escenas.escena_puente,
    escenas.escena_cueva,
    escenas.escena_torre,
)


def texto_final(jugador: Jugador) -> str:
    """Elige el cierre según lo que el mago conserva y cuánta vida le queda."""
    if not jugador.sigue_en_pie():
        return "Tu inventario queda en el polvo del camino. Otra mano lo recogerá."

    tiene_grimorio = jugador.inventario.contiene("Grimorio de chispas")
    tiene_cristal = jugador.inventario.contiene("Cristal de maná")
    if tiene_grimorio and tiene_cristal:
        return (
            "Encajas el cristal en la tapa del grimorio. La torre enciende "
            "una ventana y el camino de vuelta queda marcado con chispas."
        )
    if tiene_grimorio:
        return (
            "Lees el grimorio a la luz de la puerta. Vuelves con hechizos nuevos "
            "y los bolsillos más pesados que al salir."
        )
    if jugador.vida < 40:
        return "Sales cojeando. Llevas menos magia de la que esperabas, pero sigues en pie."
    return "Dejas la torre cerrada y regresas por el sendero con lo que decidiste guardar."


def jugar() -> None:
    nombre = interfaz.pedir_nombre()
    jugador = crear_mago(nombre)
    interfaz.titulo(f"{jugador.nombre} sale al camino")
    interfaz.narrar(
        "Eres un mago. Empiezas con el inventario primario de la torre: "
        "una espada, una poción y una capa. En cada hallazgo la terminal "
        "te preguntará si quieres recoger el item."
    )
    interfaz.mostrar_estado(jugador)

    for escena in ESCENAS:
        if not jugador.sigue_en_pie():
            break
        vida_antes = jugador.vida
        items_antes = jugador.inventario.nombres()
        titulo = escena(jugador)
        interfaz.mostrar_actualizacion(titulo, vida_antes, items_antes, jugador)

    interfaz.titulo("Fin de la partida")
    interfaz.narrar(texto_final(jugador))
    print()
    interfaz.mostrar_estado(jugador)
