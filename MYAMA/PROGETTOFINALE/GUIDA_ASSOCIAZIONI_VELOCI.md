# Guida Rapida: Inserimento Veloce delle Associazioni in Visual Paradigm

Questa guida illustra il metodo più rapido in assoluto (chiamato **Sticky Tool** o **Disegno Continuo**) per trasferire le relazioni da un documento testuale o Markdown (.md) al diagramma di Visual Paradigm, limitando al minimo gli spostamenti del mouse.

---

## 1. Preparazione dell'Area di Lavoro

Per massimizzare la velocità, è fondamentale impostare lo schermo in modo da non dover mai cambiare finestra:
1. **Dividi lo schermo a metà:** 
   * Metà sinistra: apri il file di testo/markdown con l'elenco delle relazioni (es. *Cittadino -> Prenotazione*).
   * Metà destra: tieni aperto Visual Paradigm con il tuo Class Diagram.
2. Assicurati che **tutte le classi** siano già state create o trascinate nel diagramma, anche se sono disposte in modo disordinato.

---

## 2. Il Metodo "Sticky Tool" (Clic Continuo)

Invece di selezionare lo strumento di collegamento, cliccare le due classi e poi dover tornare sulla barra degli strumenti per il collegamento successivo, procedi così:

1. Vai nella barra degli strumenti di Visual Paradigm (solitamente a sinistra).
2. Fai **DOPPIO CLIC** rapido sull'icona della relazione che devi inserire (ad esempio la freccia **Association**).
   * *Risultato:* L'icona rimarrà evidenziata e il tuo cursore rimarrà bloccato in modalità "creazione associazione".
3. Ora leggi la prima riga dal tuo elenco e clicca in sequenza:
   * Clicca sulla classe **Sorgente**
   * Clicca sulla classe **Destinazione**
4. La linea apparirà all'istante. **Senza fare nient'altro**, leggi la seconda riga del tuo elenco e continua a cliccare: *Sorgente -> Destinazione*.
5. Procedi a "raffica" per tutte le relazioni di quel tipo.

---

## 3. Cambiare Tipo di Relazione

Quando finisci tutte le *Association* e devi iniziare a inserire, ad esempio, le *Composition* o le *Generalization*:

1. Premi il tasto **ESC** sulla tastiera. (Questo sblocca il cursore dal precedente Sticky Tool).
2. Fai **DOPPIO CLIC** sulla nuova icona (es. *Composition*) nella barra degli strumenti.
3. Ricomincia a cliccare in serie sulle classi.

---

## Suggerimenti Finali

* **Non preoccuparti del disordine:** All'inizio il diagramma sembrerà un nido di ragno incomprensibile. L'importante in questa fase è inserire tutte le relazioni correttamente.
* **Sistemazione grafica:** Solo dopo aver tracciato tutte le linee, potrai spostare le classi e usare i pallini di ancoraggio delle frecce per raddrizzarle (usando lo stile ortogonale se preferisci).
* **Shortcut da tastiera (Avanzato):** Se preferisci, puoi andare su Window > Application Options > Keys, cercare "Association" e assegnargli una scorciatoia (es. Ctrl+1). In quel caso basterà cliccare la prima classe, premere Ctrl+1 e cliccare la seconda. Ma il doppio clic rimane solitamente il metodo più comodo se stai leggendo da una lista.
