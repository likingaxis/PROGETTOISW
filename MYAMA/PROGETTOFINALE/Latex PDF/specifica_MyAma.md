# 📄 Specifica dei Requisiti Software — Progetto MyAma
### Standard di riferimento: IEEE 830-1998 / OOA
**Università degli Studi di Roma "Tor Vergata"**  
**Corso di Ingegneria del Software (A.A. 2025/2026)**  
**Docente:** Prof. Andrea D'Ambrogio  

---

## 👥 Componenti del Gruppo
- **sbers** — Matricola: `sbers`
- **sbers** — Matricola: `sbers`
- **sbers** — Matricola: `sbers`
- **sbers** — Matricola: `sbers`
- **sbers** — Matricola: `sbers`

---

## 📑 Indice dei Contenuti
1. [1. Introduzione](#1-introduzione)
2. [2. Glossario dei Termini di Dominio](#2-glossario-dei-termini-di-dominio)
3. [3. User Requirements Definition & Use Cases](#3-user-requirements-definition--use-cases)
   - 3.1 Use Case Utente Non Registrato / Visitatore
   - 3.2 Use Case Cittadino Registrato
   - 3.3 Use Case Autista AMA
   - 3.4 Use Case Operatore di Sede AMA
   - 3.5 Use Case Amministratore di Sede AMA
   - 3.6 Use Case Amministratore Generale AMA
4. [4. System Requirements](#4-system-requirements)
   - 4.1 Requisiti Funzionali
   - 4.2 Requisiti Non Funzionali
   - 4.3 Requisiti di Dominio
   - 4.4 Verificabilità dei Requisiti
5. [5. System Architectural Models (OOA)](#5-system-architectural-models-ooa)
   - 5.1 Activity Diagrams
   - 5.2 Sequence Diagrams (BCE)
   - 5.3 Class Diagrams (Unrefined e Refined)
6. [6. Design Patterns](#6-design-patterns)
   - 6.1 Observer Pattern
   - 6.2 Strategy Pattern

---

# 1. Introduzione

Il progetto **MyAma** si propone come un prodotto finalizzato a mettere in comunicazione i cittadini con AMA, attraverso una piattaforma dedicata alla gestione dello smaltimento e del ritiro dei rifiuti ingombranti. Il sistema è utilizzato da cittadini, autisti AMA, personale AMA, Amministratori di sede AMA e dall'Amministratore Generale AMA, fornendo funzionalità differenti in base al ruolo ricoperto all’interno della piattaforma.

In breve, l’obiettivo principale di **MyAma** è rendere più semplice e organizzata la gestione del processo attraverso cui un cittadino può smaltire un rifiuto ingombrante, senza che debba conoscere o gestire direttamente l’organizzazione interna del servizio. Dal punto di vista aziendale, il prodotto permette invece di organizzare le risorse e la logistica necessarie allo svolgimento del servizio, ottimizzando l'assegnazione dei veicoli e facilitando la gestione dei ritiri e dei conferimenti.

Il servizio è accessibile alle seguenti classi di utenza:
- **Cittadino (non registrato / visitatore):** può consultare liberamente le informazioni generali sui servizi offerti, le tipologie di rifiuti ammesse, le sedi territoriali attive e le relative tariffe. Per procedere alla prenotazione di un servizio, può registrarsi fornendo i propri dati anagrafici e di contatto (nome, cognome, indirizzo, recapito telefonico ed email).
- **Cittadino (registrato):** può usufruire della piattaforma per richiedere un ritiro a domicilio o prenotare un conferimento diretto presso una sede AMA, specificando le caratteristiche del rifiuto (con eventuale caricamento foto), indicando l'indirizzo/CAP e selezionando una fascia oraria disponibile. Può inoltre monitorare lo stato di avanzamento delle proprie richieste, ricevere notifiche di conferma ed eventualmente annullare una prenotazione attiva entro i limiti temporali previsti.
- **Autista AMA:** tramite l'applicazione dedicata, consulta l'elenco dei ritiri assegnati per il proprio turno con i dettagli logistici (indirizzo, fascia oraria, tipologia di carico e capienza residua del mezzo) e registra l'esito dell'attività svolta (completato, cittadino assente, rifiuto non conforme).
- **Operatore di sede AMA:** gestisce le attività di accettazione presso il centro di raccolta, verificando le prenotazioni dei cittadini in arrivo, controllando la conformità dei rifiuti conferiti e registrando l'esito del servizio.
- **Amministratore di sede AMA:** gestisce l'organizzazione logistica della propria struttura: registra il personale operativo della sede, definisce le disponibilità di lavoratori e veicoli, imposta le fasce orarie e associa le sedi alle rispettive zone o CAP serviti.
- **Amministratore Generale AMA:** opera a livello direttivo aziendale; è responsabile della gestione degli account degli Amministratori di sede (creazione, abilitazione e revoca) e della consultazione di report e statistiche aggregate sui servizi erogati.

---

# 2. Glossario dei Termini di Dominio

| Termine | Descrizione |
|---|---|
| **MyAma** | Piattaforma digitale integrata dedicata alla gestione, pianificazione e prenotazione dei servizi di smaltimento dei rifiuti ingombranti e speciali per la città di Roma. |
| **Cittadino (Non Registrato / Visitatore)** | Utente esterno non autenticato che accede al sistema per consultare informazioni pubbliche sui servizi, tariffe, regolamenti e sedi AMA attive, e che può effettuare la registrazione. |
| **Cittadino (Registrato)** | Utente esterno autenticato che usufruisce dei servizi di MyAma per richiedere ritiri a domicilio o prenotare conferimenti in sede, monitorare lo stato delle proprie richieste, rilasciare valutazioni e ricevere notifiche. |
| **Autista AMA** | Dipendente operativo AMA incaricato dello svolgimento dei ritiri a domicilio. Consulta i ritiri assegnati, raggiunge l'indirizzo indicato dal Cittadino, effettua il carico e registra l'esito del servizio. |
| **Operatore di sede AMA** | Dipendente operativo AMA che presidia un centro di raccolta (sede/isola ecologica). Gestisce l'accoglienza del Cittadino, verifica la prenotazione e la conformità del rifiuto e registra l'esito del conferimento. |
| **Lavoratore AMA** | Categoria generale del personale operativo che comprende Autisti e Operatori di sede. Ogni lavoratore è caratterizzato da mansioni, turni di servizio e disponibilità oraria. |
| **Amministratore di sede AMA** | Figura responsabile della gestione logistica e operativa di una specifica sede AMA. Gestisce l'anagrafica del personale della sede, le disponibilità di lavoratori e mezzi, le fasce orarie e l'associazione tra sede e CAP/zone servite. |
| **Amministratore Generale AMA** | Figura direttiva a livello aziendale. Gestisce gli account degli Amministratori di sede (creazione, abilitazione e revoca) e accede a report e statistiche aggregate sui servizi erogati. |
| **Ritiro a domicilio** | Servizio logistico in cui AMA preleva il rifiuto ingombrante direttamente presso l'indirizzo indicato dal Cittadino. Richiede la verifica di copertura del CAP, l'assegnazione di un Autista e di un Veicolo compatibile con il carico. |
| **Conferimento in sede** | Servizio in cui il Cittadino si reca personalmente presso una sede AMA (centro di raccolta) per consegnare il rifiuto ingombrante, previa prenotazione di una fascia oraria. |
| **Prenotazione** | Entità informativa che formalizza la richiesta di smaltimento (a domicilio o in sede). Include dettagli sul rifiuto, indirizzo/sede, data e fascia oraria, dati del Cittadino e stato di avanzamento. |
| **Stato della prenotazione** | Condizione in cui si trova una prenotazione nel suo ciclo di vita: *In attesa, Confermata, In corso, Completata, Annullata, Non eseguita*. |
| **Codice Prenotazione / Pass di Conferimento** | Identificativo univoco (codice alfanumerico o QR code) generato dal sistema alla conferma della prenotazione, utilizzato per il riconoscimento e la validazione del servizio al varco o al domicilio. |
| **Tariffa / Preventivo** | Quota economica calcolata dal sistema per l'erogazione del servizio di smaltimento, determinata in base alla tipologia, al volume del rifiuto o alla presenza di servizi speciali oltre la franchigia comunale gratuita. |
| **Itinerario di Ritiro** | Sequenza ordinata degli appuntamenti di ritiro a domicilio assegnati a uno specifico Autista e Mezzo per un dato turno lavorativo all'interno della zona di competenza. |
| **Valutazione / Feedback** | Giudizio qualitativo (espresso tramite scala di punteggio ed eventuali note descrittive) che il Cittadino può rilasciare al termine di un servizio completato per misurare gradimento e puntualità. |
| **Rifiuto ingombrante** | Bene durevole, oggetto voluminoso o materiale speciale (es. mobili, grandi elettrodomestici, RAEE) che non può essere conferito nei normali cassonetti stradali. |
| **Tipologia di rifiuto** | Classificazione merceologica e normativa del rifiuto (es. legno, metallo, RAEE, ingombranti misti), necessaria per verificare la conformità di scarico e il mezzo idoneo. |
| **Sede AMA / Centro di Raccolta** | Struttura fisica territoriale (isola ecologica) abilitata alla ricezione e allo stoccaggio temporaneo di determinate tipologie di rifiuti conferiti dai cittadini. |
| **CAP / Zona servita** | Suddivisione territoriale che delimita la competenza operativa di una sede AMA e determina se un indirizzo è coperto dal servizio di ritiro a domicilio. |
| **Veicolo / Mezzo AMA** | Automezzo aziendale impiegato per i ritiri a domicilio, caratterizzato da limiti di portata utile (peso massimo) e volume di carico. |
| **Disponibilità / Slot Orario** | Fascia temporale definita (data e intervallo orario) in cui un servizio può essere prenotato ed erogato, calcolata in base alla capienza residua dei mezzi e ai turni del personale. |
| **Assegnazione** | Associazione formale e logistica tra una prenotazione di ritiro a domicilio e le risorse operative aziendali (Autista, Veicolo, data e percorso). |
| **Esito del servizio** | Registrazione conclusiva dell'intervento da parte del personale AMA (*Completato con successo, Cittadino assente, Rifiuto non conforme/respinto*). |
| **Notifica** | Comunicazione automatica generata dal sistema (email, SMS o notifica in-app) per aggiornare il Cittadino o il personale su conferme, promemoria o variazioni di stato delle prenotazioni. |
| **Report / Statistiche** | Informazioni aggregate e indicatori di performance (volumi gestiti, ritiri completati, trend per zona) consultabili dalla direzione aziendale per finalità analitiche e decisionali. |
| **Sistema** | L'applicazione software integrata MyAma nel suo complesso, comprensiva di tutti i moduli web e mobili per i diversi profili utente. |

---

# 3. User Requirements Definition & Use Cases

## 3.1 Use Case Utente Non Registrato / Visitatore
- **UC-U01 — Consultazione Informazioni e Tariffe:** Accesso pubblico a categorie di rifiuti ammesse, sedi aperte e tariffario comunale.
- **UC-U02 — Registrazione al Sistema:** Compilazione form di registrazione con dati anagrafici, indirizzo, CAP, email e presa visione informativa privacy.

## 3.2 Use Case Cittadino Registrato
- **UC-C01 — Prenotazione Ritiro a Domicilio:** Richiesta di prelievo rifiuti ingombranti a domicilio con validazione CAP e scelta slot orario.
  - `<<extend>>` Caricamento Foto Rifiuto (opzionale per stima volumetrica).
- **UC-C02 — Prenotazione Conferimento in Sede:** Prenotazione accesso all'isola ecologica con rilascio del Pass di Conferimento (QR code).
- **UC-C03 — Consultazione Stato e Storico Prenotazioni:** Tracking avanzamento richieste.
  - `<<extend>>` Annullamento Prenotazione (se con almeno 24h di anticipo).
- **UC-C04 — Valutazione del Servizio:** Rilascio feedback a 5 stelle su interventi completati.

## 3.3 Use Case Autista AMA
- **UC-A01 — Consultazione Itinerario e Ritiri Assegnati:** Visualizzazione piano di viaggio giornaliero e carichi del mezzo.
- **UC-A02 — Registrazione Esito Ritiro:** Chiusura intervento con esito (*Completato / Assente / Rifiutato*).
- **UC-A03 — Contatto Cittadino:** Chiamata o notifica in prossimità dell'arrivo.

## 3.4 Use Case Operatore di Sede AMA
- **UC-O01 — Consultazione Prenotazioni di Sede:** Monitoraggio degli accessi programmati all'isola ecologica.
- **UC-O02 — Convalida e Registrazione Conferimento al Varco:** Scansione pass QR, verifica materiale e registrazione scarico.

## 3.5 Use Case Amministratore di Sede AMA
- **UC-S01 — Gestione Personale e Turni Sede:** Gestione anagrafica e turnazione autisti/operatori.
- **UC-S02 — Gestione Veicoli e Disponibilità Mezzi:** Controllo portata, manutenzione e disponibilità flotta.
- **UC-S03 — Configurazione Sede e Associazione Zone/CAP:** Orari varco e mappatura bacini territoriali CAP.

## 3.6 Use Case Amministratore Generale AMA
- **UC-G01 — Gestione Account Amministratori di Sede:** Creazione, abilitazione e revoca responsabili.
- **UC-G02 — Consultazione Reportistica e Statistiche Globali:** Analisi indicatori di performance, volumi e indici di gradimento cittadini.

---

# 4. System Requirements

## 4.1 Requisiti Funzionali
- **RF-01 ... RF-27:** Formalizzazione completa di tutti i servizi del sistema, tracciati in modo biunivoco verso i casi d'uso.

## 4.2 Requisiti Non Funzionali
- **RNF-01 (Prestazioni):** Risposta $\le 2.0\text{s}$ per ricerca disponibilità al 95° percentile sotto 200 utenti simultanei.
- **RNF-02 (Disponibilità):** 99.5% nelle fasce 07:00 -- 22:00.
- **RNF-03 (Usabilità):** Flusso guidato in $\le 4$ step con design responsive mobile.
- **RNF-04 (Sicurezza):** Crittografia TLS 1.3, hashing bcrypt con work factor $\ge 12$.
- **RNF-05 (Integrità):** Transazioni ACID per prevenire overbooking e doppie assegnazioni.
- **RNF-06 (Portabilità):** Piena compatibilità cross-browser (Chrome, Firefox, Safari, Edge).

## 4.3 Requisiti di Dominio
- **RD-01:** Limite portata veicolo ($\sum P_i \le \text{PortataMax}$).
- **RD-02:** Competenza territoriale vincolata ai CAP di distretto.
- **RD-03:** Conferimento RAEE e rifiuti speciali solo presso sedi autorizzate.
- **RD-04:** Finestra temporale di cancellazione autonoma $\ge 24\text{h}$.

## 4.4 Verificabilità dei Requisiti
Matrice strutturata che correla ciascun requisito (funzionale e non funzionale) con specifico metodo di test (Funzionale, Stress Test, Integrazione, Security Audit) e criterio formale di accettazione.

---

# 5. System Architectural Models (OOA)
- **Activity Diagrams:** Processo di Prenotazione Ritiro, Esecuzione Ritiro Autista, Accettazione al Varco Operatore.
- **Sequence Diagrams (BCE):** Realizzazione dinamica degli Use Case tramite Boundary, Control, Entity.
- **Class Diagrams:** Modello Unrefined (analisi concettuale) e Refined (specifica consolidata con tipi, visibilità e operazioni).

---

# 6. Design Patterns
- **Observer Pattern:** Notifica asincrona e disaccoppiata delle transizioni di stato della `Prenotazione` verso Cittadino, Autista e Pannello Sede.
- **Strategy Pattern:** Algoritmi intercambiabili di allocazione e routing dei carichi ai veicoli (`MaxCaricoStrategy`, `ProssimitaCAPStrategy`, `BilanciamentoCaricoStrategy`).
