# Fuzzer
Ho realizzato questo fuzzer circa 2 anni fa e sono in procinto di migliorarlo.

## Descrizione e risultati
La caccia ai bug è un compito comune a tutti i programmatori, ma soprattutto a quelli preoccupati per la sicurezza informatica. Sebbene i bug possano essere una seccatura per gli utenti tipici (ad esempio, le persone si infastidiscono quando i programmi si bloccano o non si comportano come previsto),
i bug sono una risorsa vitale per gli attori malintenzionati. Trovare i bug in un programma è il primo passo per isolare i bug sfruttabili che possono essere sfruttati per attacchi contro quel programma.

Un fuzzer è un programma che cerca di trovare bug in altri programmi. Questo fuzzer prenderà due input: (1) una specifica del programma in formato XML,
e (2) il percorso del programma di destinazione. Quindi esegue ripetutamente il programma di destinazione con diversi argomenti della riga di comando nel tentativo di causare l'arresto anomalo del programma di destinazione. Riporta quali input della riga di comando hanno causato l'arresto anomalo del programma di destinazione. Nel mondo reale,
lo sviluppatore del programma di destinazione utilizzerà quindi queste informazioni per trovare e correggere i bug nel proprio programma.

Ciascuno di questi risultati finali è descritto in maggior dettaglio di seguito.

## Sfondo
Esistono molti strumenti e framework che aiutano i programmatori a trovare i bug. Alcuni, come gli unit test, sono sviluppati dal programmatore, inclusi nel codice sorgente,
e sono strettamente integrati con un determinato programma. Questo progetto è stata un'opportunità per attingere a quelle capacità di sviluppo del test.

Altri strumenti di ricerca dei bug sono più generali e sono progettati per aiutare a trovare i bug in qualsiasi programma. Il test fuzz, o semplicemente fuzzing, è una tecnica black-box per tentare di trovare bug nei programmi.
Questa tecnica è spesso implementata in un programma chiamato fuzzer. L'obiettivo di un fuzzer è eseguire ripetutamente un programma target e tentare di bloccarlo fornendogli una varietà di strani input. In altre parole, l'obiettivo del fuzzer è trovare bug nel target, dove il programmatore non è riuscito a gestire corner-
casi nel codice di gestione dell'input. Il fuzzing è una tecnica black-box perché non dipende dal codice sorgente del target. Qualsiasi programma che accetta input esterni (e quasi tutti lo fanno) può essere sfocato.

## Esempio motivante
Immaginiamo che qualcuno abbia scritto un'app calcolatrice da riga di comando molto semplice. Il programma di calcolo funziona in questo modo:

$ ./calc
Utilizzo: $ ./calc [numero] [operazione (+, -, *, /)] [numero]
$ ./calcolo 1 + 1
2
$ ./calcolo 10 / 5
2

calc accetta esattamente tre argomenti della riga di comando: un numero, una stringa che indica una semplice operazione matematica e un altro numero.

Gli esempi sopra dimostrano che calc funziona come previsto...
quando gli input della riga di comando sono conformi alla specifica del programma. Tuttavia, prenditi un momento e specula su tutti i modi in cui calc potrebbe arrestarsi in modo anomalo se fosse fornito con input da riga di comando imprevisti o accuratamente realizzati. Pensa a tutti i casi d'angolo che lo sviluppatore di calc potrebbe aver dimenticato di gestire nel proprio codice. Per esempio:
Cosa succede se l'utente fornisce meno di tre argomenti? E se fornissero più di tre argomenti?
    Cosa succede se l'utente non inserisce un numero per l'argomento uno o tre?
    Cosa succede se l'utente non inserisce "+", "-", "*" o "/" per l'argomento due?
    Cosa succede se l'utente inserisce un numero negativo?
    Cosa succede se l'utente immette davvero,
numero davvero grande?
    Cosa succede se l'utente immette zero per il terzo argomento quando l'argomento due è impostato su divisione?

L'idea alla base di un fuzzer è che eseguirà automaticamente un programma di destinazione, come calc, più e più volte con diverse combinazioni di input della riga di comando, per provare a attivare i bug ed esporli, in modo che possano essere corretti.
## Specifiche e design di Fuzzer
Un programma a riga di comando denominato fuzzer che esegue il controllo basato su modello di altri programmi a riga di comando.

$ ./fuzzer [percorso del file di configurazione XML] [percorso del programma di destinazione]

Il programma fuzzer accetta esattamente due argomenti della riga di comando, ognuno dei quali è un percorso di file. Il primo percorso punterà a un XML-
file di configurazione formattato che descrive il modello per il test fuzz del programma di destinazione. Il secondo percorso punta al programma di destinazione stesso. Utilizza il modello fornito per costruire una varietà di argomenti della riga di comando per il programma di destinazione ed eseguirà ripetutamente il programma di destinazione per vedere se si arresta in modo anomalo.
I fuzzer emettono quindi tutte le righe di comando che hanno causato l'arresto anomalo del programma di destinazione. Tornando al nostro esempio di calcolo, il fuzzer potrebbe generare il seguente output:

$ ./fuzzer calc_model.xml calc
./calc A B C
./calc 1 A B
./calc 1 / 0

Ciascuno di questi insiemi di argomenti della riga di comando provoca l'arresto anomalo di calc. Ad esempio, ./calc A B C e .
/calc 1 A B provoca l'arresto anomalo perché uno o più argomenti che dovrebbero essere numeri non lo sono.

$ ./calc A B C
Tracciamento (ultima chiamata più recente):
    File "./calc", riga 9, in <modulo>
    n1 = int(sys.argv[1])
ValueError: letterale non valido per int() con base 10: 'A'
Nota che fuzzer ha provato a eseguire calc con molti altri set di argomenti della riga di comando che non hanno provocato arresti anomali, quindi non sono stati stampati. Alcune altre righe di comando di esempio che potrebbe aver provato includono:

    ./calc A, non si arresta in modo anomalo perché il programma si assicura che vengano forniti esattamente tre argomenti della riga di comando
    ./calc A B C D,
non si blocca per lo stesso motivo di cui sopra
    ./calc 1 A 1, non si arresta in modo anomalo o stampa nulla, perché l'argomento due non è un operatore matematico valido

## Specifiche del modello
Il mio programma fuzzer è in grado di testare un'ampia varietà di programmi a riga di comando.

È qui che entra in gioco il modello. Il fuzzer legge un modello, specificato in XML,
che descrive gli argomenti della riga di comando del programma di destinazione. Il formato XML generale dei modelli è il seguente:

<specifica>
    <opzioni>
        <opzione>
            <name>Nome dell'argomento opzionale</name>
            <type>Tipo dell'argomento opzionale</type>
        </opzione>
        ...altre opzioni...
    </opzioni>
    <posizionale>
<arg>
            <type>Tipo dell'argomento posizionale</type>
        </arg>
        ...altri argomenti posizionali...
    </posizionale>
</spec>

La specifica del modello è divisa in due sezioni: argomenti facoltativi e argomenti posizionali. Gli argomenti facoltativi sono argomenti della riga di comando che in genere sono preceduti da - o --,
e come suggerisce il loro nome, sono facoltativi. Il <nome> di un argomento facoltativo è letteralmente il suo nome sulla riga di comando. Gli argomenti posizionali sono gli argomenti della riga di comando che devono essere passati al programma di destinazione, in un ordine specifico, affinché funzioni. Sia gli argomenti facoltativi che posizionali hanno un <tipo>,
che è il tipo di dati di quell'argomento. Ai fini di questo progetto, gli unici tipi di cui mi sono occupato sono interi, stringhe e null, che è un caso speciale per argomenti opzionali.

Tornando al nostro esempio di calcolo, questo programma accetta esattamente tre argomenti posizionali della riga di comando. La specifica del modello per calc sarebbe:

<specifica>
<posizionale>
        <arg>
            <tipo>numero intero</tipo>
        </arg>
        <arg>
            <tipo>stringa</tipo>
        </arg>
        <arg>
            <tipo>numero intero</tipo>
        </arg>
    </posizionale>
</spec>

Questo modello cattura la nostra comprensione di come dovrebbe funzionare calc: richiede tre argomenti, il primo e il terzo sono numeri interi
, e il secondo è una stringa.

Ecco un esempio leggermente più complesso:

$ ./compra cibo
utilizzo: buy-food [-h] [--biologico] [--quantità QUANTITÀ] [--store NEGOZIO] area alimentare
compra-cibo: errore: sono richiesti i seguenti argomenti: cibo, zona
$ ./compra-cibo -h
utilizzo: buy-food [-h] [--biologico] [--quantità QUANTITÀ] [--store NEGOZIO] area alimentare
Acquista cibo online digitando quello che vuoi e la città a cui consegnarlo.
Attualmente supporta solo consegne nell'area di Boston.

argomenti posizionali:
  cibo Il nome del cibo che desideri
  area Il nome dell'area in cui effettuare la consegna

argomenti facoltativi:
  -h, --help mostra questo messaggio di aiuto ed esce
  -o, --
biologico Assicurati che il cibo sia biologico. Predefinito=Falso
  -q QUANTITÀ, --quantità QUANTITÀ
                        Quanti pezzi di cibo vuoi? Predefinito=1
  -s NEGOZIO, --store NEGOZIO
                        Consegna dal negozio indicato. Predefinito=Commerciante Joes
$ ./compra-cibo taco roslindale
Ottimo, stiamo consegnando il tuo taco a roslindale!
$.
/buy-food --biologico "succo di vongole" "harvard square"
Ottimo, stiamo consegnando il tuo succo di vongole biologico ad Harvard Square!

Questo programma ha tre argomenti opzionali della riga di comando (quattro se si conta --help, ma non ci interessa) e due argomenti posizionali obbligatori. La specifica XML per buy-food è:

<specifica>
    <opzioni>
        <opzione>
<name>--organico</name>
            <tipo>null</tipo>
        </opzione>
        <opzione>
            <name>--quantità</name>
            <tipo>numero intero</tipo>
        </opzione>
        <opzione>
            <name>--negozio</name>
            <tipo>stringa</tipo>
        </opzione>
    </opzioni>
    <posizionale>
        <arg>
<tipo>stringa</tipo>
        </arg>
        <arg>
            <tipo>stringa</tipo>
        </arg>
    </posizionale>
</spec>

I tipi di dati di --quantity e --store hanno un senso intuitivo. --organic ha un tipo di dati "null" perché non accetta dati aggiuntivi sulla riga di comando.
Questo tipo di argomento della riga di comando viene spesso definito flag e in genere attiva o disattiva alcune funzionalità del programma (in questo caso, il desiderio di cibo biologico).