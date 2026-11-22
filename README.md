# Inventario del mago

Partida de terminal en Python. Un mago sale al camino con una espada, una poción y una capa. En cada escena puede recoger lo que encuentra, y al terminar ves cómo cambiaron su inventario y sus puntos de vida.

El juego solo usa la biblioteca estándar. El entorno virtual deja el intérprete aislado del resto del sistema.

## Requisitos

Python 3.11 o posterior. Este proyecto se probó con Python 3.14.6.

## Entorno virtual

Desde la carpeta del proyecto:

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python main.py
```

`requirements.txt` no declara paquetes de terceros. El comando de instalación deja el entorno al día y termina sin añadir librerías.

En Windows, activa el entorno con `venv\Scripts\activate` y luego ejecuta `python main.py`.

Para salir del entorno: `deactivate`.

Si la carpeta `venv` ya existe, no hace falta crearla otra vez. Basta con activarla y ejecutar `python main.py`.

## Cómo se juega

Las decisiones se escriben en la terminal.

- **Enter** deja el nombre por defecto, Aldric.
- **s** o **n** responde si recoges un item o si bebes un consumible.
- Un **número** elige el camino o el frasco, cuando hay más de una opción.

Empiezas con 100 puntos de vida. La capa, la espada y el amuleto reducen daño en las escenas que les corresponden. La poción menor restaura 30 y el frasco de savia restaura 20. Si recoges el grimorio, recuperas 10. El cierre de la partida depende de lo que hayas guardado.

## Escenas

1. **El sendero de niebla.** Puedes recoger el bastón de fresno.
2. **El puente agrietado.** Cruzas por el puente o por el vado.
3. **La cueva del eco.** Los murciélagos hieren y aparece el cristal de maná.
4. **La torre dormida.** Un sello hace daño y el grimorio de chispas espera en el atril.

## Módulos

| Archivo | Responsabilidad |
|---|---|
| `main.py` | Arranca la partida |
| `juego.py` | Ordena las escenas y cierra |
| `escenas.py` | Una función por escena |
| `acciones.py` | Recoger, recibir daño y beber |
| `interfaz.py` | Preguntas y texto en la terminal |
| `jugador.py` | Vida del mago e inventario primario |
| `inventario.py` | Agrega, quita y consulta objetos |
| `item.py` | Define cada objeto y el catálogo |
