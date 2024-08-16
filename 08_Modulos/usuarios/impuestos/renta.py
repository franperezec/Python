

# # si pongo puntos me voy atrasando en las carpetas y voy pontiendo el nombre de la carpeta para ver uso cntrl+espacio
# from ..gestion.crud import guardar

# # print(__name__)  # usuarios.impuestos.renta


# def impuesto_renta():
#     print("Pagando impuesto de renta")
#     # Llamamos a la función `guardar` para simular la acción de guardar un usuario.
#     guardar()


# solución de problemas

if __name__ != "__main__":
    from ..gestion.crud import guardar  # import relative
    # from usuarios.gestion.crud import guardar # import absolute puedo usar cualquiera de los dos

    print("Este mensaje se mostrará solo si ejecutamos este archivo directamente. Tarea de mantenimiento")
    print(__name__)  # usuarios.impuestos.renta

    def impuesto_renta():
        print("Pagando impuesto de renta")
        # Llamamos a la función `guardar` para simular la acción de guardar un usuario.
        guardar()

if __name__ == "__main__":
    print("Este mensaje se mostrará solo si ejecutamos este archivo directamente. Tarea de mantenimiento")
