#!/usr/bin/env python3
# el modulo logging ayuda a depurar códiog en lugar de usar prints!!!
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
from elprint import elprint as elprinto

Numeros = [1,2,3,4,5,6,7,8,9,0]
Letras = ["a" ,"b", "c" ,"d","e","f","g","h","i","j","k"]
Mix = {}
Mix2 = {}
Mix3 = {}
Lix = []

for Numero , Letra in zip(Numeros, Letras):
    logging.info(f"las variable , {Numero}, {Letra}")
    Mix[Numero] = Letra
    logging.debug(f"el diccitionario , {Mix[Numero]}")
    Mix2[Numero] = str(Numero)+Letra
    logging.warning(f"el diccitionario 2, {Mix2[Numero]}")
    Mix3[Letra] = str(Numero)+Letra
    logging.error(f"el diccitionario 3, {Mix3[Letra]}")
    Lix.append(str(Numero)+Letra)
    logging.critical(f"la Lista, {Lix}")
    
elprinto(Mix)
elprinto(Lix)
elprinto(Mix2)
elprinto(Mix3)


def test():
    print("")
