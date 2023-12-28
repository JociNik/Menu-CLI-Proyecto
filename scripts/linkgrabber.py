import pyperclip
from colorama import init
import time

def ConsoleLog(string):
     print(f'\033[0m{string}')

def ConsoleDebugLog(string):
      print(f'\033[0;1m<linkgrabber> \033[0m{string}')

archivo = open("./config/lista.txt", "a")

var = pyperclip.paste()

init(convert=True)

ConsoleLog("\n\033[1mBienvenido a \033[31mLinkgrabber!\n\033[0;1mEste programa copia automáticamente el contenido de tu portapapeles y lo pega en el archivo \"lista.txt\"")
ConsoleLog("\n* Para volver al menú principal usá Ctrl+C *\n\n")

while True:
    if var != pyperclip.paste():
        var = pyperclip.paste()
        ConsoleLog(var)
        archivo.write(f'\n{var}')
        archivo.flush()
        ConsoleLog("\033[36mCopiado!\n")
    time.sleep(0.2)