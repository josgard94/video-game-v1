"""Entrada y salida por la terminal. No modifica al jugador."""

from collections import Counter

from jugador import Jugador


ANCHO = 62


def _leer(prompt: str) -> str:
    try:
        return input(prompt)
    except EOFError:
        print()
        raise SystemExit("Entrada cerrada. Fin de la partida.") from None


def separador() -> None:
    print("-" * ANCHO)


def titulo(texto: str) -> None:
    print()
    separador()
    print(texto)
    separador()


def narrar(texto: str) -> None:
    print(texto)


def pedir_nombre() -> str:
    nombre = _leer("Nombre del mago (Enter para usar Aldric): ").strip()
    return nombre or "Aldric"


def confirmar(pregunta: str) -> bool:
    """Lee un sí o un no. Repite hasta obtener una respuesta válida."""
    while True:
        respuesta = _leer(f"{pregunta} [s/n]: ").strip().lower()
        if respuesta in {"s", "si", "sí"}:
            return True
        if respuesta in {"n", "no"}:
            return False
        print("Responde s (sí) o n (no).")


def elegir(pregunta: str, opciones: list[str]) -> int:
    """Devuelve el índice elegido, empezando en cero."""
    print(pregunta)
    for numero, opcion in enumerate(opciones, start=1):
        print(f"  {numero}. {opcion}")
    while True:
        texto = _leer("Elige un número: ").strip()
        if texto.isdigit():
            indice = int(texto) - 1
            if 0 <= indice < len(opciones):
                return indice
        print("Elige un número de la lista.")


def mostrar_estado(jugador: Jugador) -> None:
    print(f"{jugador.nombre}, {jugador.clase}")
    print(f"Vida: {jugador.vida}/{jugador.vida_maxima}")
    print("Inventario:")
    if not jugador.inventario.items():
        print("  (vacío)")
        return
    for numero, item in enumerate(jugador.inventario.items(), start=1):
        extra = f", +{item.curacion} vida" if item.es_consumible() else ""
        print(f"  {numero}. {item.nombre} ({item.categoria}{extra})")
        print(f"     {item.descripcion}")


def mostrar_actualizacion(
    titulo_escena: str,
    vida_antes: int,
    items_antes: tuple[str, ...],
    jugador: Jugador,
) -> None:
    """Compara la vida y el inventario de antes y después de una escena."""
    titulo(f"Actualización — {titulo_escena}")
    print(f"Vida: {vida_antes} → {jugador.vida}")

    altas = Counter(jugador.inventario.nombres()) - Counter(items_antes)
    bajas = Counter(items_antes) - Counter(jugador.inventario.nombres())
    if not altas and not bajas:
        print("Inventario: sin cambios")
    else:
        for nombre, cantidad in altas.items():
            sufijo = f" x{cantidad}" if cantidad > 1 else ""
            print(f"Inventario: + {nombre}{sufijo}")
        for nombre, cantidad in bajas.items():
            sufijo = f" x{cantidad}" if cantidad > 1 else ""
            print(f"Inventario: - {nombre}{sufijo}")

    print()
    mostrar_estado(jugador)
