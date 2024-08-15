# Duck typing: si se ve como un pato, nada como un pato, entonces es un pato

# tipado dinámico: no se especifica el tipo de dato de una variable, se infiere en tiempo de ejecución


# Clase User que hereda de Model


class User():
    # Implementación del método guardar para User
    def guardar(self):
        print("Guardando usuario en la base de datos")

# Clase Session que hereda de Model, identifica una sesión de usuario


class Session():
    # Implementación del método guardar para Session
    def guardar(self):
        print("Guardando sesión en archivo de texto")

# Función guardar que demuestra el polimorfismo


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()  # Se llama al método guardar específico de cada objeto


# Crear instancias de User y Session
usuario = User()
sesion = Session()

# Polimorfismo: se ejecuta el método guardar de cada clase para ahorrar código
guardar([sesion, usuario])
# Salida:
# Guardando sesión en archivo de texto
# Guardando usuario en la base de datos


# -------------------------------------------------------------

# # Duck Typing en Python
# # =====================
# # En programación, el término "Duck Typing" proviene del dicho: "Si se ve como un pato, nada como un pato,
# # entonces es un pato". En el contexto de la programación, Duck Typing significa que el tipo de un objeto no
# # se determina por su herencia de una clase específica, sino por su comportamiento, es decir, si tiene los
# # métodos y propiedades correctos para ser usado en un determinado contexto.

# # Tipado dinámico en Python
# # =========================
# # Python es un lenguaje de tipado dinámico, lo que significa que no es necesario especificar el tipo de una
# # variable cuando se declara. El tipo se infiere en tiempo de ejecución en función del valor asignado. Esto
# # permite una gran flexibilidad, pero también requiere cuidado para evitar errores de tipo en tiempo de ejecución.

# # Clase User
# # ----------
# # Esta clase representa un usuario en el sistema. Aunque no hereda explícitamente de ninguna clase abstracta,
# # implementa un método `guardar`, que es lo que la hace compatible con la función `guardar` de más adelante.

# class User:
#     # Implementación del método guardar para User
#     def guardar(self):
#         """
#         Simula la acción de guardar un usuario en una base de datos.
#         Este método es suficiente para que un objeto de la clase User
#         sea considerado "un pato" en el contexto de la función `guardar`.
#         """
#         print("Guardando usuario en la base de datos")

# # Clase Session
# # -------------
# # Esta clase representa una sesión de usuario. Similar a la clase `User`, no necesita heredar de una clase base
# # específica, siempre que implemente el método `guardar`. Esto ilustra cómo el comportamiento (tener un método
# # `guardar`) define el "tipo" en el contexto de la función `guardar`.

# class Session:
#     # Implementación del método guardar para Session
#     def guardar(self):
#         """
#         Simula la acción de guardar una sesión en un archivo de texto.
#         Al igual que `User`, esta clase es compatible con la función `guardar`
#         simplemente porque tiene un método `guardar`.
#         """
#         print("Guardando sesión en archivo de texto")

# # Función `guardar`
# # -----------------
# # Esta función es un ejemplo de polimorfismo en Python, que se logra a través de Duck Typing. No importa
# # de qué clase sean las instancias en la lista `entidades`; lo que importa es que cada instancia tenga un
# # método `guardar` que se pueda invocar. Python no verifica el tipo de `entidades`, solo espera que cada
# # objeto en la lista se comporte de la manera esperada.

# def guardar(entidades):
#     """
#     Esta función recibe una lista de objetos y llama al método `guardar` de cada uno.
#     Gracias a Duck Typing, cualquier objeto que implemente un método `guardar` puede
#     ser procesado por esta función, sin importar su clase concreta.
#     """
#     for entidad in entidades:
#         entidad.guardar()  # Se llama al método guardar específico de cada objeto

# # Ejecución del Código
# # --------------------
# # Se crean instancias de las clases `User` y `Session`. Luego, la función `guardar` se llama con una lista que
# # contiene ambas instancias. Como ambas clases tienen un método `guardar`, la función las maneja de manera uniforme.

# # Crear instancias de User y Session
# usuario = User()
# sesion = Session()

# # Duck Typing en acción: se ejecuta el método `guardar` de cada objeto
# guardar([sesion, usuario])

# # Salida esperada:
# # Guardando sesión en archivo de texto
# # Guardando usuario en la base de datos

# # Análisis del Duck Typing y Polimorfismo
# # ---------------------------------------
# # En este ejemplo, el polimorfismo se logra sin necesidad de herencia explícita o de implementar una interfaz común.
# # En lugar de eso, se basa en Duck Typing: si un objeto tiene un método `guardar`, entonces puede ser procesado
# # por la función `guardar`. Esto muestra la flexibilidad del tipado dinámico en Python, donde el tipo de un objeto
# # se define por su comportamiento (los métodos que implementa), y no necesariamente por su lugar en una jerarquía
# # de clases.
