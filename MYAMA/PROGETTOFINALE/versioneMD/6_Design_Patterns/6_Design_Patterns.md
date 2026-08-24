# 6. Design Patterns (Pattern di Progettazione)


% =========================================================================
% 6.1 INTRODUZIONE E METODOLOGIA
% =========================================================================
## Introduzione e Metodologia di Selezione

Si vogliono ora introdurre i Design Pattern 

### Analisi Critica del Class Diagram Refined

La selezione dei Design Pattern per la piattaforma **MyAma** è scaturita da un'attenta analisi critica del *Class Diagram Refined*. Anziché forzare a priori l'inserimento di strutture complesse non richieste dal dominio, il gruppo di lavoro ha esaminato le entità e i controller del modello per individuare reali punti critici (*hotspots*) e potenziali violazioni di design (quali catene condizionali rigide o accoppiamenti indebiti tra entità di dominio e moduli periferici).

La la tabella seguente riassume la valutazione comparativa effettuata sui pattern candidati della letteratura GoF.



| # | Problema nel Refined | Entità Coinvolte | Pattern | Valutazione e Idoneità |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Politiche variabili di assegnazione e routing dei ritiri** | RitiroDomicilio, Assegnazione, AutistaAMA, Veicolo | **Strategy** | **Scelta Primaria (Ottimo)**: incapsula e rende intercambiabili le politiche logistiche di scheduling senza intaccare il controller. |
| **2** | **Reazione distribuita al cambio di stato della prenotazione** | Prenotazione, Cittadino, AutistaAMA, SedeAMA | **Observer** | **Scelta Primaria (Ottimo)**: disaccoppia il ciclo di vita della prenotazione da notifiche e dashboard dipendenti. |
| **3** | Condivisione dello scheletro del ciclo di vita tra Ritiro e Conferimento | Prenotazione, RitiroDomicilio, ConferimentoSede | Template Method | *Candidato Valido*: buona aderenza, ma meno incisivo rispetto a Strategy e Observer. |
| **4** | Creazione specializzata delle differenti tipologie di utente | UserFactory, UtenteSistema, ruoli derivati | Factory Method | *Possibile*: presente come concetto, ma richiederebbe un refactoring più invasivo della gerarchia. |
| **5** | Aggiunta dinamica di servizi opzionali | Prenotazione, servizi accessori | Decorator | *Non Idoneo*: il dominio di MyAma non prevede opzioni a cascata componibili a runtime. |
| **6** | Gestione ricorsiva di strutture composte e foglie | Sedi e Zone territoriali | Composite | *Non Idoneo*: le relazioni parte-tutto nel dominio sono composizioni semplici e non ricorsive. |
| **7** | Integrazione con interfacce legacy o incompatibili | Comunicazioni esterne | Adapter | *Non Idoneo*: non sono presenti API terze o sistemi preesistenti incompatibili da adattare. |
| **8** | Creazione di intere famiglie di prodotti correlati | Tipologie utente / servizi | Abstract Factory | *Non Idoneo*: assenza di famiglie alternative parallele di oggetti nel modello. |

In virtù dell'analisi effettuata, sono stati selezionati per l'integrazione nel sistema **MyAma** due pattern comportamentali complementari:

    * **Observer Pattern:** per risolvere la dipendenza uno-a-molti generata dagli eventi di transizione di stato delle prenotazioni.
    * **Strategy Pattern:** per incapsulare e rendere dinamicamente intercambiabili gli algoritmi di ottimizzazione e assegnazione dei carichi di lavoro.


% =========================================================================
% 6.2 OBSERVER PATTERN
% =========================================================================
## Observer Pattern (Pattern Comportamentale)


### Descrizione del Problema e Criticità di Design

All'interno del dominio applicativo di MyAma, la classe `Prenotazione` rappresenta una delle entità centrali, la quale subisce continui cambiamenti di stato nel corso del suo ciclo di vita (es. passaggio da *In attesa* a *Confermata*, *In corso*, *Completata* o *Annullata*). Ad ogni transizione di stato, è fondamentale che diversi sottosistemi indipendenti vengano informati per reagire di conseguenza:

    * **Modulo Notifiche (`NotificaCittadino**):` invio di comunicazioni telematiche (email, SMS, notifiche in-app) al cittadino per informarlo dell'accettazione o della variazione del servizio;
    * **Dashboard Autista (`AggiornamentoAutista**):` aggiornamento dell'itinerario e del carico pianificato per il turno corrente sul dispositivo mobile dell'autista;
    * **Registro di Sede (`AggiornamentoSede**):` aggiornamento dei contatori di flusso, delle statistiche di transito e dei posti occupati nel centro di raccolta.


Qualora la classe `Prenotazione` dovesse istanziare e invocare direttamente i metodi delle classi concrete di questi sottosistemi, si creerebbe un forte accoppiamento (*tight coupling*). Questo violerebbe pesantemente il principio *Open/Closed*: ogni volta che si volesse aggiungere un nuovo modulo interessato ai cambiamenti della prenotazione (es. un modulo di tracciamento o un sistema di telemetria), si renderebbe necessaria una modifica al codice sorgente della classe `Prenotazione` stessa.

### Soluzione Progettuale e Vantaggi Architetturali

Per risolvere tale criticità è stato applicato il Design Pattern comportamentale **Observer**. Tale pattern consente di definire una dipendenza uno-a-molti tra gli oggetti, facendo in modo che quando l'oggetto osservato (*Subject*) cambia stato, tutti gli oggetti dipendenti (*Observers*) vengano notificati e si aggiornino automaticamente.
In questo modo, la classe `Prenotazione` si limita a mantenere una lista di riferimenti all'interfaccia astratta `ObserverPrenotazione` e si occupa esclusivamente di lanciare una notifica generica di aggiornamento, senza conoscere la logica implementativa o la natura dei ricevitori.

### Partecipanti


    * **Subject (Observable):** la classe `Prenotazione`. Contiene i metodi per registrare (`registraObserver(obs)`), rimuovere (`rimuoviObserver(obs)`) e notificare (`notificaObserver()`) gli ascoltatori, oltre alla gestione del proprio stato interno (`StatoPrenotazione`).
    * **Observer:** l'interfaccia `ObserverPrenotazione` che espone il metodo polimorfico `update(stato: StatoPrenotazione)`.
    * **ConcreteObserver:** le classi concrete che implementano l'interfaccia, ovvero `NotificaCittadino`, `AggiornamentoAutista` e `AggiornamentoSede`. Ciascuna di esse implementa la propria logica specifica all'interno del metodo `update`.


\begin{figure}[H]
    \centering
    \includegraphics[width=0.95\textwidth]{figure/pattern_observer.jpg}
    \caption{Struttura UML del Design Pattern Observer applicato a MyAma}
    \label{fig:pattern_observer}
\end{figure}

% =========================================================================
% 6.3 STRATEGY PATTERN
% =========================================================================
## Strategy Pattern (Pattern Comportamentale)


### Descrizione del Problema e Criticità di Design

La gestione operativa dei ritiri a domicilio e la composizione dell'itinerario dei veicoli AMA sono processi complessi che variano a seconda delle condizioni quotidiane, delle politiche aziendali e delle disponibilità di mezzi e personale. In particolare, il sistema supporta differenti algoritmi di assegnazione:

    * **Politica di Massimizzazione del Carico (`AssegnazionePerCapacita**):` algoritmo mirato a ottimizzare il riempimento (in volume e peso) dei mezzi prima del loro rientro in sede, minimizzando il numero complessivo di corse;
    * **Politica di Prossimità Territoriale (`AssegnazionePerZona**):` algoritmo mirato a minimizzare i tempi e i chilometri percorsi, raggruppando i ritiri per aree limitrofe (stesso CAP).


Inserire la logica di tutti questi algoritmi direttamente all'interno del controllore di assegnazione, impiegando complesse e lunghe catene condizionali (`if-else` o `switch-case`), porterebbe alla creazione di una "God Class" difficilmente manutenibile (violazione del *Single Responsibility Principle*). Inoltre, l'aggiunta di una futura nuova politica di smistamento richiederebbe la modifica di codice già testato e consolidato.

### Soluzione Progettuale e Vantaggi Architetturali

Al fine di garantire flessibilità e manutenibilità, si è optato per l'applicazione dello **Strategy Pattern**. Questo pattern permette di incapsulare una famiglia di algoritmi all'interno di classi separate e intercambiabili a tempo di esecuzione, rendendo l'algoritmo indipendente dal client che ne fa uso.
Il controller dedicato alla pianificazione interagirà unicamente con un'interfaccia comune, delegando a runtime il calcolo dell'itinerario all'algoritmo (strategia) attualmente selezionato dall'amministratore di sede o dal sistema.

### Partecipanti


    * **Context:** la classe di controllo (`GestoreAssegnazione` / `PrenotazioneControl`). Essa mantiene un riferimento all'interfaccia `StrategiaAssegnazione` ed espone le operazioni per coordinare l'allocazione delle risorse delegando alla strategia attiva.
    * **Strategy:** l'interfaccia `StrategiaAssegnazione` che dichiara il metodo astratto polimorfico `assegna(ritiro: RitiroDomicilio): Assegnazione`.
    * **ConcreteStrategy:** le classi concrete che incapsulano le singole logiche aziendali, ovvero `AssegnazionePerCapacita` e `AssegnazionePerZona`. Ciascuna di esse implementa in modo differente il metodo dell'interfaccia.


\begin{figure}[H]
    \centering
    \includegraphics[width=0.95\textwidth]{figure/pattern_strategy.jpg}
    \caption{Struttura UML del Design Pattern Strategy per l'allocazione delle risorse}
    \label{fig:pattern_strategy}
\end{figure}


