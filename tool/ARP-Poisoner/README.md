# ARP-Spoofer
Utilizzato negli exploit MITM.

## Scopo e Background
Creato uno scanner di rete in precedenza per mostrarci gli indirizzi mac e l'indirizzo IP accoppiato. Possiamo usarlo per
manipolare i dati. Poiché non abbiamo bisogno di una richiesta per inviare una risposta, possiamo inviare una risposta. Il router
penserà che siamo il bersaglio e il bersaglio penserà che siamo il router.
## Inoltro IP
Ci saranno pacchetti che passeranno attraverso la nostra macchina perché è nel mezzo. La nostra macchina deve
inoltrare i pacchetti alla destinazione e al suo router.
    - root@kali:~# echo 1 > /proc/sys/net/ipv4/ip forward

## Strategia
- Ho utilizzato lo scanner di rete che ho creato in precedenza per trovare l'indirizzo MAC del target.
-
Per controllare la tabella ARP per vedere se ha funzionato:
    - root@kali:~# arp -a

## Utilizzo
python3 arpPosion.py -t ##.#.#.# -g ##.#.#.#