# MyAma — Idea del progetto

## A cosa serve questo documento

Questo file serve semplicemente a far capire a tutto il gruppo **che progetto vogliamo realizzare**.

Non è ancora la specifica da consegnare al professore e non contiene la parte metodologica di Ingegneria del Software. Non dobbiamo quindi preoccuparci, per ora, di Use Case, Class Diagram, Sequence Diagram o Design Pattern.

L'obiettivo è molto più semplice:

> dopo aver letto questo documento, tutti i membri del gruppo devono avere in testa la stessa idea di MyAma e sapere, a grandi linee, che cosa dovrebbe fare il sistema.

---

# L'idea in breve

**MyAma** è una piattaforma digitale pensata per gestire la prenotazione e l'organizzazione del ritiro o del conferimento di **rifiuti ingombranti**.

L'idea nasce da un precedente progetto sviluppato nell'ambito di Basi di Dati e viene ora riutilizzata come dominio per il progetto di Ingegneria del Software.

Il funzionamento di base è semplice:

- un cittadino deve liberarsi di un rifiuto ingombrante;
- accede a MyAma;
- indica il tipo di rifiuto e le informazioni necessarie;
- sceglie come consegnarlo:
  - **ritiro a domicilio**;
  - **conferimento presso una sede AMA**;
- il sistema gestisce la prenotazione tenendo conto della zona, delle disponibilità e delle risorse necessarie;
- i lavoratori AMA visualizzano e gestiscono le attività che sono state assegnate loro.

Quindi MyAma mette in contatto due esigenze:

- il cittadino vuole prenotare il servizio in modo semplice;
- AMA deve organizzare correttamente sedi, lavoratori, veicoli e prenotazioni.

---

# Quale problema vogliamo affrontare

L'idea parte da un problema molto concreto: organizzare un servizio di ritiro dei rifiuti ingombranti richiede di coordinare molte informazioni.

Non basta sapere che un cittadino vuole effettuare un ritiro.

Bisogna anche sapere, ad esempio:

- dove si trova;
- quale sede serve quella zona;
- quale rifiuto deve essere ritirato;
- quando vuole effettuare il servizio;
- quali lavoratori sono disponibili;
- quale veicolo può essere utilizzato;
- se il mezzo è adatto al carico previsto.

Allo stesso modo, se il cittadino decide di portare personalmente il rifiuto presso una sede, deve sapere:

- quali sedi sono disponibili;
- quale sede è compatibile con la propria zona;
- quando può presentarsi;
- come viene registrato e completato il conferimento.

L'idea di MyAma è quindi quella di **centralizzare queste informazioni in un unico sistema**, invece di trattarle come operazioni separate e poco coordinate.

---

# I due servizi principali

Il cuore di MyAma ruota attorno a due possibilità.

## Ritiro a domicilio

Il cittadino richiede che il rifiuto venga ritirato presso il proprio domicilio.

A grandi linee:

1. il cittadino accede al sistema;
2. indica il rifiuto da ritirare;
3. specifica il luogo del ritiro;
4. il sistema controlla che la zona sia servita;
5. vengono mostrate le disponibilità compatibili;
6. il cittadino sceglie data e orario;
7. la prenotazione viene registrata;
8. AMA organizza il personale e il veicolo necessari;
9. l'autista effettua il ritiro;
10. l'esito del servizio viene registrato.

In questo caso entrano quindi in gioco soprattutto:

- cittadino;
- prenotazione;
- indirizzo/CAP;
- rifiuto;
- autista;
- veicolo;
- disponibilità.

## Conferimento presso una sede AMA

Il cittadino può invece decidere di trasportare autonomamente il rifiuto presso una sede o centro di raccolta.

In questo caso:

1. il cittadino indica il rifiuto;
2. il sistema individua le sedi compatibili;
3. il cittadino sceglie una sede;
4. seleziona una data o fascia disponibile;
5. viene registrata la prenotazione;
6. il cittadino si presenta presso la sede;
7. un operatore verifica e conclude il conferimento.

Qui diventano particolarmente importanti:

- cittadino;
- prenotazione;
- sede;
- CAP/zona;
- operatore di sede;
- rifiuto.

---

# Chi utilizza MyAma

## Cittadino / Cliente
È la persona che utilizza il servizio per smaltire un rifiuto ingombrante.

Le attività centrali che immaginiamo per il cittadino sono:

- accedere al sistema;
- richiedere un ritiro a domicilio;
- prenotare un conferimento presso una sede;
- indicare le informazioni sul rifiuto;
- scegliere tra le disponibilità offerte;
- consultare le proprie prenotazioni;
- eventualmente modificare o annullare una richiesta quando consentito.

Il cittadino non deve occuparsi dell'organizzazione interna di AMA: non decide quale lavoratore o quale veicolo verrà assegnato.

## Autista AMA
È il lavoratore che si occupa dei ritiri a domicilio.

Dovrebbe poter vedere le attività che gli vengono assegnate e le informazioni necessarie per svolgerle, ad esempio:

- luogo del ritiro;
- data e orario;
- rifiuto da ritirare;
- eventuali informazioni operative utili.

Dopo il servizio registra l'esito del ritiro.

## Operatore di sede
Lavora presso il centro in cui il cittadino porta personalmente il rifiuto.

Dovrebbe poter:

- vedere le prenotazioni previste per la sede;
- verificare la prenotazione del cittadino;
- gestire l'arrivo del rifiuto;
- registrare l'esito del conferimento.

## Gestione operativa AMA
È probabile che serva anche una figura che gestisca gli aspetti organizzativi del servizio, ad esempio:

- sedi;
- zone/CAP serviti;
- lavoratori;
- disponibilità;
- veicoli;
- assegnazioni.

Il ruolo preciso di questa figura dovrà essere definito meglio quando inizieremo la specifica.

---

# Le informazioni principali che MyAma deve gestire

Senza parlare ancora di classi software o database, possiamo già riconoscere alcuni concetti centrali del dominio:

- **Cliente**
- **Prenotazione**
- **Rifiuto**
- **Tipologia di rifiuto**
- **Sede AMA**
- **CAP / zona servita**
- **Lavoratore AMA**
- **Autista**
- **Operatore di sede**
- **Veicolo**
- **Disponibilità**

Questi concetti derivano direttamente dal funzionamento del servizio e saranno il punto di partenza quando inizieremo a modellare il sistema.

---

# Alcune regole importanti del servizio

MyAma non è soltanto un elenco di funzioni: esistono anche regole che collegano le varie informazioni.

Per esempio:

- una sede serve soltanto determinate zone o CAP;
- un cittadino deve poter visualizzare soltanto opzioni compatibili con la propria zona;
- per un ritiro a domicilio devono esserci risorse disponibili;
- un veicolo non può essere utilizzato oltre la propria capacità;
- un lavoratore può svolgere soltanto attività compatibili con il proprio ruolo e la propria disponibilità;
- una prenotazione può cambiare stato durante la sua gestione;
- un servizio completato deve essere distinguibile da uno annullato o non eseguito.

Queste regole saranno importanti più avanti perché ci aiuteranno a trasformare l'idea generale in requisiti precisi.

---

# Funzionalità che possiamo valutare

Il vecchio progetto MyAma contiene anche altre possibilità interessanti, ma per il momento non dobbiamo considerarle tutte automaticamente parte del progetto.

Tra queste:

- caricamento di una foto del rifiuto;
- calcolo di un eventuale costo;
- notifiche per conferme o modifiche;
- storico delle prenotazioni;
- valutazione del servizio;
- statistiche e reportistica interna;
- autenticazione tramite SPID.

Sono tutte idee compatibili con il dominio, ma verranno valutate insieme quando definiremo meglio il perimetro del progetto.

La regola sarà:

> prima definiamo bene il nucleo di MyAma, poi decidiamo quali funzionalità aggiuntive servono davvero.

---

# Un esempio molto semplice

Immaginiamo un cittadino che deve smaltire un vecchio armadio.

Accede a MyAma e sceglie il **ritiro a domicilio**.

Inserisce le informazioni richieste sul rifiuto e il proprio indirizzo.

Il sistema verifica la zona e propone le disponibilità possibili.

Il cittadino sceglie un appuntamento e conferma.

A questo punto la prenotazione entra nella parte organizzativa di AMA: devono essere individuate le risorse necessarie per effettuare il servizio.

L'autista vede il ritiro assegnato, raggiunge l'indirizzo e registra l'esito dell'operazione.

Lo stesso sistema deve permettere al cittadino di scegliere, quando possibile, l'alternativa del **conferimento presso una sede AMA**.

Questo esempio riassume abbastanza bene l'idea centrale del progetto.

---

# Cosa non stiamo decidendo adesso

Questo documento serve solo ad allineare il gruppo sull'idea.

Non stiamo ancora decidendo:

- come sarà strutturato il software internamente;
- quali classi UML esisteranno;
- quanti Use Case avremo;
- quali diagrammi realizzeremo;
- quali Design Pattern utilizzeremo;
- quale tecnologia verrà usata;
- come sarà fatto il database;
- come divideremo il lavoro tra i membri del gruppo.

Queste decisioni verranno prese progressivamente durante il progetto.

In particolare, non vogliamo scegliere in anticipo dei Design Pattern e poi modificare artificialmente MyAma per riuscire a inserirli.

Prima modelleremo bene il sistema; solo successivamente vedremo quali problemi progettuali emergono realmente.

---

# In sintesi

MyAma è un sistema per organizzare in modo digitale il servizio di gestione dei rifiuti ingombranti.

Il cittadino deve poter scegliere principalmente tra:

- **ritiro a domicilio**;
- **conferimento presso una sede AMA**.

Il sistema deve poi coordinare le informazioni necessarie affinché il servizio possa essere effettivamente svolto, coinvolgendo:

- cittadini;
- prenotazioni;
- sedi;
- zone;
- lavoratori;
- veicoli;
- rifiuti.

Per il momento questa è la cosa più importante da condividere:

> **stiamo progettando un sistema che permette al cittadino di prenotare facilmente lo smaltimento di un rifiuto ingombrante e ad AMA di organizzare in modo coerente il servizio necessario per soddisfare quella richiesta.**

Da questa idea comune partiremo poi per costruire, con la guida di progetto, la vera specifica di MyAma.
