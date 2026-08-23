# 📄 Specifica di Progetto: Hotel TorVergata

> **Autori**: Francesco Mongelli, Giacomo Pace, Mihai Alexandru Sandu, Niccolò Giorgio Rossi Paccani  
> **Pagine totali**: 59  
> **Trascrizione**: Estratta dal documento originale per consultazione testuale diretta.

---


<!-- Pagina PDF 1 -->
## 📑 Pagina 1

Mongelli Francesco
0327829
Pace Giacomo
0326924
Sandu Mihai Alexandru
0327308
Rossi Paccani Niccol` o Giorgio
0327821


---

<!-- Pagina PDF 2 -->
## 📑 Pagina 2

Hotel TorVergata
Contents
1 Introduzione 2
2 Glossario 3
3 User Requirements Definition 4
3.1 Use Case Utente . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.1.1 Diagramma . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.1.2 Documentazione . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.2 Use Case Cliente . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
3.2.1 Diagramma . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
3.2.2 Documentazione . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
3.3 Use Case Amministrazione . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3.3.1 Diagramma . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3.3.2 Documentazione . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
3.4 Use Case Servizio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.4.1 Diagramma . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.4.2 Documentazione . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
4 System Requirements 15
4.1 Requisiti Funzionali . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
4.2 Requisiti Non Funzionali . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
4.3 Requisiti di Dominio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
5 System Architectural Models 17
5.1 Activity Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
5.1.1 Activity Diagram Utente . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
5.1.2 Activity Diagram Cliente . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
5.1.3 Activity Diagram Amministrazione . . . . . . . . . . . . . . . . . . . . . . . . . . 23
5.1.4 Activity Diagram Servizio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
5.2 Sequence Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
5.2.1 Sequence Diagram Utente . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
5.2.2 Sequence Diagram Cliente . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
5.2.3 Sequence Diagram Amministrazione . . . . . . . . . . . . . . . . . . . . . . . . . 42
5.2.4 Sequence Diagram Servizio . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
5.3 Class Diagrams . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
5.3.1 Class Diagram Unrefined . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 55
5.3.2 Class Diagram Refined . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
6 Design Patterns 57
1


---

<!-- Pagina PDF 3 -->
## 📑 Pagina 3

1 Introduzione
Il software ` e progettato per facilitare la gestione operativa di una struttura alberghiera, automatizzando
le principali attivit` a organizzative e amministrative al fine di ridurre il rischio di errori e ottimizzare
l’efficienza del personale. L’hotel opera durante tutto l’anno, ospitando clienti con esigenze eterogenee
e gestendo al contempo servizi interni complessi, che coinvolgono diversi attori con ruoli ben definiti.
I clienti, tramite il portale, possono effettuare prenotazioni personalizzate selezionando tipologia
di camera, periodo di soggiorno e servizi aggiuntivi. Una volta confermata la prenotazione, il sistema
invia notifiche automatiche e consente al cliente di modificare o annullare la propria richiesta in base
alle politiche della struttura. I pagamenti sono gestiti attraverso metodi sicuri e integrati, mentre al
termine del soggiorno il cliente pu` o lasciare una recensione pubblica consultabile da altri utenti.
Parallelamente, il personale dell’hotel svolge attivit` a operative distinte: l’amministrazione gestisce il
check-in/check-out e monitora le prenotazioni in tempo reale; il personale addetto alle pulizie aggiorna
lo stato delle camere; il personale del ristorante riceve e processa ordini dei clienti. La gestione dei
reclami e delle comunicazioni con i clienti ` e centralizzata e assegnata a figure specifiche, mentre gli
amministratori di sistema supervisionano l’intera infrastruttura gestionale, coordinando utenti, camere,
prenotazioni e servizi.
Il sistema supporta anche la gestione del personale, consentendo la creazione e la disattivazione
degli account interni, l’assegnazione di ruoli e l’organizzazione dei turni di lavoro. Per garantire la
trasparenza e la tracciabilit` a, tutte le operazioni rilevanti vengono registrate in un sistema di audit
log. Inoltre, un modulo di reportistica consente alla direzione di monitorare l’andamento economico
della struttura attraverso dashboard e analisi aggregate.
Le comunicazioni tra sistema e utenti sono gestite tramite notifiche automatiche, inviate via e-mail,
SMS o all’interno del portale stesso, in modo da garantire un flusso informativo costante e aggiornato.
Gli utenti non registrati possono consultare informazioni pubbliche come tariffe, disponibilit` a camere
e recensioni, mentre gli utenti autenticati hanno accesso a funzionalit` a avanzate come la gestione delle
prenotazioni, l’aggiunta ai preferiti e la visualizzazione delle spese sostenute.
L’obiettivo finale del sistema ` e semplificare la gestione alberghiera, offrire un servizio fluido agli
ospiti e fornire al personale uno strumento versatile per migliorare la qualit` a del lavoro e del soggiorno.
2


---

<!-- Pagina PDF 4 -->
## 📑 Pagina 4

2 Glossario
Termine Definizione
Utente Persona che accede al sistema, senza specifici privilegi e dotato di fun-
zionalit` a base.
Utente registrato utente che ha effettuato la registrazione e pu` o accedere a funzionalit` a
avanzate.
Cliente Utente registrato che effettua prenotazioni, richiede servizi extra, paga
online, lascia recensioni e interagisce con il sistema per gestire il proprio
soggiorno.
Amministrazione Utente registrato con privilegi di gestione che si occupa di creare, mod-
ificare e cancellare prenotazioni, assegnare camere, gestire check-in e
check-out, gestire reclami, amministrare gli account utenti e monitorare
l’attivit` a generale della struttura.
Servizio Personale o modulo del sistema dedicato alla gestione dei servizi interni
come la ristorazione e le pulizie, inclusa la gestione degli ordini dei cli-
enti, aggiornamento del men` u, visualizzazione delle camere da pulire e
modifica dello stato pulizia.
Prenotazione La richiesta formale effettuata dal Cliente per riservare una camera in
una data specifica. Pu` o essere modificata, cancellata o completata con
servizi extra.
Servizi Extra Opzioni aggiuntive associate a una prenotazione, come colazione, spa o
lavanderia, che il Cliente pu` o selezionare per arricchire il proprio sog-
giorno.
Pagamento Online Procedura con cui il Cliente effettua il pagamento della prenotazione
utilizzando metodi digitali come carta di credito o PayPal.
Recensione Feedback lasciato dal Cliente al termine del soggiorno, composto da un
voto e un commento testuale sull’esperienza.
Camera Unit` a abitativa della struttura ricettiva assegnata a un Cliente in base
alle preferenze e disponibilit` a.
Check-in Procedura di registrazione dell’arrivo del Cliente in struttura.
Check-out Procedura di registrazione della partenza del Cliente dalla struttura.
Reclamo Segnalazione formale effettuata dal Cliente per evidenziare problem-
atiche riscontrate durante il soggiorno.
Ordine (Ristorazione) Richiesta di pietanze da parte del Cliente, gestita dal Servizio ris-
torazione e consegnata in camera o in sala.
Men` u Lista delle pietanze offerte dal servizio ristorazione, soggetta a modifiche
da parte degli operatori autorizzati.
Stato Pulizia Camera Indicazione del livello di pulizia o necessit` a di intervento su una camera
specifica, aggiornata dagli operatori del Servizio Pulizia.
Sistema L’applicazione software per la gestione completa dell’hotel.
Portale Interfaccia web o app tramite cui gli utenti interagiscono con il sistema.
3


---

<!-- Pagina PDF 5 -->
## 📑 Pagina 5

3 User Requirements Definition
3.1 Use Case Utente
3.1.1 Diagramma
3.1.2 Documentazione
Use Case - Visualizzazione Offerte e Camere Disponibili
Elemento Descrizione
Passi Azione 1. L’utente non registrato entra nel sistema.
2. Seleziona il periodo di tempo per cui desidera visualizzare le
offerte.
3. Il sistema mostra le offerte e le camere disponibili con prezzi e
servizi associati.
Attori Utente non registrato
Precondizioni Nessuna precondizione particolare, l’utente deve solo accedere al
sistema.
Scenario principale L’utente consulta le offerte e le camere disponibili senza autenti-
cazione.
Scenari alternativi 3.1 La camera scelta da visualizzare non ` e disponibile nel periodo
scelto.
3.2 Il sistema mostra opzioni alternative disponibili per quel peri-
odo.
Post-condizioni L’utente non registrato ha visionato le informazioni di cui aveva
bisogno.
4


---

<!-- Pagina PDF 6 -->
## 📑 Pagina 6

Use Case - Registrazione
Elemento Descrizione
Passi Azione 1. L’utente accede alla sezione “Registrati” e inserisce le infor-
mazioni richieste (nome utente, password, email, ecc.).
2. Il sistema valida i dati e crea un nuovo profilo utente registrato.
Attori Utente non registrato
Precondizioni L’utente accede alla sezione “Registrati” del sistema.
Scenario principale L’utente si registra al sistema per accedere a funzionalit` a aggiun-
tive.
Scenari alternativi 2.1 Il sistema rileva errori nei dati inseriti (es. dati non validi,
email gi` a in uso).
2.2 Il sistema mostra un messaggio di errore esplicativo e riporta
l’utente al form.
Post-condizioni L’utente ha un nuovo account ed ` e ora considerato utente regis-
trato.
Use Case - Effettua accesso
Elemento Descrizione
Passi Azione 1. L’utente richiede la pagina principale.
2. Il sistema mostra la pagina di login.
3. L’utente inserisce email e password.
4. Il sistema verifica le credenziali.
5. Se corrette, l’utente accede al pannello personale.
Attori Utente registrato
Precondizioni L’utente deve essere registrato e avere credenziali valide.
Scenario principale L’utente inserisce correttamente le credenziali ed entra nel sis-
tema.
Scenari alternativi 1. L’utente inserisce credenziali errate: il sistema mostra un mes-
saggio d’errore.
2. L’utente ha dimenticato la password: pu` o accedere alla fun-
zione “Recupera password”.
Post-condizioni L’utente ha accesso alla propria area personale.
Use Case - Cancellazione account
Elemento Descrizione
Passi Azione 1. L’utente accede alla sezione ”Gestione Account”.
2. Seleziona “Elimina Account”.
3. Il sistema chiede conferma.
4. L’utente conferma l’intenzione.
5. Il sistema elimina o disattiva l’account, rimuovendo i dati per-
sonali ove possibile.
Attori Utente registrato
Precondizioni L’utente deve essere autenticato.
Scenario principale L’utente conferma la volont` a di cancellare il proprio account.
Scenari alternativi 1. L’utente annulla l’operazione: l’account rimane attivo.
Post-condizioni L’account viene cancellato o disattivato.
5


---

<!-- Pagina PDF 7 -->
## 📑 Pagina 7

Use Case - Aggiornamento dati personali
Elemento Descrizione
Passi Azione 1. L’utente accede alla sezione ”Profilo personale”.
2. Seleziona il campo da modificare (nome, email, telefono, pass-
word, ecc.).
3. Inserisce i nuovi dati.
4. Conferma la modifica.
5. Il sistema aggiorna le informazioni nel database.
Attori Utente registrato
Precondizioni L’utente deve essere autenticato.
Scenario principale L’utente aggiorna correttamente uno o pi` u dati del proprio profilo.
Scenari alternativi 1. L’utente inserisce un formato non valido: il sistema mostra un
errore.
2. L’utente lascia campi obbligatori vuoti: il sistema blocca la
modifica.
Post-condizioni I dati personali dell’utente risultano aggiornati nel sistema.
6


---

<!-- Pagina PDF 8 -->
## 📑 Pagina 8

3.2 Use Case Cliente
3.2.1 Diagramma
3.2.2 Documentazione
Use Case - Effettua prenotazione
Elemento Descrizione
Passi Azione 1. Il cliente accede al sistema e seleziona le date di arrivo e
partenza.
2. Il cliente seleziona la tipologia di camera desiderata.
3. Il cliente conferma i dati e completa la prenotazione.
Attori Cliente
Precondizioni Il cliente ha effettuato l’accesso al sistema.
Scenario principale Il cliente effettua una prenotazione per un soggiorno.
Scenari alternativi La camera selezionata potrebbe non essere disponibile, viene sug-
gerita un’alternativa.
Post-condizioni La prenotazione ` e registrata nel sistema e visibile nella sezione
personale del cliente.
7


---

<!-- Pagina PDF 9 -->
## 📑 Pagina 9

Use Case - Gestione prenotazioni
Elemento Descrizione
Passi Azione 1. Il cliente visualizza la lista delle prenotazioni effettuate.
2. Il cliente seleziona una prenotazione da modificare o cancellare.
3. Il sistema applica le modifiche richieste oppure elimina la preno-
tazione.
Attori Cliente, Amministrazione
Precondizioni Il cliente ha effettuato almeno una prenotazione e ha effettuato
l’accesso.
Scenario principale Il cliente modifica o cancella una prenotazione esistente.
Scenari alternativi La prenotazione non ` e modificabile (es. troppo vicino alla data
d’arrivo), viene mostrato un messaggio di errore.
Post-condizioni La prenotazione ` e aggiornata o rimossa dal sistema.
Use Case - Richiesta servizi extra
Elemento Descrizione
Passi Azione 1. Il cliente accede alla sezione “Servizi Extra” della prenotazione.
2. Il cliente seleziona uno o pi` u servizi disponibili.
3. Il sistema aggiorna la prenotazione con i servizi richiesti.
Attori Cliente
Precondizioni Il cliente ha una prenotazione attiva.
Scenario principale Il cliente aggiunge servizi aggiuntivi (es. colazione, spa, lavande-
ria).
Scenari alternativi Alcuni servizi potrebbero non essere disponibili nelle date selezion-
ate.
Post-condizioni I servizi extra vengono associati alla prenotazione.
Use Case - Pagamento online
Elemento Descrizione
Passi Azione 1. Il cliente accede alla sezione pagamenti della prenotazione.
2. Seleziona il metodo di pagamento (es. carta di credito, PayPal).
3. Il sistema processa il pagamento e lo conferma.
Attori Cliente
Precondizioni Il cliente ha una prenotazione valida e accesso al sistema.
Scenario principale Il cliente paga online per la prenotazione.
Scenari alternativi Il pagamento pu` o fallire (es. carta rifiutata), viene mostrato un
messaggio d’errore.
Post-condizioni La prenotazione risulta pagata e pronta per il check-in.
8


---

<!-- Pagina PDF 10 -->
## 📑 Pagina 10

Use Case - Scrivi recensione
Elemento Descrizione
Passi Azione 1. Il cliente accede alla sezione “Recensioni”.
2. Verifica di aver soggiornato almeno una volta.
3. Inserisce un voto e un commento testuale.
4. Il sistema salva la recensione.
Attori Cliente
Precondizioni Il cliente ha almeno una prenotazione conclusa.
Scenario principale Il cliente recensisce l’hotel dopo il soggiorno.
Scenari alternativi Il cliente prova a recensire senza aver mai effettuato una preno-
tazione → messaggio di errore.
Post-condizioni La recensione viene salvata e mostrata pubblicamente.
9


---

<!-- Pagina PDF 11 -->
## 📑 Pagina 11

3.3 Use Case Amministrazione
3.3.1 Diagramma
3.3.2 Documentazione
Use Case - Gestione Prenotazioni e Assegnazione Camere
Elemento Descrizione
Passi Azione 1. L’Amministrazione visualizza le prenotazioni esistenti nel sis-
tema.
2. L’Amministrazione crea una nuova prenotazione su richiesta
del cliente.
3. L’Amministrazione modifica o cancella una prenotazione es-
istente.
4. L’Amministrazione verifica la disponibilit` a delle camere.
5. L’Amministrazione assegna una camera compatibile con le pref-
erenze del cliente.
Attori Amministrazione, cliente
Precondizioni L’Amministrazione ha effettuato il login al sistema.
Scenario principale L’Amministrazione gestisce le prenotazioni e assegna le camere ai
clienti.
Scenari alternativi 1. Se il cliente cambia data o preferenze, la prenotazione viene
aggiornata.
2. Se non ci sono camere disponibili del tipo scelto, vengono
proposte soluzioni alternative.
Post-condizioni Prenotazioni e assegnazioni sono aggiornate nel sistema.
10


---

<!-- Pagina PDF 12 -->
## 📑 Pagina 12

Use Case - Gestione Check-in / Check-out
Elemento Descrizione
Passi Azione 1. L’Amministrazione registra il check-in del cliente all’arrivo.
2. Registra il check-out del cliente alla partenza.
Attori Amministrazione
Precondizioni Il cliente ha una prenotazione confermata.
Scenario principale L’Amministrazione gestisce l’ingresso e l’uscita del cliente.
Scenari alternativi 1. Il sistema gestisce orari flessibili in caso di arrivo anticipato o
ritardato.
2. Eventuali anomalie durante il check-out vengono segnalate.
Post-condizioni Il soggiorno del cliente ` e registrato come completato.
Use Case - Gestione Reclami
Elemento Descrizione
Passi Azione 1. L’Amministrazione riceve un reclamo dal cliente.
2. Registra la segnalazione nel sistema.
3. Smista la segnalazione al reparto competente.
Attori Amministrazione, cliente
Precondizioni Il cliente ha effettuato una prenotazione.
Scenario principale L’Amministrazione gestisce e assegna le segnalazioni ai reparti.
Scenari alternativi 1. Le segnalazioni urgenti sono marcate con priorit` a alta.
2. Quelle generiche vengono messe in coda.
Post-condizioni La richiesta ` e stata presa in carico.
Use Case - Gestione Utenti nel Sistema
Elemento Descrizione
Passi Azione 1. L’Amministrazione (con permessi amministrativi) accede al
pannello utenti.
2. Crea un nuovo utente inserendo i dati e il ruolo.
3. Modifica i dati di un utente esistente.
4. Disattiva un utente non pi` u abilitato.
Attori Amministrazione (con ruolo amministratore)
Precondizioni L’Amministrazione ` e autenticato con privilegi di gestione utenti.
Scenario principale L’Amministrazione amministra gli account utente.
Scenari alternativi 1. Se l’utente non esiste, viene mostrato un errore.
2. Se gi` a disattivato, l’azione ` e bloccata.
Post-condizioni Il sistema utenti ` e aggiornato.
11


---

<!-- Pagina PDF 13 -->
## 📑 Pagina 13

Use Case - Monitoraggio Generale delle Attivit` a
Elemento Descrizione
Passi Azione 1. L’Amministrazione (con ruolo amministratore) accede alla
dashboard di monitoraggio.
2. Seleziona il tipo di statistica da visualizzare.
3. Il sistema mostra i dati aggiornati.
Attori Amministrazione (con ruolo amministratore)
Precondizioni Accesso autorizzato alla dashboard statistica.
Scenario principale L’Amministrazione monitora l’andamento della struttura.
Scenari alternativi 1. Se i dati non sono disponibili, il sistema segnala l’anomalia.
2. Se il filtro applicato ` e errato, viene richiesta la correzione.
Post-condizioni L’Amministrazione ha consultato i dati.
12


---

<!-- Pagina PDF 14 -->
## 📑 Pagina 14

3.4 Use Case Servizio
3.4.1 Diagramma
3.4.2 Documentazione
Use Case - Gestione Ordini dei Clienti
Elemento Descrizione
Passi Azione 1. Il sistema manda una notifica dell’ordine effettuato.
2. Il Ristoratore visualizza i dettagli dell’ordine (pietanza, n. cam-
era, ecc.).
3. L’ordine viene preparato, consegnato e contrassegnato ”com-
pleto”.
Attori Servizio, Cliente
Precondizioni Un Cliente effettua una richiesta di servizio ristorazione.
Scenario principale Il Servizio Ristorazione riceve e gestisce ordini in camera e in sala.
Scenari alternativi 3.1a L’ordine non soddisfa il cliente (pietanza sbagliata, mal
preparata, ecc.).
3.2a L’ordine deve essere ripreparato, modificato o annullato su
richiesta del cliente.
3.1b Il Cliente non ` e presente in camera.
3.2b L’ordine viene contrassegnato ”consegna fallita”.
Post-condizioni L’ordine del Cliente ` e stato gestito.
13


---

<!-- Pagina PDF 15 -->
## 📑 Pagina 15

Use Case - Aggiornamento Men` u
Elemento Descrizione
Passi Azione 1. Accesso all’area ”Modifica Men` u” e selezione men` u da modifi-
care.
2. Effettuare le modifiche desiderate, aggiunta o rimozione
pietanze.
3. Visualizzazione della versione aggiornata del Men` u.
Attori Servizio
Precondizioni L’utente ` e autorizzato alla modifica del men` u.
Scenario principale Il Servizio Ristorazione pu` o modificare i men` u, aggiungendo o
rimuovendo pietanze.
Scenari alternativi 2.1 Le modifiche non sono valide (dati insufficienti o con errori).
2.2 Il sistema mostra errore e ritorna al form di modifica.
Post-condizioni Il men` u ` e stato aggiornato ed ` e visualizzabile.
Use Case - Visualizzazione Camere da Pulire
Elemento Descrizione
Passi Azione 1. Accesso all’area ”Camere” e selezione ”visualizza camere da
pulire”.
2. Visualizzazione delle camere con necessit` a del servizio di
pulizia.
Attori Servizio
Precondizioni L’utente ` e autenticato come operatore di Servizio.
Scenario principale Il Servizio Pulizia pu` o visualizzare le camere con necessit` a di essere
pulite.
Scenari alternativi 2.1 Non sono presenti camere da pulire.
2.2 Il sistema notifica la non necessit` a del servizio.
Post-condizioni L’utente del Servizio di Pulizia ` e aggiornato sullo stato delle
camere e su quali hanno necessit` a del servizio.
Use Case - Modifica Stato Pulizia Camera
Elemento Descrizione
Passi Azione 1. Accesso all’area ”Camere”.
2. Selezione della camera di cui modificare lo stato.
3. Selezione ”modifica stato” con il nuovo stato.
4. Modifica avvenuta e ritorno all’area ”Camere” con la camera
aggiornata.
Attori Servizio
Precondizioni L’utente ` e autenticato come operatore di servizio.
Scenario principale Il Servizio Pulizia modifica lo stato di pulizia di una camera.
Scenari alternativi 3.1 Lo stato della camera inserito non ` e valido.
3.2 Il sistema mostra errore e ritorna all’area ”Camere”.
Post-condizioni Lo stato della camera ` e stato aggiornato.
14


---

<!-- Pagina PDF 16 -->
## 📑 Pagina 16

4 System Requirements
4.1 Requisiti Funzionali
•Il sistema software deve consentire al cliente di visualizzare, modificare o cancellare le prenotazioni
effettuate.
•Il sistema software deve permettere al cliente di selezionare e richiedere servizi extra associati
alla prenotazione.
•Il sistema software deve consentire al cliente di effettuare il pagamento online tramite metodi
come carta di credito o PayPal.
•Il sistema software deve permettere al cliente di inserire una recensione relativa al soggiorno,
comprensiva di voto e commento.
•Il sistema software deve permettere all’amministrazione di visualizzare, creare, modificare o can-
cellare le prenotazioni dei clienti.
•Il sistema software deve consentire all’amministrazione di assegnare camere disponibili in base
alle preferenze indicate dal cliente.
•Il sistema software deve permettere all’amministrazione di gestire le operazioni di check-in e
check-out.
•Il sistema software deve consentire all’amministrazione di ricevere, registrare e smistare reclami
dei clienti.
•Il sistema software deve consentire all’amministrazione (con ruolo amministratore) di gestire gli
account utente: creazione, modifica, disattivazione.
•Il sistema software deve fornire una dashboard di monitoraggio accessibile all’amministrazione
per visualizzare statistiche sull’andamento della struttura.
•Il sistema software deve permettere al personale del servizio di visualizzare, preparare, contrasseg-
nare come completati o falliti gli ordini.
•Il sistema software deve consentire la modifica dei menu da parte del personale autorizzato.
•Il sistema software deve consentire al personale addetto alla pulizia di visualizzare le camere da
pulire e modificarne lo stato.
4.2 Requisiti Non Funzionali
•Il sistema software deve essere accessibile tramite browser moderni e supportare un’interfaccia
responsive per dispositivi mobili.
•Il sistema software non deve rilasciare ai suoi operatori nessuna informazione personale relativa
ai clienti, tranne nominativo e identificatore.
•Il sistema software deve completare le operazioni critiche (login, prenotazione, pagamento) in
meno di 3 secondi in condizioni normali.
•I documenti di progetto (derivabili) devono essere conformi allo standard ISO/IEC 25010.
•Il sistema software deve implementare un sistema di autenticazione sicuro, con protezione da
accessi non autorizzati.
•Il sistema software deve mantenere la disponibilit` a dei servizi anche in caso di malfunzionamenti
parziali.
•Il sistema software deve essere documentato con specifiche tecniche aggiornate per facilitare la
manutenzione.
•Il sistema software deve supportare il tracciamento delle attivit` a utente (audit log) per garantire
la rintracciabilit` a.
15


---

<!-- Pagina PDF 17 -->
## 📑 Pagina 17

4.3 Requisiti di Dominio
•Il sistema software deve impedire la modifica o la cancellazione delle prenotazioni se queste sono
troppo vicine alla data di arrivo, secondo le politiche aziendali.
•Il sistema software deve mostrare solo i servizi extra effettivamente disponibili per il periodo
selezionato dal cliente.
•Il sistema software deve rispettare le normative sulla protezione dei dati personali secondo il
Regolamento Generale sulla Protezione dei Dati (GDPR).
•Il sistema software deve permettere la gestione delle camere in base allo stato di pulizia, aggior-
nato dal personale di servizio dopo ogni soggiorno.
16


---

<!-- Pagina PDF 18 -->
## 📑 Pagina 18

5 System Architectural Models
5.1 Activity Diagrams
5.1.1 Activity Diagram Utente
Activity Diagram - Operazione Utente
17


---

<!-- Pagina PDF 19 -->
## 📑 Pagina 19

Activity Diagram - Registrazione Utente
18


---

<!-- Pagina PDF 20 -->
## 📑 Pagina 20

Activity Diagram - Visualizzazione Offerte Utente
19


---

<!-- Pagina PDF 21 -->
## 📑 Pagina 21

5.1.2 Activity Diagram Cliente
Activity Diagram - Cliente Effettua Prenotazione
20


---

<!-- Pagina PDF 22 -->
## 📑 Pagina 22

Activity Diagram - Cliente Gestione Prenotazione
21


---

<!-- Pagina PDF 23 -->
## 📑 Pagina 23

Activity Diagram - Cliente fa Recensione
22


---

<!-- Pagina PDF 24 -->
## 📑 Pagina 24

5.1.3 Activity Diagram Amministrazione
Activity Diagram - Amministazione Check-In e Check-Out
23


---

<!-- Pagina PDF 25 -->
## 📑 Pagina 25

Activity Diagram - Amministrazione Gestione Utenti
24


---

<!-- Pagina PDF 26 -->
## 📑 Pagina 26

Activity Diagram - Amministrazione Monitoraggio
25


---

<!-- Pagina PDF 27 -->
## 📑 Pagina 27

Activity Diagram - Amministrazione Prenotazione
26


---

<!-- Pagina PDF 28 -->
## 📑 Pagina 28

5.1.4 Activity Diagram Servizio
Activity Diagram - Servizio Aggiornamento Men` u
27


---

<!-- Pagina PDF 29 -->
## 📑 Pagina 29

Activity Diagram - Servizio Gestione Ordini Cliente
28


---

<!-- Pagina PDF 30 -->
## 📑 Pagina 30

Activity Diagram - Segnala Completamento Pulizia
29


---

<!-- Pagina PDF 31 -->
## 📑 Pagina 31

Activity Diagram - Servizio Pulizia Camere
30


---

<!-- Pagina PDF 32 -->
## 📑 Pagina 32

Activity Diagram - Servizio Visualizzazione Camere da Pulire
31


---

<!-- Pagina PDF 33 -->
## 📑 Pagina 33

5.2 Sequence Diagrams
5.2.1 Sequence Diagram Utente
Sequence Diagram - Utente Accesso
32


---

<!-- Pagina PDF 34 -->
## 📑 Pagina 34

Sequence Diagram - Utente Operazione Account
33


---

<!-- Pagina PDF 35 -->
## 📑 Pagina 35

Sequence Diagram - Utente Registrazione Account
34


---

<!-- Pagina PDF 36 -->
## 📑 Pagina 36

5.2.2 Sequence Diagram Cliente
Sequence Diagram - Cliente Aggiunta Servizio
35


---

<!-- Pagina PDF 37 -->
## 📑 Pagina 37

Sequence Diagram - Cliente Elimina Prenotazione
36


---

<!-- Pagina PDF 38 -->
## 📑 Pagina 38

Sequence Diagram - Cliente Pagamento Online
37


---

<!-- Pagina PDF 39 -->
## 📑 Pagina 39

Sequence Diagram - Cliente Effettua Prenotazione
38


---

<!-- Pagina PDF 40 -->
## 📑 Pagina 40

Sequence Diagram - Cliente Effettua Reensione
39


---

<!-- Pagina PDF 41 -->
## 📑 Pagina 41

Sequence Diagram - Cliente Modifica Prenotazione
40


---

<!-- Pagina PDF 42 -->
## 📑 Pagina 42

Sequence Diagram - Cliente Gestisce Ordine
41


---

<!-- Pagina PDF 43 -->
## 📑 Pagina 43

5.2.3 Sequence Diagram Amministrazione
Sequence Diagram - Serivizio Modifica Stato Camera
42


---

<!-- Pagina PDF 44 -->
## 📑 Pagina 44

Sequence Diagram - Servizio Gestione Ordine
Sequence Diagram - Servizio Visualizzazione Camere
43


---

<!-- Pagina PDF 45 -->
## 📑 Pagina 45

44


---

<!-- Pagina PDF 46 -->
## 📑 Pagina 46

Sequence Diagram - Servizio Modifica Men` u
45


---

<!-- Pagina PDF 47 -->
## 📑 Pagina 47

5.2.4 Sequence Diagram Servizio
Sequence Diagram - Amministrazione Check-in e Check-out
46


---

<!-- Pagina PDF 48 -->
## 📑 Pagina 48

Sequence Diagram - Amministrazione Cancella Prenotazione
47


---

<!-- Pagina PDF 49 -->
## 📑 Pagina 49

Sequence Diagram - Amministrazione Crea Utenti
48


---

<!-- Pagina PDF 50 -->
## 📑 Pagina 50

Sequence Diagram - Amministrazione Inserimento Offerta
49


---

<!-- Pagina PDF 51 -->
## 📑 Pagina 51

Sequence Diagram - Amministrazione Operazioni su Utente
50


---

<!-- Pagina PDF 52 -->
## 📑 Pagina 52

Sequence Diagram - Amministrazione Modifica Prenotazione
51


---

<!-- Pagina PDF 53 -->
## 📑 Pagina 53

Sequence Diagram - Amministrazione Modulo Reclamo
52


---

<!-- Pagina PDF 54 -->
## 📑 Pagina 54

Sequence Diagram - Amministrazione Monitoraggio Attivit` a
53


---

<!-- Pagina PDF 55 -->
## 📑 Pagina 55

Sequence Diagram - Amministrazione Crea Prenotazione
54


---

<!-- Pagina PDF 56 -->
## 📑 Pagina 56

5.3 Class Diagrams
5.3.1 Class Diagram Unrefined
55


---

<!-- Pagina PDF 57 -->
## 📑 Pagina 57

5.3.2 Class Diagram Refined
56


---

<!-- Pagina PDF 58 -->
## 📑 Pagina 58

6 Design Patterns
Design Pattern - Decorator Prenotazione
Nel contesto della gestione di prenotazioni alberghiere, pu` o essere utile strutturare il sistema in
modo flessibile, cos` ı che a una prenotazione base possano essere aggiunti dinamicamente uno o pi` u
servizi extra (come colazione o spa), senza dover creare una classe diversa per ogni combinazione
possibile. Per ottenere questo comportamento modulare e scalabile, adottiamo il pattern strutturale
Decorator , che consente di estendere dinamicamente le funzionalit` a ad un oggetto Prenotazione senza
modificarne la struttura.
Design Pattern - Factory Method Servizio
Ogni dipendente dell’hotel che svolge un servizio (nel nostro caso Ristorazione e Pulizia) appartiene
alla classe Servizio. In un,ottica pi` u specializzata si pu` o applicare il Design Pattern Factory Method per
delegare la creazione del servizio specifico per ogni dipendente alla Factory associata. Questo, inoltre
57


---

<!-- Pagina PDF 59 -->
## 📑 Pagina 59

ci permette di implementare, in futuro, nuove Factory per eventuali nuovi servizi eventualmente forniti
dall’hotel.
Design Pattern - Observer Ordini Ristorazione
Nella nostra analisi risulta responsabilit` a del Dipendente adibito al Servizio di Ristorazione il
monitoraggio e la gestione di eventuali nuovi ordini creati e inviati dal Cliente. `E pi` u consigliabile,
nonch´ e banalmente pi` u sicuro e utile, sia presente un Observer che venga notificato all’invio dell’ordine,
in modo che possa essere gestito on demand. In modo tale il Dipendente che gestisce l’ordine non ha
pi` u la responsabilit` a di accertarsi che non ci siano nuovi ordini.
Design Pattern - Observer Modulo Reclamo
Per la gestione dei reclami ` e stato adottato il design pattern Observer con l’obiettivo di separare
la logica di notifica e monitoraggio dallo stato interno del modulo di reclamo. In particolare, ogni
volta che lo stato o la priorit` a di un reclamo cambia, il sistema notifica automaticamente tutti gli
observer registrati come SistemaMonitoraggio senza accoppiare direttamente il modulo reclamo con
i componenti esterni. Questo approccio migliora la modularit` a e consente di estendere il sistema
facilmente aggiungendo nuovi observer senza modificare la logica del reclamo stesso.
58


---