import colorama
import os

def wait_for_enter():
    input(colorama.Fore.YELLOW + "Tekan (enter) untuk melanjutkan...\n" + colorama.Style.RESET_ALL)
    os.system('cls' if os.name == 'nt' else 'clear')

def intro():
    colorama.init(autoreset=True)

    print(colorama.Fore.CYAN + "\n===============================================\n" + colorama.Style.RESET_ALL)
    print(colorama.Fore.GREEN + "Tools Analisis Sistem Informasi SIAKAD!\n" + colorama.Style.RESET_ALL)
    print(colorama.Fore.CYAN + "===============================================\n" + colorama.Style.RESET_ALL)
    print(colorama.Fore.CYAN + f"Analyst: SIAKAD" + colorama.Style.RESET_ALL)
    print(colorama.Fore.CYAN + f"Student: Muhamad Farhan (NIM: 22020057)" + colorama.Style.RESET_ALL)
    print(colorama.Fore.CYAN + f"Mata Kuliah: Analisis Sistem Informasi" + colorama.Style.RESET_ALL)
    print(colorama.Fore.CYAN + f"Dosen Pengajar: Eko Retnadi, M. Kom.\n" + colorama.Style.RESET_ALL)
    print(colorama.Fore.YELLOW + "Mari kita mulai analisis sistem Siakad!" + colorama.Style.RESET_ALL)