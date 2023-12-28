from configparser import ConfigParser
import os


settings = ConfigParser()
settings.read("./config/settings.ini")
xettings = ConfigParser()
xettings.read("./config/xettings.ini")


def ConsoleLog(string):
     print(f'\033[0m{string}')

def ConsoleDebugLog(string):
      print(f'\033[0;1m<settings> \033[0m{string}')


def MostrarMensaje(int):
    if int == 1:
        ConsoleLog("\033[31mArgumento no válido\n\033[0m")
    if int == 2:
            ConsoleLog("\033[32mAtributo cambiado!\n\033[0m")
    if int == 3:
            ConsoleLog("\033[31mLos valores deben ser del mismo tipo\n\033[0m")
def CambiarSettings(seccion, name, eleccion):
    if DeterminarTipo(seccion, name) == "str":
        eleccion = eleccion.replace("\"", "")
        eleccion = eleccion.replace("\'", "")
        eleccion = f"\'{eleccion}\'"
    if DeterminarTipo(seccion, name) == "bool":
        if eleccion.lower == "true": eleccion = "True"
        if eleccion.lower == "false": eleccion = "False"
    settings.set(seccion, name, eleccion)
    with open("./config/settings.ini", 'w') as settingsFile:
        settings.write(settingsFile)
    
def DeterminarTipo(seccion, name):
    try: settings.getint(seccion, name)
    except:
        try: settings.getboolean(seccion, name)
        except: return "str"
        else: return "bool"
    else: return "int"
def DeterminarTipo2(arg):
    try: int(arg)
    except:
        if arg == "True" or arg == "False": return "bool"
        else: return "str"
    else: return "int"
def PaginaActual(seccion):
    return settings.sections().index(seccion) + 1
def MostrarPagina(seccion, idMensaje = 0):
    os.system("cls")
    ConsoleLog("\n---------------------------------------------------------------------------------------------")
    ConsoleLog(f"\n(Página {PaginaActual(seccion)} de {len(settings.sections())})")
    ConsoleLog(f"\033[1mConfiguración de {seccion}:\n\n")
    for name, value in settings.items(seccion):
        ConsoleLog(f'{xettings.get(seccion, name)}')
        ConsoleLog(f"\033[36m{name} \033[0m= \033[33;1m{value}\n")
    ConsoleLog("---------------------------------------------------------------------------------------------")
    if settings.sections().index(seccion) + 1 == 1:
        ConsoleLog("\nIngresá el nombre del atributo que te gustaría cambiar, 2 para avanzar página, o 1 para salir\n")
        MostrarMensaje(idMensaje)
    if settings.sections().index(seccion) + 1 == len(settings.sections()):
        ConsoleLog("\nIngresá el nombre del atributo que te gustaría cambiar, 1 para retroceder página, o 2 para salir\n")
        MostrarMensaje(idMensaje)
    eleccion = input()
    if eleccion == "1":
        RetrocederPagina(seccion)
    if eleccion == "2":
        AvanzarPagina(seccion)
    contador = 0
    for name, value in settings.items(seccion):
        if contador <= len(settings.items(seccion)):
            if eleccion == name:
                ConsoleLog(f"\nIngresa un nuevo valor para el atributo \033[36m{name}\n\033[1;33m")
                eleccion = input()
                if DeterminarTipo2(eleccion) != DeterminarTipo(seccion, name):
                    MostrarPagina(seccion, 3)
                CambiarSettings(seccion, name, eleccion)
                MostrarPagina(seccion, 2)
                break
            contador += 1
    MostrarPagina(seccion, 1)
def RetrocederPagina(seccion):
    if PaginaActual(seccion) <= 1:
        from .. import Main
    else:
        MostrarPagina(settings.sections()[PaginaActual(seccion) - 2])
def AvanzarPagina(seccion):
    if PaginaActual(seccion) >= len(settings.sections()):
        from .. import Main
    else:
        MostrarPagina(settings.sections()[PaginaActual(seccion)])
MostrarPagina("XXXXXXXXXXXXXXXX")
