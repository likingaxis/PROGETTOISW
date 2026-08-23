# 📄 Documento di Specifica: MyAma (Basi di Dati)

> **Autori**: Samuele De Santis, Luca Gugliotta, Davide Luci  
> **Pagine totali**: 30  
> **Trascrizione**: Estratta dal documento originale per consultazione testuale diretta.

---


<!-- Pagina PDF 1 -->
## 📑 Pagina 1

Basi di Dati e di Conoscenza
 2023/2023
Documento di specifica: < MyAma>
Progetto < MyAma – Gestione prenotazioni per rifiuti ingombranti >
Autori:
• Samuele De Santis
• Luca Gugliotta
• Davide Luci
Corso di Laurea :  Informatica
Data: 2024/2025
1. Parte Prima: Generalità
1.1. Descrizione generale del prodotto
Il progetto riguarda la realizzazione di un sistema informativo per un portale AMA (ispirato
all’Azienda Municipale Ambiente), pensato per consentire ai cittadini la prenotazione del
ritiro o la consegna in sede di rifiuti ingombranti.
Il portale permette la gestione completa degli utenti, dei lavoratori, delle sedi AMA, dei veicoli
impiegati e delle prenotazioni. Il sistema tiene conto della disponibilità dei lavoratori e dei
vincoli logistici, come il codice di avviamento postale (CAP) e la capacità dei veicoli.
1.2. Obiettivi del Progetto:
(con priorità assegnata da   a      )
OBIETTIVI PRIMARI
•       Consentire la registrazione dei clienti  (codice fiscale, nome, cognome,
e-mail, password, numero di telefono).
•       Consentire la registrazione dei lavoratori AMA  (CID, nome, cognome,
data di nascita, ruolo, e-mail, orari lavorativi, numero di telefono).
•      Consentire ai clienti di prenotare un ritiro a domicilio  oppure scegliere di
portare il rifiuto presso una sede.
•      Validare la disponibilità di lavoratori e veicoli  per le prenotazioni a
domicilio.
•      Permettere la scelta di data, ora e luogo, con limitazioni sul CAP servito.
•      Visualizzare l’elenco delle sedi AMA disponibili in base alla zona del cliente.
•     Calcolare il costo della prenotazione  in base alla tipologia del rifiuto e al
peso stimato.
•     Gestire le assegnazioni dei lavoratori e dei veicoli  alle singole
prenotazioni.


---

<!-- Pagina PDF 2 -->
## 📑 Pagina 2

Basi di Dati e di Conoscenza
 2023/2023
•    Permettere l’upload di una foto del rifiuto per valutazioni preliminari.
•    Gestire un archivio delle tipologie di rifiuti, con relativi costi e categorie.
OBIETTIVI SECONDARI
•       Sistema di notifica simulato  per comunicare conferme,
modifiche o annullamenti delle prenotazioni.
•       Controllo del carico massimo dei veicoli , per evitare che
vengano assegnati a prenotazioni eccedenti la capacità.
•     Gestione dello storico delle prenotazi  oni per ciascun cliente,
con visualizzazione di stato, data, costo e modalità (ritiro o consegna).
•     Reportistica interna per AMA, con statistiche su:
o Numero di ritiri per zona o sede;
o Tipologie di rifiuti più frequenti;
o Carico di lavoro medio per lavoratore.
•     Valutazione del servizio  da parte del cliente dopo il ritiro, con
voto (1–5) e commento.
•    Gestione dei CAP serviti  da ogni sede, per mostrare solo le opzioni
valide durante la prenotazione.
1.3. Utenti
1. Cliente
Profilo
È il cittadino che utilizza il portale per prenotare il ritiro o la consegna di rifiuti
ingombranti. L’accesso è consentito tramite registrazione con SPID o credenziali
tradizionali.
Obiettivi e bisogni
• Accedere facilmente al servizio.
• Prenotare un ritiro o una consegna in autonomia.
• Visualizzare solo le opzioni compatibili con la propria zona.
• Caricare informazioni dettagliate sul rifiuto (foto, peso, tipologia).
• Essere informato su costi, disponibilità e tempistiche.
• Monitorare lo storico delle proprie prenotazioni.
• Valutare il servizio ricevuto.
Azioni consentite
• Registrarsi.
• Prenotare ritiro o consegna.


---

<!-- Pagina PDF 3 -->
## 📑 Pagina 3

Basi di Dati e di Conoscenza
 2023/2023
• Selezionare data, ora, sede.
• Caricare foto e specifiche del rifiuto.
• Visualizzare e cancellare prenotazioni attive.
• Lasciare valutazioni post-servizio.
Limitazioni
• Nessun accesso ai dati di altri clienti o lavoratori.
• Nessuna visibilità su veicoli, orari e assegnazioni interne.
2. Lavoratore AMA
Profilo
 È un operatore incaricato della gestione fisica dei rifiuti. Si divide in:
• Autista: gestisce il ritiro a domicilio, è associato a uno o più veicoli.
• Operatore di sede: lavora nei centri AMA dove i clienti portano i rifiuti.
Obiettivi e bisogni
• Visualizzare le prenotazioni assegnate in base al proprio ruolo.
• Registrare l’esito del ritiro o della consegna.
• Operare solo nei turni assegnati.
• Interagire solo con i dati operativi strettamente necessari.
Azioni consentite
• Visualizzare le prenotazioni assegnate.
• Segnalare problemi o confermare l’avvenuto ritiro/consegna.
• Consultare CAP e dati di contatto operativi dei clienti.
Limitazioni
• Nessuna possibilità di modificare o creare nuove prenotazioni.
• Nessun accesso ai dati personali completi dei clienti.
• Nessun privilegio amministrativo.
3. Amministratori e gestori del database
Profilo
 Sono figure tecniche incaricate della gestione e manutenzione del sistema e del
database sottostante.
Obiettivi e bisogni
• Garantire l’integrità dei dati e la sicurezza del sistema.
• Monitorare e ottimizzare le performance.
• Intervenire in caso di errori o anomalie.
• Gestire ruoli, accessi e configurazioni.
Azioni consentite
• Gestire tabelle, vincoli, utenti e ruoli.


---

<!-- Pagina PDF 4 -->
## 📑 Pagina 4

Basi di Dati e di Conoscenza
 2023/2023
• Assegnare permessi.
• Eseguire backup, verifiche e report.
• Monitorare l'attività del sistema.
Limitazioni
• Non interagiscono operativamente con le prenotazioni.
• Non possono agire come clienti o lavoratori nel sistema.
2. Parte seconda: Raccolta e analisi dei Requisiti
• Utenti (interviste, documentazione scritta)
• Analisi dell’utente: a quali utenti è destinato il progetto?
Il progetto “MyAma“ è destinato a due categorie principali di utenti:
1. Cittadini di Roma (Clienti)
Rappresentano i fruitori finali del servizio. Sono persone fisiche che, tramite il portale, possono
prenotare facilmente il ritiro o la consegna in sede dei propri rifiuti ingombranti.  Questo
progetto ha lo scopo, per loro, di:
• facilitare richieste di prenotazione per gettare rifiuti ingombranti nei modi più semplici e
corretti per l'ambiente
• avere una visione ampia di tutti i servizi che può offrire la piattaforma “MyAma” e che ci
si possa interagire facilmente
2. Lavoratori AMA (Operatori e Autisti)
Sono i dipendenti operativi dell’azienda, incaricati del ritiro o della ricezione dei rifiuti
ingombranti. Per loro il progetto è fondamentale per:
• avere una piattaforma che consent a di lavorare in maniera uniforme e organizzata ,
senza mancanze di dettagli e informazioni
• Analisi dei bisogni: quali sono le necessità di tali utenti?
1. Cittadini di Roma (Clienti)
• Avere un servizio semplice, trasparente e accessibile anche tramite SPID.
• Ridurre al minimo i passaggi burocratici nella prenotazione.
• Ricevere un’esperienza utente chiara e intuitiva, con informazioni dettagliate su costi,
tipologie di rifiuti e disponibilità.
• Contribuire allo smaltimento corretto dei rifiuti, nel rispetto dell’ambiente.
• Avere visibilità completa sui servizi disponibili tramite la piattaforma e poter interagire
in modo autonomo con lo storico, le valutazioni e le modifiche alle prenotazioni.


---

<!-- Pagina PDF 5 -->
## 📑 Pagina 5

Basi di Dati e di Conoscenza
 2023/2023
2. Lavoratori AMA (Operatori e Autisti)
• Disporre di una piattaforma chiara, funzionale e coerente, che consenta di lavorare in
modo uniforme e organizzato.
• Accedere alle prenotazioni assegnate con tutte le informazioni necessarie (luogo, orario,
tipo di rifiuto, dati operativi del cliente).
• Evitare errori dovuti a informazioni mancanti o disorganizzate.
• Semplificare il flusso operativo giornaliero, migliorando la produttività e la gestione del
tempo.
• Documentazione esistente (normative, leggi e regolamenti del settore, regolamenti
interni, procedure aziendali, moduli)
Il progetto MyAma si inserisce all’interno del contesto normativo e operativo legato alla
gestione dei rifiuti urbani. Le fonti rilevanti da considerare includono:
• Normative nazionali e locali sullo smaltimento dei rifiuti ingombranti, come:
o Regolamento AMA su rifiuti speciali e ingombranti.
o Codice dell’Ambiente (D.Lgs. 152/2006).
o Regolamenti comunali di Roma Capitale in materia ambientale.
• Procedure aziendali AMA:
o Prenotazione via telefono o sito web tradizionale.
o Verifica manuale della disponibilità di sedi e operatori.
o Coordinamento tra sedi e squadre tramite strumenti eterogenei (e -mail, fogli
Excel, telefonate).
• Modulistica:
o Modulo cartaceo o online per prenotazione del ritiro.
o Documenti di identificazione rifiuto per l'accettazione in sede.
o Moduli di autorizzazione al trasporto e tracciabilità.
• Regole interne:
o Suddivisione operativa tra autisti e operatori di sede.
o Turnazione dei lavoratori e assegnazione veicoli.
o Obbligo di comunicazione dell’avvenuto ritiro o di eventuali problemi.
• Realizzazioni preesistenti (applicativi da rimpiazzare, applicazioni che dovranno
interagire col sistema da realizzare)
Attualmente, la gestione delle prenotazioni AMA avviene tramite sistemi obsoleti o
frammentati, che il progetto MyAma si propone di centralizzare e sostituire:
• Applicativi da rimpiazzare:
o Moduli di prenotazione online statici, non integrati con la disponibilità reale di
personale e veicoli.
o Sistemi manuali di gestione turni (Excel o cartacei).
o Scambi informativi non tracciati tra clienti e personale operativo.
• Applicazioni da integrare:
o Sistema SPID per l’autenticazione dei cittadini.
o Eventuale CRM interno AMA per storicizzazione e report.
o Sistema interno per la gestione dei turni e dei veicoli (se digitalizzato).
o Eventuale sistema di notifiche (e -mail o SMS gateway) per conferme o
promemoria.


---

<!-- Pagina PDF 6 -->
## 📑 Pagina 6

Basi di Dati e di Conoscenza
 2023/2023
Il progetto MyAma punta a offrire una piattaforma centralizzata , accessibile da tutte le
classi di utenti, che migliori l’efficienza operativa, riduca gli errori e semplifichi l’accesso al
servizio per i cittadini.
2.1. Elenco dei requisiti
• Sicurezza dei dati : controllo degli accessi e gestione delle credenziali (con
crittografia delle password), uso di SPID per l’autenticazione sicura dei cittadini.
• Scalabilità: il sistema deve essere in grado di gestire molteplici prenotazioni
contemporanee da parte di clienti e operatori, specialmente in orari di picco.
• Backup e persistenza: salvataggio periodico dei dati e garanzia di integrità in caso
di malfunzionamenti o aggiornamenti.
• Privacy: rispetto della normativa GDPR per la protezione dei dati personali dei
clienti e dei lavoratori AMA.
• Gestione contenuti: gestione e controllo di:
• Tipologie di rifiuti e costi associati;
• Dati operativi delle prenotazioni (foto, peso, descrizione);
• Disponibilità lavoratori, veicoli e sedi;
• Cronologia delle operazioni e notifiche simulate.
• Validazioni logiche : impedire prenotazioni duplicate, gestire limiti di orario, CAP
non serviti, carico massimo veicoli.
• Interazione tra utenti : il cliente può lasciare valutazioni dopo il servizio, e
ricevere notifiche simulate su stato e modifiche della prenotazione.
• Interfaccia utente: semplice, chiara, accessibile anche da dispositivi mobili; uso di
SPID per semplificare la registrazione.
• Gestione differenziata dei ruoli : permessi e viste diverse per clienti, autisti,
operatori e amministratori.
• Manutenzione del sistema : il database deve essere aggiornato e monitorato
periodicamente dagli amministratori tecnici.
• Disponibilità del sistema : il portale deve essere disponibile h24, salvo brevi
periodi di manutenzione programmata.
• Accesso concorrente : il sistema deve supportare l’accesso contemporaneo da
parte di più utenti (clienti e operatori), senza riduzioni di prestazioni.
2.2. Glossario dei termini
Termine Significato
Cliente Cittadino registrato che effettua prenotazioni per lo smaltimento rifiuti.
Lavoratore AMA Dipendente operativo (autista o operatore di sede).
Prenotazione Richiesta da parte del cliente per il ritiro o la consegna di un rifiuto.
Ritiro a domicilio Servizio svolto da un autista AMA per raccogliere rifiuti dal domicilio.
Sede AMA Centro fisico dove è possibile portare i rifiuti ingombranti.


---

<!-- Pagina PDF 7 -->
## 📑 Pagina 7

Basi di Dati e di Conoscenza
 2023/2023
CAP Codice di Avviamento Postale, usato per limitare disponibilità per zona.
Rifiuto
ingombrante Oggetto di grandi dimensioni non smaltibile tramite raccolta ordinaria.
SPID Sistema Pubblico di Identità Digitale, usato per l'autenticazione.
Autista Lavoratore AMA che effettua i ritiri con un veicolo.
Operatore di sede Lavoratore AMA che accoglie rifiuti portati direttamente in sede.
Veicolo Mezzo utilizzato dagli autisti per effettuare ritiri.
Amministratore Figura tecnica con accesso completo al sistema e al database.
Notifica simulata Campo nel database che informa il cliente su modifiche/stato delle
operazioni.
Storico delle
prenotazioni Elenco delle richieste precedenti effettuate da un cliente.
2.3. Dimensionamento dei dati
L’applicativo MyAma nasce per operare all’interno del contesto urbano della città di Roma e dei
comuni limitrofi in cui AMA svolge il proprio servizio. Considerando l’estensione e la densità
abitativa dell’area servita, si stima una platea potenziale composta da oltre due milioni di
utenti. A questi si aggiunge il personale AMA, formato da migliaia di lavoratori , suddivisi in
ruoli operativi (autisti e operatori di sede) e figure di coordinamento o amministrative.
Ogni anno, l’azienda gestisce un elevato numero di prenotazioni  per il ritiro o la consegna
di rifiuti ingombranti. Ciascuna di queste prenotazioni comporta l’archiviazione di dati
strutturati (data, sede, tipo di rifiuto, peso stimato, costo), contenuti multimediali  (foto
allegate dal cliente) e informazioni operative (lavoratore e veicolo assegnato).
Il sistema dovrà quindi essere in grado di sostenere un carico notevole , con accessi
simultanei frequenti da parte sia dei clienti sia degli operatori, in particolare durante le fasce
orarie di punta o in occasione di campagne di raccolta straordinaria.
Alla luce di queste considerazioni, il database dovrà offrire prestazioni costanti anche in
condizioni di carico elevato , assicurando l’integrità dei dati e supportando operazioni in
tempo reale. Sarà inoltre fondamentale garantire la scalabilità del sistema , per consentire
un’estensione futura ad altri comuni, ad altri tipi di rifiuto (es. RAEE o pericolosi), o
all’integrazione con servizi esterni.
2.4. Elenco operazioni
Le operazioni si possono principalmente dividere in quattro tipologie:
Operazioni di inserimento
• Inserimento di un nuovo cliente (con SPID o credenziali manuali).
• Inserimento di un nuovo lavoratore AMA (autista o operatore di sede).


---

<!-- Pagina PDF 8 -->
## 📑 Pagina 8

Basi di Dati e di Conoscenza
 2023/2023
• Inserimento di una nuova prenotazione da parte del cliente
o Inserimento della foto del rifiuto nella prenotazione.
o Inserimento dei dettagli del rifiuto: tipologia, peso stimato, categoria.
• Inserimento di una nuova sede AMA nel sistema.
• Inserimento di un nuovo veicolo disponibile per i ritiri.
• Assegnazione automatica o manuale di un lavoratore e di un veicolo a una
prenotazione.
• Inserimento di turni/orari lavorativi associati ai dipendenti.
• Inserimento di una valutazione del servizio da parte del cliente.
• Inserimento delle zone (CAP) servite da ciascuna sede.
Operazioni di aggiornamento
• Modifica delle informazioni anagrafiche del cliente o del lavoratore.
• Modifica dello stato della prenotazione (attiva, completata, cancellata).
• Aggiornamento dei dati relativi al rifiuto (es. peso modificato dopo verifica).
• Aggiornamento del costo totale sulla base della tipologia e peso.
• Modifica dell’orario o della sede selezionata dal cliente.
• Aggiornamento della disponibilità dei lavoratori in base ai turni.
• Aggiornamento della disponibilità dei veicoli.
• Modifica dei CAP serviti da ciascuna sede.
• Aggiornamento della valutazione inserita (entro limiti temporali).
Operazioni di cancellazione
• Cancellazione di una prenotazione da parte del cliente (entro i termini).
• Rimozione di un lavoratore non più attivo nel sistema.
• Cancellazione di un veicolo dismesso o non più utilizzabile.
• Eliminazione di una sede (solo se non associata a prenotazioni attive).
• Annullamento di un’associazione lavoratore-veicolo su una determinata prenotazione.
• Cancellazione di valutazioni non conformi o segnalate.
• Cancellazione di un cliente su richiesta
Operazioni di visualizzazione
• Visualizzazione delle prenotazioni effettuate da un cliente.
• Visualizzazione dello storico dei ritiri/consegne da parte di un lavoratore.
• Visualizzazione delle sedi disponibili in base al CAP inserito.
• Visualizzazione dei costi associati a ciascuna tipologia di rifiuto.
• Visualizzazione dei veicoli disponibili e assegnati.
• Visualizzazione degli orari disponibili per il ritiro/consegna.
• Visualizzazione dello stato di una prenotazione.
• Visualizzazione della valutazione media del servizio.
• Visualizzazione della cronologia completa per scopi di report.
2.5. Classi di utenza
Il sistema MyAma prevede tre classi distinte di utenza:
1. Clienti
o Accedono tramite SPID o credenziali.
o Possono effettuare prenotazioni, caricare dati, consultare lo storico, cancellare o
modificare le richieste.
o Hanno visibilità solo sui propri dati.


---

<!-- Pagina PDF 9 -->
## 📑 Pagina 9

Basi di Dati e di Conoscenza
 2023/2023
2. Lavoratori AMA
o Divisi in Autisti (gestiscono i ritiri a domicilio) e Operatori di sede  (gestiscono
i conferimenti diretti).
o Possono visualizzare le prenotazioni assegnate e segnarne l’esito.
o Non possono modificare i dati anagrafici o gestionali.
3. Amministratori
o Gestiscono il sistema, i ruoli, i dati e le configurazioni.
o Possono accedere a tutte le sezioni, eseguire controlli, backup e manutenzione.
Ogni classe ha permessi specifici , impostati per garantire sicurezza, tracciabilità e integrità
dei dati.
2.6. Specifiche, assunzioni e vincoli d’integrità
Assunzioni:
1. Gli utenti che si registrano come clienti devono essere maggiorenni e far parte dei
comuni associati ad AMA.
2. Gli autisti sono sempre associati ad almeno un veicolo per effettuare i ritiri.
3. I CAP inseriti nelle prenotazioni devono essere tra quelli serviti da almeno una sede.
4. Un lavoratore può essere assegnato a una sola prenotazione per fascia oraria.
5. Ogni foto del rifiuto  viene caricata in formato valido (.jpg, .png) e non supera una
dimensione predefinita di 10mb.
6. Le prenotazioni possono essere cancellate fino a 2 ore prima dell'orario previsto per il
ritiro o la consegna.
7. I veicoli hanno una capacità massima espressa in kg e non possono eccedere tale
limite nella somma dei ritiri assegnati.
Vincoli di integrità
1. Vincoli di chiave primaria
• Ogni tabella (utenti, prenotazioni, rifiuti, veicoli, ecc.) ha un identificatore univoco.
2. Vincoli di chiave esterna
• Le prenotazioni fanno riferimento:
o a un cliente registrato (FK su Clienti);
o a una sede AMA (FK su Sedi);
o a un lavoratore (se assegnato);
o a un veicolo (se assegnato).
3. Vincoli di dominio
• I CAP devono essere numerici e compresi tra 00010 e 00199 (esempio di range per
Roma).
• Il peso del rifiuto deve essere > 0.
• Le e-mail devono contenere il carattere @.
• Le password devono avere almeno 8 caratteri  e almeno 1 carattere speciale
(demandato all’applicazione che sfrutta il database).
• Le valutazioni devono essere comprese tra 1 e 5.
4. Vincoli di unicità
• Il codice fiscale dei clienti è univoco.
• Il CID dei lavoratori AMA è univoco.
• Il numero targa dei veicoli è univoco.


---

<!-- Pagina PDF 10 -->
## 📑 Pagina 10

Basi di Dati e di Conoscenza
 2023/2023
5. Vincoli temporali
• Una valutazione può essere inserita solo dopo la conclusione del servizio.
6. Vincoli di integrità referenziale
• L’eliminazione di un cliente comporta anche la cancellazione delle sue prenotazioni
• Se una sede viene rimossa, le prenotazioni collegate vanno gestite
3. Parte Terza: Progettazione concettuale
3.1. Diagramma E-R
• Schema scheletro
• Schema concettuale non ristrutturato


---

<!-- Pagina PDF 11 -->
## 📑 Pagina 11

Basi di Dati e di Conoscenza
 2023/2023
3.2. Dizionario dei Dati
ENTITÀ DESCRIZIONE ATTRIBUTI CHIAVI PRIMARIE
Prenotazione
Contiene tutte le
informazioni
relative a una
prenotazione
effettuata
• Foto_rifiuto
• Descrizione_oggetto
• Tipo_prenotazione
• Data_prenotazione
• Orario_prenotazione
• Stato_prenotazione
• Costo_prenotazione
• Peso_rifiuto
Data, Orario, Cliente
Valutazione
Valutazioni
associate a
prenotazioni
concluse
• Data_valutazione
• Voto_valutazione
Data, Cliente,
Prenotazione
Cliente
Persona
registrata nel
sistema come
cliente
• Codice_fiscale
• Nome
• Cognome
• E-mail
• Password
• Data_di_nascita
• Indirizzo_domicilio
• CAP_domicilio
• Token_SPID
Codice_fiscale


---

<!-- Pagina PDF 12 -->
## 📑 Pagina 12

Basi di Dati e di Conoscenza
 2023/2023
• Telefono
Lavoratore
Dipendente
dell’AMA con
ruolo specifico
• Nome
• Cognome
• E-mail
• Password
• Data_di_nascita
• Ruolo
E-mail, Data_di_nascita
Turno
Contiene i turni
assegnati ai
lavoratori
• Data_turno
• Orario_inizio
• Orario_fine
• Pausa_inizio
• Pausa_fine
Data, Orario_inizio,
Orario_fine, lavoratore
Veicolo
Veicolo
disponibile o in
uso per le
prenotazioni
• Targa
• Tipologia
• Carico_massimo
• Stato
Targa
Sede AMA
Sede operativa
AMA con
lavoratori
assegnati
• Indirizzo
• CAP Indirizzo, CAP
Lista CAP
Associa CAP ai
territori serviti
da ciascuna
sede
• CAP CAP, Sede AMA
Orario
Elenco degli
orari di attività e
delle fasce di
pausa
giornaliera per
ogni sede AMA.
• Ora
• Inizio_pausa
• Fine_pausa
• Data
Data, Sede AMA
RELAZIONI DESCRIZIONE COMPONENTI
effettuare Collega ciascun cliente alle
prenotazioni da lui effettuate Cliente – Prenotazione
ottenere Una prenotazione può essere
associata a una valutazione Prenotazione – Valutazione
scrivere Collega ogni cliente alla valutazione
che ha scritto Cliente – Valutazione
ingaggiare Collega ogni prenotazione al
lavoratore assegnato Prenotazione – Lavoratore


---

<!-- Pagina PDF 13 -->
## 📑 Pagina 13

Basi di Dati e di Conoscenza
 2023/2023
utilizzare Collega un lavoratore al veicolo
assegnato Lavoratore – Veicolo
gestire Collega ciascuna sede AMA alle
prenotazioni che gestisce Sede AMA – Prenotazione
servire Specifica quali CAP sono serviti da
ogni sede AMA Sede AMA – Lista CAP
lavorare Collega un lavoratore alla sede in
cui opera Lavoratore – Sede AMA
rispettare Collega ciascun lavoratore ai turni
che deve rispettare Lavoratore – Turno
avere Collega ogni sede AMA ai suoi orari
di apertura e chiusura Sede AMA – Orario
4. Parte Quarta: Progettazione Logica
4.1. Schema E-R concettuale ristrutturato
Nella fase di ristrutturazione dello Schema E -R concettuale abbiamo apportato alcune
modifiche per facilitarne la lettura e la trasposizione negli altri metodi di rappresentazione del
database.
Di seguito le modifiche effettuate:
• Nella tabella Prenotazione abbiamo rinominato l’attributo tipologia in
`tipologia_servizio` e a nche l’attributo stato in stato_prenotazione, per maggiore
coerenza semantica ; inoltre è stato aggiunto l’attributo ‘Peso_rifiuto’ per rispettare i
vintoli di dominio.
• Nella tabella Orari è stato diviso l’attributo ora in `ora_inizio` e `ora_fine`, in modo da
rispettare la Prima Forma Normale (1NF) ed evitare valori non atomici.
• Sono state aggiunte due nuove entità intermedie per rappresentare in modo più
flessibile e normalizzato gli orari e i turni settimanali:
o Orari Settimanali, che collega Sede AMA a più Orari;
o Turni Settimanali, che collega Lavoratore a più Turni.
• Le cardinalità delle relazioni sono state modificate per rappresentare meglio la realtà
dell’applicazione:
o Più lavoratori possono rispettare più turni, e viceversa;
o Più turni possono appartenere a più schemi settimanali;
o Più sedi possono avere più orari settimanali, e viceversa.
• Per entrambe le entità intermedie (Orari Settimanali e Turni Settimanali), la chiave
primaria non è stata inventata, ma è derivata dagli attributi già presenti nelle entità
collegate.


---

<!-- Pagina PDF 14 -->
## 📑 Pagina 14

Basi di Dati e di Conoscenza
 2023/2023
4.2. Schema E-R logico


---

<!-- Pagina PDF 15 -->
## 📑 Pagina 15

Basi di Dati e di Conoscenza
 2023/2023
4.3. Schema relazionale
LEGENDA attributi
Chiave primaria
Foreign key*
Foreign key e anche
chiave primaria*
Cliente ( codice_fiscale,   nome,    cognome,    email,    password,    data_nascita,
indirizzo_domicilio,    cap,    telefono,    token_spid)
Lavoratore (cid,    nome,    cognome,    email,    password,    data_nascita,    ruolo)
Veicolo (targa,    tipologia,    carico_massimo,    stato,    cid_lavoratore*)
Orario (ID_Orario,    data,    ora_inizio, ora_fine,  inizio_pausa,    fine_pausa)
Turno (ID_turno,    data,    ora_inizio,    ora_fine,    inizio_pausa,    fine_pausa)
Sede (codice_sede,    indirizzo,    cap)


---

<!-- Pagina PDF 16 -->
## 📑 Pagina 16

Basi di Dati e di Conoscenza
 2023/2023
Lista_CAP (codice_sede*,    cap)
Prenotazione (codice_prenotazione,    foto_rifiuto,    descrizione_oggetto,  tipologia_servizio,
data, orario,    stato_prenotazione, peso_rifiuto,    costo,    codice_fiscale_cliente*,
cid_lavoratore*,     codice_sede*)
Valutazione (codice_prenotazione*,    voto,    commento)
Tabelle di associazione per le relazioni N,N
Orario Settimanale (ID_Orario*, codice_sede*) (Relazione N,N tra sede – orario)
Turno Settimanale (Id_turno*, cid_lavoratore*) (Relazione N,N tra lavoratore – turno)
4.4. Dizionario entità e relazioni
ENTITÀ DESCRIZIO
NE ATTRIBUTI CHIAVE
PRIMARIA
CHIAVE
Esterne
Cliente
Cittadino
registrato per
effettuare
prenotazioni
codice_fiscale, nome,
cognome, email,
password, data_nascita,
indirizzo_domicilio, cap,
telefono, token_spid
codice_fiscale -
Lavoratore
Dipendente
AMA,
operatore o
autista
cid, nome, cognome,
email, password,
data_nascita, ruolo
cid -
Veicolo
Veicolo usato
dai lavoratori
per i ritiri a
domicilio
targa, tipologia,
carico_massimo, stato,
cid_lavoratore
targa cid_lavoratore
Orario
Orario di
apertura e
pausa
associato a
una sede
id_orario, data, ora_inizio,
ora_fine, inizio_pausa,
fine_pausa
id_orario -
Orario
Settimanal
e
Consente la
gestione
flessibile dei
turni e della
loro
ricorrenza.
id_orario, codice_sede id_orario,
codice_sede
id_orario,
codice_sede


---

<!-- Pagina PDF 17 -->
## 📑 Pagina 17

Basi di Dati e di Conoscenza
 2023/2023
Turno
Turno
lavorativo
assegnato a
un lavoratore
id_turno, data, ora_inizio,
ora_fine, inizio_pausa,
fine_pausa
id_turno -
Turno
Settimanal
e
Consente di
associare più
orari a più
sedi.
cid_lavoratore, id_turno cid_lavoratore,
id_turno
cid_lavoratore,
id_turno
Sede Sede AMA
fisica codice_sede, indirizzo, cap codice_sede -
Lista_CAP
Associazione
tra CAP e sedi
che li servono
codice_sede, cap codice_sede* codice_sede,
CAP
Prenotazion
e
Prenotazione
effettuata dal
cliente per il
ritiro o la
consegna in
sede
codice_prenotazione,
foto_rifiuto,
descrizione_oggetto,
tipologia_servizio, data,
orario, stato_prenotazione,
costo,
codice_fiscale_cliente,
cid_lavoratore,
codice_sede,peso_rifiuto
codice_prenota
zione
codice_fiscale_c
liente,
cid_lavoratore,
codice_sede
Valutazione
Feedback
fornito dal
cliente dopo il
servizio
codice_prenotazione, voto,
commento
codice_prenota
zione
codice_prenotaz
ione
RELAZIONE DESCRIZIONE ENTITÀ COINVOLTE
effettuare Un cliente può effettuare più
prenotazioni Cliente – Prenotazione
ottenere Ogni prenotazione può avere una
valutazione
Prenotazione –
Valutazione
scrivere Ogni cliente può scrivere una
valutazione Cliente – Valutazione
ingaggiare Ogni prenotazione ha un lavoratore
assegnato
Prenotazione –
Lavoratore
utilizzare Ogni lavoratore può essere associato
a un veicolo Lavoratore – Veicolo
gestire Ogni sede gestisce più prenotazioni Sede – Prenotazione
servire Una sede serve uno o più CAP Sede – Lista CAP


---

<!-- Pagina PDF 18 -->
## 📑 Pagina 18

Basi di Dati e di Conoscenza
 2023/2023
lavorare Un lavoratore è associato a una sede Lavoratore – Sede
rispettare Un lavoratore è associato ai turni
lavorativi
Lavoratore – Turni
Settimanali
avere Una sede ha orari giornalieri di
apertura/chiusura
Orari Settimanali –
Orari
possedere
Collega ogni sede AMA a uno o più
schemi di orari settimanali
condivisibili tra sedi.
Sede – Orari
Settimanali
scaglionare
Collega uno schema di un turno
settimanale a più turni giornalieri
pianificati.
Turni Settimanali -
Turni
4.5. Analisi delle forme normali.
1NF:
• Tutti gli attributi delle tabelle sono atomici e non multi-valore
• Ogni tupla è identificata in modo univoco da una chiave primaria
2NF:
• Tutte le tabelle sono già in 1NF
• Gli attributi non chiave dipendono dall’intera chiave primaria scelta e non da una parte
di essa
• Tutte le tabelle con chiavi composte non contengono attributi , se non le chiavi quindi
automaticamente rispettano la 2NF
o Le altre hanno una semplice chiave primaria  quindi non presentano
problematiche
3NF:
• Tutte le tabelle sono già in 2NF
• Non ci sono dipendenze transitive tra attributi non chiave
• Ogni attributo non chiave è funzionalmente dipendente solo dalla chiave primaria
Quindi lo schema è normalizzato fino alla terza forma normale
4.6. Indici di prestazione e carico applicativo
 Costo delle operazioni
Le operazioni più pesanti a livello computazionale sono le visualizzazioni aggregate
(storico prenotazioni, carico di lavoro dei dipendenti, medie delle valutazioni), poiché
coinvolgono più join e grandi quantità di dati.


---

<!-- Pagina PDF 19 -->
## 📑 Pagina 19

Basi di Dati e di Conoscenza
 2023/2023
Le operazioni di prenotazione sono invece critiche per l’esperienza utente, e devono
essere ottimizzate con indici su data, cap, cliente, e sede.
 Occupazione di memoria
Il fatto che si sia deciso di aggiungere le immagini dei rifiuti nella tabella
Prenotazioni comporta un appesantimento del Database nell'ordine dei GB di spazio
di memoria occupati
5. Parte Quinta: Progettazione Fisica
5.1. Schema fisico con indici
QUERY DI CREAZIONE DEL DATABASE
CREATE DATABASE progetto_basi;
USE progetto_basi;
CREATE TABLE SEDE_AMA
(
codice_sede INT AUTO_INCREMENT PRIMARY KEY,
  indirizzo VARCHAR(100) NOT NULL,
  cap SMALLINT NOT NULL
);
CREATE TABLE CLIENTE
(
codice_fiscale VARCHAR(16) PRIMARY KEY,
 nome VARCHAR(100) NOT NULL,
 cognome VARCHAR(100) NOT NULL,
 email VARCHAR(100) NOT NULL,
 password VARCHAR(64) NOT NULL,
 numero_telefono VARCHAR(15) NOT NULL,
 indirizzo VARCHAR(100),
 cap SMALLINT,
 token_spid VARCHAR(24),
 data_nascita DATE NOT NULL,


---

<!-- Pagina PDF 20 -->
## 📑 Pagina 20

Basi di Dati e di Conoscenza
 2023/2023
 CHECK (INSTR(email, '@') > 1)
);
create table LISTA_CAP
(
codice_sede INT,
  CAP SMALLINT,
PRIMARY KEY(codice_sede, CAP),
FOREIGN KEY(codice_sede) REFERENCES SEDE_AMA(codice_sede)
);
CREATE TABLE LAVORATORE
(
CID_lavoratore INT AUTO_INCREMENT PRIMARY KEY,
 nome VARCHAR(100) NOT NULL,
 cognome VARCHAR(100) NOT NULL,
 email VARCHAR(100) NOT NULL,
 password VARCHAR(64) NOT NULL,
 data_nascita DATE NOT NULL,
 ruolo ENUM('in_sede', 'corriere')
);
CREATE TABLE PRENOTAZIONE
(
 codice_prenotazione INT AUTO_INCREMENT PRIMARY KEY,
 foto TEXT NOT NULL,
 descrizione TEXT,
 tipologia_servizio VARCHAR(100) NOT NULL,
 data_prenotazione DATE NOT NULL,
 orario_prenotazione TIME NOT NULL,
 stato_prenotazione VARCHAR(100) NOT NULL,


---

<!-- Pagina PDF 21 -->
## 📑 Pagina 21

Basi di Dati e di Conoscenza
 2023/2023
 costo_prenotazione DECIMAL(8,2) NOT NULL,
 codice_fiscale VARCHAR(16) NOT NULL,
 codice_sede INT NOT NULL,
CID_lavoratore INT NOT NULL,
 peso_rifiuto DECIMAL(8,2) NOT NULL,
 FOREIGN KEY (codice_fiscale) REFERENCES CLIENTE(codice_fiscale)  ON DELETE
CASCADE,
 FOREIGN KEY (codice_sede) REFERENCES SEDE_AMA(codice_sede)  ON DELETE
CASCADE,
 FOREIGN KEY (CID_lavoratore) REFERENCES LAVORATORE(CID_lavoratore)
CHECK(peso_rifiuto>0)
 );
CREATE TABLE VALUTAZIONE
(
codice_prenotazione INT PRIMARY KEY,
 voto TINYINT NOT NULL
CHECK (voto BETWEEN 1 AND 5),
 commento VARCHAR(200),
 FOREIGN KEY (codice_prenotazione) REFERENCES
PRENOTAZIONE(codice_prenotazione)
);
CREATE TABLE VEICOLO
 (
targa VARCHAR(7) PRIMARY KEY,
 tipologia VARCHAR(30),
 CID_lavoratore INT,
 carico_massimo DECIMAL(8,2),
 stato ENUM('disponibile','occupato','manutenzione'),
 FOREIGN KEY (CID_lavoratore) REFERENCES LAVORATORE(CID_lavoratore)
 );
CREATE TABLE TURNO


---

<!-- Pagina PDF 22 -->
## 📑 Pagina 22

Basi di Dati e di Conoscenza
 2023/2023
(
id_turno INT AUTO_INCREMENT PRIMARY KEY,
 data_turno DATE NOT NULL,
 orario_inizio TIME NOT NULL,
orario_fine TIME NOT NULL,
 pausa_inizio TIME NOT NULL,
 pausa_fine TIME NOT NULL
 );
CREATE TABLE TURNO_SETTIMANALE
(
CID_lavoratore INT,
id_turno INT,
 PRIMARY KEY (CID_lavoratore, id_turno),
 FOREIGN KEY (CID_lavoratore) REFERENCES LAVORATORE(CID_lavoratore),
FOREIGN KEY (id_turno) REFERENCES TURNO(id_turno)
);
CREATE TABLE ORARIO
(
 id_orario INT AUTO_INCREMENT PRIMARY KEY,
orario_inizio TIME NOT NULL,
orario_fine TIME NOT NULL,
inizio_pausa TIME NOT NULL,
fine_pausa TIME NOT NULL,
data DATE NOT NULL
);
CREATE TABLE ORARIO_SETTIMANALE
(
 id_orario INT,
codice_sede INT,


---

<!-- Pagina PDF 23 -->
## 📑 Pagina 23

Basi di Dati e di Conoscenza
 2023/2023
PRIMARY KEY (id_orario, codice_sede),
FOREIGN KEY (id_orario) REFERENCES ORARIO(id_orario),
FOREIGN KEY (codice_sede) REFERENCES SEDE_AMA(codice_sede)
 );
QUERY CHE POPOLANO IL DATABASE
INSERT INTO TURNO(data_turno, orario_inizio, orario_fine, pausa_inizio, pausa_fine)
VALUES ('2025-06-09', '08:00', '18:00', '12:00', '13:00'),
  ('2025-06-10', '08:30', '17:30', '12:00', '13:00'),
  ('2025-06-11', '9:30', '17:30', '12:00', '14:00');
INSERT INTO SEDE_AMA(indirizzo,cap)
VALUES ('Via Calderon de la Barca 87',00142),
  ('Via del Verano 74',00185),
  ('Via Capo d’Africa 23B',00184);
INSERT INTO CLIENTE
VALUES ('DSNFR1DVG810JDED', 'Paolo', 'Rossi', ' paolorossi@gmail.com', 'Paol.1456',
333567541, 'Via dei Corazzieri 110', 00143, 'A7X9F2KD3LQ8Z1MV5T6W4B0J', '1998-09-06'),
   ('RSSMRA79P15H501T', 'Maria', 'Rossi', ' maria.rossi@example.com', 'Mari@2024',
328456789, 'Via Appia Nuova 200', 00179, 'L9X3C7DMT0WJ8ZQP5N2R6KAY', '1979-03-15'),
   ('BNCLGU88S10F205K', 'Luigi', 'Bianchi', ' luigi.bianchi@email.com', 'Luig#1988',
347112233, 'Viale Trastevere 50', 00153, 'Z4E1W8NRK6MP3TQX9V7JB2YD', '1988 -11-10'),
  ('VRDGPP95L20C351U', 'Giuseppe', 'Verdi', ' giuseppe.verdi@demo.it', 'Gius$1995',
339998877, 'Piazza Bologna 10', 00162, 'Q2K7LPX43JM9AHYTF6WDEN8Z', '1995-07-20');
INSERT INTO LISTA_CAP (codice_sede, CAP)
VALUES (1, 00142),
  (1, 00143),
  (2, 00185),
  (3, 00184);
INSERT INTO LAVORATORE (nome, cognome, email, password, data_nascita, ruolo)


---

<!-- Pagina PDF 24 -->
## 📑 Pagina 24

Basi di Dati e di Conoscenza
 2023/2023
VALUES ('Luca', 'Neri', 'luca.neri@ama.it', 'X8t9bP2q', '1985-05-10', 'corriere'),
('Elena', 'Rizzo', 'elena.rizzo@ama.it', 'aD4r9T6z', '1992-07-15', 'in_sede'),
('Marco', 'Gallo', 'marco.gallo@ama.it', 'P3kLm8vQ', '1988-10-22', 'corriere');
INSERT INTO PRENOTAZIONE (foto, descrizione, tipologia_servizio, data_prenotazione,
orario_prenotazione, stato_prenotazione,  peso_rifiuto, costo_prenotazione, codice_fiscale,
codice_sede, CID_lavoratore)
VALUES ('foto1.jpg', 'Divano a 3 posti', 'ritiro a domicilio', '2025 -06-12', '09:00', 'attiva', 26,
35.00, 'RSSMRA79P15H501T', 1, 1),
('foto2.jpg', 'Lavatrice vecchia', 'ritiro a domicilio', '2025 -06-13', '10:00',
'completata',12 , 40.00, 'BNCLGU88S10F205K', 2, 3),
('foto3.jpg', 'Materasso matrimoniale', 'consegna in sede', '2025 -06-14', '11:00',
'attiva', 65, 0.00, 'VRDGPP95L20C351U', 3, 2);
INSERT INTO VEICOLO (targa, tipologia, CID_lavoratore, carico_massimo, stato)
VALUES ('AB123CD', 'Furgone', 1, 1200.50, 'disponibile'),
 ('EF456GH', 'Camioncino', 3, 1500.00, 'occupato'), ('IJ789KL', 'Furgone', NULL,
1100.75, 'manutenzione');
INSERT INTO VALUTAZIONE (codice_prenotazione, voto, commento)
VALUES (2, 5, 'Tutto perfetto');
INSERT INTO TURNO_SETTIMANALE (CID_lavoratore, id_turno)
VALUES (1, 1),
  (2, 2),
  (3, 3);
INSERT INTO ORARIO (orario_inizio,orario_fine,inizio_pausa,fine_pausa,data)
VALUES ('08:00','18:00','12:00','13:00','2025-06-09'),
  ('08:00','18:00','12:00','13:00','2025-06-10'),
  ('08:00','18:00','12:00','13:00','2025-06-11');


---

<!-- Pagina PDF 25 -->
## 📑 Pagina 25

Basi di Dati e di Conoscenza
 2023/2023
INSERT INTO ORARIO_SETTIMANALE (id_orario, codice_sede)
VALUES (1, 1), (2, 2), (3, 3);
CREAZIONE DI INDICI
Gli indici servono per avere accesso rapido a determinati attributi per effettuare query con
maggiore velocità
• Tabella prenotazione avrà indici su:
o Codice_fiscale
o CID_lavoratore
o Codice_sede
• Tabella Cliente avrà indici su:
o E-mail
o Numero di telefono
• Tabella Veicolo avrà indice su:
o Stato del veicolo
• Tabella Lavoratore avrà indice su:
o Ruolo del lavoratore
CREATE INDEX idx_prenotazione_cliente ON PRENOTAZIONE(codice_fiscale);
CREATE INDEX idx_prenotazione_lavoratore ON PRENOTAZIONE(CID_lavoratore);
CREATE INDEX idx_prenotazione_sede ON PRENOTAZIONE(codice_sede);
CREATE INDEX idx_cliente_email ON CLIENTE(email);
CREATE INDEX idx_cliente_telefono ON CLIENTE(numero_telefono);
CREATE INDEX idx_veicolo_stato ON VEICOLO(stato);
CREATE INDEX idx_lavoratore_ruolo ON LAVORATORE(ruolo);
5.2. Viste
IDEE VISTE
QUI INIZIANO LE VISTE DI SAMUELE
• VistaPrenotazioniClienti


---

<!-- Pagina PDF 26 -->
## 📑 Pagina 26

Basi di Dati e di Conoscenza
 2023/2023
o Mostra tutte le prenotazioni effettuate con i dati anagrafici dei clienti (nome,
cognome, email).
CREATE VIEW VistaPrenotazioniClienti AS
 SELECT C.nome,
C.cognome,
C.email
FROM
PRENOTAZIONE P JOIN CLIENTE C ON P.codice_fiscale=C.codice_fiscale;
• VistaPrenotazioniCompletate
o Elenco delle prenotazioni con stato "completata", includendo eventuali
valutazioni.
CREATE VIEW VistaPrenotazioniCompletate AS
  SELECT P.*,
       V.voto,
       V.commento
   FROM PRENOTAZIONE P
   LEFT JOIN VALUTAZIONE V ON P.codice_prenotazione = V.codice_prenotazione
   WHERE P.stato_prenotazione = 'completata';
• VistaDisponibilitaVeicoli
o Elenco dei veicoli attualmente disponibili, con informazioni sull’autista assegnato
(se presente).
CREATE VIEW VistaDisponibilitaVeicoli AS
 SELECT V.*,
       L.nome,
       L.cognome,
       L.ruolo
   FROM VEICOLO V
LEFT JOIN LAVORATORE L ON V.CID_lavoratore = L.CID_lavoratore
   WHERE V.stato = 'disponibile';
• VistaOrariSede
o Raccoglie gli orari settimanali associati a ciascuna sede AMA, per facilitarne la
consultazione.
CREATE VIEW VistaOrariSede AS
 SELECT S.*,
       O.*
   FROM ORARIO_SETTIMANALE OS
   JOIN SEDE_AMA S ON OS.codice_sede = S.codice_sede
   JOIN ORARIO O ON OS.id_orario = O.id_orario;
• VistaTurniLavoratori
o Mostra i turni assegnati a ciascun lavoratore, con date e fasce orarie.
CREATE VIEW VistaTurniLavoratori AS
 SELECT L.*,
       T.*
   FROM TURNO_SETTIMANALE TS
   JOIN LAVORATORE L ON L.CID_lavoratore = TS.CID_lavoratore
   JOIN TURNO T ON T.id_turno = TS.id_turno;


---

<!-- Pagina PDF 27 -->
## 📑 Pagina 27

Basi di Dati e di Conoscenza
 2023/2023
• VistaClientiAttivi
o Elenco dei clienti che hanno effettuato almeno una prenotazione negli ultimi 30
giorni.
CREATE VIEW VistaClientiAttivi AS
 SELECT *
   FROM CLIENTE C
   JOIN PRENOTAZIONE P ON C.codice_fiscale = P.codice_fiscale
   WHERE P.data_prenotazione >= CURDATE() - INTERVAL 30 DAY;
• VistaPrenotazioniPerCAP
o Restituisce le quantità di prenotazioni suddivise per CAP dei clienti diversi, utile
per analisi geografiche.
CREATE VIEW VistaPrenotazioniPerCAP AS
 SELECT C.cap, COUNT(DISTINCT C.codice_fiscale) as conta_cap
   FROM CLIENTE C
   JOIN PRENOTAZIONE P ON C.codice_fiscale = P.codice_fiscale
   GROUP BY C.cap;
QUI INIZIANO LE VISTE DI LUCA
• VistaValutazioniClienti
o Mostra per ogni cliente le valutazioni lasciate, includendo commento e voto,
ordinate per data.
CREATE VIEW VistaValutazioniClienti AS
   SELECT C.nome,
       P.data_prenotazione,
       V.voto,
       V.commento
   FROM CLIENTE C
   JOIN PRENOTAZIONE P ON C.codice_fiscale = P.codice_fiscale
   JOIN VALUTAZIONE V ON P.codice_prenotazione = V.codice_prenotazione
   ORDER BY P.data_prenotazione DESC;
• VistaPrenotazioniLavoratore
o Elenco di tutte le prenotazioni prese in carico da ciascun lavoratore, con info sul
cliente e il tipo di servizio.
CREATE VIEW VistaPrenotazioniLavoratore AS
   SELECT P.tipologia_servizio,
       C.nome,
       C.cognome,
       C.numero_telefono,
       L.nome,
      L.cognome
   FROM PRENOTAZIONE P
   JOIN LAVORATORE L ON P.CID_lavoratore = L.CID_lavoratore
   JOIN CLIENTE C ON C.codice_fiscale=P.codice_fiscale
   ORDER BY L.nome;
• VistaStatisticheSedi
o Conta quante prenotazioni ha gestito ogni sede AMA, utile per report interni.


---

<!-- Pagina PDF 28 -->
## 📑 Pagina 28

Basi di Dati e di Conoscenza
 2023/2023
CREATE VIEW VistaStatisticheSedi AS
   SELECT  P.codice_sede,
COUNT(P.codice_sede) as  numero_prenotazioni_per_sede
FROM PRENOTAZIONE P
GROUP BY P.codice_sede;
• VistaClientiSenzaPrenotazioni
o Elenca i clienti registrati che non hanno mai effettuato una prenotazione.
CREATE VIEW VistaClientiSenzaPrenotazioni AS
   SELECT C.nome,
         C.cognome
   FROM CLIENTE C
   LEFT JOIN PRENOTAZIONE P ON C.codice_fiscale  = P.codice_fiscale
   WHERE P.codice_prenotazione IS NULL;
• VistaVeicoliAssegnati
o Raccoglie tutti i veicoli con relativo lavoratore assegnato, filtrando solo quelli in
uso o occupati.
CREATE VIEW VistaVeicoliAssegnati AS
SELECT V.targa,
       V.stato,
        L.nome
   FROM VEICOLO V
   JOIN LAVORATORE L ON V.cid_lavoratore = L.cid_lavoratore
   WHERE V.stato = "occupato" or V.stato = "disponibile";
• VistaOrariCompletiPerSede
o Combina le informazioni sugli orari, le pause e le sedi in un’unica vista
consultabile.
CREATE VIEW VistaOrariCompletiPerSede AS
   SELECT O.orario_inizio,
         O.orario_fine,
         O.inizio_pausa,
         O.fine_pausa,
         S.codice_sede
   FROM SEDE_AMA S
   JOIN ORARIO_SETTIMANALE OS ON S.codice_sede = OS.codice_sede
   JOIN ORARIO O ON O.id_orario = OS.id_orario;
• VistaPrenotazioniConFoto
o Restituisce solo le prenotazioni che hanno foto associate, utile per verifiche
operative.
CREATE VIEW VistaPrenotazioniConFoto AS
   SELECT P.*
   FROM PRENOTAZIONE P
   WHERE P.foto IS NOT NULL;
QUI INIZIANO LE VISTE DI DAVIDE
• VistaPrenotazioniPerDataEOra


---

<!-- Pagina PDF 29 -->
## 📑 Pagina 29

Basi di Dati e di Conoscenza
 2023/2023
o Mostra tutte le prenotazioni ordinate per data e orario, utile per pianificare gli
interventi giornalieri.
CREATE VIEW V istaPrenotazioniPerDataOra AS
 SELECT *
   FROM PRENOTAZIONE
   ORDER BY data_prenotazione ,orario_prenotazione ;
• VistaPrenotazioniConCosto
o Elenco delle prenotazioni che hanno un costo maggiore di zero, quindi solo
quelle a pagamento.
CREATE VIEW V istaPrenotrazioniConCosto AS
   SELECT *
   FROM PRENOTAZIONE
   WHERE PRENOTAZIONE.costo_prenotazione > 0;
• VistaLavoratoriCorrieriAttivi
o Mostra solo i lavoratori con ruolo "corriere" che sono attualmente associati a
veicoli.
CREATE VIEW V istaCorrieriAttivi AS
   SELECT *
   FROM LAVORATORE AS L
   WHERE L.ruolo = "corriere" AND EXISTS (
    SELECT *
    FROM VEICOLO AS V
   WHERE L.CID_lavoratore = V.CID_lavoratore);
• VistaClientiConValutazioniAlte
o Restituisce i clienti che hanno lasciato solo valutazioni pari o superiori a 4.
CREATE VIEW VistaClientiConValutazioniAlte AS
SELECT *
FROM CLIENTE AS C
WHERE EXISTS (
SELECT *
FROM VALUTAZIONE AS V
JOIN PRENOTAZIONE AS P ON P. codice_prenotazione =
                                   V.codice_prenotazione
WHERE P.codice_fiscale = C.codice_fiscale AND V.voto >= 4);
• VistaPrenotazioniConDettagliCompleti
o Unisce informazioni da più tabelle (cliente, lavoratore, sede, veicolo)
per ogni prenotazione.
CREATE VIEW V istaPrenotazioniConDettagliCompleti AS
    SELECT P.*, C.codice_fiscale AS codice_fiscale_cliente,
    C.numero_telefono AS numero_telefono_cliente,
    L.CID_lavoratore, L.email AS email_lavoratore, L.ruolo AS
     ruolo_lavoratore,
    V.targa AS targa_veicolo, V.tipologia AS tipologia_veicolo,
    S.indirizzo AS indirizzo_sede
    FROM PRENOTAZIONE P
    JOIN CLIENTE C ON P.codice_fiscale = C.codice_fiscale
    JOIN LAVORATORE L ON P.CID_lavoratore = L.CID_lavoratore
    JOIN SEDE_AMA S ON P.codice_sede = S.codice_sede


---

<!-- Pagina PDF 30 -->
## 📑 Pagina 30

Basi di Dati e di Conoscenza
 2023/2023
    JOIN VEICOLO V ON V.CID_lavoratore  = L.CID_lavoratore;
o VistaSediConOrariDisponibili
o Elenco delle sedi che hanno almeno un orario settimanale associato.
CREATE VIEW V istaSediConOrariDisponibili AS
   SELECT *
   FROM SEDE_AMA AS S
   WHERE EXISTS(
    SELECT *
    FROM ORARIO_SETTIMANALE AS O
    WHERE O.codice_sede = S.codice_sede);
o VistaVeicoliInManutenzione
o Mostra i veicoli attualmente nello stato "manutenzione", con eventuale
assegnazione lavoratore.
CREATE VIEW VistaVeicoliInManutenzione AS
   SELECT *
   FROM VEICOLO AS V
   WHERE V.stato = "manutenzione";
TRIGGER PER GESTIRE LIMITAZIONI DEL DATABASE
TRIGGER CHE ASSICURA LA MAGGIORE ETÀ DEL CLIENTE CHE STA PER ESSERE INSERITO
CREATE TRIGGER verifica_eta_cliente
BEFORE INSERT ON CLIENTE
FOR EACH ROW
BEGIN
  IF NEW.data_nascita > CURDATE() - INTERVAL 18 YEAR THEN
SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Il cliente deve essere maggiorenne
(almeno 18 anni)';
END IF;
END;


---