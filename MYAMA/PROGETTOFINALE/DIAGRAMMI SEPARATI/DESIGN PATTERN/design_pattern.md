# 7. DESIGN PATTERN

## 7.1. Introduzione e Metodologia di Selezione

Nel contesto dell'Ingegneria del Software, i **Design Pattern** (secondo la canonica classificazione della *Gang of Four* - GoF) rappresentano soluzioni consolidate, collaudate e riutilizzabili a problemi ricorrenti di progettazione orientata agli oggetti. L'obiettivo primario della loro introduzione non è meramente stilistico, bensì quello di garantire che il sistema software rispetti le proprietà cardine di manutenibilità, estendibilità, basso accoppiamento (*Low Coupling*) e alta coesione (*High Cohesion*), oltre ai principi fondamentali di progettazione **SOLID** (in particolare il principio *Open/Closed* e il *Single Responsibility Principle*).

### Metodologia di Analisi sul Class Diagram Refined
La selezione dei Design Pattern per la piattaforma **MyAma** è scaturita da un'attenta analisi critica del *Class Diagram Refined*. Anziché forzare a priori l'inserimento di strutture complesse non richieste dal dominio, il gruppo di lavoro ha esaminato le entità e i controller del modello per individuare reali punti critici (*hotspots*) e potenziali violazioni di design (quali catene condizionali rigide o accoppiamenti indebiti tra entità di dominio e moduli periferici).

La seguente tabella riassume la valutazione comparativa effettuata sui pattern candidati:

| # | Problema Architetturale nel Refined | Entità / Moduli Coinvolti | Design Pattern Candidato | Valutazione e Idoneità |
|---|---|---|---|---|
| **1** | **Politiche variabili di assegnazione e routing dei ritiri** | `RitiroDomicilio`, `Assegnazione`, `AutistaAMA`, `Veicolo` | **Strategy** | **Scelta Primaria (Ottimo)**: incapsula e rende intercambiabili le politiche logistiche di scheduling senza intaccare il controller. |
| **2** | **Reazione distribuita al cambio di stato della prenotazione** | `Prenotazione`, `Cittadino`, `AutistaAMA`, `SedeAMA` | **Observer** | **Scelta Primaria (Ottimo)**: disaccoppia il ciclo di vita della prenotazione da notifiche e dashboard dipendenti. |
| **3** | Condivisione dello scheletro del ciclo di vita tra Ritiro e Conferimento | `Prenotazione`, `RitiroDomicilio`, `ConferimentoSede` | Template Method | *Candidato Valido*: buona aderenza, ma meno incisivo rispetto a Strategy e Observer. |
| **4** | Creazione specializzata delle differenti tipologie di utente | `UserFactory`, `UtenteSistema`, ruoli derivati | Factory Method | *Possibile*: presente come concetto, ma richiederebbe un refactoring più invasivo della gerarchia. |
| **5** | Aggiunta dinamica di servizi opzionali | `Prenotazione`, servizi accessori | Decorator | *Non Idoneo*: il dominio di MyAma non prevede opzioni a cascata componibili a runtime. |
| **6** | Gestione ricorsiva di strutture composte e foglie | Sedi e Zone territoriali | Composite | *Non Idoneo*: le relazioni parte-tutto nel dominio sono composizioni semplici e non ricorsive. |
| **7** | Integrazione con interfacce legacy o incompatibili | Comunicazioni esterne | Adapter | *Non Idoneo*: non sono presenti API terze o sistemi preesistenti incompatibili da adattare. |
| **8** | Creazione di intere famiglie di prodotti correlati | Tipologie utente / servizi | Abstract Factory | *Non Idoneo*: assenza di famiglie alternative parallele di oggetti nel modello. |

In virtù dell'analisi effettuata, sono stati selezionati per l'integrazione nel sistema **MyAma** due pattern comportamentali complementari:
1. **Observer Pattern:** per risolvere la dipendenza uno-a-molti generata dagli eventi di transizione di stato delle prenotazioni.
2. **Strategy Pattern:** per incapsulare e rendere dinamicamente intercambiabili gli algoritmi di ottimizzazione e assegnazione dei carichi di lavoro.

---

## 7.2. Observer Pattern (Pattern Comportamentale)

### Descrizione del Problema e Criticità di Design
All'interno del dominio applicativo di MyAma, la classe `Prenotazione` rappresenta una delle entità centrali, la quale subisce continue transizioni di stato nel corso del suo ciclo di vita (es. passaggio da *In attesa* a *Confermata*, *In corso*, *Completata* o *Annullata*). Ad ogni cambio di stato, è indispensabile che diversi sottosistemi indipendenti vengano informati in tempo reale per eseguire compiti specifici:
* **Modulo Notifiche:** invio di comunicazioni telematiche (email, SMS, push) al cittadino per informarlo dell'accettazione o della variazione del servizio;
* **Dashboard Autista:** aggiornamento dell'itinerario e del carico pianificato per il turno corrente sul dispositivo mobile dell'autista;
* **Registro di Sede:** aggiornamento dei contatori di flusso, delle statistiche di transito e dei posti occupati nel centro di raccolta.

Qualora la classe `Prenotazione` dovesse istanziare e invocare direttamente i metodi delle classi concrete di ciascun ricevitore, si verrebbe a creare un accoppiamento rigido (*tight coupling*). Ciò comporterebbe una grave violazione del principio **Open/Closed**: l'eventuale aggiunta futura di un nuovo componente interessato allo stato della prenotazione (es. un modulo di tracciamento GPS o un sistema di telemetria) richiederebbe la modifica diretta e la ricompilazione della classe `Prenotazione`.

### Soluzione Progettuale e Vantaggi Architetturali
Per superare tale criticità è stato applicato il Design Pattern comportamentale **Observer**. Il pattern stabilisce una relazione di dipendenza uno-a-molti disaccoppiata: il soggetto (`Subject`), quando muta il proprio stato interno, invoca un metodo di notifica polimorfico broadcast verso tutti gli ascoltatori (`Observer`) registrati.
In questo modo, la classe `Prenotazione` mantiene unicamente una lista di puntatori all'interfaccia astratta degli osservatori, ignorando completamente i dettagli implementativi e l'identità concreta dei singoli destinatari.

### Partecipanti al Pattern
* **Subject (Observable):** La classe `Prenotazione`, che fornisce l'interfaccia per collegare (`attach`), scollegare (`detach`) e notificare (`notifyObservers`) gli oggetti ascoltatori.
* **Observer:** L'interfaccia `PrenotazioneObserver`, che dichiara l'operazione polimorfica di aggiornamento `update(prenotazione: Prenotazione)`.
* **ConcreteObserver:** Le classi concrete `EmailNotifier`, `DashboardAutistaNotifier` e `RegistroSedeObserver`, le quali implementano l'interfaccia definendo le rispettive azioni reattive all'evento.

![Diagramma UML Observer Pattern](figure/pattern_observer.jpg)

---

## 7.3. Strategy Pattern (Pattern Comportamentale)

### Descrizione del Problema e Criticità di Design
La gestione operativa dei ritiri a domicilio e la composizione dell'itinerario dei veicoli AMA sono processi complessi che dipendono da vincoli logistici, contingenze quotidiane e direttive aziendali. In particolare, il sistema deve poter supportare differenti algoritmi di assegnazione:
* **Politica di Massimizzazione del Carico:** mira a saturare la portata in peso e volume del veicolo prima del rientro in sede, minimizzando il numero complessivo di viaggi;
* **Politica di Prossimità Territoriale:** raggruppa le richieste limitrofe all'interno della medesima area CAP per minimizzare le distanze chilometriche e i tempi di percorrenza;
* **Politica di Bilanciamento del Carico di Lavoro:** distribuisce in modo equo il numero di ritiri e il carico complessivo tra tutti gli autisti in servizio nel turno.

Codificare la logica di tutti questi criteri all'interno di un'unica classe (`GestoreAssegnazione`) tramite costrutti condizionali annidati (`if-else` o `switch-case`) genererebbe una classe "God Object", fragile e con complessità ciclomatica elevata. Tale approccio violerebbe sia il **Single Responsibility Principle** che l'**Open/Closed Principle**, poiché l'integrazione di una nuova politica di routing imporrebbe la riscrittura e il re-test dell'intero controllore.

### Soluzione Progettuale e Vantaggi Architetturali
Al fine di conferire al sistema la massima flessibilità, è stato adottato il Design Pattern **Strategy**. Tale pattern consente di incapsulare ciascun algoritmo di ottimizzazione logistica all'interno di classi separate e intercambiabili a tempo di esecuzione, rendendo la logica di calcolo completamente indipendente dal contesto che la utilizza.
Il controllore `GestoreAssegnazione` mantiene un riferimento all'interfaccia astratta della strategia, potendo variare dinamicamente l'algoritmo impiegato (tramite iniezione delle dipendenze o configurazione a runtime) senza subire alcuna modifica strutturale.

### Partecipanti al Pattern
* **Context:** La classe `GestoreAssegnazione`, che mantiene il riferimento a un oggetto di tipo `AssegnazioneStrategy` ed espone il metodo `pianificaRitiri()` per coordinare l'esecuzione.
* **Strategy:** L'interfaccia `AssegnazioneStrategy`, che definisce la firma polimorfica del metodo di calcolo `calcolaAssegnazione(richieste: List, mezzi: List)`.
* **ConcreteStrategy:** Le classi concrete `MaxCaricoStrategy`, `ProssimitaCAPStrategy` e `BilanciamentoCaricoStrategy`, ciascuna contenente l'implementazione specialistica del corrispondente algoritmo logistico.

![Diagramma UML Strategy Pattern](figure/pattern_strategy.jpg)
