# Appunti-Logger

### Panoramica
Controlla cosa c'è negli appunti della macchina di destinazione ogni 5 secondi e se è nuovo, lo aggiunge a un registro. Questo registro viene inviato tramite e-mail all'indirizzo specificato ogni 5 minuti.

### Discussione
La maggior parte dei professionisti della sicurezza informatica ha familiarità con i keylogger.
Il concetto di base è registrare ogni sequenza di tasti sulla macchina su cui è in esecuzione entro una certa quantità di
tempo e poi esportando in qualche modo (il mio mi invia un'e-mail). L'altro giorno stavo pensando se fosse possibile estrapalare qualcos'altro allo stesso modo. I keylogger funzionano solo per
afferrare le credenziali se si digita la password a mano.
Dal momento che tutti usano i gestori di password in questi giorni (o almeno dovrebbero esserlo) sarebbe logico che se tu
potrebbe raggiungere gli appunti di qualcuno entro il tempo necessario affinché quegli appunti vengano cancellati dal gestore password, potresti ottenere la sua password. Controllando il
appunti per una nuova voce ogni cinque secondi e trattando tutto il resto come un normale keylogger, questo "strumento" prenderà quelle password. Ne afferrerà anche qualcuno
altro testo che aggiungi agli appunti mentre questo programma è in esecuzione. Questo è stato incredibilmente facile da realizzare e, combinato con un keylogger, copre la maggior parte
situazioni in cui qualcuno starebbe inserendo le credenziali. Potresti anche usare uno sniffer...

### Utilizzo
Basta clonare, spostare l'e-mail e la password exfil nel punto in cui desideri che venga inviata e, presto, ti stai sorvegliando.
In alternativa, puoi modificare il tempo di controllo (5 secondi) e la frequenza delle e-mail (ogni 5 minuti) in base alle tue esigenze.
Inoltre, puoi commentare la chiamata alla funzione di invio e-mail e stamparla sulla console.

Divertiti.