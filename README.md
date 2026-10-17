# Laboratorio 7: Minimax y Poda Alfa-Beta
## 1. Objetivo
Implementar los algoritmos Minimax y Poda Alfa-Beta en Python para resolver árboles de decisiones, comparar sus resultados y comprobar cómo la poda reduce la cantidad de nodos evaluados.
## 2. Requisitos
- Python 3.13
- pytest
- pytest-cov
## 3. Estructura del proyecto
```text
alpha-beta-lab/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   ├── __init__.py
│   ├── game_tree.py
│   ├── minimax.py
│   ├── alpha_beta.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_algorithms.py
├── .gitignore
├── README.md
└── requirements.txt
```
## 4. Instalación y ejecución
Instalar las dependencias:
```bash
python -m pip install -r requirements.txt
```
Ejecutar el programa:
```bash
python -m src.main
```
Ejecutar las pruebas unitarias:
```bash
python -m pytest -v
```
Ejecutar las pruebas con cobertura:
```bash
python -m pytest --cov=src --cov-report=term-missing
```
## 5. Resultados obtenidos
En la comparación del árbol mediano se obtuvieron los siguientes resultados:
| Indicador | Minimax | Alfa-Beta |
|---|---:|---:|
| Valor óptimo | 7 | 7 |
| Nodos evaluados | 12 | 8 |
| Ramas podadas | No aplica | 3 |
Alfa-Beta obtuvo el mismo valor óptimo que Minimax, pero evaluó cuatro nodos menos. Esto representa una reducción aproximada del 33,3 % en los nodos evaluados para este ejemplo.
Las pruebas unitarias finalizaron con cinco pruebas aprobadas.
## 6. Preguntas de análisis
### 1. ¿Por qué Alfa-Beta devuelve el mismo resultado que Minimax si no evalúa todo el árbol?
Porque la poda Alfa-Beta descarta ramas que no pueden cambiar la decisión final. Aunque no evalúa todos los nodos, conserva la información necesaria para encontrar el mismo valor óptimo que Minimax.
### 2. ¿Qué representa alfa?
Alfa representa el mejor valor que MAX puede garantizar hasta el momento durante la búsqueda. Se utiliza para determinar cuándo una rama deja de ser relevante.
### 3. ¿Qué representa beta?
Beta representa el mejor valor, desde la perspectiva de MIN, que se ha encontrado hasta el momento. Permite establecer un límite para decidir si conviene continuar explorando una rama.
### 4. ¿En qué situaciones Alfa-Beta ahorra más trabajo?
Ahorra más trabajo cuando el árbol es grande y el orden de exploración permite identificar pronto las ramas que no pueden mejorar la decisión. En esas condiciones, se pueden evitar muchas evaluaciones.
### 5. ¿Por qué el orden de exploración afecta al rendimiento?
Porque explorar primero las ramas más prometedoras permite actualizar alfa y beta antes. Esto puede producir más podas. Un orden menos favorable puede obligar a evaluar más nodos, aunque el resultado final siga siendo el mismo.
### 6. ¿Qué ocurre si el oponente no es racional?
Minimax supone que el oponente elige las respuestas que más perjudican al jugador MAX. Si el oponente toma decisiones diferentes, el resultado real puede variar respecto a la predicción del algoritmo.
### 7. ¿Qué relación tienen estos algoritmos con los motores de ajedrez?
Se utilizan para analizar posibles movimientos y respuestas del oponente, estimando qué decisiones ofrecen mejores resultados. La poda Alfa-Beta permite reducir la búsqueda de movimientos que no pueden mejorar la decisión actual.
### 8. ¿Cuáles son sus limitaciones frente a las redes neuronales y el aprendizaje por refuerzo?
Minimax y Alfa-Beta dependen de la representación del árbol, de las evaluaciones disponibles y del coste de explorar las posibilidades. En juegos con árboles enormes, la búsqueda puede resultar costosa. Las redes neuronales pueden estimar posiciones y el aprendizaje por refuerzo puede aprender estrategias, aunque estos métodos también requieren recursos y entrenamiento.
## 7. Integración continua
El proyecto incluye un flujo de GitHub Actions que instala las dependencias y ejecuta automáticamente las pruebas unitarias. La ejecución del flujo en GitHub finalizó correctamente.
## 8. Conclusión
Se implementaron Minimax y Alfa-Beta, se compararon sus resultados y se verificó su funcionamiento mediante cinco pruebas unitarias aprobadas. En el árbol mediano, ambos algoritmos encontraron el valor óptimo de 7, mientras que Alfa-Beta evaluó menos nodos. La integración continua permitió automatizar la verificación del código.
