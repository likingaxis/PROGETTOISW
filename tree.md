# 🌳 Mappa della Repository - `tree.md`

Questa mappa descrive la struttura dell'intero workspace, dettagliando ogni cartella, file, trascrizione Markdown (`.md`) e contenuto degli archivi con una spiegazione sintetica (oneline) del relativo scopo.

---

## 📁 Struttura ad Albero

```text
PROGETTOISW/
├── 📄 README.md
├── 📄 ideaprogetto.md
├── 📄 infoprof.md
├── 📄 tree.md
│
├── 📂 MYAMABASIDATI/
│   ├── 📄 BASI PROGETTO.pdf                                  # PDF originale del progetto Basi di Dati (30 pag.)
│   └── 📝 BASI_PROGETTO.md                                   # Trascrizione testuale integrale pagina per pagina
│
├── 📂 ALTRI/
│   ├── 📝 Progetto_Cipolletta_Pesca.md                       # Trascrizione testuale integrale progetto "Pesca" (76 pag.)
│   ├── 📄 Progetto_Cipolletta_Noce_Salvucci_Sfeir.pdf        # PDF originale "Campionato Pesca Sportiva"
│   │
│   ├── 📝 Progetto_Mongelli_Hotel.md                         # Trascrizione testuale integrale progetto "Hotel" (59 pag.)
│   ├── 📄 Progetto_Mongelli_Pace_Rossi_Sandu.pdf             # PDF originale "Hotel TorVergata"
│   │
│   ├── 📝 Progetto_Bianchini_RistorApp.md                    # Trascrizione testuale integrale progetto "RistorApp" (80 pag.)
│   ├── 📂 Progetto_Bianchini_Corsetti_Mazzenga/              # Cartella estratta con PDF e sorgenti .vpp
│   │   ├── 📄 Progetto_Bianchini_Corsetti_Mazzenga.pdf
│   │   ├── 📄 Progetto_Bianchini_Corsetti_Mazzenga.vpp
│   │   └── 📄 Solo per i Class Diagrams (Unrefined, Refined).vpp
│   ├── 📦 Progetto_Bianchini_Corsetti_Mazzenga.zip
│   │
│   ├── 📂 FileProgetto/                                      # Cartella estratta dei modelli Visual Paradigm "Hotel"
│   │   ├── 📄 DESIGNPATTERNS.vpp
│   │   ├── 📄 CLASSE UNREFINED.vpp
│   │   ├── 📄 CLASSE REFINED.vpp
│   │   ├── 📄 UTENTE.vpp
│   │   ├── 📄 CLIENTE.vpp
│   │   ├── 📄 SERVIZIO.vpp
│   │   └── 📄 AMMINISTRAZIONE.vpp
│   └── 📦 FileProgetto.zip
│
└── 📂 TEORIA/
    ├── 📂 ISW_obsidian_full/
    │   └── 📂 ISW_obsidian_full/
    │       ├── 📄 ISW.md                                     # Trascrizione completa teoria ISW (~372 KB)
    │       ├── 📄 README.txt
    │       └── 📂 assets/ (178 figure/diagrammi)
    └── 📂 IS_andrea_obsidian_full/
        └── 📂 IS_andrea_obsidian_full/
            ├── 📄 IS_andrea.md                               # Trascrizione completa teoria Andrea (90 pag.)
            ├── 📄 README.md
            └── 📂 assets/ (50 figure/diagrammi)
```

---

## 📋 Descrizione Dettagliata delle Cartelle e dei File

### 0. File Principali di Root
- **[`README.md`](file:///c:/Users/Luca/Desktop/PROGETTOISW/README.md)**: Presentazione generale del repository con badge, navigazione rapida, visione del progetto MyAma e riepilogo dei requisiti d'esame.
- **[`ideaprogetto.md`](file:///c:/Users/Luca/Desktop/PROGETTOISW/ideaprogetto.md)**: Documento di visione e analisi di dominio per "MyAma", che illustra obiettivi, attori, servizi, regole di business e opportunità di modellazione OOA/Design Pattern.
- **[`infoprof.md`](file:///c:/Users/Luca/Desktop/PROGETTOISW/infoprof.md)**: Istruzioni ufficiali del docente per il task progettuale e scadenze di consegna.
- **[`tree.md`](file:///c:/Users/Luca/Desktop/PROGETTOISW/tree.md)**: Mappa strutturale completa dell'intera repository con descrizione oneline di ogni elemento.

---

### 1. `MYAMABASIDATI/`
*Cartella contenente il tuo progetto pregresso del corso di Basi di Dati (disponibile sia in PDF che in trascrizione Markdown per consultazione diretta).*

- **[`MYAMABASIDATI/`](file:///c:/Users/Luca/Desktop/PROGETTOISW/MYAMABASIDATI)**: Cartella del progetto di riferimento per il dominio "MyAma".
- **[`BASI_PROGETTO.md`](file:///c:/Users/Luca/Desktop/PROGETTOISW/MYAMABASIDATI/BASI_PROGETTO.md)**: Trascrizione integrale in formato Markdown (pagina per pagina) della specifica di "MyAma".
- **[`BASI PROGETTO.pdf`](file:///c:/Users/Luca/Desktop/PROGETTOISW/MYAMABASIDATI/BASI%20PROGETTO.pdf)**: Documento originale in formato PDF (30 pag.).

---

### 2. `ALTRI/`
*Cartella contenente i tre progetti d'esame completi di riferimento (relazioni in PDF e in Markdown `.md`, oltre ai sorgenti UML `.vpp` estratti e compressi).*

- **[`ALTRI/`](file:///c:/Users/Luca/Desktop/PROGETTOISW/ALTRI)**: Raccolta di progetti benchmark.
- **[`Progetto_Cipolletta_Pesca.md`](file:///c:/Users/Luca/Desktop/PROGETTOISW/ALTRI/Progetto_Cipolletta_Pesca.md)**: Trascrizione testuale completa (76 pagine) del progetto "Campionato di Pesca Sportiva".
- **[`Progetto_Cipolletta_Noce_Salvucci_Sfeir_250128_154245.pdf`](file:///c:/Users/Luca/Desktop/PROGETTOISW/ALTRI/Progetto_Cipolletta_Noce_Salvucci_Sfeir_250128_154245.pdf)**: File PDF originale del progetto Pesca.
- **[`Progetto_Mongelli_Hotel.md`](file:///c:/Users/Luca/Desktop/PROGETTOISW/ALTRI/Progetto_Mongelli_Hotel.md)**: Trascrizione testuale completa (59 pagine) del progetto "Hotel TorVergata".
- **[`Progetto_Mongelli_Pace_Rossi_Sandu (1).pdf`](file:///c:/Users/Luca/Desktop/PROGETTOISW/ALTRI/Progetto_Mongelli_Pace_Rossi_Sandu%20(1).pdf)**: File PDF originale del progetto Hotel.
- **[`Progetto_Bianchini_RistorApp.md`](file:///c:/Users/Luca/Desktop/PROGETTOISW/ALTRI/Progetto_Bianchini_RistorApp.md)**: Trascrizione testuale completa (80 pagine) del progetto "RistorApp".
- **[`Progetto_Bianchini_Corsetti_Mazzenga/`](file:///c:/Users/Luca/Desktop/PROGETTOISW/ALTRI/Progetto_Bianchini_Corsetti_Mazzenga)**: Cartella con PDF e sorgenti Visual Paradigm estratti per RistorApp.
- **[`FileProgetto/`](file:///c:/Users/Luca/Desktop/PROGETTOISW/ALTRI/FileProgetto)**: Cartella con i modelli sorgente Visual Paradigm (`.vpp`) per il progetto Hotel TorVergata.

---

### 3. `TEORIA/`
*Cartella contenente le dispense teoriche complete del corso di Ingegneria del Software in formato Obsidian Vault Markdown con immagini, tabelle e diagrammi integrati.*

- **[`TEORIA/`](file:///c:/Users/Luca/Desktop/PROGETTOISW/TEORIA)**: Cartella principale con i compendi di teoria.
- **[`ISW_obsidian_full/`](file:///c:/Users/Luca/Desktop/PROGETTOISW/TEORIA/ISW_obsidian_full)**: Vault Obsidian con [`ISW.md`](file:///c:/Users/Luca/Desktop/PROGETTOISW/TEORIA/ISW_obsidian_full/ISW_obsidian_full/ISW.md) (teoria completa) e 178 immagini.
- **[`IS_andrea_obsidian_full/`](file:///c:/Users/Luca/Desktop/PROGETTOISW/TEORIA/IS_andrea_obsidian_full)**: Vault Obsidian con [`IS_andrea.md`](file:///c:/Users/Luca/Desktop/PROGETTOISW/TEORIA/IS_andrea_obsidian_full/IS_andrea_obsidian_full/IS_andrea.md) (90 pagine di appunti) e 50 figure.
