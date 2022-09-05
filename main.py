import os
import time

class color:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    OPERATIONAL = '\033[92m'
    DOWN = '\033[91m'
    INFO = '\033[93m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

clear()

while True:
    time.sleep(0.05)
    print(color.PURPLE + "___________          __________.__                " + color.ENDC)
    time.sleep(0.05)
    print(color.PURPLE + "\__    ___/______  __\______   \__| ____    ____  " + color.ENDC)
    time.sleep(0.05)
    print(color.BLUE + "  |    | /  _ \  \/  /|     ___/  |/    \  / ___\ " + color.ENDC)
    time.sleep(0.05)
    print(color.BLUE + "  |    |(  <_> >    < |    |   |  |   |  \/ /_/  >" + color.ENDC)
    time.sleep(0.05)
    print(color.CYAN + "  |____| \____/__/\_ \|____|   |__|___|  /\___  / " + color.ENDC)
    time.sleep(0.05)
    print(color.CYAN + "                    \/                 \//_____/  " + color.ENDC)
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print(color.INFO + " ┏━━━ " + color.UNDERLINE + "root" + color.ENDC + color.INFO + "$" + color.UNDERLINE + "toxping" + color.ENDC)
    time.sleep(0.05)
    hostname = input(color.INFO + " ┗━━━ Hostname (google.com): " + color.ENDC)
    clear()
    print("(" + color.INFO + "!" + color.ENDC +") " + "Pinging "+ color.INFO + hostname + color.ENDC +"...")
    response = os.system("ping -n 1 " + hostname)

    if response == 0:
        clear()
        status = "(" + color.OPERATIONAL + "✓" + color.ENDC +") " + hostname + " is"+ color.OPERATIONAL + " operational" + color.ENDC +"!"
    else:
        clear()
        status = "(" + color.DOWN + "✗" + color.ENDC +") " + hostname + " is"+ color.DOWN + " down" + color.ENDC +"..."
        
    print(status)
    time.sleep(5)
    clear()

input("")
