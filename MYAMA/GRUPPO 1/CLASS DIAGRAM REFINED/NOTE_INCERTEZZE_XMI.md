# NOTE E INCERTEZZE SUL FILE XMI — STEP 3

## ✅ Cosa è stato fatto con certezza

1. **XML sintatticamente valido** — verificato con `xmllint`.
2. **Formato XMI 2.1** — compatibile con Visual Paradigm per l'import via "File > Import > XMI".
3. **46 classi totali** modellate (19 Entity, 14 Boundary, 13 Control).
4. **Tutte le operazioni** estratte dai 5 `project.xml` dei sequence diagram sono state incluse.
5. **Tutti gli attributi** dal Class Diagram Unrefined sono stati preservati.
6. **8 generalizzazioni** correttamente modellate.
7. **14 associazioni** con molteplicità corrette dal CD Unrefined.
8. **2 nuove classi Entity** emerse dai sequence diagram: `ZonaCAP` e `Assegnazione`.

---

## ⚠️ Incertezze e potenziali problemi

### 1. Importazione in Visual Paradigm
> **Visual Paradigm potrebbe non posizionare automaticamente le classi nel diagramma.**
> Dopo l'import, probabilmente dovrai creare manualmente un nuovo Class Diagram e trascinare le classi dal Model Explorer.
> L'XMI definisce il modello (classi, attributi, metodi, relazioni), NON il layout grafico.

### 2. UserRegistry vs AMAServiceRegister
> Nei sequence diagram di Davide ci sono **due lifeline diverse** che svolgono ruoli simili:
> - `UserRegistry` — usato per registrazione/creazione utenti
> - `AMAServiceRegister` — usato per operazioni su prenotazioni (book, availability, cancel)
>
> Li ho **unificati in `UserRegistry`** nel refined, perché tutti i metodi convergono lì.
> **Se volete tenerli separati**, basta duplicare la classe e redistribuire i metodi.

### 3. Tipi di dato
> Ho usato i tipi primitivi UML standard (`String`, `Integer`, `Boolean`).
> Per i tipi come `LocalDate` e `LocalTime` (presenti nel CD Unrefined per `data`, `oraInizio`, `oraFine`),
> li ho mappati come `String` nell'XMI perché Visual Paradigm potrebbe non riconoscere `LocalDate` come tipo nativo.
> **Potete cambiarli a mano in VP dopo l'import** selezionando il tipo Java corretto.

### 4. Stereotipi BCE
> Gli stereotipi `<<boundary>>`, `<<control>>`, `<<entity>>` **non sono inclusi nell'XMI come stereotipi UML formali**
> perché richiederebbero un profilo UML custom.
> Le classi sono organizzate in **package separati** (`Entity`, `Boundary`, `Control`) per chiarezza.
> **In Visual Paradigm potete applicare gli stereotipi manualmente** dopo l'import.

### 5. Operazioni duplicate tra sequence diagram diversi
> Alcuni metodi appaiono con firme leggermente diverse tra i diversi autori (es. `registrationForward` in Davide vs `forwardData` in Valerio).
> Ho incluso **tutte le varianti** per completezza. Potreste voler consolidare durante il review.

### 6. Classe `Assegnazione`
> Appare come lifeline in Alfredo (SequenceVisualizzareRitiriAssegnati) ma **non ha attributi specifici nei sequence diagram**.
> Gli attributi `idAssegnazione` e `dataAssegnazione` sono stati **inferiti** dal contesto.

### 7. AccountDB di Valerio
> Valerio usa una lifeline `Account DB` che non corrisponde a una classe entity nel CD Unrefined.
> L'ho **mappata come parte di UserRegistry** (che agisce da persistence layer).
> Se volete un'entità separata per il database, è da aggiungere.

---

## 📋 Come importare in Visual Paradigm

1. Apri Visual Paradigm
2. Vai su **File > Import > XMI...**
3. Seleziona il file `REFINE CLASS DIAGRAM.xmi`
4. Conferma le opzioni di import (mantieni i default)
5. Le classi appariranno nel **Model Explorer** sotto il package `MyAma_RefinedClassDiagram`
6. Crea un nuovo **Class Diagram** e trascina le classi dal Model Explorer
7. Applica gli stereotipi BCE manualmente se necessario
8. Verifica che le generalizzazioni e associazioni siano visualizzate correttamente
