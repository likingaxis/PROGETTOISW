# 📐 Modelli Visual Paradigm & Diagrammi — *MyAma*

In questa cartella vengono conservati i file di modellazione UML e le esportazioni grafiche del progetto MyAma.

---

## 📁 Struttura della Cartella

```text
visual-paradigm/
├── README.md               # Istruzioni operative sul tool
├── MyAma.vpp               # Progetto sorgente Visual Paradigm (condiviso)
└── diagrammi/              # Esportazioni ad alta risoluzione (.png)
    ├── UCD_Generale.png
    ├── AD_RitiroDomicilio.png
    ├── SD_PrenotazioneDomicilio.png
    ├── CD_Unrefined.png
    └── CD_Refined.png
```

---

## ⚙️ Istruzioni per il Team

1. **Versione Unica Condivisa**:
   - Per evitare conflitti binari non risolvibili su Git, **una sola persona alla volta** modifica il file `.vpp`.
   - Prima di aprire Visual Paradigm, eseguire sempre `git pull`.
   - Dopo aver terminato le modifiche, salvare il file `.vpp`, esportare le immagini aggiornate nella cartella `diagrammi/` ed effettuare subito `git commit` e `git push`.

2. **Esportazione Diagrammi**:
   - In Visual Paradigm: `Project` $\to$ `Export` $\to$ `Active Diagram as Image...` (oppure `Export All Diagrams as Images...`).
   - Selezionare formato **PNG** ad alta qualità (300 DPI o scala 100%).
