# encoding: utf-8

from Encode import *
from CreateKey import *
import sys

def Decode(EncodedBlock, priv):
    #Decode of encoded char blocs by the public key


    d = priv[0]
    n = priv[1]

    Mots = []


    for i in trange(0, len(EncodedBlock)):

        #We use (encoded letter ^ d)%n to find the initial ascii
        #We then convert the ascii into the initial character
        letter = EncodedBlock[i]
        a = (letter**d) % n

        Mots.append(chr(a))

    return "".join(Mots)
