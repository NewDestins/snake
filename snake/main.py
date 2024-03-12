import time
import os
from map import *
from map import fruit


HEIGHT = 10
WIDTH = 10

def main():
    x,y = 3, 3
    harta = Map(height=HEIGHT, width=WIDTH)

    
    while True:
        os.system("cls")
        harta.update()
        time.sleep(0.1)


if __name__ == "__main__":
    main()