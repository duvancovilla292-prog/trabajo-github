# Práctica Colaborativa Git y Python (trabajo-github)

## Descripción Técnica
Repositorio de iniciación al control de versiones colaborativo mediante Git. Contiene una colección de scripts introductorios en Python que exploran operaciones de I/O, control de flujo (bucles `for`), manejo de excepciones (`try-except`) y cálculos matemáticos.

## Estructura de Archivos
*   `archivo.py`: Script básico de interacción con el usuario.
*   `azucar.py`: Script funcional que genera patrones visuales en consola (triángulos de caracteres) e incluye una función para el cálculo preciso del número áureo (Phi).
*   `keiler.py` y `texto1.txt`: Archivos de prueba utilizados para simulaciones de *commits* y resolución de conflictos.

## ⚠️ Análisis de Bugs Detectados
1.  **Redefinición de Funciones Nativas (`archivo.py`):**
    La instrucción `nombre = input = ("como te llamas")` es sintácticamente errónea para capturar datos. En su lugar, sobrescribe la función integrada `input()` con una tupla/cadena. Esto anula la capacidad del script de recibir información real del teclado.
    *Fix:* `nombre = input("¿Cómo te llamas?: ")`
2.  **Colapso por Variable no Enlazada (`azucar.py`):**
    En la función `n()`, si el bloque `try` falla (porque el usuario ingresa un texto en lugar de un número), la excepción se captura pero el script continúa ejecutándose. Al llegar a `range(u+1)`, el programa se detiene abruptamente con un `UnboundLocalError` porque la variable `u` jamás fue creada.

## Colaboradores
* Javier Suarez
* Duvan Covilla
* Keiler Serrano
