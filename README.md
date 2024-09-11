# Guess the Number


## 1. Consideraciones generales
- El proyecto debe implementarse en python y no se podrá utilizar ninguna librería a excepción de `rich`.
- El juego se llevará a cabo en la terminal.
- Se utilizará un número aleatorio entre 1 y 100 como número secreto
- Después de cada turno, se mostrará información sobre la suposición realizada
- El juego termina, una vez se adivine el número.

## 2. Consideraciones Técnicas
El juego se llevará a cabo en la terminal usando Python. El objetivo de la actividad es hacer uso de los temas vistos en clase, tales como bucles, condicionales y listas.

## 3. Hitos

### 3.1 Pasos Iniciales
1. Haz un fork del presente repositorio. Puedes ayudarte del [siguiente video](https://youtu.be/3m7Z3g_U-Cs?si=eCA7q8u5OVMbl3Sx&t=257)
2.  Una vez forkeado, clona/descarga el repositorio:
  ```bash
    git clone URL-DEL-REPO-FORKEADO
  ```
3. Abre la carpeta descargada en Visual Studio Code

4. Crea un nuevo archivo llamado `main.py` y agrega el siguiente código
```python
print("Hola mundo")
```
5. Ejecuta `main.py`. Deberías ver `Hola mundo` en la consola
6. Ya estás listo para empezzar a implementar el juego.

### 3.2 Implementa el juego

A continuación te comparto los pasos generales que deberías seguir:
1. Genera un número aleatorio entre 1 y 100. Puedes utilizar la función `randint` del módulo `random` de Python.
2. Implementa un bucle que solicite al jugador que adivine el número. Utiliza la función `input` para esto.
3. Compara la entrada del usuario, con el número secreto:
  a. Si el usuario adivina correctamente, termina el juego
  b. Si el usuario no adivina el número secreto, proporciona una pista sobre si el número secreto es mayor o menor que la entrada del usuario.
4. Implementa la lógica para el turno del ordenador. El ordenador puede hacer una suposición aleatoria.
5. Continúa el juego hasta que el jugado o el ordenador adivinen correctamente el número.

#### Referencias 

- [Generación de números aleatorios en python](https://www.w3schools.com/python/ref_random_randint.asp)
- [El bucle While](https://www.w3schools.com/python/python_while_loops.asp)


### 3.3 Ninja Version

Una vez tengas una versión básica del juego y que cumple con los requerimientos mínimos, puedes hacer mejoras:
  1. Lleva un registro de las suposiciones del jugador y del ordenador. Cuando el juego termine, muestra todas las suposiciones que hizo quien gane.
  2. Añade una opción de jugar de nuevo: Cuando el juego termine, pregunta al usuario si desea jugar de nuevo

## 4. Entregables
Una vez termines el juego, deberás compartir en UVirtual:
- El link al Pull Request con tu solución. El Pull request deberá llevar tu nombre