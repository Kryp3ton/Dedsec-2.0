# Scanner di rete
La mia versione di netdiscover
- Mostra quali tipi di dispositivi sono presenti nella nostra rete

## Motivazioni per realizzarlo (Build futuri che lo richiedono)
- Risoluzione dell'indirizzo
    - Associare l'indirizzo IP e l'indirizzo IP locale di una rete
- Una volta che siamo nella stessa rete di altre persone, siamo potenzialmente vulnerabili
- Spoofing ARP
- MITM
-
Vedi le informazioni che arrivano attraverso la rete

## sfuggente
- Invia e ricevi pacchetti

## ARP
- Sta per protocollo di risoluzione degli indirizzi

## Come funziona
- Fai una richiesta ARP
- Trasmetti la richiesta
- Ottieni una risposta
- Gestisci quella risposta
- Compatibile con Python3

## Utilizzo
- python network_scanner.py -i (indirizzo IP qui)