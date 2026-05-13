# HeartCheck - Aplicación de Test de Ruffier

Este proyecto es una aplicación de escritorio simple, desarrollada en Python con el framework Kivy, que guía al usuario a través del Test de Ruffier-Dickson para una evaluación primaria del rendimiento cardíaco.

## ¿Qué es el Test de Ruffier?

El test de Ruffier es una prueba de aptitud cardiovascular que consiste en medir la frecuencia cardíaca en tres momentos:
1.  En reposo (P1).
2.  Inmediatamente después de realizar 30 sentadillas en 45 segundos (P2).
3.  Un minuto después del esfuerzo (P3).

Con estos tres valores, se calcula un índice que determina el estado del corazón de la persona.

## Arquitectura del Proyecto

La aplicación utiliza el framework Kivy y sigue una arquitectura que separa la lógica de la interfaz de usuario. La navegación entre las diferentes etapas del test se gestiona mediante un `ScreenManager`.

La estructura se puede entender de la siguiente manera:

-   **Modelo**: La lógica de negocio para calcular el índice y los resultados del test se encuentra en `ruffier.py`. Los datos del usuario (nombre, edad, pulsos) se manejan a través de variables globales en `main.py`.
-   **Vista**: La interfaz de usuario está definida en `main.py` mediante clases de Kivy (`Screen`, `Label`, `Button`, etc.). Los textos y las instrucciones se han externalizado al módulo `instructions.py` para facilitar su mantenimiento.
-   **Controlador**: La lógica de control de flujo y la respuesta a eventos del usuario (clics de botón, finalización de temporizadores) se implementan en los métodos de las clases de pantalla dentro de `main.py`.

## Módulos del Proyecto

El proyecto está dividido en los siguientes archivos Python:

### `main.py`

Es el punto de entrada de la aplicación.
-   **Responsabilidades**:
    -   Define y gestiona las diferentes pantallas (`Screen`) de la aplicación usando un `ScreenManager`.
    -   Construye la interfaz de usuario para cada pantalla (instrucciones, entrada de datos, temporizadores y resultados).
    -   Maneja la lógica de navegación y el flujo de la aplicación.
    -   Recopila los datos introducidos por el usuario.
-   **Clases principales**: `InstrScr`, `PulseScr`, `CheckSits`, `PulseScr2`, `Result`.

### `ruffier.py`

Contiene toda la lógica de cálculo específica del test de Ruffier.
-   **Responsabilidades**:
    -   Calcular el "Índice de Ruffier" a partir de las tres mediciones de pulso.
    -   Determinar los umbrales de resultado según la edad del usuario.
    -   Interpretar el índice para devolver un resultado textual sobre el rendimiento cardíaco.
-   **Funciones principales**: `ruffier_index()`, `neud_level()`, `ruffier_result()`, `test()`.

### `instructions.py`

Este módulo almacena todas las cadenas de texto (instrucciones, etiquetas, etc.) que se muestran en la interfaz de usuario.
-   **Responsabilidades**:
    -   Centralizar los textos de la aplicación para facilitar su modificación o traducción.
    -   Separar el contenido textual de la lógica de la interfaz.

### `seconds.py`

Este módulo contiene el widget `Seconds`, una clase personalizada que hereda de `kivy.uix.label.Label`.
-   **Responsabilidades**:
    -   Funcionar como un temporizador visual que cuenta los segundos de forma ascendente.
    -   Mostrar en pantalla el tiempo transcurrido.
    -   Se utiliza en las pantallas de medición de pulso para guiar al usuario durante los 15 segundos de conteo.
    -   Utiliza una propiedad `done` (`BooleanProperty`) para notificar a otras partes de la aplicación cuando el temporizador ha finalizado.

## Librerías Utilizadas

-   **Kivy**: Framework principal para la construcción de la interfaz gráfica de usuario multiplataforma.

## Cómo Ejecutar la Aplicación

1.  Asegúrate de tener Python instalado en tu sistema.
2.  Instala la librería Kivy:
    ```bash
    pip install kivy
    ```
3.  Ejecuta el archivo principal desde la terminal:
    ```bash
    python main.py
    ```
