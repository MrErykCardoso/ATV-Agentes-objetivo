import os
import platform
from colorama import Fore, init

# inicializa cores
init(autoreset=True)

# ---------------------- DECORAÇÃO ----------------------
def clear():
    """Usado para limpar o terminal e dar um visual mais limpo."""
    sistem = platform.system()
    
    if sistem == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def titulo(texto):
    """Usado para decorar os títulos do programa."""
    print(Fore.CYAN + "═" * 55)
    print(Fore.CYAN + f"{texto.center(55)}")
    print(Fore.CYAN + "═" * 55)

def prompt(texto):
    """Usando para decora os inputs do programa."""
    return input(Fore.YELLOW + f"➤ {texto}: " + Fore.WHITE)

def erroPrint(texto):
    """Usando para decora os inputs do programa."""
    return print(Fore.RED + f"➤ {texto}: " + Fore.WHITE)

def okPrint(texto):
    """Usando para decora os inputs do programa."""
    return print(Fore.LIGHTBLUE_EX + f"➤ {texto}: " + Fore.WHITE)

def listar_opcoes(msg, opcoes):
    """Imprime as opções decoradas na cor selecionada."""
    print(Fore.MAGENTA + f"\n{msg}")
    for i, item in enumerate(opcoes):
        print(Fore.GREEN + f"[{i}] " + Fore.WHITE + f"{item}")

def loading(msg="Processando"):
    """Imprime uma mensagem decorativa que simula o carregamento do programa."""
    import time, sys
    for i in range(3):
        sys.stdout.write(Fore.BLUE + f"\r{msg}{'.' * (i+1)}   ")
        sys.stdout.flush()
        time.sleep(0.3)
    print()

# --------------------------------------------------------