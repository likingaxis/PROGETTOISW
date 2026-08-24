# 7. DESIGN PATTERN

Come richiesto dalle linee guida di progetto, in questa sezione vengono presentati due Design Pattern (classificati secondo la definizione della *Gang of Four*) applicati all'interno del sistema **MyAma**. L'introduzione di tali pattern ha l'obiettivo di risolvere specifiche criticità architetturali, favorendo principi fondamentali dell'ingegneria del software quali il basso accoppiamento (low coupling), l'alta coesione (high cohesion) e il principio Open/Closed.

---

## 7.1. Observer Pattern (Pattern Comportamentale)

### Descrizione del Problema e Criticità di Design
All'interno del dominio applicativo di MyAma, la classe \Prenotazione\ rappresenta una delle entità centrali, la quale subisce continui cambiamenti di stato nel corso del suo ciclo di vita (es. passaggio da *In attesa* a *Confermata*, *In corso*, *Completata* o *Annullata*). Ad ogni transizione di stato, è fondamentale che diversi sottosistemi indipendenti vengano informati per reagire di conseguenza:
* Il sistema di notifica (per avvisare il cittadino via email o SMS);
* La dashboard degli autisti (per aggiornare in tempo reale l'itinerario giornaliero);
* Il registro operativo della sede (per tracciare i flussi e compilare statistiche).

Qualora la classe \Prenotazione\ dovesse istanziare e invocare direttamente i metodi delle classi concrete di questi sottosistemi, si creerebbe un accoppiamento rigido e unidirezionale. Questo violerebbe pesantemente il principio *Open/Closed*: ogni volta che si volesse aggiungere un nuovo modulo interessato ai cambiamenti della prenotazione, si renderebbe necessaria una modifica al codice sorgente della classe \Prenotazione\ stessa.

### Soluzione Progettuale
Per risolvere tale criticità è stato applicato il Design Pattern comportamentale **Observer**. Tale pattern consente di definire una dipendenza uno-a-molti tra gli oggetti, facendo in modo che quando l'oggetto osservato (Subject) cambia stato, tutti gli oggetti dipendenti (Observers) vengano notificati e si aggiornino automaticamente.
In questo modo, la classe \Prenotazione\ si limita a mantenere una lista di riferimenti a un'interfaccia astratta e si occupa esclusivamente di lanciare una notifica generica di aggiornamento, senza conoscere la logica implementativa o la natura dei ricevitori.

### Partecipanti (Elementi del Diagramma UML)
* **Subject (Observable):** La classe \Prenotazione\. Contiene i metodi per registrare (\ttach\), rimuovere (\detach\) e notificare (\
otifyObservers\) gli ascoltatori, oltre al proprio stato interno.
* **Observer:** L'interfaccia \PrenotazioneObserver\ che espone il metodo \update(prenotazione: Prenotazione)\.
* **ConcreteObserver:** Le classi concrete che implementano l'interfaccia, ovvero \EmailNotifier\, \DashboardAutistaNotifier\ e \RegistroSedeObserver\. Ciascuna di esse implementa la propria logica specifica all'interno del metodo \update\.

*(Inserire qui il diagramma UML esportato da Visual Paradigm)*

---

## 7.2. Strategy Pattern (Pattern Comportamentale)

### Descrizione del Problema e Criticità di Design
La gestione operativa dei ritiri a domicilio e la composizione dell'itinerario dei veicoli AMA sono processi complessi che variano a seconda delle condizioni quotidiane, delle politiche aziendali e delle disponibilità di mezzi e personale. In particolare, il sistema deve poter supportare differenti algoritmi di assegnazione:
* **Politica di Massimizzazione del Carico:** algoritmo mirato a ottimizzare il riempimento (in volume e peso) dei mezzi prima del loro rientro in sede.
* **Politica di Prossimità Territoriale:** algoritmo mirato a minimizzare i tempi e i chilometri percorsi, raggruppando i ritiri per aree limitrofe (stesso CAP).
* **Politica di Bilanciamento del Carico di Lavoro:** algoritmo mirato a distribuire equamente il numero di richieste tra gli autisti in turno.

Inserire la logica di tutti questi algoritmi direttamente all'interno della classe \GestoreAssegnazione\, impiegando complesse e lunghe catene condizionali (\if-else\ o \switch-case\), porterebbe alla creazione di una "God Class" difficilmente manutenibile (violazione del *Single Responsibility Principle*). Inoltre, l'aggiunta di una futura nuova politica di smistamento richiederebbe la modifica di codice già testato e consolidato.

### Soluzione Progettuale
Al fine di garantire flessibilità e manutenibilità, si è optato per l'applicazione dello **Strategy Pattern**. Questo pattern permette di incapsulare una famiglia di algoritmi all'interno di classi separate e intercambiabili a tempo di esecuzione, rendendo l'algoritmo indipendente dal client che ne fa uso.
Il controller dedicato alla pianificazione interagirà unicamente con un'interfaccia comune, delegando a runtime il calcolo dell'itinerario all'algoritmo (strategia) attualmente selezionato dall'amministratore di sede o dal sistema.

### Partecipanti (Elementi del Diagramma UML)
* **Context:** La classe \GestoreAssegnazione\. Essa mantiene un riferimento all'interfaccia \AssegnazioneStrategy\ ed espone un metodo (es. \pianificaRitiri()\) che al suo interno richiama l'algoritmo della strategia.
* **Strategy:** L'interfaccia \AssegnazioneStrategy\ che dichiara il metodo astratto polimorfico \calcolaAssegnazione(richieste: List, mezzi: List)\.
* **ConcreteStrategy:** Le classi concrete che incapsulano le singole logiche aziendali, ovvero \MaxCaricoStrategy\, \ProssimitaCAPStrategy\ e \BilanciamentoCaricoStrategy\. Ciascuna di esse implementa in modo differente il metodo dell'interfaccia.

*(Inserire qui il diagramma UML esportato da Visual Paradigm)*
