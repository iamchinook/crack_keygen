from os import system, name

class bcolors:
    COLOR1 = '\033[93m'
    COLOR2 = '\033[0m'
    COLOR3 = '\033[91m'
    COLOR4 = '\033[92m'

def shell():
    print(bcolors.COLOR1 + "\n")
    print(" ██████╗██████╗  █████╗  ██████╗██╗  ██╗    ██╗  ██╗███████╗██╗   ██╗ ██████╗ ███████╗███╗   ██╗")
    print("██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝    ██║ ██╔╝██╔════╝╚██╗ ██╔╝██╔════╝ ██╔════╝████╗  ██║")
    print("██║     ██████╔╝███████║██║     █████╔╝     █████╔╝ █████╗   ╚████╔╝ ██║  ███╗█████╗  ██╔██╗ ██║")
    print("██║     ██╔══██╗██╔══██║██║     ██╔═██╗     ██╔═██╗ ██╔══╝    ╚██╔╝  ██║   ██║██╔══╝  ██║╚██╗██║")
    print("╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗    ██║  ██╗███████╗   ██║   ╚██████╔╝███████╗██║ ╚████║")
    print(" ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚══════╝╚═╝  ╚═══╝")
    print("                                                                         Nestor Alejandro Garcia")

def keygen():
    print(bcolors.COLOR2 + "\nEscriba 'exit' para salir\n")
    userID = input(bcolors.COLOR1 + "User ID: " + bcolors.COLOR2)
    if userID == "exit":
        clear()
    else:
        userID = int(userID)
        if userID >= 0 and userID <= 10000:
            num = userID * 786
            validCode = num * 17
            num = int(validCode)/12
            validCode = int(num + 1991)
            print(bcolors.COLOR1 + "Código: " + bcolors.COLOR2 + format(validCode) +  "\n")
            recode = input(bcolors.COLOR4 + "Desea verificar otro usuario? S/N: " + bcolors.COLOR2)
            if recode == "S" or recode == "s":
                clear()
                shell()
                keygen()
            else:
                clear()
        else:
            print(bcolors.COLOR3 + "\nError: el ID debe ser entre 0 y 10.000")
            keygen()

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

    

shell()
keygen()



                                                                                                