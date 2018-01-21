def Encode(code, publ):
    """Encoding code or words in RSA with the public key"""


    EncodedCode = [];

    e = publ[0];
    n = publ[1];



    for i in range(0, len(code)):

        ascii = ord(code[i]);

        if ascii > n:
            print("The two prime numbers are two small. Please consider revising them.")
            return []
        EncodedLetter = (ascii ** e)%n
        EncodedCode.append(EncodedLetter)




    return EncodedCode
