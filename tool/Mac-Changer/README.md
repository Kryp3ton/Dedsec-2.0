# CAMBIO MAC

Ci offre l'opportunità di cambiare il nostro indirizzo MAC. Questo verrà spiegato di seguito e nei commenti nel codice effettivo.

Puoi usare Pycharm come IDE ma io uso praticamente esclusivamente vim.

## Aggiornamento indirizzo IP e Mac:
- Digitando ifconfig si ottengono l'indirizzo mac e gli indirizzi IP delle interfacce disponibili.
- Le reti funzionano come tali:
- I dispositivi si connettono a un router che si connette a Internet che gestisce le richieste e le risposte
  - Se eseguiamo il ping di google.com è una richiesta e riceviamo la risposta dal router.
  - Un IP pubblico è ciò che utilizziamo per connetterci a Internet. Non vuoi che nessuno conosca il tuo indirizzo IP pubblico.
  -
Ogni dispositivo connesso al router ha lo stesso IP pubblico.
  - Hanno anche il proprio ID locale, specificando quale dispositivo sono.
 
## Perché vogliamo cambiare un indirizzo mac?
- Ogni interfaccia come una scheda wireless o una connessione via cavo ha un indirizzo mac. Essenzialmente un numero hadware.
- Non cambia se cambia dispositivo.
-
Modifica l'IP pubblico utilizzando una VPN.
- I router possono dire "Puoi connetterti se hai questo indirizzo mac"
- Quindi, se vogliamo connetterci a una rete, possiamo cambiare il nostro indirizzo mac in modo che accetterà.

## Modifica manuale
- Possiamo farlo manualmente attraverso i seguenti comandi:
  - ifconfig <interfaccia> giù
  - macchanger -m <mac> <interfaccia>
  -
ifconfig <interfaccia> su
  
- Ma non è abbastanza divertente, quindi sto creando il mio cambia Mac.

## Modo attuale per eseguire questo programma:
- Nel tipo di terminale:
  - python my_mac_changer.py --interface (interfaccia) --mac (indirizzo mac desiderato)
  - puoi cercare <> argomenti eseguendo ifconfig nella riga di comando
  -
Il programma esegue ifconfig e confronta l'indirizzo desiderato con il risultato finale e restituisce "Success!" o "Errore!" di conseguenza