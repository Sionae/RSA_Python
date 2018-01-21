from fractions import gcd

def CreateKey(p, q):
    """RSA Key creation. p and q must be the largest prime numbers possible
    Returns the public key (e, n) and the private key (d, n)"""

    n = p*q
    phi = (p-1)*(q-1)

    PGCD = 0
    e=max(p, q)
    c=0

    while PGCD != 1:

        while True:
            
            e+=1
            
            if p < e and q < e and e < phi:
                break
            

            if e > phi:
                disp('These two prime numbers do not work well with each other (calculation becomes too long).')
                return False, False

        PGCD = gcd(e, phi)

    publ = (e, n)

    d = 0

    while True:
        if e*d % phi == 1 and p < d and q < d and d < phi:
            break
        d += 1

    priv = (d, n)

    return publ, priv
