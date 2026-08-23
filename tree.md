# 📂 Mappa della Repository (Progetto ISW - MyAma)

Questo documento fornisce una panoramica strutturata e descrittiva di tutte le cartelle e i file presenti nella repository. Serve come bussola per orientarsi rapidamente tra i vari documenti di progetto, le dispense di teoria e i progetti di riferimento.

- **[`README.md`](./README.md)**: Presentazione generale del progetto, ruoli, struttura e requisiti d'esame.
- **[`idea.md`](./idea.md)**: Visione sintetica del progetto per allineare il gruppo sul dominio di MyAma.
- **[`tree.md`](./tree.md)**: Mappa strutturale completa dell'intera repository con collegamenti diretti.

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

### 2. `KNOWLEDGE/` (Dominio di Business e Visione)
*Documentazione fondamentale sul dominio e sulle regole di business del sistema MyAma.*

- **[`KNOWLEDGE/ideaprogetto.md`](./KNOWLEDGE/ideaprogetto.md)**: **Documento di Visione ed Esplorazione del Dominio**: specifica dettagliata del problem statement, analisi dei servizi (ritiro a domicilio e conferimento in sede), matrice degli attori, regole di business e mappatura dei requisiti OOA con opportunità per i Design Pattern.

---

### 3. `MYAMA/` (Cartella Operativa di Progetto)
*Spazio di lavoro dedicato alla stesura, modellazione e integrazione della specifica software d'esame.*

#### 📂 `MYAMA/PROGETTOFINALE/` (Artefatti Consolidati di Progetto)
- **[`MYAMA/PROGETTOFINALE/glossario.md`](./MYAMA/PROGETTOFINALE/glossario.md)**: Glossario formale dei termini di dominio del sistema MyAma.
- **[`MYAMA/PROGETTOFINALE/specifica_MyAma.md`](./MYAMA/PROGETTOFINALE/specifica_MyAma.md)**: Specifica integrata e consolidata in formato Markdown.
- **[`MYAMA/PROGETTOFINALE/ACTIVITY DIAGRAM/`](./MYAMA/PROGETTOFINALE/ACTIVITY%20DIAGRAM)**:
  - **[`LISTA ACTIVITY DIAGRAM.md`](./MYAMA/PROGETTOFINALE/ACTIVITY%20DIAGRAM/LISTA%20ACTIVITY%20DIAGRAM.md)**: Indice e tracciamento di tutti gli Activity Diagram previsti.
  - Cartelle con diagrammi esportati (`.jpg`/`.png`) e modelli sorgente (`.vpp`) suddivisi per membro del gruppo: Alfredo, Davide (`davidelUseCase.vpp`), Luca (`ActivityLuca.vpp`), Samuele (sottocartelle per Amministratore Generale e Utente non registrato/Cittadino), Valerio.
- **[`MYAMA/PROGETTOFINALE/CLASS DIAGRAM/`](./MYAMA/PROGETTOFINALE/CLASS%20DIAGRAM)**:
  - `class diagram unrefined.vpp`: Modello sorgente Visual Paradigm dell'Unrefined Class Diagram.
- **[`MYAMA/PROGETTOFINALE/INTRODUZIONE/`](./MYAMA/PROGETTOFINALE/INTRODUZIONE)**:
  - `INTRODUZIONE CHAT GPT.md` e `INTRODUZIONE NO CHAT GPT.md`: Bozze e testi per l'introduzione e il problem statement della relazione.
- **[`MYAMA/PROGETTOFINALE/SYSTEM REQUIREMENTS/`](./MYAMA/PROGETTOFINALE/SYSTEM%20REQUIREMENTS)**:
  - **[`System Requirements.md`](./MYAMA/PROGETTOFINALE/SYSTEM%20REQUIREMENTS/System%20Requirements.md)**: Specifica dei Requisiti Funzionali, Non Funzionali e di Dominio.
- **[`MYAMA/PROGETTOFINALE/USE CASE DIAGRAM/`](./MYAMA/PROGETTOFINALE/USE%20CASE%20DIAGRAM)**:
  - **[`LISTA USE CASE.md`](./MYAMA/PROGETTOFINALE/USE%20CASE%20DIAGRAM/LISTA%20USE%20CASE.md)**: Elenco completo e strutturato di tutti i Casi d'Uso del sistema.
  - **[`User requirements definition.md`](./MYAMA/PROGETTOFINALE/USE%20CASE%20DIAGRAM/User%20requirements%20definition.md)**: Schede descrittive dettagliate per ciascun Use Case.
  - **`Use Case/`**: Modelli `.vpp` (`davidelUseCase.vpp`, `ValerioUseCase.vpp`) e diagrammi esportati in JPG per ciascun attore.
- **[`MYAMA/PROGETTOFINALE/Latex PDF/`](./MYAMA/PROGETTOFINALE/Latex%20PDF)**: Progetto LaTeX master per la relazione d'esame:
  - [`main.tex`](./MYAMA/PROGETTOFINALE/Latex%20PDF/main.tex): Master file con configurazione grafica, frontespizio e inclusione dei capitoli.
  - [`main.pdf`](./MYAMA/PROGETTOFINALE/Latex%20PDF/main.pdf): Documento PDF compilato della relazione finale.
  - [`compile_pdf.py`](./MYAMA/PROGETTOFINALE/Latex%20PDF/compile_pdf.py): Script Python di automazione per la compilazione del documento.
  - [`sezioni/`](./MYAMA/PROGETTOFINALE/Latex%20PDF/sezioni): Capitoli modulari LaTeX (`01_introduzione.tex`, `02_glossario.tex`, `03_user_requirements.tex`, `04_system_requirements.tex`, `05_modelli_ooa.tex`, `06_design_patterns.tex`).
  - [`figure/`](./MYAMA/PROGETTOFINALE/Latex%20PDF/figure): Repository di tutte le immagini e i diagrammi esportati ad alta risoluzione per il PDF.

#### 📂 `MYAMA/GRUPPO 1/` (Workspace di Lavoro Sottogruppo 1)
- `ProgettoVPdavidel.vpp`, `RefinedClassDIagam.vpp`: Modelli di lavoro preliminari.
- **[`MYAMA/GRUPPO 1/SEQUENCE DIAGRAM/`](./MYAMA/GRUPPO%201/SEQUENCE%20DIAGRAM)**:
  - **[`LISTA SEQUENCE DIAGRAM.md`](./MYAMA/GRUPPO%201/SEQUENCE%20DIAGRAM/LISTA%20SEQUENCE%20DIAGRAM.md)**: Elenco dei sequence diagram da realizzare.
  - **[`MESSAGGI.md`](./MYAMA/GRUPPO%201/SEQUENCE%20DIAGRAM/MESSAGGI.md)**, **[`METODI.md`](./MYAMA/GRUPPO%201/SEQUENCE%20DIAGRAM/METODI.md)**, **[`METODI ASSOCIATI A MESSAGGI.md`](./MYAMA/GRUPPO%201/SEQUENCE%20DIAGRAM/METODI%20ASSOCIATI%20A%20MESSAGGI.md)**, **[`SINCRONA E ASINCRONA.md`](./MYAMA/GRUPPO%201/SEQUENCE%20DIAGRAM/SINCRONA%20E%20ASINCRONA.md)**: Note metodologiche per la modellazione dei flussi dinamici BCE.

#### 📂 `MYAMA/GRUPPO 2/` (Workspace di Lavoro Sottogruppo 2)
- Cartella di lavoro per il secondo sottogruppo.

---

### 4. `PROGETTO DATA BASI/` (Dominio Pregresso MyAma)
*Cartella contenente il progetto pregresso del corso di Basi di Dati (disponibile sia in PDF che in trascrizione Markdown per consultazione diretta del dominio).*

- **[`PROGETTO DATA BASI/`](./PROGETTO%20DATA%20BASI)**: Cartella del progetto di riferimento per il dominio "MyAma".
- **[`PROGETTO DATA BASI/BASI_PROGETTO.md`](./PROGETTO%20DATA%20BASI/BASI_PROGETTO.md)**: Trascrizione integrale in formato Markdown (pagina per pagina) della specifica di "MyAma" per Basi di Dati.
- **[`PROGETTO DATA BASI/BASI PROGETTO.pdf`](./PROGETTO%20DATA%20BASI/BASI%20PROGETTO.pdf)**: Documento originale in formato PDF (30 pag.).
- **[`PROGETTO DATA BASI/prompt_immagine.md`](./PROGETTO%20DATA%20BASI/prompt_immagine.md)**: Documento ausiliario.

---

### 5. `OTHER PROGETTI/` (Benchmark e Progetti d'Esame di Riferimento)
*Cartella contenente i progetti d'esame di riferimento, ciascuno organizzato in una propria sottocartella dedicata contenente PDF, trascrizioni Markdown `.md` e modelli UML `.vpp`.*

- **[`OTHER PROGETTI/`](./OTHER%20PROGETTI)**: Raccolta dei progetti benchmark di altri studenti.
- **[`OTHER PROGETTI/Progetto_Pesca_Cipolletta/`](./OTHER%20PROGETTI/Progetto_Pesca_Cipolletta)**:
  - [`Progetto_Cipolletta_Pesca.md`](./OTHER%20PROGETTI/Progetto_Pesca_Cipolletta/Progetto_Cipolletta_Pesca.md): Trascrizione testuale integrale (76 pagine).
  - [`Progetto_Cipolletta_Noce_Salvucci_Sfeir_250128_154245.pdf`](./OTHER%20PROGETTI/Progetto_Pesca_Cipolletta/Progetto_Cipolletta_Noce_Salvucci_Sfeir_250128_154245.pdf): Documento PDF originale.
- **[`OTHER PROGETTI/Progetto_Hotel_Mongelli/`](./OTHER%20PROGETTI/Progetto_Hotel_Mongelli)**:
  - [`Progetto_Mongelli_Hotel.md`](./OTHER%20PROGETTI/Progetto_Hotel_Mongelli/Progetto_Mongelli_Hotel.md): Trascrizione testuale integrale (59 pagine).
  - [`Progetto_Mongelli_Pace_Rossi_Sandu.pdf`](./OTHER%20PROGETTI/Progetto_Hotel_Mongelli/Progetto_Mongelli_Pace_Rossi_Sandu.pdf): Documento PDF originale.
  - [`FileProgetto/`](./OTHER%20PROGETTI/Progetto_Hotel_Mongelli/FileProgetto): Modelli sorgente Visual Paradigm estratti (`.vpp`).
  - [`FileProgetto.zip`](./OTHER%20PROGETTI/Progetto_Hotel_Mongelli/FileProgetto.zip): Archivio compresso dei modelli.
- **[`OTHER PROGETTI/Progetto_RistorApp_Bianchini/`](./OTHER%20PROGETTI/Progetto_RistorApp_Bianchini)**:
  - [`Progetto_Bianchini_RistorApp.md`](./OTHER%20PROGETTI/Progetto_RistorApp_Bianchini/Progetto_Bianchini_RistorApp.md): Trascrizione testuale integrale (80 pagine).
  - [`Progetto_Bianchini_Corsetti_Mazzenga.pdf`](./OTHER%20PROGETTI/Progetto_RistorApp_Bianchini/Progetto_Bianchini_Corsetti_Mazzenga.pdf): Documento PDF originale.
  - [`Progetto_Bianchini_Corsetti_Mazzenga.vpp`](./OTHER%20PROGETTI/Progetto_RistorApp_Bianchini/Progetto_Bianchini_Corsetti_Mazzenga.vpp): File di progetto Visual Paradigm.
  - [`Solo per i Class Diagrams (Unrefined, Refined).vpp`](./OTHER%20PROGETTI/Progetto_RistorApp_Bianchini/Solo%20per%20i%20Class%20Diagrams%20%28Unrefined,%20Refined%29.vpp): File di modelli per i Class Diagram.
  - [`Progetto_Bianchini_Corsetti_Mazzenga.zip`](./OTHER%20PROGETTI/Progetto_RistorApp_Bianchini/Progetto_Bianchini_Corsetti_Mazzenga.zip): Archivio compresso del progetto.
- **[`OTHER PROGETTI/Progetto_Buongiorno_Machowski/`](./OTHER%20PROGETTI/Progetto_Buongiorno_Machowski)**:
  - [`Progetto_Buongiorno_Machowski_Muscillo_Politano.pdf`](./OTHER%20PROGETTI/Progetto_Buongiorno_Machowski/Progetto_Buongiorno_Machowski_Muscillo_Politano.pdf): Documento PDF originale di riferimento primario per la struttura della specifica IEEE 830.
- **[`OTHER PROGETTI/SteamPlatform_Arbia,Di Iacovo, Malatesta, Marzi, Quartucci/`](./OTHER%20PROGETTI/SteamPlatform_Arbia,Di%20Iacovo,%20Malatesta,%20Marzi,%20Quartucci)**:
  - [`ProgettoISW_25_26.pdf`](./OTHER%20PROGETTI/SteamPlatform_Arbia,Di%20Iacovo,%20Malatesta,%20Marzi,%20Quartucci/ProgettoISW_25_26.pdf): Documento PDF della relazione.
  - `ISW Progetto.vpp`: File di progetto Visual Paradigm.

---

### 6. `TEORIA/` (Compendi Teorici Completi)
*Cartella contenente le dispense teoriche complete del corso di Ingegneria del Software in formato Obsidian Vault Markdown con immagini, tabelle e diagrammi integrati.*

- **[`TEORIA/`](./TEORIA)**: Cartella principale con i compendi di teoria.
- **[`TEORIA/ISW_obsidian_full/`](./TEORIA/ISW_obsidian_full)**: Vault Obsidian con [`ISW.md`](./TEORIA/ISW_obsidian_full/ISW_obsidian_full/ISW.md) (dispensa teorica generale completa) e 178 immagini a corredo.
- **[`TEORIA/IS_andrea_obsidian_full/`](./TEORIA/IS_andrea_obsidian_full)**: Vault Obsidian con [`IS_andrea.md`](./TEORIA/IS_andrea_obsidian_full/IS_andrea_obsidian_full/IS_andrea.md) (90 pagine di appunti del corso) e 50 figure integrate.
