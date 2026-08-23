# GUIDA COLLEGAMENTO CLASSI UML — Refined Class Diagram MyAma

> Questo file descrive **come e perché** le classi nel file `REFINE CLASS DIAGRAM.xmi` sono collegate tra loro.
> Usalo come riferimento quando lavori in Visual Paradigm per ricostruire le relazioni.

---

## 1. GENERALIZZAZIONI (Ereditarietà)

La generalizzazione UML si rappresenta con una **freccia con triangolo vuoto** che punta dalla sottoclasse alla superclasse.

> **Regola generale:** la sottoclasse eredita TUTTI gli attributi e le operazioni della superclasse, quindi NON vanno ridefiniti.

### 1.1 Gerarchia UtenteSistema

```
                    UtenteSistema (abstract)
                    ├── id : int
                    ├── nome : String
                    ├── cognome : String
                    ├── email : String
                    └── password : String
                           │
          ┌────────────────┼────────────────┬──────────────────┐
          ▼                ▼                ▼                  ▼
     Cittadino      LavoratoreAMA     Amministratore      Amministratore
                     (abstract)        SedeAMA           GeneraleAMA
                        │
                  ┌─────┴─────┐
                  ▼           ▼
             AutistaAMA   OperatoreSedeAMA
```

| # | Superclasse | Sottoclasse | Motivazione |
|---|-------------|-------------|-------------|
| G1 | `UtenteSistema` | `Cittadino` | Condividono id, nome, cognome, email, password. Cittadino aggiunge codiceFiscale, telefono, indirizzo, CAP |
| G2 | `UtenteSistema` | `LavoratoreAMA` | Lavoratore è un utente del sistema con attributi aggiuntivi (idDipendente, telefono) |
| G3 | `UtenteSistema` | `AmministratoreSedeAMA` | Admin Sede è un utente con metodo getSedeAssociata() |
| G4 | `UtenteSistema` | `AmministratoreGeneraleAMA` | Admin Generale è un utente con metodi getElencoAdminSede(), getDettagli() |
| G5 | `LavoratoreAMA` | `AutistaAMA` | Autista è un lavoratore specializzato con getRitiriAssegnati() |
| G6 | `LavoratoreAMA` | `OperatoreSedeAMA` | Operatore è un lavoratore specializzato che opera in sede |

**Come farlo in VP:**
1. Seleziona lo strumento **Generalization** dalla toolbar
2. Clicca sulla **sottoclasse** (es. `Cittadino`)
3. Trascina fino alla **superclasse** (es. `UtenteSistema`)
4. La freccia col triangolo vuoto appare automaticamente

---

### 1.2 Gerarchia Prenotazione

```
                Prenotazione (abstract)
                ├── idPrenotazione : int
                ├── data : LocalDate
                ├── fasciaOraria : String
                └── stato : String
                        │
               ┌────────┴────────┐
               ▼                 ▼
        RitiroDomicilio    ConferimentoSede
        └── indirizzoRitiro : String
```

| # | Superclasse | Sottoclasse | Motivazione |
|---|-------------|-------------|-------------|
| G7 | `Prenotazione` | `RitiroDomicilio` | Ritiro è una prenotazione con indirizzo aggiuntivo |
| G8 | `Prenotazione` | `ConferimentoSede` | Conferimento è una prenotazione associata a una sede |

**Verifica nei Sequence Diagram:**
- In Davide: `new RitiroADomicilio(in: data)` e `new ConferimentoSede(in: data)` — entrambi creano sottotipi di Prenotazione
- In Davide: `destroyEntity()` e `setValutazione(data)` sono chiamati su `Prenotazione` — confermano che sono operazioni della superclasse

---

## 2. ASSOCIAZIONI

Le associazioni UML si rappresentano con una **linea semplice** tra le due classi, con le **molteplicità** agli estremi.

> **Regola generale:** le molteplicità indicano quanti oggetti di una classe possono essere collegati a un oggetto dell'altra.
> - `1` = esattamente uno
> - `0..1` = zero o uno
> - `0..*` = da zero a molti
> - `1..*` = da uno a molti

### 2.1 Tabella completa associazioni

| # | Classe A | Classe B | Molt. A | Molt. B | Nome relazione | Evidenza nei SD |
|---|----------|----------|---------|---------|----------------|-----------------|
| A1 | Cittadino | Prenotazione | 1 | 0..* | `ha` | Davide: il Cittadino richiede prenotazioni (ritiro, conferimento) |
| A2 | Prenotazione | Rifiuto | 1 | 1 | `riguarda` | CD Unrefined: ogni prenotazione riguarda un rifiuto |
| A3 | Prenotazione | Valutazione | 1 | 0..1 | `haValutazione` | Davide: `setValutazione()` → `new Valutazione` (opzionale) |
| A4 | Rifiuto | TipologiaRifiuto | 0..* | 1 | `haTipologia` | CD Unrefined: ogni rifiuto ha una tipologia |
| A5 | RitiroDomicilio | AutistaAMA | 0..* | 1 | `assegnatoA` | Alfredo: l'autista visualizza i ritiri assegnati |
| A6 | AutistaAMA | Veicolo | 0..* | 1 | `guida` | CD Unrefined: un autista guida un veicolo |
| A7 | ConferimentoSede | SedeAMA | 0..* | 1 | `pressoSede` | Davide: il conferimento viene creato in contesto sede |
| A8 | OperatoreSedeAMA | SedeAMA | 1..* | 1 | `lavoraPresso` | Luca: l'operatore gestisce prenotazioni della SUA sede |
| A9 | AmministratoreSedeAMA | CodiceInvito | 1 | 1..* | `gestisceCodici` | Alfredo: l'admin genera codici invito |
| A10 | LavoratoreAMA | Disponibilita | 0..* | 0..* | `haDisponibilita` | Luca: gestione disponibilità dei lavoratori |
| A11 | Veicolo | Disponibilita | 0..* | 0..* | `haDisponibilitaVeicolo` | Samuele: gestione disponibilità dei veicoli |
| A12 | SedeAMA | ZonaCAP | 1..* | 0..* | `serveZona` | Luca: `associaZonaCAP()`, `rimuoviZonaCAP()` |
| A13 | RitiroDomicilio | Assegnazione | 1 | 0..* | `haAssegnazione` | Alfredo: lifeline Assegnazione nel SD VisualizzareRitiriAssegnati |
| A14 | Assegnazione | AutistaAMA | 0..* | 1 | `assegnatoAutista` | Alfredo: l'assegnazione collega ritiro e autista |

**Come farlo in VP:**
1. Seleziona lo strumento **Association** dalla toolbar
2. Clicca sulla **prima classe** → trascina alla **seconda classe**
3. Doppio click sulla linea per aprire le proprietà
4. Imposta le **molteplicità** su ciascun estremo
5. Imposta il **nome** della relazione (colonna "Nome relazione")

---

### 2.2 Come leggere le molteplicità

Esempio per **A1: Cittadino (1) ←→ (0..*) Prenotazione**:

```
  ┌──────────────┐         ha          ┌──────────────┐
  │  Cittadino    │ 1 ─────────── 0..* │ Prenotazione  │
  └──────────────┘                     └──────────────┘
```

- **Lato Cittadino = `1`** → ogni prenotazione appartiene a ESATTAMENTE 1 cittadino
- **Lato Prenotazione = `0..*`** → un cittadino può avere da 0 a molte prenotazioni

---

## 3. DIPENDENZE BCE (Boundary → Control → Entity)

Le dipendenze BCE si rappresentano con una **freccia tratteggiata** (`<<use>>`).

> **Regola BCE:**
> - Un **Boundary** comunica SOLO con un **Control** (mai direttamente con Entity)
> - Un **Control** comunica con **Entity** e con altri **Control**
> - Un **Entity** NON comunica con Boundary

### 3.1 Dipendenze Boundary → Control

| # | Boundary | Control | Justification |
|---|----------|---------|---------------|
| D1 | RegistrationInterface | UserAccessEndpoint | SD: `richiediRegistrazione()` → `registrationForward()` |
| D2 | InvitationRegistrationInterface | UserAccessEndpoint | SD: registrazione con codice invito → `registrationForward(role, userData)` |
| D3 | LoginInterface | UserAccessEndpoint | SD: `richiediLogin()` → `loginForward()` |
| D4 | HomeBookInterface | AMAServiceController | SD: `getAvailability()` → `forwardAvailabilityRequest()` |
| D5 | WasteDisposalInterface | AMAServiceController | SD: `getAvailability()` → `requestAvailabilityCheck()` |
| D6 | BookingHistory | AMAServiceController | SD: `getStoricoPrenotazioni()` → `forwardBookHistoryRequest()` |
| D7 | PannelloAutistaUI | GestoreRitiriController | SD: `richiediRitiriAssegnati()` → `visualizzaRitiriAssegnati()` |
| D8 | PannelloAutistaUI | GestoreEsitoController | SD: `inserisciEsito()` → `registraEsito()` |
| D9 | PannelloAutistaUI | ContattoController | SD: `mostraChiamata()` → `richiediDettagli()` |
| D10 | PannelloSedeUI | GestioneSedeController | SD: `richiediPrenotazioniSede()` → `recuperaPrenotazioniSede()` |
| D11 | ControlloVarcoUI | AccettazioneController | SD: `inserisciIdPrenotazione()` → `cercaPrenotazione()` |
| D12 | GestioneConferimentoUI | GestioneConferimentoController | SD: `selezionaPrenotazione()` → `selezionaPrenotazione()` |
| D13 | GestioneCodiciUI | CodiciController | SD: `richiediCodiceAdminSede()` → `generaCodice()` |
| D14 | GestionePersonaleUI | GestionePersonaleController | SD: `richiediGenerazioneCodice()` → `generaCodiceInvito()` |
| D15 | GestioneSedeUI | GestioneSedeController | SD: `richiediDisponibilitaSede()` → `modificaDisponibilita()` |
| D16 | GestioneVeicoliUI | GestioneVeicoliController | SD: `richiediVeicoliSede()` → `recuperaVeicoli()` |

### 3.2 Dipendenze Control → Entity

| # | Control | Entity utilizzate | Justification |
|---|---------|-------------------|---------------|
| D17 | UserAccessEndpoint | UtenteSistema, Cittadino, LavoratoreAMA | Crea utenti, verifica credenziali |
| D18 | UserRegistry | UtenteSistema, Cittadino, Prenotazione, Valutazione, RitiroDomicilio, ConferimentoSede | CRUD su prenotazioni e utenti |
| D19 | UserFactory | UtenteSistema, Cittadino | Factory per creare utenti per ruolo |
| D20 | AMAServiceController | Prenotazione, RitiroDomicilio, ConferimentoSede, Valutazione | Forwarding operazioni prenotazione |
| D21 | GestoreRitiriController | AutistaAMA, Prenotazione, Assegnazione | Gestisce ritiri assegnati |
| D22 | GestoreEsitoController | Prenotazione, RitiroDomicilio | Registra esito del ritiro |
| D23 | ContattoController | Cittadino | Recupera dati contatto cittadino |
| D24 | CodiciController | AmministratoreGeneraleAMA, CodiceInvito | Genera/rimuove codici admin |
| D25 | GestioneSedeController | SedeAMA, Prenotazione, Disponibilita, ZonaCAP | Gestione completa sede |
| D26 | AccettazioneController | Prenotazione, OperatoreSedeAMA | Verifica prenotazione al varco |
| D27 | GestioneConferimentoController | Prenotazione | Registra esito conferimento |
| D28 | GestionePersonaleController | LavoratoreAMA, CodiceInvito, AmministratoreSedeAMA, Disponibilita | Gestione personale sede |
| D29 | GestioneVeicoliController | Veicolo, SedeAMA, Disponibilita, AmministratoreSedeAMA | Gestione veicoli sede |

### 3.3 Dipendenze Control → Control

| # | Control sorgente | Control destinazione | Justification |
|---|------------------|---------------------|---------------|
| D30 | UserAccessEndpoint | UserRegistry | `registrationForward()` → `createUser()` |
| D31 | UserAccessEndpoint | UserFactory | `forwardCreateUserByRole()` → `createUserByRole()` |
| D32 | AMAServiceController | UserRegistry | `forwardBookRequest()` → `newHomeBookRequest()` |

**Come farlo in VP:**
1. Seleziona lo strumento **Dependency** dalla toolbar
2. Clicca sulla classe **sorgente** (es. `RegistrationInterface`)
3. Trascina fino alla classe **destinazione** (es. `UserAccessEndpoint`)
4. La freccia tratteggiata appare automaticamente
5. Opzionale: aggiungi stereotipo `<<use>>` cliccando sulla freccia

---

## 4. COMPOSIZIONI vs AGGREGAZIONI

> **Composizione** (rombo pieno ◆): il componente NON può esistere senza il contenitore.
> **Aggregazione** (rombo vuoto ◇): il componente PUÒ esistere indipendentemente.

| Tipo | Classe contenitore | Classe componente | Motivazione |
|------|-------------------|-------------------|-------------|
| **Composizione** ◆ | Prenotazione | Valutazione | La valutazione non ha senso senza la prenotazione (A3) |
| **Aggregazione** ◇ | SedeAMA | ZonaCAP | La zona CAP esiste indipendentemente dalla sede (A12) |
| **Aggregazione** ◇ | SedeAMA | Veicolo | Il veicolo può essere riassegnato (A6 transitivo) |
| **Composizione** ◆ | RitiroDomicilio | Assegnazione | L'assegnazione non esiste senza il ritiro (A13) |

**Come farlo in VP:**
- Per **Composizione**: seleziona **Composition** dalla toolbar
- Per **Aggregazione**: seleziona **Aggregation** dalla toolbar
- Clicca dal **contenitore** verso il **componente**

---

## 5. CLASSI ASTRATTE

> **Regola:** una classe è **abstract** se NON può essere istanziata direttamente, ma serve come superclasse.

| Classe | Perché è abstract |
|--------|-------------------|
| `UtenteSistema` | Non esiste un "utente generico", è sempre Cittadino, Autista, etc. |
| `LavoratoreAMA` | Non esiste un "lavoratore generico", è sempre Autista o Operatore |
| `Prenotazione` | Non esiste una "prenotazione generica", è sempre Ritiro o Conferimento |

**Come farlo in VP:**
1. Doppio click sulla classe
2. Nella sezione proprietà, spunta **Abstract**
3. Il nome apparirà in *corsivo*

---

## 6. SCHEMA VISIVO RIEPILOGATIVO

```
┌─────────────────────────────────────────────────────────────────┐
│                        BOUNDARY LAYER                           │
│  RegistrationInterface    HomeBookInterface    PannelloAutistaUI │
│  LoginInterface           WasteDisposalInterface  PannelloSedeUI│
│  InvitationRegInterface   BookingHistory       ControlloVarcoUI │
│  GestioneCodiciUI  GestionePersonaleUI  GestioneSedeUI          │
│  GestioneConferimentoUI   GestioneVeicoliUI                     │
└──────────────────────────────┬──────────────────────────────────┘
                               │ <<use>> (freccia tratteggiata)
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                        CONTROL LAYER                            │
│  UserAccessEndpoint      AMAServiceController    UserRegistry   │
│  UserFactory             GestoreRitiriController                │
│  GestoreEsitoController  ContattoController      CodiciController│
│  GestioneSedeController  AccettazioneController                 │
│  GestioneConferimentoController  GestionePersonaleController    │
│  GestioneVeicoliController                                      │
└──────────────────────────────┬──────────────────────────────────┘
                               │ <<use>> (freccia tratteggiata)
                               ▼
┌─────────────────────────────────────────────────────────────────┐
│                        ENTITY LAYER                             │
│  UtenteSistema ◁── Cittadino, LavoratoreAMA, AdminSede, AdminGen│
│  LavoratoreAMA ◁── AutistaAMA, OperatoreSedeAMA                │
│  Prenotazione ◁── RitiroDomicilio, ConferimentoSede             │
│  Valutazione  Rifiuto  TipologiaRifiuto  SedeAMA               │
│  Veicolo  Disponibilita  CodiceInvito  ZonaCAP  Assegnazione   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. CHECKLIST RAPIDA PER VP

- [ ] Importa `REFINE CLASS DIAGRAM.xmi` via **File > Import > XMI**
- [ ] Crea un nuovo **Class Diagram** vuoto
- [ ] Trascina TUTTE le 19 classi Entity dal Model Explorer
- [ ] Trascina TUTTE le 14 classi Boundary
- [ ] Trascina TUTTI i 13 classi Control
- [ ] Traccia le **8 generalizzazioni** (sezione 1)
- [ ] Traccia le **14 associazioni** con molteplicità (sezione 2)
- [ ] Segna le **composizioni** con rombo pieno (sezione 4)
- [ ] Segna le **aggregazioni** con rombo vuoto (sezione 4)
- [ ] Traccia le **dipendenze BCE** con frecce tratteggiate (sezione 3)
- [ ] Imposta le **3 classi astratte** in corsivo (sezione 5)
- [ ] Applica gli **stereotipi** `<<boundary>>`, `<<control>>`, `<<entity>>` manualmente
- [ ] Verifica che ogni Boundary comunichi SOLO con Control (mai direttamente con Entity)
