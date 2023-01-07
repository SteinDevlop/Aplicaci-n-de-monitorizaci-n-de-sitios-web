from cls.comandos import Command as Cm
from cls.mensajes import Msj
from colorama import Fore, Style
import time
eleccion_tipo = None
while eleccion_tipo != 4:
    print(f"""
    {Msj.titulo}

    {Msj.advertencia}

    {Msj.eleciones}
    """)
    try:
        eleccion_tipo = int(input(f"{Fore.GREEN}(1/2/3){Style.RESET_ALL}: "))
    except Exception as e:
        print(f"{Fore.RED}Error encontrado tipo:{Style.RESET_ALL} {type(e)}")
    if eleccion_tipo == 1:
        try:
            print("".center(50,"-"))
            Cm.requestPerSecond = int(input("""Indique cada cuando se haran las peticiones para verificar cambios:
            """))
            Cm.site = str(input("Indique la url del sitio: "))
            print("Proceso de monitoria iniciado")
            print(f"""
            ----------Update Inicial ----
            Pagina web: {Cm.site}
            Cambios en la pagina detectado: {Cm.cambios}
            -------------------------------
            """)
            print(f"""
            ----------Informacion relevante ----
            Si hay muchos cambios, es extremamente probable que
            la pagina cambie su codigo con cada recarga,
            aconsejamos dejar de usar la herramienta en url como ellas.
            -------------------------------
            """)
            while True:
                # Ejecutar la función
                print(f"Cambios en la pagina: {Cm.cambios}",end="\r")
                Cm.check_website()
                time.sleep(Cm.requestPerSecond)

            print("".center(50,"-"))
        except Exception as e:
            print(f"{Fore.RED}Error encontrado tipo:{Style.RESET_ALL} {type(e)}")
            print("Volviendo a panel de opciones ...")
    elif eleccion_tipo == 2:
        try:
            print("".center(50,"-"))
            pass
            print("".center(50,"-"))
        except Exception as e:
            print(f"{Fore.RED}Error encontrado tipo:{Style.RESET_ALL} {type(e)}")
            print("Volviendo a panel de opciones ...")

    elif eleccion_tipo == 3:
        exit()