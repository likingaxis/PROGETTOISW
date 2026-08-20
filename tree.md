# 🌳 Mappa della Repository - `tree.md`

Questa mappa descrive la struttura dell'intero workspace, dettagliando ogni cartella, file, trascrizione Markdown (`.md`) e contenuto degli archivi con una spiegazione sintetica (oneline) del relativo scopo.

---

## 📁 Struttura ad Albero

```text
PROGETTOISW/
├── 📄 README.md                                              # Presentazione generale del repository e guida rapida
├── 💡 idea.md                                                 # Idea sintetica del progetto per allineare rapidamente il gruppo
├── 📋 ideaprogetto.md                                         # Documento di visione, dominio e regole di business MyAma
├── 📘 guida-progetto.md                                       # Teoria orientata al progetto e modello mentale (da Problem Statement a Design Pattern)
├── 🚀 guida-operativa.md                                      # Guida operativa passo-passo (flusso sequenziale e step concreti per la specifica)
├── 👥 divisione-compiti.md                                    # Piano di divisione compiti per 5 persone (fasi, coppie, review e merge)
├── 🛠️ guida-git.md                                            # Guida pratica a Git/GitHub per collaboratori del gruppo
├── 📄 infoprof.md                                            # Linee guida esame e scadenze del docente
├── 📄 tree.md                                                # Mappa dettagliata e commentata dell'albero file
│
├── 📂 MYAMA/                                                 # Cartella operativa di sviluppo del progetto d'esame
│   ├── 📂 specifica/
│   │   └── 📄 specifica.md                                   # Documento di Specifica Software (SRS) standard IEEE 830-1998
│   ├── 📂 lavoro/
│   │   ├── 📄 decisioni.md                                   # Registro decisioni terminologiche e prefissi identificativi (ID)
│   │   └── 📄 tracciabilita.md                               # Matrice di tracciabilità Requisiti ↔ Use Case ↔ Diagrammi
│   └── 📂 visual-paradigm/
│       ├── 📄 README.md                                      # Guida all'uso del file .vpp condiviso e regole di export
│       └── 📂 diagrammi/                                     # Immagini PNG ad alta risoluzione dei diagrammi esportati
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
- **[`README.md`](./README.md)**: Presentazione generale del repository con badge, indice di navigazione rapida, visione del progetto MyAma e sintesi dei requisiti d'esame.
- **[`idea.md`](./idea.md)**: **Visione Sintetica del Progetto**: documento agile e intuitivo per allineare l'intero gruppo sul funzionamento di massima di MyAma (cittadino, sedi, ritiro a domicilio, conferimento e ruoli dei lavoratori AMA).
- **[`ideaprogetto.md`](./ideaprogetto.md)**: **Dominio & Analisi Approfondita**: documento formale con analisi del problema (*problem statement*), attori, regole di business, servizi erogati e scenari di modellazione OOA.
- **[`guida-progetto.md`](./guida-progetto.md)**: **Teoria orientata al progetto & Modello Mentale**: guida che costruisce il filo conduttore logico del progetto (perché si parte dal Problem Statement, come si passa agli attori e ai Use Case, come dai Use Case si ricavano i requisiti, perché servono i diagrammi Activity/Sequence/Class e perché i Design Pattern arrivano solo su un modello sufficientemente maturo).
- **[`guida-operativa.md`](./guida-operativa.md)**: **Guida Operativa Passo-Passo**: manuale pratico che scandisce il workflow concreto di redazione della specifica (Problem Statement $\to$ Glossario $\to$ Attori $\to$ Use Case $\to$ Requisiti $\to$ Verificabilità $\to$ Activity $\to$ Classi candidate $\to$ Bozza Class Diagram $\to$ BCE $\to$ Sequence $\to$ Class Unrefined $\to$ Class Refined $\to$ Problemi di design & Design Pattern $\to$ Revisione), con analisi delle fasi parallelizzabili per il team.
- **[`divisione-compiti.md`](./divisione-compiti.md)**: **Piano Organizzativo di Team**: piano di ripartizione e coordinamento per 5 persone (lavoro insieme, coppie, gruppi da 3, review incrociate e convergenza).
- **[`guida-git.md`](./guida-git.md)**: **Guida Git & GitHub per Collaboratori**: istruzioni operative per il team (accettazione inviti, setup iniziale, comandi quotidiani `pull`/`add`/`commit`/`push`, branch di lavoro e risoluzione assistita dei conflitti).
- **[`infoprof.md`](./infoprof.md)**: Istruzioni ufficiali del docente (Prof. Andrea D'Ambrogio) relative a standard IEEE 830-1998, OOA, tool Visual Paradigm e scadenze d'esame.
- **[`tree.md`](./tree.md)**: Mappa strutturale completa dell'intera repository con descrizione *oneline* e dettagliata di ogni singolo elemento.

---

### 1. `MYAMA/` (Cartella Operativa di Progetto)
*Spazio di lavoro dedicato alla stesura, modellazione e integrazione della specifica software d'esame.*

- **[`MYAMA/`](./MYAMA)**: Cartella di sviluppo del progetto MyAma.
- **[`specifica/specifica.md`](./MYAMA/specifica/specifica.md)**: Documento principale della Specifica dei Requisiti Software (SRS) conforme allo standard IEEE 830-1998 (Capitoli 1-5 ed Appendice Design Pattern).
- **[`lavoro/decisioni.md`](./MYAMA/lavoro/decisioni.md)**: Registro delle decisioni terminologiche, naming conventions e prefissi identificativi (UC, RF, RNF, RD).
- **[`lavoro/tracciabilita.md`](./MYAMA/lavoro/tracciabilita.md)**: Matrice di tracciabilità bidirezionale tra requisiti utente, casi d'uso, diagrammi dinamici e classi di dominio.
- **[`visual-paradigm/README.md`](./MYAMA/visual-paradigm/README.md)**: Guida pratica per la gestione del file sorgente `.vpp` condiviso e l'esportazione dei diagrammi in alta risoluzione.
- **[`visual-paradigm/diagrammi/`](./MYAMA/visual-paradigm/diagrammi)**: Directory destinata ad ospitare le immagini PNG/SVG esportate da Visual Paradigm.

---

### 2. `MYAMABASIDATI/`
*Cartella contenente il progetto pregresso del corso di Basi di Dati (disponibile sia in PDF che in trascrizione Markdown per consultazione diretta del dominio).*

- **[`MYAMABASIDATI/`](./MYAMABASIDATI)**: Cartella del progetto di riferimento per il dominio "MyAma".
- **[`BASI_PROGETTO.md`](./MYAMABASIDATI/BASI_PROGETTO.md)**: Trascrizione integrale in formato Markdown (pagina per pagina) della specifica di "MyAma".
- **[`BASI PROGETTO.pdf`](./MYAMABASIDATI/BASI%20PROGETTO.pdf)**: Documento originale in formato PDF (30 pag.).

---

### 3. `ALTRI/`
*Cartella contenente i tre progetti d'esame completi di riferimento (relazioni in PDF e in Markdown `.md`, oltre ai sorgenti UML `.vpp` estratti e compressi).*

- **[`ALTRI/`](./ALTRI)**: Raccolta di progetti benchmark.
- **[`Progetto_Cipolletta_Pesca.md`](./ALTRI/Progetto_Cipolletta_Pesca.md)**: Trascrizione testuale completa (76 pagine) del progetto "Campionato di Pesca Sportiva".
- **[`Progetto_Cipolletta_Noce_Salvucci_Sfeir.pdf`](./ALTRI/Progetto_Cipolletta_Noce_Salvucci_Sfeir.pdf)**: File PDF originale del progetto Pesca.
- **[`Progetto_Mongelli_Hotel.md`](./ALTRI/Progetto_Mongelli_Hotel.md)**: Trascrizione testuale completa (59 pagine) del progetto "Hotel TorVergata".
- **[`Progetto_Mongelli_Pace_Rossi_Sandu.pdf`](./ALTRI/Progetto_Mongelli_Pace_Rossi_Sandu.pdf)**: File PDF originale del progetto Hotel.
- **[`Progetto_Bianchini_RistorApp.md`](./ALTRI/Progetto_Bianchini_RistorApp.md)**: Trascrizione testuale completa (80 pagine) del progetto "RistorApp".
- **[`Progetto_Bianchini_Corsetti_Mazzenga/`](./ALTRI/Progetto_Bianchini_Corsetti_Mazzenga)**: Cartella con PDF e sorgenti Visual Paradigm estratti per RistorApp.
- **[`FileProgetto/`](./ALTRI/FileProgetto)**: Cartella con i modelli sorgente Visual Paradigm (`.vpp`) per il progetto Hotel TorVergata.

---

### 4. `TEORIA/`
*Cartella contenente le dispense teoriche complete del corso di Ingegneria del Software in formato Obsidian Vault Markdown con immagini, tabelle e diagrammi integrati.*

- **[`TEORIA/`](./TEORIA)**: Cartella principale con i compendi di teoria.
- **[`ISW_obsidian_full/`](./TEORIA/ISW_obsidian_full)**: Vault Obsidian con [`ISW.md`](./TEORIA/ISW_obsidian_full/ISW_obsidian_full/ISW.md) (teoria completa) e 178 immagini.
- **[`IS_andrea_obsidian_full/`](./TEORIA/IS_andrea_obsidian_full)**: Vault Obsidian con [`IS_andrea.md`](./TEORIA/IS_andrea_obsidian_full/IS_andrea_obsidian_full/IS_andrea.md) (90 pagine di appunti) e 50 figure.
