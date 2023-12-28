import time
from colorama import init
import os
from configparser import ConfigParser

settings = ConfigParser()

def ConsoleLog(string):
     print(f'\033[0m{string}')

def ConsoleDebugLog(string):
      print(f'\033[0;1m<Main> \033[0m{string}')

version = "v1.1.0"

init(convert=True)


def main(mostrarError = False):
    while True:
        settings.read("./config/settings.ini")
        
        os.system("cls")
        ConsoleLog("\nBienvenid@!")
        ConsoleLog("\n---------------------------------------------------------------------------------------------\n")
        ConsoleLog(f"\033[1;36m   ____                    _                                 \n  / __ \                  | |                                \n | |  | |   ___  _ __   __| | __ _   _ __   __ _ _ __  _   _ \n | |  | |  / _ \| '_ \ / _` |/ _` | | '_ \ / _` | '_ \| | | |\n | |__| | | (_) | | | | (_| | (_| | | |_) | (_| | |_) | |_| |\n  \___\_\  \___/|_| |_|\__,_|\__,_| | .__/ \__,_| .__/ \__,_|\n                                    | |         | |          \n                                    |_|         |_|           {version}\n\n")
        ConsoleLog("1 = \033[1mEjecutar programa")
        ConsoleLog("2 = \033[1mEjecutar Linkgrabber")
        ConsoleLog("3 = \033[1mOpciones")
        ConsoleLog("4 = \033[1mSalir\n")
        ConsoleLog("---------------------------------------------------------------------------------------------\n")
        ConsoleLog("¿Qué te gustaría hacer?\n")
        if mostrarError:
            ConsoleLog("\033[31mArgumento no válido\n\033[0m")
        try: eleccion = input()
        except: ConsoleLog("\033[36mPrograma terminado por el usuario!\033[0m\n"); exit()
        ConsoleLog("")
        ejecutado = False

        if eleccion == "1":
            ConsoleLog("\nEjecutando programa...")
            ConsoleLog("* Para salir del programa Usa Ctrl+C *\n")
            time.sleep(2)
            #while True:
            #    try:
            #        from scripts import xxxxxxxxxx
            #    except KeyboardInterrupt:
            #        ConsoleLog("\033[36m\nPrograma terminado por el usuario!")
            #        ejecutado = True
            #        break
            #    except:
            #        if settings.getboolean("SteamCardsProfit", "autoReinicio"):
            #            ConsoleLog("\033[31m\nEl programa finalizó debido a un error, reiniciando...")
            #            continue
            #        ConsoleLog("\033[31m\nEl programa finalizó debido a un error")
            #        input()
            #        ejecutado = True
            #        break

        if eleccion == "2":
            try:
                from scripts import linkgrabber
            except:
                pass
            main()

        if eleccion == "3":
            try:
                from scripts import settingsscript
            except:
                pass
            main()
            
        if eleccion == "4":
            ConsoleLog("\033[36mPrograma terminado por el usuario!\033[0m\n")
            exit()
        if not ejecutado:
            main(True)


main()