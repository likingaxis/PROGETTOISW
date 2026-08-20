# 📄 Specifica di Progetto: Campionato di Pesca Sportiva

> **Autori**: Matteo Cipolletta, Davide Noce, Franco Salvucci, Christian Sfeir  
> **Pagine totali**: 76  
> **Trascrizione**: Estratta dal documento originale per consultazione testuale diretta.

---


<!-- Pagina PDF 1 -->
## 📑 Pagina 1

Cipolletta Matteo
0306676
Noce Davide
0306904
Salvucci Franco
0306609
Sfeir Christian
0284535


---

<!-- Pagina PDF 2 -->
## 📑 Pagina 2

2


---

<!-- Pagina PDF 3 -->
## 📑 Pagina 3

Indice
1 Introduzione 2
2 Glossario 3
3 User Requirements Definition 4
3.1 Use Case Arbitro . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.1.1 Diagramma . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.1.2 Documentazione . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.2 Use Case Organizzatore del Campionato . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
3.2.1 Diagramma . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
3.2.2 Documentazione . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
3.3 Use Case Giudice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.3.1 Diagramma . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.3.2 Documentazione . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.4 Use Case Partecipante . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.4.1 Diagramma . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.4.2 Documentazione . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
3.5 Use Case Utente . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.5.1 Diagramma . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.5.2 Documentazione . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
4 System Requirements 16
4.1 Requisiti Funzionali . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
4.2 Requisiti Non Funzionali . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
4.3 Requisiti di Dominio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
5 System Architectural Models 20
5.1 Activity Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
5.1.1 Activity Diagrams Arbitro . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
5.1.2 Activity Diagrams Organizzatore del Campionato . . . . . . . . . . . . . . . . . . . . . . 23
5.1.3 Activity Diagrams Giudice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
5.1.4 Activity Diagrams Partecipante . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
5.1.5 Activity Diagrams Utente . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
5.2 Sequence Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
5.2.1 Sequence Diagrams Arbitro . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
5.2.2 Sequence Diagrams Organizzatore del Campionato . . . . . . . . . . . . . . . . . . . . . . 38
5.2.3 Sequence Diagrams Giudice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.2.4 Sequence Diagrams Partecipante . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
5.2.5 Sequence Diagrams Utente . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
5.3 Class Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
5.3.1 Class Diagrams Unrefined . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
5.3.2 Class Diagrams Refined . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
6 Design Pattern 52
6.1 Observer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
6.2 Decorator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 53
6.3 Singleton . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
6.4 Strategy . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
1


---

<!-- Pagina PDF 4 -->
## 📑 Pagina 4

1 Introduzione
Campionato di Pesca Sportiva
Il software ` e progettato per facilitare la gestione di un campionato di pesca, organizzato da un comitato ter-
ritoriale, automatizzando le attivit` a principali per ridurre il rischio di errori e velocizzare l’organizzazione e il
monitoraggio delle gare. Il campionato si svolge in periodi specifici dell’anno, con gare che vedono la parteci-
pazione di diversi attori, ciascuno con un ruolo preciso. I partecipanti al campionato, ossia i pescatori, devono
confermare la propria disponibilit` a alle gare, cos` ı che l’organizzatore possa reagire tempestivamente in caso
di assenze. Durante le gare, il rispetto delle regole ` e monitorato dagli arbitri, che valutano la validit` a delle
catture, inseriscono i risultati a fine evento e completano il referto della gara entro il weekend. Tali risultati,
pubblicati automaticamente online, aggiornano in tempo reale la classifica del campionato. Il responsabile di
gara ` e deputato alla scelta degli arbitri ad ogni gara. Inoltre ogni arbitro pu` o dichiararsi disponibile tramite
il portale e la gestione delle disponibilit` a viene gestita dal responsabile di gara. L’organizzatore supervisiona
la gestione generale del campionato e coordina le attivit` a, mentre il giudice ha il compito di convalidare ogni
gara, previa ricezione del referto e pu` o, se necessario, annullarla o richiedere una rischedulazione. Il giudice
pu` o inoltre emettere sanzioni per eventuali infrazioni, assegnando multe o penalit` a ai pescatori. Anche data,
ora e luogo delle gare possono essere modificati per necessit` a organizzative o su richiesta preventiva del giudice.
Attraverso notifiche sull’applicazione, il sistema comunica con tutti gli attori coinvolti, assicurando un flusso
continuo di informazioni. Ogni tipo di comunicazione (ad es.: arbitro rifiuta la partecipazione ad una deter-
minata gara, il responsabile di gara viene notificato tramite app.) avviene tramite notifica via SMS, e-mail e
portale dell’applicazione. Gli utenti non registrati possono consultare calendari, risultati e la classifica, mentre
gli utenti registrati hanno accesso a funzioni avanzate come seguire competizioni e partecipanti di interesse,
aggiungerli ai preferiti e visualizzare sanzioni, multe. Qualunque utente, che sia registrato o no, pu` o seguire le
varie dirette streaming delle gare.
2


---

<!-- Pagina PDF 5 -->
## 📑 Pagina 5

2 Glossario
Termine Descrizione
Arbitro; Ufficiale di gara Dirige le competizioni sportive garantendo il rispetto dei regola-
menti. I campionati di pesca prevedono uno o pi` u arbitri, talvolta
per questioni di organico e costi ne viene designato solo uno.
Modulo Documento associato ad una partita, contenente il referto, il rap-
porto ed il punteggio finale.
Referto Documento ufficiale avente valenza legale. Riporta la cronologia
degli eventi punto per punto. L’elenco dei partecipanti viene con-
segnato agli arbitri, mentre il referto viene compilato dallo stesso
arbitro, che poi caricher` a sul portale. Viene visionato dal giudice e
gran parte delle sue decisioni passano attraverso esso.
Rapporto Documento compilato dall’arbitro con osservazioni sullo svolgimen-
to della partita.
Responsabile di gara Persona appositamente incaricata dall’organizzatore del campiona-
to per associare gli arbitri alle partite. Conosce dettagliatamente
l’organico in maniera tale da poter fare abbinamenti ponderati.
Partecipante Pescatore che intende partecipare al campionato.
Gara; Partita; Incontro Evento nel quale due partecipanti competono per la vittoria.
Giudice Convalida le partite e sulla base di quanto scritto nel referto, ed
eventualmente dopo aver sentito le parti coinvolte, commina san-
zioni ai partecipanti.
Organizzatore del campionato Crea, Organizza e Gestisce i vari campionati.
Sanzione Multa, squalifica o sospensione per i partecipanti.
Incontro schedulato Incontro per la quale ` e stata assegnata data, orario ed un campo
di gioco. L’ incontro pu` o essere rischedulato.
Utente; Utente Non Registrato Curioso o appassionato che utilizza l’applicazione o visualizza il
sito.
Utente Registrato Utente che ha creato il suo account, ha alcune funzionalit` a aggiun-
tive di personalizzazione di preferenze.
Utente Speciale Utente a cui vengono assegnati privilegi speciali da parte dell’Orga-
nizzatore del campionato.(Ad esempio Aribtro,Partecipante,Etc...)
3


---

<!-- Pagina PDF 6 -->
## 📑 Pagina 6

3 User Requirements Definition
3.1 Use Case Arbitro
3.1.1 Diagramma
3.1.2 Documentazione
Use case Inserisce risultato incontro
Descrizione Passo Azione
1 L’arbitro, dalla pagina dedicata, seleziona l’ incontro di cui vuole
inserire il risultato.
2 Il sistema aggiorna risultato e classifica.
3 Il sistema notifica il risultato agli utenti registrati che hanno sca-
ricato l’applicazione e a quanti hanno accettato la ricezione di ag-
giornamenti tramite email e/o SMS dei partecipanti (pescatori) da
loro selezionati nelle preferenze.
Attori Arbitro, Utente Registrato.
Precondizioni L’arbitro ha effettuato il login ed ha completato l’arbitraggio della partita della
quale vuole inserire il risultato.
Scenario principale L’arbitro inserisce il risultato della partita.
Scenari alternativi Se l’arbitro sbaglia l’inserimento del risultato, cancella il risultato errato
appena inserito, e lo reinserisce nello stesso modo.
Post-condizioni L’arbitro pu` o continuare la compilazione del rapporto.
4


---

<!-- Pagina PDF 7 -->
## 📑 Pagina 7

Use case Compila il rapporto e carica il referto della giornata
Descrizione Passo Azione
1 L’arbitro, dalla pagina dedicata, seleziona l’ incontro di cui vuole
inserire il rapporto e caricare il referto.
2 L’arbitro compila il rapporto.
3 L’arbitro carica la scansione del referto.
4 L’ incontro “completato” appare tra quelli visionabili dal giudice.
Attori Arbitro, Giudice.
Precondizioni L’arbitro ha inserito il risultato dell’ incontro di cui vuole inserire
il rapporto e caricare il referto.
Scenario principale L’arbitro inserisce il rapporto dell’ incontro e carica il referto.
Scenari alternativi Se l’arbitro sbaglia l’inserimento del rapporto pu` o correggerlo fino a quando
non ` e stato visionato dal giudice. Se sbaglia a caricare i file pu` o rimuoverli e
inserirli nuovamente allo stesso modo. Nell’eventualit` a di tali scenari di errore,
se le modifiche non vengono apportate entro 24 ore dall’inserimento dei dati,
ci` o verr` a automaticamente notificato.
Post-condizioni Il giudice pu` o visualizzare il rapporto e il referto.
Use case Giorni disponibili per arbitrare
Descrizione Passo Azione
1 L’arbitro, dalla pagina dedicata, seleziona i giorni in cui ` e
disponibile.
Attori Arbitro.
Precondizioni L’arbitro ha effettuato l’accesso.
Scenario principale L’arbitro inserisce le sue disponibilit` a.
Scenari alternativi L’arbitro pu` o in un qualsiasi momento modificare la sua disponibilit` a.
Post-condizioni Il responsabile di gara potr` a, dalla sua area dedicata, sapere chi poter designare
e chi no.
Use case Conferma/Rifiuta arbitraggio proposto.
Descrizione Passo Azione
1 L’arbitro dalla pagina dedicata accetta o rifiuta l’ incontro
assegnato tramite portale o App.
2 Viene aggiornato lo stato degli incontri a livello di assegnazione
arbitraggi per una visualizzione da parte del responsabile di gara.
I rifiuti di disponibilit` a generano una notifica con email, che verr` a
visionata nell’ apposita pagina per il responsabile di gara.
Attori Arbitro, Responsabile di Gara
Precondizioni L’arbitro ha ricevuto una designazione per l’arbitraggio proposto.
Scenario principale L’arbitro accetta o rifiuta l’ incontro, l’accettazione compare nel portale del
responsabile di gara anche tramite notifica, il rifiuto fa arrivare solo la notifica.
Scenari alternativi L’arbitro impiega troppo tempo ad accettare o rifiutare, il responsabile
sollecita.
Post-condizioni Tutti gli incontri devono avere arbitri assegnati.
5


---

<!-- Pagina PDF 8 -->
## 📑 Pagina 8

Use case Assegna arbitraggi
Descrizione Passo Azione
1 Il responsabile di gara sceglie l’ incontro alla quale designare.
2 Il responsabile di gara sceglie l’arbitro a cui assegnare l’ incontro
tra quelli disponibili.
3 Il sistema notifica all’arbitro l’ incontro ricevuto tramite email, SMS
e notifica sull’App.
Attori Responsabile di Gara, Arbitro
Precondizioni Il responsabile di gara ha degli incontri da assegnare.
Scenario principale Il responsabile di gara sceglie incontri e relativi arbitri.
Scenari alternativi Particolari incontri possono richiedere di designare pi` u arbitri.
Post-condizioni Tutti gli arbitri scelti hanno la possibilit` a di gestire gli incontri a loro assegnate.
3.2 Use Case Organizzatore del Campionato
3.2.1 Diagramma
6


---

<!-- Pagina PDF 9 -->
## 📑 Pagina 9

3.2.2 Documentazione
Use case Crea Campionato
Descrizione Passo Azione
1 L’organizzatore del campionato crea il campionato assegnandogli
un nome.
2 L’organizzatore del campionato inserisce i partecipanti.
Attori Organizzatore del campionato
Precondizioni Deve essere creato un nuovo campionato.
Scenario principale L’organizzatore vuole inserire tutto ci` o che riguarda il nuovo campionato.
Scenari alternativi L’organizzatore assegna al campionato un nome e un’edizione gi` a utilizzati per
un altro campionato creato precedentemente. Il sistema quindi restituisce un
messaggio di errore.
Post-condizioni Campionato creato, ` e possibile creare e schedulare partite per lo stesso.
Use case Crea incontri
Descrizione Passo Azione
1 L’organizzatore del campionato visualizza i partecipanti del cam-
pionato per i quali vuole creare l’incontro.
2 L’organizzatore del campionato crea l’incontro inserendo i parteci-
panti.
Attori Organizzatore del campionato
Precondizioni L’organizzatore del campionato vuole creare un’incontro per il campionato
desiderato.
Scenario principale L’organizzatore del campionato crea un incontro non schedulato.
Scenari alternativi Esiste gi` a un incontro non schedulato con gli stessi partecipanti e nella stessa
data, il sistema manda un avviso di schedulare il primo incontro non schedulato
gi` a esistente. L’organizzatore schedula il primo incontro gi` a esistente e cancella
la schedulazione del secondo incontro
Post-condizioni Campionato creato, ` e possibile creare e schedulare partite per lo stesso.
Use case Elimina account utente speciale
Descrizione Passo Azione
1 Seleziona la tipologia di utente da eliminare.
2 Seleziona l’utente da eliminare.
3 Conferma l’eliminazione.
4 L’utente in questione riceve una mail di notifica.
Attori Organizzatore del Campionato, Utente Speciale (Arbitro, Partecipante, Giu-
dice)
Precondizioni Un Utente Speciale ha chiesto l’eliminazione del suo account.
Scenario principale Deve essere eliminato l’account di un utente con dei diritti particolari.
Scenari alternativi //
Post-condizioni E’ stato eliminato correttamente l’account di un utente con particolari privi-
legi, ` e arrivata la notifica via mail all’interessato.
7


---

<!-- Pagina PDF 10 -->
## 📑 Pagina 10

Use case Crea account utente speciale
Descrizione Passo Azione
1 Inserisci la tipologia di account da creare.
2 Inserisci i dati dell’utente da creare.
3 L’utente in questione riceve una mail di notifica.
Attori Organizzatore del Campionato, Utente Speciale (Arbitro, Partecipante, Giu-
dice).
Precondizioni Un utente speciale ha chiesto la creazione di un account.
Scenario principale Deve essere creato l’account di un utente con dei diritti particolari.
Scenari alternativi Viene creato l’account richiesto senza i privilegi corretti. In questo
caso l’organizzatore elimina l’account e lo ricrea in modo corretto.
Post-condizioni E’ stato creato correttamente l’account di un utente con particolari privilegi,
` e arrivata la notifica via mail all’interessato.
Use case Visualizza incontri da schedulare
Descrizione Passo Azione
1 L’Organizzatore visiona quali incontri devono essere schedulati.
Attori Organizzatore del Campionato
Precondizioni L’Organizzatore del Campionato necessita di visualizzare le partite da sche-
dulare.
Scenario principale L’Organizzatore visualizza le partite da schedulare.
Scenari alternativi //
Post-condizioni L’Organizzatore pu` o schedulare gli incontri non programmati. Eventualmente
schedula gli incontri da rigiocare.
Use case Schedula Incontri
Descrizione Passo Azione
1 L’Organizzatore del Campionato inserisce data e orario in cui far
giocare l’incontro da schedulare.
Attori L’Organizzatore del Campionato
Precondizioni L’Organizzatore del Campionato vuole schedulare un’ incontro ancora non
programmato o da rigiocare sotto richiesta del giudice.
Scenario principale L’Organizzatore del Campionato schedula un incontro non ancora program-
mato.
Scenari alternativi L’ incontro era stato gi` a giocato, la procedura sar` a identica a quella di un’
incontro non programmata.
Post-condizioni L’ incontro apparir` a correttamente schedulata
8


---

<!-- Pagina PDF 11 -->
## 📑 Pagina 11

3.3 Use Case Giudice
3.3.1 Diagramma
3.3.2 Documentazione
Use case Richiede rapporto compilato
Descrizione Passo Azione
1 Il giudice seleziona la partita di cui vuole leggere il rapporto tra
quelle pronte.
2 Il giudice seleziona e consulta il rapporto.
Attori Giudice, Arbitro
Precondizioni Il Giudice, per convalidare le partite, ha bisogno di leggere il rapporto e visua-
lizzare il referto inviato dall’arbitro.
Scenario principale Il giudice sceglie la partita in esame.
Scenari alternativi Il rapporto ed il referto potrebbero non essere stati ancora caricati, dovr` a
aspettare.
Post-condizioni Il giudice ` e pronto a dare un giudizio sulla partita.
9


---

<!-- Pagina PDF 12 -->
## 📑 Pagina 12

Use case Giudica l’incontro
Descrizione Passo Azione
1 Il giudice convalida o meno la partita sulla base del referto e del
rapporto inviati dall’arbitro.
2 Sulla base del referto e del rapporto pu` o decretare sanzioni.
Attori Giudice, Arbitro, Organizzatore del campionato.
Precondizioni Il giudice ha visionato il rapporto ed il referto dell’arbitro sull’in-
contro in esame.
Scenario principale Il giudice giudica positivamente o negativamente l’incontro.
Scenari alternativi Il giudice decide per la ripetizione della partita, sar` a inviata una notifica al-
l’organizzatore del campionato che dovr` a rischedulare la partita in nuova data
e con un arbitro possibilmente differente.
Post-condizioni Il risultato della partita apparir` a come ufficializzato.
Use case Assegna le sanzioni
Descrizione Passo Azione
1 Il giudice, a seguito del processo di giudizio della partita, pu` o de-
cretare sanzioni ai partecipanti.
Attori Giudice
Precondizioni Il giudice ha visionato il rapporto ed il referto, di conseguenza giudica la par-
tita.
Scenario principale Il giudice giudica e decreta eventuali sanzioni.
Scenari alternativi Il giudice potrebbe in taluni casi assegnare delle sanzioni a prescindere dalle
partite, determinate da eventuali comportamenti scorretti o infrazioni di rego-
le.
Post-condizioni Ogni partecipante potr` a visionare le sanzioni ricevute.
Use case Richiede la rischedulazione dell’incontro
Descrizione Passo Azione
1 Il giudice, a seguito del processo di giudizio della partita, decide
che la partita deve essere rischedulata.
2 Il giudice non convalida il modulo.
3 La richiesta di rischedulazione della partita arriva all’organizzatore
del campionato, il quale dovr` a a rischedularla.
Attori Giudice, Organizzatore del campionato
Precondizioni Il giudice ha visionato il rapporto e i documenti in suo possesso,
sta giudicando la partita.
Scenario principale Il giudice decide che la partita deve essere rischedulata.
Scenari alternativi Per motivi esterni alla propria volont` a, il giudice potrebbe comunque decidere
che una partita ”dubbia” venga annullata, ma non rischedulata.
Post-condizioni L’organizzatore del campionato, tramite il suo portale utente, sar` a in grado
di visionare la nuova partita da rischedulare e svolgere tutte le operazioni del
caso.
10


---

<!-- Pagina PDF 13 -->
## 📑 Pagina 13

3.4 Use Case Partecipante
3.4.1 Diagramma
3.4.2 Documentazione
Use case Visualizzazione classifica
Descrizione Passo Azione
1 Il partecipante visualizza la classifica in tempo reale.
2 Il partecipante pu` o applicare filtri ai dati visualizzati.
Attori Partecipante
Precondizioni Il partecipante vuole visionare la classifica.
Scenario principale Il partecipante visualizza la classifica.
Scenari alternativi //
Post-condizioni La classifica viene visonata sull’App.
Use case Iscrizione al campionato
Descrizione Passo Azione
1 Il partecipante si iscrive al campionato.
Attori Partecipante
Precondizioni Il partecipante vuole iscriversi al campionato.
Scenario principale Il partecipante si iscrive al campionato
Scenari alternativi //
Post-condizioni Il partecipante viene iscritto regolarmente al campionato.
Use case Ritiro dal campionato
Descrizione Passo Azione
1 Il partecipante si ritira dal campionato.
Attori Partecipante
Precondizioni Il partecipante vuole ritirarsi dal campionato.
Scenario principale Il partecipante si ritira dal campionato
Scenari alternativi Il partecipante non comunica il ritiro dal campionato, viene quindi notificato
al giudice che lo sanziona.
Post-condizioni Il partecipante si ritira, e viene cancellato regolarmente dal campionato.
11


---

<!-- Pagina PDF 14 -->
## 📑 Pagina 14

Use case Visualizza sanzioni
Descrizione Passo Azione
1 Il partecipante visualizza le sue sanzioni.
2 Il partecipante applica un filtro alla lista di sanzioni.
Attori Partecipante
Precondizioni Il partecipante vuole vedere le sue sanzioni.
Scenario principale Il partecipante vede le sue sanzioni.
Scenari alternativi //
Post-condizioni Il partecipante vede le sanzioni.
3.5 Use Case Utente
3.5.1 Diagramma
3.5.2 Documentazione
Use case Effettua registrazione
Descrizione Passo Azione
1 L’utente richiede la pagina principale.
2 Il sistema visualizza la pagina di accesso. L’utente non registrato
pu` o selezionare la voce “registrazione”
3 L’utente non registrato inserisce i dati personali, qualora decida di
effettuare la registrazione.
4 Il sistema aggiunge l’utente al database
5 L’utente non registrato ottiene i privilegi dell’utente registrato
Attori Utente non registrato.
Precondizioni L’utente non registrato deve acconsentire al trattamento dei dati
personali.
Scenario principale L’utente non registrato pu` o decidere se registrarsi al sistema.
Scenari alternativi 1. L’utente non pu` o registrarsi, se non acconsente al trattamento dei dati
personali oppure se non vengono rispettati i canoni imposti durante la
registrazione.
2. I dati personali inseriti coincidono con quelli di un account gi` a presente
all’interno del sistema, la registrazione non v` a a buon fine.
Post-condizioni L’utente effettua con successo la registrazione al servizio.
12


---

<!-- Pagina PDF 15 -->
## 📑 Pagina 15

Use case Effettua accesso
Descrizione Passo Azione
1 L’utente richiede la pagina principale.
2 Il sistema visualizza la pagina di accesso. L’utente registrato pu` o
selezionare la voce “login”.
3 L’utente registrato effettua il login con le credenziali d’accesso.
Attori Utente registrato.
Precondizioni L’utente registrato, durante la registrazione, ha acconsentito al
trattamento dei dati personali.
Scenario principale L’utente registrato pu` o effettuare il login con le sue credenziali di
accesso o richiedere di recuperare la propria password, in alterna-
tiva, l’utente registrato pu` o effettuare il logout.
Scenari alternativi
1. L’utente inserisce delle credenziali d’accesso errate, gli vengono forniti
altri due tentativi prima che venga messo in “timeout” dal servizio per
15 minuti di tempo.
2. L’utente seleziona la voce “recupera password”, un messaggio di recupero
verr` a inviato all’indirizzo email associato al suo account.
Post-condizioni L’utente effettua con successo il login nell’applicazione, l’utente gi` a
loggato pu` o effettuare il logout.
Use case Visualizza risultati
Descrizione Passo Azione
1 L’utente richiede di poter visualizzare i risultati delle partite.
2.a Nel caso l’utente sia registrato, pu` o essere stata applicata una per-
sonalizzazione dei risultati visualizzati per nascondere risultati in-
desiderati.
2.b Nel caso l’utente non sia registrato, pu` o solo visualizzare i risultati.
Attori Utente registrato, utente non registrato.
Precondizioni
1. L’utente registrato ha effettuato il login
2. L’utente non registrato ha deciso di visualizzare i risultati.
Scenario principale
1. L’utente registrato decide di visualizzare i risultati delle partite, con in
primo piano quelle risultanti dalle operazioni di personalizzazione.
2. L’utente non registrato decide di visualizzare i risultati delle partite,
nessuna personalizzazione viene applicata.
Scenari alternativi Se applicati i filtri nessuna partita risulta rispettare la selezione, verr` a notifi-
cato tramite un banner.
Post-condizioni Entrambi gli utenti visualizzano con successo i risultati delle parti-
te.
13


---

<!-- Pagina PDF 16 -->
## 📑 Pagina 16

Use case Aggiorna dati personali
Descrizione Passo Azione
1 L’utente accede alla propria pagina personale.
2 L’utente richiede al sistema di poter cambiare i propri dati perso-
nali.
3 L’utente seleziona quale dato personale vuole cambiare.
4 L’utente salva i cambiamenti.
Attori Utente registrato
Precondizioni L’utente registrato ha effettuato il login.
Scenario principale L’utente decide di aggiornare i propri dati personali.
Scenari alternativi Se l’utente si dimentica di salvare i cambiamenti prima di uscire, gli viene
fornito un messaggio di avviso, comunicandogli che alcuni cambiamenti non
sono stati salvati; da qui, l’utente pu` o decidere se:
• Tornare ad impostare le proprie personalizzazioni
• Uscire, salvando la personalizzazione
• Uscire, non salvando la personalizzazione
Post-condizioni L’utente ha aggiornato con successo i propri dati personali.
Use case Personalizza risultati con filtro
Descrizione Passo Azione
1 L’utente, dalla propria pagina personale, richiede di poter persona-
lizzare quali risultati visualizzare e quali no.
2 L’utente seleziona le proprie personalizzazioni, in particolare i par-
tecipanti di maggiore interesse.
3 L’utente salva le nuove personalizzazioni.
Attori Utente registrato.
Precondizioni L’utente registrato ha effettuato il login e si trova nella propria area personale.
Scenario principale L’utente personalizza la visualizzazione dei risultati.
Scenari alternativi //
Post-condizioni L’utente ha effettuato con successo la creazione di una personaliz-
zazione per i risultati da visualizzare.
14


---

<!-- Pagina PDF 17 -->
## 📑 Pagina 17

Use case Richiedi cancellazione dell’account
Descrizione Passo Azione
1 L’utente, dalla propria pagina personale, richiede di voler cancellare
il proprio account.
2 Il sistema chiede all’utente se ` e sicuro della propria scelta di voler
cancellare il proprio account.
3 L’utente conferma la sua scelta.
4 Il sistema invia all’utente un’email di conferma per la cancellazione
del proprio account.
5 L’utente conferma la cancellazione.
6 L’account dell’utente effettua automaticamente il logout.
7 Il sistema cancella l’account dell’utente dal suo database.
Attori Utente registrato
Precondizioni L’utente registrato ha effettuato il login e si trova nella propria area
personale.
Scenario principale L’utente decide di voler cancellare il proprio account.
Scenari alternativi Se l’utente si dimentica di confermare la cancellazione dell’account tramite il
messaggio inviato via email entro 15 minuti, il sistema annulla la cancellazione.
Nel caso l’utente registrato sia uno tra i seguenti:
• Arbitro
• Giudice
• Responsabile squadra
Egli non potr` a decidere di cancellare autonomamente il proprio account: tale
operazione verr` a prima notificata e poi gestita dall’organizzatore del campio-
nato.
Post-condizioni L’utente ha effettuato con successo la cancellazione del proprio account, sar` a
libero di effettuare una nuova registrazione quando desidera.
15


---

<!-- Pagina PDF 18 -->
## 📑 Pagina 18

4 System Requirements
4.1 Requisiti Funzionali
Attore ID Requisiti Funzionali Descrizione
Utente non registrato 1.1 Registrazione Un utente non registrato pu` o decidere di effettuare la
registrazione al servizio e quindi inserire le sue informa-
zioni personali nel sistema.
1.2 Visualizzazione risul-
tati
Un utente non registrato pu` o decidere di visualizzare i
risultati delle partite, senza per` o avere la possibilit` a di
personalizzare i risultati mostrati.
Utente registrato 2.1 Effettua accesso Un utente, regolarmente registrato, pu` o effettuare l’ac-
cesso tramite mail e password.
2.2 Aggiornamento dati
personali
L’utente pu` o avere libero accesso alla propria area per-
sonale, nella quale pu` o visualizzare e modificare le in-
formazioni fornite in fase di registrazione.
2.3 Personalizzazione del-
la visualizzazione dei
risultati
L’utente registrato potr` a applicare dei filtri in base alle
sue preferenze per migliorare la visualizzazione dei risul-
tati.
2.4 Visualizzazione risul-
tati
Un utente registrato pu` o decidere di visualizzare i risul-
tati delle partite, avendo anche la possibilit` a di poter
personalizzare i risultati mostrati.
2.5 Cancellazione account L’utente ha la possibilit` a di decidere di cancellare il suo
account. Nel caso di utenti che svolgono un ruolo attivo,
quindi aventi privilegi speciali, la cancellazione dovr` a
essere gestita dall’organizzatore del campionato.
Partecipante 3.1 Capacit` a utente regi-
strato
Il partecipante gode di ogni altro privilegio di un qual-
siasi utente registrato, e pu` o effettuare le stesse azioni
che pu` o effettuare quest’ultimo.
3.2 Gestisci dati personali Il partecipante deve essere in grado di poter modificare
i dati personali, come:
• Nome
• Cognome
• Data nascita
• Email
• Indirizzo di casa
• Numero di telefono
3.3 Visualizza sanzioni Il partecipante deve essere in grado di poter visualizzare
le sanzioni a lui assegnate.
Arbitro 4.1 Capacit` a utente spe-
ciale
Un arbitro gode di ogni altro privilegio di un qualsiasi
utente speciale, e pu` o effettuare azioni dipendenti dal
suo ruolo.
4.2 Inserimento risultati Al termine degli incontri l’arbitro deve essere in grado
di inserirne l’esito.
Compilazione rappor-
to e caricamento refer-
to
L’arbitro, in seguito all’inserimento del risultato, deve
compilare il rapporto e caricare il referto sul portale.
4.3 Selezionamento dispo-
nibilit` a
Un arbitro deve potere essere in grado di selezionare
giorni e fasce orarie in cui risulta disponibile per svolgere
l’attivit` a di arbitraggio.
16


---

<!-- Pagina PDF 19 -->
## 📑 Pagina 19

4.4 Gestione arbitraggi
proposti
Un arbitro ` e in grado di poter accettare o rifiutare gli
arbitraggi che gli sono stati proposti in base alle dispo-
nibilit` a da lui fornite.
Responsabile di gara 5.1 Capacit` a utente spe-
ciale
Il responsabile di gara gode di ogni altro privilegio di un
qualsiasi utente speciale, e pu` o effettuare azioni dipen-
denti dal suo ruolo.
5.2 Assegnazione arbi-
traggi
Il responsabile di gara, per ogni incontro da assegnare,
deve essere in grado di visualizzare gli arbitri disponibili
al fine di scegliere quello da assegnare all’incontro.
Organizzatore del
Campionato
6.1 Capacit` a utente spe-
ciale
L’organizzatore del campionato gode di ogni altro pri-
vilegio di un qualsiasi utente speciale, e pu` o effettuare
azioni dipendenti dal suo ruolo.
6.2 Creazione del campio-
nato
L’organizzatore del campionato pu` o creare un campio-
nato.
Creazione giornate L’organizzatore del campionato sceglie una locazione di
pesca dove si ambienter` a il campionato.
Visualizza giornate da
schedulare
L’organizzatore del campionato pu` o visualizzare le gior-
nate alle quali non sono ancora state assegnate data e
ora.
6.3 Schedulazione delle
giornate
L’organizzatore del campionato assegna alle giornate an-
cora non schedulate data e ora. Le giornate possono
anche essere rischedulate in seguito ad annullamento o
richiesta di modifica da parte del Giudice.
Creazione account
speciali
L’organizzatore del campionato pu` o creare degli account
con funzioni aggiuntive per i seguenti utenti:
• Arbitro
• Giudice
• Partecipante
• Responsabile di gara
6.4 Cancellazione account
speciali
Nel caso la cancellazione sia stata richiesta da uno dei
seguenti utenti:
• Arbitro
• Giudice
• Partecipante
• Responsabile di gara
L’organizzatore del campionato deve poter essere in gra-
do di gestire le suddette richieste.
17


---

<!-- Pagina PDF 20 -->
## 📑 Pagina 20

4.2 Requisiti Non Funzionali
ID Requisito Descrizione
1 Performance Le operazioni effettuate sono semplici e in quanto tali
ci si aspetta di ricevere risposte rapide dal sistema in
seguito all’inoltro delle richieste. Il sistema deve poter
supportare 500 utenti per ora e fornire le pagine richieste
in meno di 2 secondi, sia sul portale che sull’applicazio-
ne, includendo la formattazione del testo e la visualiz-
zazione delle immagini.
2 Scalabilit` a Con il tempo potrebbe essere richiesta l’aggiunta di nuo-
ve funzionalit` a, aumento di traffico, e nel tempo l’im-
magazzinamento di consistenti quantit` a di dati, mante-
nendo le performance. L’obiettivo ` e di fare in modo da
facilitare queste migliorie, aggiungendo quindi dei requi-
siti senza stravolgere la parte di codice gi` a presente e in
funzione.
3 Portabilit` a Le due modalit` a di accesso (sito web e applicazione)
devono essere facilmente utilizzabili dalla maggior parte
dei dispositivi. In particolare per l’applicazione saranno
previste le versioni per Android e iOS (versioni correnti e
tre versioni passate), mentre per il sito sar` a garantita la
compatibilit` a con la maggior parte dei browser esistenti
(Chrome, Firefox, Opera, Safari, Edge).
4 Affidabilit` a Il sistema deve funzionare senza guasti nel 95% dei casi.
5 Manutenibilit` a Ci si aspetta che la manutenzione del sistema sia sem-
plice. Una divisione in moduli facilita queste procedure.
In particolare deve essere particolarmente agile la ma-
nutenzione perfettiva, in quanto possiamo prevedere che
possano essere in futuro aggiunte nuove funzionalit` a o
che si decida di automatizzare altre procedure correlate.
In caso di guasti deve essere auspicabile che il sistema
torni a funzionare correttamente entro un paio d’ore.
6 Disponibilit` a Le funzionalit` a del sistema devono essere disponibili per
il 90% del tempo di attivit` a.
7 Usabilit` a Non si pu` o presupporre che tutti gli utenti, anche quelli
con permessi specifici, abbiano competenze informati-
che avanzate. L’interfaccia deve quindi essere intuitiva,
semplice da utilizzare e non richiedere alcuna formazio-
ne particolare. Ogni operazione deve poter essere com-
pletata rapidamente e senza difficolt` a. Inoltre, il design
dell’interfaccia deve essere responsive, adattandosi auto-
maticamente a diverse dimensioni e tipi di dispositivi, e
User-Friendly. Sar` a garantito anche un supporto tecnico
dedicato. Durante la fase di test, l’obiettivo ` e mantene-
re il tasso di errore degli utenti sotto il 10%.
8 Sicurezza La gestione dei dati sensibili, come email e numeri di te-
lefono degli utenti, e l’esecuzione di operazioni critiche
richiedono particolare attenzione. Un utilizzo non auto-
rizzato degli account potrebbe causare gravi disservizi
e compromettere il regolare svolgimento delle attivit` a,
incluse le competizioni. Per garantire la sicurezza, ogni
account deve essere protetto con username e password.
Inoltre, le funzionalit` a critiche devono essere assegnate
solo agli account delle persone che possiedono le respon-
sabilit` a necessarie, suddividendo con attenzione i privi-
legi operativi.
18


---

<!-- Pagina PDF 21 -->
## 📑 Pagina 21

4.3 Requisiti di Dominio
1. Normativa europea per il trattamento dei dati personali GDPR (General Data Protection Regulation)
2016/679, accessibile tramite il seguente link.
2. Regolamento (UE) 2016/679 del Parlamento europeo e del Consiglio, del 27 aprile 2016, relativo alla prote-
zione delle persone fisiche con riguardo al trattamento dei dati personali, nonch´ e alla libera circolazione di
tali dati e che abroga la direttiva 95/46/CE (regolamento generale sulla protezione dei dati) (16CE1278);
3. Esempio Regolamento del campionato, accessibile tramite il seguente link
4. Esempio di circolare normativa, accessibile tramite il seguente link.
19


---

<!-- Pagina PDF 22 -->
## 📑 Pagina 22

5 System Architectural Models
5.1 Activity Diagrams
5.1.1 Activity Diagrams Arbitro
Activity Diagram ”Inserisci Risultato”.
20


---

<!-- Pagina PDF 23 -->
## 📑 Pagina 23

Activity Diagram ”Conferma/Rifiuta arbitraggio proposto”.
21


---

<!-- Pagina PDF 24 -->
## 📑 Pagina 24

Activity Diagram ”Giorni disponibili per arbitrare”.
22


---

<!-- Pagina PDF 25 -->
## 📑 Pagina 25

5.1.2 Activity Diagrams Organizzatore del Campionato
Activity Diagram ”Crea account utente speciale”.
Activity Diagram ”Cancella account utente speciale”.
23


---

<!-- Pagina PDF 26 -->
## 📑 Pagina 26

Activity Diagram ”Crea campionato”.
Activity Diagram ”Visualizza incontri da schedulare”.
24


---

<!-- Pagina PDF 27 -->
## 📑 Pagina 27

Activity Diagram ”Schedula incontri”.
25


---

<!-- Pagina PDF 28 -->
## 📑 Pagina 28

Activity Diagram ”Crea incontri”.
26


---

<!-- Pagina PDF 29 -->
## 📑 Pagina 29

5.1.3 Activity Diagrams Giudice
Activity Diagram ”Richiede Rapporto Compilato”.
27


---

<!-- Pagina PDF 30 -->
## 📑 Pagina 30

Activity Diagram ”Giudica incontri”.
Activity Diagram ”Assegna Sanzioni”.
28


---

<!-- Pagina PDF 31 -->
## 📑 Pagina 31

Activity Diagram ”Richiede Rischedulazione incontro”.
29


---

<!-- Pagina PDF 32 -->
## 📑 Pagina 32

5.1.4 Activity Diagrams Partecipante
Activity Diagram ”Visualizzazione della classifica”.
Activity Diagram ”Iscrizione o ritiro dal campionato”.
30


---

<!-- Pagina PDF 33 -->
## 📑 Pagina 33

Activity Diagram ”Visualizzazione sanzione”.
31


---

<!-- Pagina PDF 34 -->
## 📑 Pagina 34

5.1.5 Activity Diagrams Utente
Activity Diagram ”Operazioni”.
32


---

<!-- Pagina PDF 35 -->
## 📑 Pagina 35

Activity Diagram ”Visualizzazione risultati”.
33


---

<!-- Pagina PDF 36 -->
## 📑 Pagina 36

5.2 Sequence Diagrams
5.2.1 Sequence Diagrams Arbitro
Sequence Diagram ”Giorni disponibili per arbitrare”.
34


---

<!-- Pagina PDF 37 -->
## 📑 Pagina 37

Sequence Diagram ”Conferma o rifuta incarico”
35


---

<!-- Pagina PDF 38 -->
## 📑 Pagina 38

Sequence Diagram ”Assegna Arbitraggi”
36


---

<!-- Pagina PDF 39 -->
## 📑 Pagina 39

Sequence Diagram ”Inserisci Risultato”
37


---

<!-- Pagina PDF 40 -->
## 📑 Pagina 40

5.2.2 Sequence Diagrams Organizzatore del Campionato
Sequence Diagram ”Cancella Account Speciale”
38


---

<!-- Pagina PDF 41 -->
## 📑 Pagina 41

Sequence Diagram ”Crea Account Speciale”
39


---

<!-- Pagina PDF 42 -->
## 📑 Pagina 42

Sequence Diagram ”Crea Campionato”
40


---

<!-- Pagina PDF 43 -->
## 📑 Pagina 43

Sequence Diagram ”Visualizza e Schedula Incontri”
Sequence Diagram ”Crea Incontro”
41


---

<!-- Pagina PDF 44 -->
## 📑 Pagina 44

5.2.3 Sequence Diagrams Giudice
Sequence Diagram ”Richiedi Rischedulazione”
42


---

<!-- Pagina PDF 45 -->
## 📑 Pagina 45

Sequence Diagram ”Assegna Sanzioni”
43


---

<!-- Pagina PDF 46 -->
## 📑 Pagina 46

5.2.4 Sequence Diagrams Partecipante
Sequence Diagram ”Visualizza Sanzioni”
44


---

<!-- Pagina PDF 47 -->
## 📑 Pagina 47

Sequence Diagram ”Ritiro dal campionato”
Sequence Diagram ”Iscrizione al campionato”
45


---

<!-- Pagina PDF 48 -->
## 📑 Pagina 48

5.2.5 Sequence Diagrams Utente
Sequence Diagram ”Effettua Accesso/Registrazione”
46


---

<!-- Pagina PDF 49 -->
## 📑 Pagina 49

Sequence Diagram ”Cancella Account”
47


---

<!-- Pagina PDF 50 -->
## 📑 Pagina 50

Sequence Diagram ”Creazione Filtro”
48


---

<!-- Pagina PDF 51 -->
## 📑 Pagina 51

Sequence Diagram ”Modifica Dati”
49


---

<!-- Pagina PDF 52 -->
## 📑 Pagina 52

5.3 Class Diagrams
5.3.1 Class Diagrams Unrefined
50


---

<!-- Pagina PDF 53 -->
## 📑 Pagina 53

5.3.2 Class Diagrams Refined
51


---

<!-- Pagina PDF 54 -->
## 📑 Pagina 54

6 Design Pattern
6.1 Observer
Immaginiamo un sistema in cui ogni utente registrato possa richiedere notifiche sui risultati di specifici incontri.
Questo sistema potrebbe essere realizzato tramite un meccanismo di iscrizioni, in cui ad ogni incontro ` e asso-
ciato un insieme di utenti interessati ai risultati. Una soluzione del genere elimina la necessit` a per gli utenti
di controllare continuamente il portale o l’applicazione alla ricerca di aggiornamenti, evitando cos` ı un compor-
tamento simile al polling. Per implementare questa idea, sarebbe necessario introdurre metodi che consentano
di manifestare o revocare l’interesse per una determinata partita. Da questa esigenza nasce l’idea di adottare
il Design Pattern Observer, dove il soggetto ` e rappresentato dalla partita schedulata e gli osservatori sono gli
utenti interessati. Si ` e quindi deciso di adattare il sistema esistente alla nuova struttura, sfruttando l’operatore
della classe Notifier.
52


---

<!-- Pagina PDF 55 -->
## 📑 Pagina 55

6.2 Decorator
Supponiamo che l’utente possa ricevere notifiche dal portale attraverso vari canali, come WhatsApp, SMS ed
email. Si desidera garantire che le notifiche possano essere inviate simultaneamente su diverse combinazioni di
canali di comunicazione, scelte dall’utente, senza dover definire metodi specifici per ogni possibile combinazione.
Per affrontare questo problema, si potrebbe modificare la classe Notifier applicando il Design Pattern Deco-
rator. Questo approccio consentirebbe di decidere dinamicamente quale combinazione di notifiche utilizzare,
eventualmente basandosi sulle preferenze configurate dall’utente.
53


---

<!-- Pagina PDF 56 -->
## 📑 Pagina 56

6.3 Singleton
Dopo aver creato i Sequence Diagrams e il Class Diagram Raffinato, ` e emerso che la classe Notifier veniva
frequentemente referenziata. Per questo motivo, si ` e deciso di applicare il Design Pattern Singleton, cos` ı da
garantire un punto di accesso globale alla classe mantenendo, al contempo, una singola istanza per l’intero
funzionamento del software.
6.4 Strategy
Per offrire all’utente la possibilit` a di personalizzare la visualizzazione dei risultati, ` e stato scelto di utilizzare un
algoritmo di ordinamento. Per rendere questa funzionalit` a flessibile, si ` e deciso di adottare il Design Pattern
Strategy, consentendo cos` ı all’utente di selezionare il criterio di preferenza pi` u adatto alle proprie esigenze.
54


---

<!-- Pagina PDF 57 -->
## 📑 Pagina 57

*[Nessun testo estraibile in questa pagina / Contiene solo diagrammi o immagini]*


---

<!-- Pagina PDF 58 -->
## 📑 Pagina 58

*[Nessun testo estraibile in questa pagina / Contiene solo diagrammi o immagini]*


---

<!-- Pagina PDF 59 -->
## 📑 Pagina 59

*[Nessun testo estraibile in questa pagina / Contiene solo diagrammi o immagini]*


---

<!-- Pagina PDF 60 -->
## 📑 Pagina 60

*[Nessun testo estraibile in questa pagina / Contiene solo diagrammi o immagini]*


---

<!-- Pagina PDF 61 -->
## 📑 Pagina 61

*[Nessun testo estraibile in questa pagina / Contiene solo diagrammi o immagini]*


---

<!-- Pagina PDF 62 -->
## 📑 Pagina 62

*[Nessun testo estraibile in questa pagina / Contiene solo diagrammi o immagini]*


---

<!-- Pagina PDF 63 -->
## 📑 Pagina 63

*[Nessun testo estraibile in questa pagina / Contiene solo diagrammi o immagini]*


---

<!-- Pagina PDF 64 -->
## 📑 Pagina 64

*[Nessun testo estraibile in questa pagina / Contiene solo diagrammi o immagini]*


---

<!-- Pagina PDF 65 -->
## 📑 Pagina 65

*[Nessun testo estraibile in questa pagina / Contiene solo diagrammi o immagini]*


---

<!-- Pagina PDF 66 -->
## 📑 Pagina 66

*[Nessun testo estraibile in questa pagina / Contiene solo diagrammi o immagini]*


---

<!-- Pagina PDF 67 -->
## 📑 Pagina 67

*[Nessun testo estraibile in questa pagina / Contiene solo diagrammi o immagini]*


---

<!-- Pagina PDF 68 -->
## 📑 Pagina 68

*[Nessun testo estraibile in questa pagina / Contiene solo diagrammi o immagini]*


---

<!-- Pagina PDF 69 -->
## 📑 Pagina 69

*[Nessun testo estraibile in questa pagina / Contiene solo diagrammi o immagini]*


---

<!-- Pagina PDF 70 -->
## 📑 Pagina 70

*[Nessun testo estraibile in questa pagina / Contiene solo diagrammi o immagini]*


---

<!-- Pagina PDF 71 -->
## 📑 Pagina 71

*[Nessun testo estraibile in questa pagina / Contiene solo diagrammi o immagini]*


---

<!-- Pagina PDF 72 -->
## 📑 Pagina 72

*[Nessun testo estraibile in questa pagina / Contiene solo diagrammi o immagini]*


---

<!-- Pagina PDF 73 -->
## 📑 Pagina 73

*[Nessun testo estraibile in questa pagina / Contiene solo diagrammi o immagini]*


---

<!-- Pagina PDF 74 -->
## 📑 Pagina 74

*[Nessun testo estraibile in questa pagina / Contiene solo diagrammi o immagini]*


---

<!-- Pagina PDF 75 -->
## 📑 Pagina 75

*[Nessun testo estraibile in questa pagina / Contiene solo diagrammi o immagini]*


---

<!-- Pagina PDF 76 -->
## 📑 Pagina 76

*[Nessun testo estraibile in questa pagina / Contiene solo diagrammi o immagini]*


---