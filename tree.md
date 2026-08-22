# 🌳 Mappa della Repository - `tree.md`

Questa mappa descrive la struttura dell'intero workspace, dettagliando ogni cartella, file, specifica LaTeX, trascrizione Markdown (`.md`) e contenuto degli archivi con una spiegazione sintetica (*oneline*) del relativo scopo.

---

## 📁 Struttura ad Albero

```text
PROGETTOISW/
├── 📄 README.md                                              # Presentazione generale del repository e guida rapida
├── 💡 idea.md                                                 # Idea sintetica del progetto per allineare rapidamente il gruppo
├── 📋 ideaprogetto.md                                         # Documento di visione, dominio e regole di business MyAma
├── 📄 tree.md                                                # Mappa dettagliata e commentata dell'albero file
│
├── 📂 guide/                                                 # Guide metodologiche, operative e organizzative
│   ├── 📘 guida-progetto.md                                   # Teoria orientata al progetto e modello mentale (da Problem Statement a Design Pattern)
│   ├── 🚀 guida-operativa.md                                  # Guida operativa passo-passo (flusso sequenziale e step concreti per la specifica)
│   ├── 👥 divisione-compiti.md                                # Piano di divisione compiti per 5 persone (fasi, coppie, review e merge)
│   ├── 📅 plan-giorni.md                                      # Roadmap temporale e pianificazione giornaliera delle attività
│   ├── 🛠️ guida-git.md                                        # Guida pratica a Git/GitHub per collaboratori del gruppo
│   └── 📌 infoprof.md                                        # Linee guida esame e scadenze ufficiali del docente
│
├── 📂 MYAMA/                                                 # Cartella operativa di sviluppo del progetto d'esame
│   ├── 📂 GRUPPO 1/                                          # Spazio di lavoro Gruppo 1 (Requisiti, diagrammi e draft)
│   │   ├── 📄 System Requirements.md                         # Requisiti funzionali (RF-01..13), non funzionali (RNF) e di dominio (RD)
│   │   ├── 📄 davideluserRequirementsDefinition.md           # Bozza iniziale User Requirements Gruppo 1
│   │   ├── 📄 davidelUseCase.vpp                             # File di modellazione Use Case Visual Paradigm (Davide)
│   │   ├── 📄 ValerioUseCase.vpp                             # File di modellazione Use Case Visual Paradigm (Valerio)
│   │   ├── 📄 output.md                                      # Bozza introduzione, contesto e attori
│   │   ├── 📄 output2.md                                     # Bozza di raffinamento requisiti
│   │   └── 📂 FOTOusecase/                                   # Esportazioni grafiche dei diagrammi use case
│   │
│   ├── 📂 GRUPPO 2/                                          # Spazio di lavoro Gruppo 2 (Use Cases, schede e scope)
│   │   ├── 📄 LISTA USE CASE.md                              # Elenco unificato dei casi d'uso per attore
│   │   ├── 📄 User requirements definition.md                # Specifica integrale schede Use Case (tabelle formali 1:1)
│   │   ├── 📄 Documentazione Use Case — Amministratore...md  # Documentazione Use Case per Amministratore Generale
│   │   ├── 📄 FASE_1 - D, E.md                               # Analisi perimetro, scope in/out e checklist
│   │   └── 📄 CHECKLIST.md                                   # Checklist operativa di avanzamento
│   │
│   ├── 📂 Latex PDF/                                         # Progetto LaTeX per la generazione della relazione finale IEEE 830
│   │   ├── 📄 main.tex                                       # File sorgente master LaTeX (preambolo, indici, include sezioni)
│   │   ├── 📄 main.pdf                                       # Documento PDF d'esame compilato e sincronizzato
│   │   ├── 🐍 compile_pdf.py                                 # Script di compilazione a 2 passate (MiKTeX/TeX Live)
│   │   ├── 📄 README.md                                      # Guida e istruzioni di compilazione LaTeX/Overleaf
│   │   ├── 📄 specifica_MyAma.md                             # Bozza complessiva della specifica in Markdown
│   │   ├── 📂 sezioni/                                       # Moduli LaTeX dei capitoli della specifica
│   │   │   ├── 📄 01_introduzione.tex                        # Cap. 1: Introduzione e mappatura classi di utenza
│   │   │   ├── 📄 02_glossario.tex                           # Cap. 2: Glossario dei termini di dominio
│   │   │   ├── 📄 03_user_requirements.tex                   # Cap. 3: User Requirements Definition con diagrammi e tabelle
│   │   │   ├── 📄 04_system_requirements.tex                 # Cap. 4: Requisiti di sistema (RF, RNF, RD e verificabilità)
│   │   │   ├── 📄 05_modelli_ooa.tex                         # Cap. 5: Activity, Sequence e Class Diagrams
│   │   │   └── 📄 06_design_patterns.tex                     # Cap. 6: Design Patterns GoF applicati
│   │   ├── 📂 figure/                                        # Diagrammi UML esportati (.png) e loghi del documento
│   │   │   ├── 🖼️ uc_utente_non_registrato.png               # Diagramma Use Case Utente non registrato + Sistema
│   │   │   ├── 🖼️ uc_cittadino.png                           # Diagramma Use Case Cittadino registrato
│   │   │   ├── 🖼️ uc_autista.png                             # Diagramma Use Case Autista AMA
│   │   │   ├── 🖼️ uc_operatore_sede.png                      # Diagramma Use Case Operatore di sede AMA
│   │   │   ├── 🖼️ uc_amministratore_sede.png                 # Diagramma Use Case Amministratore di sede AMA
│   │   │   ├── 🖼️ uc_amministratore_generale.png             # Diagramma Use Case Amministratore generale AMA
│   │   │   ├── 🖼️ tor_vergata_logo.png                       # Logo ufficiale Ateneo per il frontespizio
│   │   │   ├── 🖼️ cover.jpg / cover.pdf                      # Elementi grafici di copertina
│   │   │   └── 📄 .gitkeep
│   │   └── 📂 sorgenti_vpp/                                  # Archivio modelli sorgente Visual Paradigm per la consegna
│   │
│   ├── 📄 glossario.md                                       # Glossario dei termini di dominio MyAma
│   └── 📄 specifica_MyAma.md                                 # Bozza unificata in Markdown della specifica MyAma
│
├── 📂 MYAMABASIDATI/                                         # Progetto pregresso di Basi di Dati (fonte di dominio)
│   ├── 📄 BASI PROGETTO.pdf                                  # PDF originale del progetto Basi di Dati (30 pag.)
│   └── 📝 BASI_PROGETTO.md                                   # Trascrizione testuale integrale pagina per pagina
│
├── 📂 progettialtrui/                                        # Benchmark e relazioni d'esame suddivise per progetto
│   ├── 📂 Progetto_Pesca_Cipolletta/                         # Progetto "Campionato Pesca Sportiva"
│   │   ├── 📝 Progetto_Cipolletta_Pesca.md                   # Trascrizione Markdown completa (76 pag.)
│   │   └── 📄 Progetto_Cipolletta_Noce_Salvucci_Sfeir.pdf    # PDF originale
│   │
│   ├── 📂 Progetto_Hotel_Mongelli/                           # Progetto "Hotel TorVergata"
│   │   ├── 📝 Progetto_Mongelli_Hotel.md                     # Trascrizione Markdown completa (59 pag.)
│   │   ├── 📄 Progetto_Mongelli_Pace_Rossi_Sandu.pdf         # PDF originale
│   │   ├── 📂 FileProgetto/                                  # Modelli Visual Paradigm (.vpp) estratti
│   │   └── 📦 FileProgetto.zip
│   │
│   ├── 📂 Progetto_RistorApp_Bianchini/                      # Progetto "RistorApp"
│   │   ├── 📝 Progetto_Bianchini_RistorApp.md                # Trascrizione Markdown completa (80 pag.)
│   │   ├── 📄 Progetto_Bianchini_Corsetti_Mazzenga.pdf       # PDF originale
│   │   ├── 📄 Progetto_Bianchini_Corsetti_Mazzenga.vpp       # Modello sorgente Visual Paradigm
│   │   ├── 📄 Solo per i Class Diagrams (Unrefined, Refined).vpp
│   │   └── 📦 Progetto_Bianchini_Corsetti_Mazzenga.zip
│   │
│   └── 📂 Progetto_Buongiorno_Machowski/                     # Progetto "Buongiorno" (Benchmark principale di struttura)
│       └── 📄 Progetto_Buongiorno_Machowski_Muscillo_Politano.pdf # PDF originale
│
└── 📂 TEORIA/                                                # Compendi teorici completi in formato Obsidian Vault
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
- **[`tree.md`](./tree.md)**: Mappa strutturale completa dell'intera repository con descrizione *oneline* e dettagliata di ogni singolo elemento.

---

### 1. `guide/` (Guide Metodologiche, Operative e di Coordinamento)
*Raccolta di tutti i manuali operativi e documenti metodologici per guidare il lavoro del team.*

- **[`guide/guida-progetto.md`](./guide/guida-progetto.md)**: **Teoria orientata al progetto & Modello Mentale**: guida che costruisce il filo conduttore logico del progetto (perché si parte dal Problem Statement, come si passa agli attori e ai Use Case, come dai Use Case si ricavano i requisiti, perché servono i diagrammi Activity/Sequence/Class e perché i Design Pattern arrivano solo su un modello sufficientemente maturo).
- **[`guide/guida-operativa.md`](./guide/guida-operativa.md)**: **Guida Operativa Passo-Passo**: manuale pratico che scandisce il workflow concreto di redazione della specifica (Problem Statement $\to$ Glossario $\to$ Attori $\to$ Use Case $\to$ Requisiti $\to$ Verificabilità $\to$ Activity $\to$ Classi candidate $\to$ Bozza Class Diagram $\to$ BCE $\to$ Sequence $\to$ Class Unrefined $\to$ Class Refined $\to$ Problemi di design & Design Pattern $\to$ Revisione), con analisi delle fasi parallelizzabili per il team.
- **[`guide/divisione-compiti.md`](./guide/divisione-compiti.md)**: **Piano Organizzativo di Team**: piano di ripartizione e coordinamento per 5 persone (lavoro insieme, coppie, gruppi da 3, review incrociate e convergenza).
- **[`guide/plan-giorni.md`](./guide/plan-giorni.md)**: **Roadmap Temporale**: pianificazione cronologica delle attività suddivisa per giorni e milestone di consegna.
- **[`guide/guida-git.md`](./guide/guida-git.md)**: **Guida Git & GitHub per Collaboratori**: istruzioni operative per il team (accettazione inviti, setup iniziale, comandi quotidiani `pull`/`add`/`commit`/`push`, branch di lavoro e risoluzione assistita dei conflitti).
- **[`guide/infoprof.md`](./guide/infoprof.md)**: Istruzioni ufficiali del docente (Prof. Andrea D'Ambrogio) relative a standard IEEE 830-1998, OOA, tool Visual Paradigm e scadenze d'esame.

---

### 2. `MYAMA/` (Cartella Operativa di Progetto)
*Spazio di lavoro dedicato alla stesura, modellazione e integrazione della specifica software d'esame.*

- **[`MYAMA/GRUPPO 1/`](./MYAMA/GRUPPO%201)**: Cartella del sottogruppo 1 con i file di lavoro relativi a Requisiti di Sistema ([`System Requirements.md`](./MYAMA/GRUPPO%201/System%20Requirements.md)), modelli Visual Paradigm (`davidelUseCase.vpp`, `ValerioUseCase.vpp`) e bozze di use case e contesto.
- **[`MYAMA/GRUPPO 2/`](./MYAMA/GRUPPO%202)**: Cartella del sottogruppo 2 con l'elenco consolidato dei casi d'uso ([`LISTA USE CASE.md`](./MYAMA/GRUPPO%202/LISTA%20USE%20CASE.md)), la specifica integrale tabellare ([`User requirements definition.md`](./MYAMA/GRUPPO%202/User%20requirements%20definition.md)) e l'analisi di perimetro e scope ([`FASE_1 - D, E.md`](./MYAMA/GRUPPO%202/FASE_1%20-%20D,%20E.md)).
- **[`MYAMA/Latex PDF/`](./MYAMA/Latex%20PDF)**: Progetto LaTeX completo e compilabile per la relazione d'esame finale:
  - [`main.tex`](./MYAMA/Latex%20PDF/main.tex): File master con configurazione grafica, frontespizio, macro e import delle sezioni.
  - [`main.pdf`](./MYAMA/Latex%20PDF/main.pdf): Documento PDF finale compilato.
  - [`compile_pdf.py`](./MYAMA/Latex%20PDF/compile_pdf.py): Script Python per la compilazione automatizzata a 2 passate.
  - [`sezioni/`](./MYAMA/Latex%20PDF/sezioni): Cartella con i 6 capitoli modulari in LaTeX (`01_introduzione.tex`, `02_glossario.tex`, `03_user_requirements.tex`, `04_system_requirements.tex`, `05_modelli_ooa.tex`, `06_design_patterns.tex`).
  - [`figure/`](./MYAMA/Latex%20PDF/figure): Immagini dei diagrammi UML esportati ad alta definizione.
- **[`MYAMA/glossario.md`](./MYAMA/glossario.md)**: Glossario dei termini di dominio del sistema MyAma.
- **[`MYAMA/specifica_MyAma.md`](./MYAMA/specifica_MyAma.md)**: Specifica integrata in formato Markdown.

---

### 3. `MYAMABASIDATI/`
*Cartella contenente il progetto pregresso del corso di Basi di Dati (disponibile sia in PDF che in trascrizione Markdown per consultazione diretta del dominio).*

- **[`MYAMABASIDATI/`](./MYAMABASIDATI)**: Cartella del progetto di riferimento per il dominio "MyAma".
- **[`MYAMABASIDATI/BASI_PROGETTO.md`](./MYAMABASIDATI/BASI_PROGETTO.md)**: Trascrizione integrale in formato Markdown (pagina per pagina) della specifica di "MyAma".
- **[`MYAMABASIDATI/BASI PROGETTO.pdf`](./MYAMABASIDATI/BASI%20PROGETTO.pdf)**: Documento originale in formato PDF (30 pag.).

---

### 4. `progettialtrui/`
*Cartella contenente i progetti d'esame di riferimento, ciascuno organizzato in una propria sottocartella dedicata contenente PDF, trascrizioni Markdown `.md` e modelli UML `.vpp`.*

- **[`progettialtrui/`](./progettialtrui)**: Raccolta dei progetti benchmark di altri studenti.
- **[`progettialtrui/Progetto_Pesca_Cipolletta/`](./progettialtrui/Progetto_Pesca_Cipolletta)**:
  - [`Progetto_Cipolletta_Pesca.md`](./progettialtrui/Progetto_Pesca_Cipolletta/Progetto_Cipolletta_Pesca.md): Trascrizione testuale integrale (76 pagine).
  - [`Progetto_Cipolletta_Noce_Salvucci_Sfeir.pdf`](./progettialtrui/Progetto_Pesca_Cipolletta/Progetto_Cipolletta_Noce_Salvucci_Sfeir.pdf): Documento PDF originale.
- **[`progettialtrui/Progetto_Hotel_Mongelli/`](./progettialtrui/Progetto_Hotel_Mongelli)**:
  - [`Progetto_Mongelli_Hotel.md`](./progettialtrui/Progetto_Hotel_Mongelli/Progetto_Mongelli_Hotel.md): Trascrizione testuale integrale (59 pagine).
  - [`Progetto_Mongelli_Pace_Rossi_Sandu.pdf`](./progettialtrui/Progetto_Hotel_Mongelli/Progetto_Mongelli_Pace_Rossi_Sandu.pdf): Documento PDF originale.
  - [`FileProgetto/`](./progettialtrui/Progetto_Hotel_Mongelli/FileProgetto): Modelli sorgente Visual Paradigm estratti (`.vpp`).
  - [`FileProgetto.zip`](./progettialtrui/Progetto_Hotel_Mongelli/FileProgetto.zip): Archivio compresso dei modelli.
- **[`progettialtrui/Progetto_RistorApp_Bianchini/`](./progettialtrui/Progetto_RistorApp_Bianchini)**:
  - [`Progetto_Bianchini_RistorApp.md`](./progettialtrui/Progetto_RistorApp_Bianchini/Progetto_Bianchini_RistorApp.md): Trascrizione testuale integrale (80 pagine).
  - [`Progetto_Bianchini_Corsetti_Mazzenga.pdf`](./progettialtrui/Progetto_RistorApp_Bianchini/Progetto_Bianchini_Corsetti_Mazzenga.pdf): Documento PDF originale.
  - [`Progetto_Bianchini_Corsetti_Mazzenga.vpp`](./progettialtrui/Progetto_RistorApp_Bianchini/Progetto_Bianchini_Corsetti_Mazzenga.vpp): File di progetto Visual Paradigm.
  - [`Solo per i Class Diagrams (Unrefined, Refined).vpp`](./progettialtrui/Progetto_RistorApp_Bianchini/Solo%20per%20i%20Class%20Diagrams%20(Unrefined,%20Refined).vpp): File di modelli per i Class Diagram.
  - [`Progetto_Bianchini_Corsetti_Mazzenga.zip`](./progettialtrui/Progetto_RistorApp_Bianchini/Progetto_Bianchini_Corsetti_Mazzenga.zip): Archivio compresso del progetto.
- **[`progettialtrui/Progetto_Buongiorno_Machowski/`](./progettialtrui/Progetto_Buongiorno_Machowski)**:
  - [`Progetto_Buongiorno_Machowski_Muscillo_Politano.pdf`](./progettialtrui/Progetto_Buongiorno_Machowski/Progetto_Buongiorno_Machowski_Muscillo_Politano.pdf): Documento PDF originale di riferimento per la struttura della specifica.

---

### 5. `TEORIA/`
*Cartella contenente le dispense teoriche complete del corso di Ingegneria del Software in formato Obsidian Vault Markdown con immagini, tabelle e diagrammi integrati.*

- **[`TEORIA/`](./TEORIA)**: Cartella principale con i compendi di teoria.
- **[`ISW_obsidian_full/`](./TEORIA/ISW_obsidian_full)**: Vault Obsidian con [`ISW.md`](./TEORIA/ISW_obsidian_full/ISW_obsidian_full/ISW.md) (teoria completa) e 178 immagini.
- **[`IS_andrea_obsidian_full/`](./TEORIA/IS_andrea_obsidian_full)**: Vault Obsidian con [`IS_andrea.md`](./TEORIA/IS_andrea_obsidian_full/IS_andrea_obsidian_full/IS_andrea.md) (90 pagine di appunti) e 50 figure.
