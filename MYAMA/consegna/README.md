# 📦 Cartella Consegna — Progetto MyAma (Ingegneria del Software)

Questa cartella contiene il **template modificabile ufficiale** per la redazione della relazione finale di specifica software secondo lo standard **IEEE 830-1998** richiesto dal Prof. Andrea D'Ambrogio.

---

## ❓ FAQ: Va scritto in LaTeX o che cosa?

### Risposta del docente e prassi del corso
- **Cosa va consegnato via email (`dambro@uniroma2.it`)**: 
  1. Il file **PDF finale** della specifica software compilata.
  2. L'archivio contenente i **file sorgenti Visual Paradigm (`.vpp`)**.
- **In che formato scrivere il documento modificabile?**
  - **LaTeX è lo standard consigliato e de facto** utilizzato per l'esame (come attestano tutti i progetti benchmark: *Hotel TorVergata*, *Pesca*, *Buongiorno*, *RistorApp*).
  - **Vantaggi di LaTeX:**
    - Generazione automatica di indice, lista figure e lista tabelle.
    - Numerazione gerarchica automatica dei capitoli, sezioni e schede Use Case (`3.1.1`, `3.1.2`, ecc.).
    - Gestione impeccabile di tabelle complesse per i Requisiti (RF, RNF, RD) e per la Verificabilità.
    - Facile inclusione e scalatura delle immagini dei diagrammi UML esportati da Visual Paradigm.
    - Collaborazione in tempo reale su **Overleaf** o tramite versionamento Git.
  - *Nota:* Se il gruppo preferisse usare Word / Google Docs o Markdown compilato, è formalmente accettato purché il **PDF finale esportato rispetti esattamente la struttura delle sezioni IEEE 830-1998**. Tuttavia il template LaTeX fornito qui è già completamente impostato e pronto.

---

## 📁 Struttura della Cartella `consegna/`

```text
consegna/
│
├── main.tex                       # File principale LaTeX (impostazioni, frontespizio, indici, include)
├── README.md                      # Questa guida operativa
├── specifica_MyAma.md             # Versione modificabile completa in formato Markdown
│
├── sezioni/                       # File .tex modulari (uno per capitolo, facili da modificare in parallelo)
│   ├── 01_introduzione.tex        # Problem Statement, Scopo, Scope IN/OUT, Attori
│   ├── 02_glossario.tex           # Tabella del Glossario dei termini di dominio
│   ├── 03_user_requirements.tex   # Use Case per attore + Schede tabellari descrittive
│   ├── 04_system_requirements.tex # RF, RNF, RD e Matrice di Verificabilità
│   ├── 05_modelli_ooa.tex         # Activity Diagram, Sequence Diagram (BCE), Class Diagrams
│   └── 06_design_patterns.tex     # Design Pattern applicati al Class Diagram (Observer, Strategy)
│
├── figure/                        # Cartella in cui salvare le immagini esportate da Visual Paradigm (.png / .pdf)
└── sorgenti_vpp/                  # Cartella per i file sorgente di Visual Paradigm (.vpp) da zippare per la consegna
```

---

## 🚀 Come usare il Template LaTeX

### Opzione 1: Utilizzo con Overleaf (Consigliato per lavorare in gruppo)
1. Vai su [Overleaf](https://www.overleaf.com/) e crea un nuovo progetto ("Blank Project" o "Upload Project").
2. Seleziona **Upload** e carica l'intero contenuto della cartella `consegna/` (o carica un archivio zip di `consegna/`).
3. Imposta `main.tex` come file principale (Main document).
4. Premi **Recompile**: il documento genererà il PDF completo con frontespizio, indice e tutte le sezioni.
5. Man mano che esportate i diagrammi da Visual Paradigm in `.png`, caricateli nella cartella `figure/` e decommentate i comandi `\includegraphics` nei file `.tex`.

### Opzione 2: Compilazione in Locale (VS Code / TeX Live / MiKTeX)
Se hai installato una distribuzione LaTeX (es. TeX Live o MiKTeX) con VS Code (estensione LaTeX Workshop):
```bash
# Compilazione da terminale:
pdflatex main.tex
pdflatex main.tex   # seconda passata per aggiornare l'indice
```

---

## 📋 Checklist per la Consegna Finale al Docente
- [ ] Compilare i dati del frontespizio in `main.tex` con nomi e matricole di tutti i 5 componenti del gruppo.
- [ ] Completare le schede Use Case e i Requisiti concordati.
- [ ] Esportare tutti i diagrammi UML da Visual Paradigm a risoluzione elevata (`.png` o `.pdf`) e inserirli nella cartella `figure/`.
- [ ] Verificare che il Class Diagram Refined sia coerente con i Sequence Diagram (BCE) e che siano illustrati almeno 2 Design Pattern.
- [ ] Compilare il PDF definitivo e verificare che non vi siano errori di impaginazione.
- [ ] Comprimere i file `.vpp` di Visual Paradigm in un file zip (es. `Sorgenti_VisualParadigm_MyAma.zip`).
- [ ] Inviare PDF + file zip a `dambro@uniroma2.it` almeno **5 giorni prima** dell'appello d'esame.
