# 📄 Specifica dei Requisiti Software (SRS) — *MyAma*
### Standard IEEE 830-1998

---

## 👥 Dati del Gruppo di Progetto
- **Corso di Laurea**: CdS in Informatica — Università degli Studi di Roma "Tor Vergata"
- **Insegnamento**: Ingegneria del Software (A.A. 2025/2026)
- **Docente**: Prof. Andrea D'Ambrogio
- **Membri del Gruppo**:
  - Componente A: `Nome Cognome` (Matricola: `...`)
  - Componente B: `Nome Cognome` (Matricola: `...`)
  - Componente C: `Nome Cognome` (Matricola: `...`)
  - Componente D: `Nome Cognome` (Matricola: `...`)
  - Componente E: `Nome Cognome` (Matricola: `...`)

---

# Capitolo 1 — Introduzione & Problem Statement

## 1.1 Scopo del Documento
Il presente documento costituisce la Specifica dei Requisiti Software (Software Requirements Specification - SRS) del sistema **MyAma**, redatta in conformità allo standard internazionale **IEEE 830-1998**. Lo scopo è definire in modo rigoroso, non ambiguo e verificabile i requisiti utente, i requisiti di sistema e i modelli di analisi orientata agli oggetti (OOA) per la gestione informatizzata del servizio di raccolta e conferimento rifiuti ingombranti e speciali per la città di Roma.

## 1.2 Problem Statement & Visione Generale
La gestione dei rifiuti ingombranti e speciali in un'area metropolitana complessa come Roma richiede una stretta sincronizzazione logistica tra:
- **Cittadini**: necessità di prenotare ritiri a domicilio o conferimenti presso centri di raccolta in date/orari compatibili.
- **Logistica e Trasporti AMA**: ottimizzazione della capienza dei mezzi di trasporto, percorsi di raccolta e assegnazione del personale.
- **Centri di Raccolta (Sedi AMA)**: controllo dei flussi in ingresso, varchi presidiati e tracciamento delle tipologie di rifiuto ammesse.

Il sistema **MyAma** risponde a queste esigenze offrendo una piattaforma unificata per la gestione delle richieste, l'assegnazione ottimizzata delle risorse e il monitoraggio in tempo reale degli stati di avanzamento.

## 1.3 Glossario dei Termini
| Termine | Definizione |
|---|---|
| **Cliente / Cittadino** | Utente autenticato che richiede un servizio di ritiro o conferimento. |
| **Sede AMA** | Centro di raccolta fisico attrezzato per la ricezione e stoccaggio temporaneo di rifiuti ingombranti. |
| **Autista AMA** | Operatore itinerante responsabile del ritiro a domicilio dei rifiuti tramite automezzo dedicato. |
| **Operatore di Sede** | Addetto al controllo varco, pesatura/verifica e accettazione del rifiuto presso la sede. |
| **Ritiro a Domicilio** | Servizio su prenotazione in cui un automezzo AMA si reca all'indirizzo indicato dal cittadino. |
| **Conferimento in Sede** | Servizio su prenotazione in cui il cittadino trasporta autonomamente il rifiuto presso una sede AMA autorizzata. |
| **Slot Orario** | Finestra temporale riservata per l'accesso ai varchi della sede o per il passaggio dell'autista. |

---

# Capitolo 2 — User Requirements Definition

## 2.1 Requisiti Funzionali Utente (User Requirements)
- **RF-01**: Il sistema deve consentire al cittadino di prenotare un ritiro a domicilio specificando indirizzo, CAP, categoria di rifiuto, stima dimensionale/peso e data desiderata.
- **RF-02**: Il sistema deve consentire al cittadino di prenotare uno slot di conferimento diretto presso un centro di raccolta autorizzato per la sua zona.
- **RF-03**: Il sistema deve calcolare automaticamente l'eventuale tariffa di ritiro sulla base del piano tariffario vigente e della tipologia di rifiuto.
- **RF-04**: Il sistema deve fornire all'autista AMA l'itinerario giornaliero dei ritiri con dettagli su carico previsto e indirizzi.
- **RF-05**: Il sistema deve consentire all'operatore di sede di validare l'accesso al varco e registrare il completamento dello scarico.

## 2.2 Requisiti Non Funzionali (RNF)
- **RNF-01 (Prestazioni)**: Il calcolo della disponibilità di slot e della tariffa deve avvenire in un tempo $\le 2.0$ secondi sotto carico nominale.
- **RNF-02 (Disponibilità)**: Il sistema deve garantire una disponibilità del servizio del $99.5\%$ su base mensile.
- **RNF-03 (Usabilità)**: L'interfaccia utente deve essere accessibile da dispositivi desktop e mobile con un numero massimo di 4 passaggi per completare una prenotazione.

## 2.3 Requisiti di Dominio (RD)
- **RD-01**: Il carico totale assegnato a un veicolo per un dato turno non può superare la portata massima omologata indicata nella scheda del mezzo.
- **RD-02**: Alcune tipologie di rifiuti speciali possono essere conferite esclusivamente presso sedi specificamente attrezzate.

---

# Capitolo 3 — Verificabilità dei Requisiti

| Requisito | Metodo di Verifica | Criteri di Accettazione e Test Plan |
|---|---|---|
| **RF-01** | Test Funzionale | Inserimento di prenotazione con dati validi $\to$ generazione ID prenotazione e notifica all'utente. |
| **RNF-01** | Test di Prestazione | Benchmark con 100 richieste concorrenti di calcolo tariffa: tempo medio $\le 1.5$s, 95° percentile $\le 2.0$s. |
| **RD-01** | Analisi dei Vincoli | Verifica automatica del check di consistenza in fase di assegnazione carichi su `Veicolo`. |

---

# Capitolo 4 — Specifica OOA (Object Oriented Analysis)

## 4.1 Use Case Diagram Generale
*(Inserire qui il diagramma generale Use Case esportato da Visual Paradigm)*

## 4.2 Schede di Dettaglio dei Use Case
*(Documentazione per ciascun caso d'uso: Attore Primario, Precondizioni, Flusso Principale, Flussi Alternativi, Postcondizioni)*

## 4.3 Activity Diagram
*(Modellazione dei flussi dinamici complessi: es. Gestione Ritiro a Domicilio e Convalida Varco)*

## 4.4 Sequence Diagram di Realizzazione
*(Diagrammi di sequenza con pattern Boundary-Control-Entity per i principali casi d'uso)*

## 4.5 Unrefined Class Diagram
*(Diagramma delle classi di analisi iniziale con entità di dominio, attributi e associazioni)*

---

# Capitolo 5 — Appendice Progettazione con Design Pattern

## 5.1 Criticità di Design Identificate
- **Criticità 1**: Algoritmi variabili per il calcolo delle tariffe di ritiro in base a promozioni stagionali, volume e zona.
- **Criticità 2**: Gestione del ciclo di vita e transizioni di stato della prenotazione (Richiesta, Assegnata, In Corso, Completata, Annullata).

## 5.2 Pattern Applicati
- **Design Pattern 1**: *Strategy Pattern* per il calcolo flessibile e dinamico delle tariffe.
- **Design Pattern 2**: *State Pattern* per la gestione formale delle transizioni di stato delle prenotazioni.

## 5.3 Refined Class Diagram
*(Class Diagram raffinato comprensivo delle classi, interfacce del pattern, tipi dei parametri e visibilità dei metodi)*
