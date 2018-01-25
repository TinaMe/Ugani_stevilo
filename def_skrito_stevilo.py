# -*- coding: utf-8 -*-

import random

def main():
    print "Pozdravljen v igrici Ugani skrito število!"

    secret = random.randint(1, 20)

    while True:
        try:
            guess = int(raw_input("Ugani skrito število (med 1 in 20): "))
        except Exception:
            print "Nepravilen vnos!"
            continue
        if guess == secret:
            print "Čestitamo! Uganil si skrito število!"
            break
        else:
            print "Žal si uganil napačno število. Poskusi še enkrat!"

    print "Adijo!"




if __name__ == '__main__':
    main()