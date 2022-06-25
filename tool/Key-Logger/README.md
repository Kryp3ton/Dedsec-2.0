# Registratore di chiavi
Realizzare uno strumento chiave di registrazione mentre si segue il corso di hacking etico.

!!!Questo keylogger funziona se lo scarichi e tutte le librerie necessarie, tuttavia, è molto semplice comprimerlo in un file .exe. Voglio stare fuori di prigione, quindi non l'ho fatto.!!!
Le seguenti informazioni saranno le istruzioni su come impostare lo spazio di lavoro necessario per realizzarlo da soli, nonché su come funziona e altri concetti:
- Questo è per Windows. Dobbiamo installare python.
  - Google e scarica Sublime Text.
  - Correre
  - Modifica le impostazioni a tuo piacimento
  - stampa "ciao" e salva come file .py.
Ora puoi vedere come appare un file python.
  - Installa python2 e python3. (per Windows)
  - Nella stessa cartella in cui hai le versioni python scaricate, prova a eseguire il tuo programma Hello World.
- Ora possiamo iniziare a creare il keylogger.
  - In pycharm crea un nuovo progetto. (o usa semplicemente vim per tutto questo specificando che si tratta di un file .
py ad eccezione del file di output .txt)
  - Crea un nuovo file in pyinput e chiamalo il tuo key logger
- Abbiamo bisogno di un modulo che ci aiuti a prendere le chiavi dalla macchina di destinazione.
  - Apri un terminale.
  - Digitare quanto segue: pip install pyinput.
  - Considera anche l'installazione di pip3.
  - Ora abbiamo le nostre librerie e prerequisiti.
  -
importa la libreria nel tuo file principale.
- Il resto delle istruzioni verrà commentato nel keylogger stesso. Se sono necessarie informazioni eccessive, sarà scritto di seguito:
  - Nota: se la macchina di destinazione è impostata in una lingua diversa, i simboli avranno un aspetto diverso. Gestiamo questo problema con la prova: usando "utf-8"
  - Per fermarlo,
nel tipo di terminale: killall python
  - A causa del modo in cui funzionano le librerie, questo sarà in python2