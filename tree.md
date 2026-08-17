# 🌳 Mappa della Repository - `tree.md`

Questa mappa descrive la struttura dell'intero workspace, dettagliando ogni cartella, file e contenuto degli archivi compressi con una spiegazione sintetica (oneline) del relativo scopo.

---

## 📁 Struttura ad Albero

```text
PROGETTOISW/
├── 📄 README.md
├── 📄 ideaprogetto.md
├── 📄 infoprof.md
├── 📄 tree.md
├── 📂 MYAMABASIDATI/
│   └── 📄 BASI PROGETTO.pdf
├── 📂 ALTRI/
│   ├── 📦 FileProgetto.zip
│   │   ├── 📄 DESIGNPATTERNS.vpp
│   │   ├── 📄 CLASSE UNREFINED.vpp
│   │   ├── 📄 CLASSE REFINED.vpp
│   │   ├── 📄 UTENTE.vpp
│   │   ├── 📄 CLIENTE.vpp
│   │   ├── 📄 SERVIZIO.vpp
│   │   └── 📄 AMMINISTRAZIONE.vpp
│   ├── 📦 Progetto_Bianchini_Corsetti_Mazzenga.zip
│   │   ├── 📄 Progetto_Bianchini_Corsetti_Mazzenga.pdf
│   │   ├── 📄 Progetto_Bianchini_Corsetti_Mazzenga.vpp
│   │   └── 📄 Solo per i Class Diagrams (Unrefined, Refined).vpp
│   ├── 📄 Progetto_Cipolletta_Noce_Salvucci_Sfeir_250128_154245.pdf
│   └── 📄 Progetto_Mongelli_Pace_Rossi_Sandu (1).pdf
└── 📂 TEORIA/
    ├── 📂 ISW_obsidian_full/
    │   └── 📂 ISW_obsidian_full/
    │       ├── 📄 ISW.md
    │       ├── 📄 README.txt
    │       └── 📂 assets/ (178 figure/diagrammi)
    └── 📂 IS_andrea_obsidian_full/
        └── 📂 IS_andrea_obsidian_full/
            ├── 📄 IS_andrea.md
            ├── 📄 README.md
            └── 📂 assets/ (50 figure/diagrammi)
```

---

## 📋 Descrizione Dettagliata delle Cartelle e dei File

### 0. File Principali di Root
- **[`README.md`](file:///c:/Users/Luca/Desktop/PROGETTOISW/README.md)**: Presentazione generale del repository con badge, navigazione rapida, visione del progetto MyAma e riepilogo dei requisiti d'esame.
- **[`ideaprogetto.md`](file:///c:/Users/Luca/Desktop/PROGETTOISW/ideaprogetto.md)**: Documento di visione e analisi di dominio per "MyAma", che illustra obiettivi, attori, servizi, regole di business e opportunità di modellazione OOA/Design Pattern.
- **[`infoprof.md`](file:///c:/Users/Luca/Desktop/PROGETTOISW/infoprof.md)**: Raccolta delle linee guida, scadenze, requisiti di specifica (IEEE 830-1998, OOA, Visual Paradigm, Design Pattern) e analisi sistematica delle 21 slide del docente.
- **[`tree.md`](file:///c:/Users/Luca/Desktop/PROGETTOISW/tree.md)**: Mappa strutturale completa dell'intera repository con descrizione oneline di ogni elemento e archivio.

---

### 1. `MYAMABASIDATI/`
*Cartella contenente il tuo progetto pregresso del corso di Basi di Dati, da cui riprendere il dominio applicativo e l'idea progettuale per il nuovo elaborato di Ingegneria del Software.*

- **[`MYAMABASIDATI/`](file:///c:/Users/Luca/Desktop/PROGETTOISW/MYAMABASIDATI)**: Cartella del progetto di riferimento per il dominio "MyAma" (gestione rifiuti ingombranti).
- **[`BASI PROGETTO.pdf`](file:///c:/Users/Luca/Desktop/PROGETTOISW/MYAMABASIDATI/BASI%20PROGETTO.pdf)**: Documento di specifica e requisiti di "MyAma - Gestione prenotazioni per rifiuti ingombranti" (30 pag.), utile per riutilizzare requisiti, scenari d'uso e modelli logici.

---

### 2. `ALTRI/`
*Cartella contenente progetti d'esame completi svolti da altri gruppi (relazioni PDF e sorgenti UML Visual Paradigm `.vpp`), fondamentali come linea guida per struttura, convenzioni e diagrammi.*

- **[`ALTRI/`](file:///c:/Users/Luca/Desktop/PROGETTOISW/ALTRI)**: Raccolta di progetti di esempio (PDF e archivi con file di modellazione Visual Paradigm).
- **[`Progetto_Cipolletta_Noce_Salvucci_Sfeir_250128_154245.pdf`](file:///c:/Users/Luca/Desktop/PROGETTOISW/ALTRI/Progetto_Cipolletta_Noce_Salvucci_Sfeir_250128_154245.pdf)**: Relazione d'esame completa (76 pag.) per il sistema "Campionato di Pesca Sportiva", ottimo riferimento per glossario, use case strutturati e sequenze.
- **[`Progetto_Mongelli_Pace_Rossi_Sandu (1).pdf`](file:///c:/Users/Luca/Desktop/PROGETTOISW/ALTRI/Progetto_Mongelli_Pace_Rossi_Sandu%20(1).pdf)**: Relazione d'esame (59 pag.) per il sistema gestionale "Hotel TorVergata" (corrisponde ai sorgenti presenti in `FileProgetto.zip`).
- **[`FileProgetto.zip`](file:///c:/Users/Luca/Desktop/PROGETTOISW/ALTRI/FileProgetto.zip)**: Archivio contenente i diagrammi sorgente Visual Paradigm (`.vpp`) del progetto "Hotel TorVergata":
  - `DESIGNPATTERNS.vpp`: Diagrammi architetturali e strutturali dei Design Pattern implementati nel progetto.
  - `CLASSE UNREFINED.vpp`: Class Diagram iniziale di analisi concettuale del dominio (livello non raffinato).
  - `CLASSE REFINED.vpp`: Class Diagram di progettazione dettagliata con tipi, metodi, visibilità e pattern (livello raffinato).
  - `UTENTE.vpp`: Use Case Diagram e scenari operativi relativi all'attore visitatore/generico (Utente).
  - `CLIENTE.vpp`: Use Case Diagram e flussi funzionali dedicati all'utente registrato (Cliente).
  - `SERVIZIO.vpp`: Use Case Diagram relativi all'erogazione e gestione dei servizi interni dell'hotel.
  - `AMMINISTRAZIONE.vpp`: Use Case Diagram per il pannello amministrativo, gestione staff e reportistica.
- **[`Progetto_Bianchini_Corsetti_Mazzenga.zip`](file:///c:/Users/Luca/Desktop/PROGETTOISW/ALTRI/Progetto_Bianchini_Corsetti_Mazzenga.zip)**: Archivio con il pacchetto completo del progetto "RistorApp" (relazione + diagrammi `.vpp`):
  - `Progetto_Bianchini_Corsetti_Mazzenga.pdf`: Relazione finale completa (80 pag.) del progetto "RistorApp" con specifica requisiti, use case, sequence diagram, class diagram e design pattern.
  - `Progetto_Bianchini_Corsetti_Mazzenga.vpp`: Progetto sorgente Visual Paradigm completo con tutti i diagrammi UML del sistema.
  - `Solo per i Class Diagrams (Unrefined, Refined).vpp`: File sorgente Visual Paradigm focalizzato specificamente sui Class Diagram di analisi e di dettaglio.

---

### 3. `TEORIA/`
*Cartella contenente le dispense teoriche complete del corso di Ingegneria del Software in formato Obsidian Vault Markdown con immagini, tabelle e diagrammi integrati.*

- **[`TEORIA/`](file:///c:/Users/Luca/Desktop/PROGETTOISW/TEORIA)**: Cartella principale contenente i due compendi completi di teoria del corso.
- **[`ISW_obsidian_full/`](file:///c:/Users/Luca/Desktop/PROGETTOISW/TEORIA/ISW_obsidian_full)**: Vault Obsidian per la dispensa generale del corso "ISW".
  - **[`ISW_obsidian_full/`](file:///c:/Users/Luca/Desktop/PROGETTOISW/TEORIA/ISW_obsidian_full/ISW_obsidian_full)**: Cartella contenitore del vault Obsidian.
    - **[`ISW.md`](file:///c:/Users/Luca/Desktop/PROGETTOISW/TEORIA/ISW_obsidian_full/ISW_obsidian_full/ISW.md)**: Documento Markdown esteso (~372 KB) con l'intera teoria del corso (modelli di processo, requisiti, UML, architetture software, design pattern e testing).
    - **[`README.txt`](file:///c:/Users/Luca/Desktop/PROGETTOISW/TEORIA/ISW_obsidian_full/ISW_obsidian_full/README.txt)**: Guida all'apertura del vault in Obsidian e spiegazione dei tag di impaginazione.
    - **`assets/`**: Raccolta di 178 immagini e schemi esplicativi estratti dalla dispensa originale e linkati nel file `ISW.md`.
- **[`IS_andrea_obsidian_full/`](file:///c:/Users/Luca/Desktop/PROGETTOISW/TEORIA/IS_andrea_obsidian_full)**: Vault Obsidian per la dispensa di teoria redatta da Andrea.
  - **[`IS_andrea_obsidian_full/`](file:///c:/Users/Luca/Desktop/PROGETTOISW/TEORIA/IS_andrea_obsidian_full/IS_andrea_obsidian_full)**: Cartella contenitore del vault di Andrea.
    - **[`IS_andrea.md`](file:///c:/Users/Luca/Desktop/PROGETTOISW/TEORIA/IS_andrea_obsidian_full/IS_andrea_obsidian_full/IS_andrea.md)**: Trascrizione integrale in Markdown (90 pagine) con note teoriche, diagrammi, pattern e tabelle riassuntive.
    - **[`README.md`](file:///c:/Users/Luca/Desktop/PROGETTOISW/TEORIA/IS_andrea_obsidian_full/IS_andrea_obsidian_full/README.md)**: Guida rapida alla consultazione del vault e riepilogo delle risorse convertite (50 figure, 3 tabelle).
    - **`assets/`**: Raccolta di 50 diagrammi e illustrazioni estratti dal PDF originale e incorporati in `IS_andrea.md`.

---

## 🎯 Come Utilizzare Questo Materiale per il Tuo Progetto ISW

1. **Dominio & Requisiti (`MYAMABASIDATI/` & `ideaprogetto.md`)**: Prendi le logiche di business, gli attori (cittadini, autisti, operatori sede, amministrazione) e i flussi di prenotazione rifiuti per formalizzarli secondo i canoni di Ingegneria del Software.
2. **Struttura della Relazione (`ALTRI/*.pdf`)**: Usa i PDF di "Campionato Pesca", "Hotel TorVergata" e "RistorApp" come modello per la struttura dei capitoli (Introduzione, Glossario, User Requirements, Use Case Specifications, Sequence Diagrams, Class Diagrams Unrefined/Refined, Design Patterns).
3. **Modellazione UML (`ALTRI/*.zip`)**: Apri i file `.vpp` con **Visual Paradigm** per vedere esattamente come impostare i diagrammi dei casi d'uso, i diagrammi delle classi e i pattern architetturali.
4. **Studio & Verifica Teorica (`TEORIA/`)**: Consulta `ISW.md` e `IS_andrea.md` per verificare le definizioni formali dei requisiti, le regole di sintassi UML, i pattern GoF/GRASP e i criteri di raffinamento delle classi.
