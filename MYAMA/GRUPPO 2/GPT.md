Ho completato il controllo sul commit `165659f` e sulla cartella definitiva `Progetto_Bernardi_DeSantis_Grande_Gugliotta_Luci`.

Verdetto: il pacchetto è tecnicamente integro e molto migliorato, ma non lo invierei ancora. Correggerei prima quattro incoerenze evidenti che il professore potrebbe notare durante l’esposizione.

## Da correggere assolutamente

### 1. Ruoli errati nella registrazione tramite invito

A pagina PDF 14, numerazione interna 9, il caso d’uso dice:

> il ruolo previsto dal codice di invito (operatore di sede AMA o amministratore di sede AMA)

Questo contraddice il resto della specifica:

* l’Amministratore di sede genera inviti per Autisti e Operatori;
* l’Amministratore generale genera inviti per Amministratori di sede;
* RF-02 comprende Autista, Operatore e Amministratore;
* RF-12 e RF-14 separano correttamente le due responsabilità.

La frase dovrebbe essere:

> il ruolo previsto dal codice di invito (autista AMA o operatore di sede AMA)

L’Amministratore di sede non dovrebbe poter creare un altro Amministratore di sede, perché quello è compito dell’Amministratore generale.

### 2. Errori semantici nei Use Case Diagram

Nei diagrammi ci sono alcune relazioni UML discutibili o incoerenti con il testo.

* Nel diagramma del Cittadino, pagina PDF 16, `Cittadino registrato` sembra specializzare sia `Utente di sistema` sia `Utente non registrato`. Un cittadino registrato non è contemporaneamente un utente non registrato: dovrebbe specializzare solamente l’utente autenticato/di sistema.
* Nel diagramma dell’Amministratore generale, pagina PDF 35, l’Amministratore generale specializza l’Amministratore di sede. Questo gli fa ereditare implicitamente tutte le operazioni di gestione della sede. Il testo, invece, gli assegna soltanto la gestione degli account degli Amministratori di sede. O si elimina la generalizzazione oppure si documentano esplicitamente i privilegi ereditati.
* Nel diagramma dell’Amministratore di sede, pagina PDF 29, compare `Gestisce la registrazione del personale AMA`, ma questo caso d’uso non è documentato nelle tabelle. La registrazione viene effettuata dall’utente non registrato tramite codice; l’amministratore genera soltanto il codice. Eliminerei questo use case dal diagramma.
* Nel primo diagramma, `Accetta dati sulla privacy` è già incluso nelle due registrazioni, ma appare anche una relazione `extend` verso `Si registra`: è ridondante e concettualmente sbagliata se l’accettazione è obbligatoria.
* Tutti i sei Use Case Diagram omettono il rettangolo che rappresenta il confine del sistema `MyAma`. Non rende il diagramma formalmente inutilizzabile, ma aggiungerlo renderebbe immediatamente chiaro cosa appartiene al sistema e cosa è un attore esterno.

### 3. Observer e Strategy non coincidono ancora con i diagrammi/VPP

Nel testo dell’Observer, pagina PDF 84, sono indicati:

* `registraObserver(obs)`
* `rimuoviObserver(obs)`
* `notificaObserver()`

Nel diagramma e nel progetto Visual Paradigm risultano invece:

* `attach(o)`
* `detach(o)`
* `notify()`

L’interfaccia `update(stato)` coincide, ma i metodi del Subject no. Bisogna scegliere una sola nomenclatura.

Per Strategy, pagina PDF 86, il testo presenta il Context come:

> `GestoreAssegnazione / PrenotazioneControl`

Nel diagramma e nel VPP esiste `GestoreAssegnazione`, mentre `PrenotazioneControl` non risulta presente. Toglierei `/ PrenotazioneControl`.

### 4. Class Diagram Refined illeggibile a dimensione normale

A pagina PDF 83, numerazione interna 78, il diagramma refined utilizza soltanto la parte superiore della pagina. Anche se ingrandibile digitalmente, su carta o durante una presentazione è praticamente illeggibile.

È il principale problema di impaginazione rimasto. Consiglio:

* pagina orizzontale dedicata;
* diagramma esteso quasi a tutta pagina;
* eventualmente suddivisione in una vista complessiva e due/tre ingrandimenti per Boundary, Control ed Entity.

Anche nei progetti degli altri gruppi i refined sono densi, ma generalmente sfruttano una superficie maggiore.

## Incoerenze contenutistiche importanti

### Glossario: “Utente di sistema”

Nell’introduzione è:

> qualsiasi entità esterna che interagisce con il software

Nel glossario è invece un:

> utente autenticato

Sono due concetti diversi. Suggerisco:

* `Utente del sistema`: attore generale;
* `Utente autenticato`: cittadino/personale/amministratore dopo il login.

Questo rende coerenti anche le generalizzazioni degli attori nei diagrammi.

### Funzionalità di reportistica

Il glossario afferma che l’Amministratore generale accede a report e statistiche aggregate. Tuttavia:

* non esiste un relativo caso d’uso;
* non esiste un requisito funzionale;
* la reportistica analitica avanzata è dichiarata out-of-scope.

Se non volete modellare la reportistica, eliminerei la frase dalla definizione dell’Amministratore generale.

### Requisiti funzionali non completamente tracciati

Sono documentati 28 casi d’uso, ma soltanto 15 requisiti funzionali. Mancano requisiti espliciti per diverse funzioni, tra cui:

* visualizzazione delle prenotazioni attive;
* storico delle prenotazioni;
* valutazione del servizio;
* visualizzazione dei dettagli;
* chiamata/consultazione del contatto;
* gestione delle associazioni sede–CAP.

Alcune possono essere considerate sottofunzioni di RF più generali, ma una breve matrice `Use Case → RF` o qualche RF aggiuntivo migliorerebbe molto la tracciabilità.

## Correzioni linguistiche residue

* Pagina 38: `i vincoli qualitativi e regole` → `i vincoli qualitativi e le regole`.
* RF-05: `in base al CAP o la zona` → `in base al CAP o alla zona`.
* Pagina 84:
  `Come successiva fase per fare una progettazione Object Oriented...`
  meglio:
  `Nella successiva fase della progettazione object-oriented vengono individuati i problemi strutturali risolvibili mediante design pattern consolidati.`
* `Dopo una attenta analisi` → `Dopo un’attenta analisi`.
* Uniformare maiuscole e terminologia: `Design Pattern/design pattern`, `Class Diagram/class diagram`, `Amministratore Generale/amministratore generale`.

I precedenti errori importanti — `<br>` visibili, `individure`, `Inseguito`, accenti mancanti e diagramma delle associazioni assente — risultano corretti.

## Pulizia del pacchetto definitivo

La cartella contiene 62 immagini, ma 10 non vengono utilizzate nel PDF:

* `act_autista_chiamare_cittadino.jpg`
* `act_autista_visualizzare_ritiri.jpg`
* `act_cittadino_chiamare_autista.jpg`
* `act_operatore_visualizzare_prenotazioni.jpg`
* `act_visualizzare_date_disponibili_conferimento.jpg`
* `act_visualizzare_date_fasce_ritiro.jpg`
* `act_visualizzare_prenotazioni_layout_orizzontale.jpg`
* `act_visualizzare_sedi_compatibili.jpg`
* `act_visualizzare_storico.jpg`
* `seq_SequenceGestireDisponibilitaVeicoli_v1_piatto.jpg`

Non sono dannose, ma la mail dice che la cartella contiene le immagini utilizzate. Conviene rimuoverle oppure scrivere che contiene “gli asset e le esportazioni dei diagrammi, comprese alcune viste aggiuntive”.

Nel VPP risultano inoltre diagrammi con nomi da bozza o duplicato:

* `Activity Diagram1`
* `VisualizzaPrenotazioniAttive`
* `SequenceGestireDisponibilitaVeicoli2`

Prima della consegna aprirei il VPP e verificherei se vadano eliminati o rinominati.

## Controlli superati

* PDF definitivo: 86 pagine A4, nessuna pagina completamente bianca.
* Nessuna immagine mancante o non leggibile.
* Nessun `<br>`, placeholder, testo AI o errore evidente di compilazione.
* Nessuna sovrapposizione grave nelle tabelle.
* 52 figure e 32 tabelle correttamente indicizzate.
* Font completamente incorporati.
* 141 collegamenti interni presenti.
* Metadati e autori corretti.
* Il PDF definitivo coincide con l’ultimo `main.pdf`.
* Il `.vpp` coincide con quello di sviluppo e supera `integrity_check`.
* Tutti i sei file PlantUML sono leggibili e strutturalmente completi.
* Archivio ZIP di prova: circa 12 MB e senza errori.
* La struttura generale è almeno pari, e per completezza spesso superiore, ai cinque progetti di riferimento.

Limite della verifica: non è disponibile Visual Paradigm per aprire graficamente il `.vpp`, né PlantUML per rigenerare i sei diagrammi. Ho comunque verificato l’integrità interna del database VPP, i nomi e i tipi dei 58 diagrammi, la struttura testuale dei `.puml` e tutte le immagini esportate.

Conclusione: dopo la correzione dei ruoli nel codice di invito, delle generalizzazioni nei Use Case Diagram, dei nomi nei Design Pattern e della leggibilità del Class Diagram Refined, per me il progetto è consegnabile. Gli altri punti sono rifiniture consigliate, ma quei quattro li sistemerei prima dell’invio.
