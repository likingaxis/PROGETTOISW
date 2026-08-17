# 🚀 Progetto di Ingegneria del Software — *MyAma*

<div align="center">

![Ingegneria del Software](https://img.shields.io/badge/Corso-Ingegneria%20del%20Software-blue?style=for-the-badge&logo=codeforces)
![Università](https://img.shields.io/badge/Ateneo-UniRoma2%20Tor%20Vergata-green?style=for-the-badge)
![Docente](https://img.shields.io/badge/Docente-Prof.%20Andrea%20D'Ambrogio-orange?style=for-the-badge)
![Anno Accademico](https://img.shields.io/badge/A.A.-2025%2F2026-purple?style=for-the-badge)
![Tool](https://img.shields.io/badge/Tooling-Visual%20Paradigm%20UML-red?style=for-the-badge)
![Standard](https://img.shields.io/badge/Standard-IEEE%20830--1998-yellow?style=for-the-badge)

</div>

---

## 📖 Panoramica del Progetto

Questa repository contiene tutto il materiale, la documentazione metodologica, i compendi teorici e gli esempi pratici per lo sviluppo del **Progetto d'Esame di Ingegneria del Software** (CdS in Informatica, Università degli Studi di Roma "Tor Vergata").

Il progetto è incentrato sull'ingegnerizzazione e specifica formale del sistema **`MyAma`**, una piattaforma digitale integrata per la **gestione, pianificazione e ottimizzazione delle prenotazioni per il ritiro e conferimento dei rifiuti urbani ingombranti e speciali** per la città di Roma.

---

## 🧭 Navigazione Rapida nei Documenti di Progetto

| Documento | Descrizione |
|---|---|
| 💡 **[`ideaprogetto.md`](./ideaprogetto.md)** | **Visione, Dominio e Idea Progettuale**: analisi del problema (*problem statement*), attori coinvolti, servizi erogati, regole di business e opportunità di applicazione dei Design Pattern. |
| 📌 **[`infoprof.md`](./infoprof.md)** | **Istruzioni Ufficiali & Guida Esame**: requisiti formali del docente (IEEE 830-1998, OOA, Visual Paradigm, appendice Design Pattern), modalità di consegna e analisi sistematica delle 21 slide di lezione. |
| 🌳 **[`tree.md`](./tree.md)** | **Mappa della Repository**: indice dettagliato con descrizione sintetica *one-line* di ogni singola cartella, file e contenuto degli archivi compressi. |

---

## 📁 Struttura della Repository

```text
PROGETTOISW/
├── 📄 README.md                                              # Presentazione generale del repository
├── 📄 ideaprogetto.md                                         # Documento di visione e dominio MyAma
├── 📄 infoprof.md                                            # Linee guida esame, scadenze e analisi slide
├── 📄 tree.md                                                # Mappa dettagliata e commentata dell'albero file
│
├── 📂 MYAMABASIDATI/                                         # Progetto pregresso di Basi di Dati (fonte di dominio)
│   └── 📄 BASI PROGETTO.pdf                                  # Relazione MyAma (specifiche di business e tabelle)
│
├── 📂 ALTRI/                                                 # Benchmark e progetti d'esame completi di riferimento
│   ├── 📦 FileProgetto.zip                                   # Sorgenti Visual Paradigm (.vpp) progetto "Hotel TorVergata"
│   ├── 📦 Progetto_Bianchini_Corsetti_Mazzenga.zip           # Relazione PDF + sorgenti .vpp progetto "RistorApp"
│   ├── 📄 Progetto_Cipolletta_Noce_Salvucci_Sfeir.pdf        # Relazione completa "Campionato Pesca" (76 pag.)
│   └── 📄 Progetto_Mongelli_Pace_Rossi_Sandu.pdf             # Relazione completa "Hotel TorVergata" (59 pag.)
│
└── 📂 TEORIA/                                                # Compendi teorici completi in formato Obsidian Vault
    ├── 📂 ISW_obsidian_full/                                 # Dispensa generale di Ingegneria del Software (con 178 figure)
    └── 📂 IS_andrea_obsidian_full/                           # Dispensa completa del corso di Andrea (con 50 figure)
```

---

## 💡 Il Dominio Applicativo: *MyAma*

Il sistema modella un servizio logistico distribuito e multi-attore:

```mermaid
graph TD
    A[Cittadino / Cliente] -->|Richiede Smaltimento| B{Piattaforma MyAma}
    
    B -->|Opzione 1| C[🚚 Ritiro a Domicilio]
    B -->|Opzione 2| D[🏢 Conferimento in Sede / Isola Ecologica]
    
    C --> C1[Verifica Territoriale CAP]
    C --> C2[Controllo Capienza & Carico Mezzo]
    C --> C3[Assegnazione Autista AMA]
    
    D --> D1[Scelta Centro di Raccolta]
    D --> D2[Prenotazione Slot Orario]
    D --> D3[Accoglienza & Validazione Operatore]
    
    B --> E[⚙️ Pannello Amministrazione]
    E --> E1[Gestione Mezzi, Turni, Tariffe & Report]
```

### Ruoli & Attori Principali:
- **Cittadino (Cliente)**: Autenticazione (credenziali / SPID), invio richiesta con geolocalizzazione e upload foto rifiuto, preventivo, tracking stato, recensione post-servizio.
- **Autista AMA (Lavoratore)**: Consultazione itinerario, gestione capienza veicolo ($\sum \text{Pesi} \le \text{CaricoMax}$), registrazione esito ritiro.
- **Operatore di Sede (Lavoratore)**: Gestione varchi centri di raccolta, verifica conformità rifiuto e convalida scarico.
- **Amministratore / Logistica**: Gestione sedi, associazione zone/CAP, anagrafica mezzi, turnazione e tariffari.

---

## 🎯 Deliverable di Progetto e Requisiti d'Esame

In conformità con quanto richiesto dal **Prof. Andrea D'Ambrogio**:

1. **Documento di Specifica Software (SRS)**:
   - Redatto secondo il template standard **IEEE 830-1998**.
   - Capitolo 1: *Introduzione & Problem Statement*.
   - Capitolo 2: *Glossario dei termini*.
   - Capitolo 3: *User Requirements Definition* (Funzionali, Non Funzionali e di Dominio).
   - Capitolo 4: *Verificabilità dei Requisiti* (criteri di accettazione e testabilità).
   - Capitolo 5: *Specifica OOA (Object Oriented Analysis)* con Use Case Diagrams, schede descrittive, Sequence Diagrams, State Diagrams e **Unrefined Class Diagram**.
2. **Appendice Progettazione con Design Pattern**:
   - Applicazione formale di almeno **2 Design Pattern** (es. *Strategy*, *State*, *Factory Method*, *Observer*).
   - Evoluzione da *Unrefined Class Diagram* a **Refined Class Diagram** (con classi del pattern, metodi, tipi e visibilità).
3. **Modelli UML Sorgente**:
   - Tutti i diagrammi realizzati e salvati in formato **Visual Paradigm** (`.vpp`).
4. **Modalità di Consegna**:
   - Invio della relazione PDF finale e dell'archivio `.vpp` via email a `dambro@uniroma2.it` almeno **5 giorni lavorativi prima dell'appello d'esame**.

---

<div align="center">
  <sub>Università degli Studi di Roma "Tor Vergata" • Corso di Laurea in Informatica</sub>
</div>
