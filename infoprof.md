# 📌 Informazioni e Istruzioni del Docente sul Progetto - Ingegneria del Software

> **Corso di Laurea**: CdS in Informatica - Università degli Studi di Roma "Tor Vergata"  
> **Docente**: Prof. Andrea D'Ambrogio (`dambro@uniroma2.it`)  
> **Anno Accademico**: 2025/2026  
> **Fonti**: Istruzioni ufficiali per il task progettuale + Analisi sistematica delle 21 slide ufficiali (Parte I + Parte II) e dei materiali del corso.

---

## 🎯 PARTE 1: Istruzioni Ufficiali Dirette per il Task Progettuale

Il task progettuale da sviluppare e consegnare per poter prendere parte agli appelli di esame consiste nella realizzazione di **attività di definizione dei requisiti utente e relativa specifica**, in un dominio applicativo da identificare.

Il task va svolto in gruppo, ciascun gruppo costituito da un numero di studenti **non superiore a cinque**.

---

### 📝 Attività Richieste

1. **Problem Statement**:
   - Identificare uno specifico dominio applicativo nel quale procedere allo sviluppo di un prodotto software, descrivendone in modo sommario le caratteristiche.
2. **Definizione dei Requisiti Utente**:
   - A partire dal problem statement, procedere alla definizione dei requisiti utente, secondo quanto illustrato durante il corso.
3. **Verificabilità dei Requisiti Utente**:
   - Descrivere gli aspetti relativi alla verificabilità dei requisiti utente definiti al punto 2.
4. **Specifica Software (OOA - Object Oriented Analysis)**:
   - A partire dai requisiti utente produrre la specifica software, facendo uso del metodo di OOA illustrato durante il corso.
5. **Template Documento di Specifica**:
   - Per la stesura del documento di specifica fare uso di un apposito template, ad esempio quello proposto nello standard **IEEE 830-1998** illustrato durante il corso.
6. **Modellazione UML & Tooling**:
   - Per la specifica dei modelli UML usare il tool **Visual Paradigm**, scaricabile e installabile tramite licenza accademica:
     - 🔗 [Visual Paradigm Academic Partner (Tor Vergata)](https://ap.visual-paradigm.com/university-of-rome-2)
7. **Estensione con Design Pattern (Appendice)**:
   - Aggiungere al documento di specifica **un'appendice che descriva l'applicazione di almeno due design pattern**, scelti tra quelli illustrati a lezione, al class diagram ottenuto in fase di specifica (passaggio formale da *Class Diagram Unrefined* a *Class Diagram Refined*).

---

### 📬 Modalità e Tempistiche di Consegna

- **Cosa inviare**: Il documento risultante (relazione PDF di specifica completa) unitamente all'archivio compresso (`.zip`) contenente tutti i file sorgente di **Visual Paradigm** (`.vpp`).
- **A chi inviare**: All'indirizzo email del docente: `dambro@uniroma2.it`.
- **Scadenza**: L'invio dovrà essere effettuato **almeno 5 giorni prima dell'appello di esame**.
- **Regole d'esame**: Gli studenti facenti parte dello stesso gruppo potranno sostenere la prova orale in appelli differenti dello stesso anno accademico.

---

## 🔍 PARTE 2: Analisi Sistematica delle Slide & Aspettative Didattiche

Anche se nelle slide delle lezioni non vi è una sezione intitolata "progetto", le slide contengono l'intero impianto metodologico su cui il professore basa la valutazione. Di seguito la sintesi ragionata di tutti i punti chiave estratti dalle slide.

---

### 1. Fasi del Ciclo di Vita del Software
*(Fonte: `01-Introduzione`, slide 8)*

Il docente definisce il ciclo di vita del software in **3 stadi e 6 fasi**:

| Stadio | Fasi |
|---|---|
| **Sviluppo** | 1. Requisiti → 2. Specifiche (analisi dei requisiti) → 3. Pianificazione → 4. Progetto (preliminare + dettagliato) → 5. Codifica → 6. Integrazione |
| **Manutenzione** | Copre circa il 60% dei costi totali del ciclo di vita |
| **Dismissione** | Ritiro e fine vita del prodotto |

> **Implicazione didattica**: La relazione deve seguire fedelmente il passaggio logico: *Dominio → Requisiti Utente → Analisi OOA → Progettazione Dettagliata con Pattern*.

---

### 2. Definizione di "Prodotto Software"
*(Fonte: `01-Introduzione`, slide 15)*

$$\text{Prodotto Software} = \text{Codice} + \text{Documentazione}$$

Gli artefatti intermedi fondamentali sono:
- **Documento dei Requisiti**
- **Documento di Specifica (SRS)**
- **Documento di Progetto**

---

### 3. Modelli di Processo Software
*(Fonte: `02-Processo software parte1`, `02-Processo software parte2`)*

Modelli presentati a lezione:
- **Waterfall** (a cascata)
- **Modello a V**
- **Incrementale / Iterativo**
- **Modello a Spirale** (guidata dall'analisi dei rischi)
- **Evolutionary / Prototipazione**
- **SCRUM / Agile**
- **Microsoft Synch-and-Stabilize** (enfasi su milestone 3-4, specifica funzionale evolutiva, frequenti build intermedie).

---

### 4. Requirements Engineering - Classificazione e Standard
*(Fonte: `03-Requisiti software`, `04-Req Engineering`)*

Distinzione rigorosa dei requisiti:
- **Funzionali**: Cosa il sistema deve fare (servizi offerti, reazioni a determinati input, comportamenti attesi).
- **Non Funzionali**: Vincoli di qualità e prestazione (affidabilità, tempi di risposta, usabilità, sicurezza, portabilità).
- **Di Dominio**: Vincoli derivanti dal settore applicativo specifico (es. normative legali, standard industriali).

**Processo di Requirements Engineering**:
1. *Feasibility study* (Studio di fattibilità)
2. *Requirements analysis and elicitation* (Elicitazione basata su Use Case e interviste)
3. *Requirements specification* (Stesura dell'**SRS** conforme a IEEE 830-1998)
4. *Requirements validation & verification* (Verificabilità dei requisiti tramite criteri di accettazione e testabilità)

---

### 5. Object-Oriented Analysis (OOA) & Diagrammi UML
*(Fonte: `05a-OOA` - 96 slide, `05b-OOA_esercizio`)*

Diagrammi UML centrali per l'OOA:
1. **Use Case Diagram**: Modellazione degli attori e dei requisiti funzionali con relazioni (`<<include>>`, `<<extend>>`, generalizzazione) e schede descrittive per ciascun caso d'uso.
2. **Class Diagram (Unrefined)**: Modello concettuale statico del dominio (classi, attributi essenziali, associazioni, molteplicità, aggregazioni/composizioni ed ereditarietà).
3. **Sequence Diagram**: Modellazione delle interazioni temporali e scambio di messaggi tra oggetti per i principali scenari d'uso.
4. **Activity Diagram**: Flussi di controllo e attività operative complesse.
5. **Statechart Diagram (Macchine a Stati)**: Stati del ciclo di vita per entità che presentano transizioni significative.

#### Convenzioni di Naming richieste (slide 35 di OOA):
- Associare ad ogni classe un **nome significativo** nello specifico dominio applicativo.
- Adottare una **convenzione standard** coerente (es. PascalCase per le classi, camelCase per attributi e metodi).
- Lunghezza massima consigliata per i nomi: **non superiore a 30 caratteri**.

---

### 6. Pianificazione del Progetto (SPMP) & Stima Costi
*(Fonte: `07-Pianificazione`)*

- Standard **IEEE Std. 1058-1998** (Standard for Software Project Management Plans) e modello NASA-SEL-84-101.
- **Stima COCOMO** (Constructive Cost Model):
  $$\text{Effort} = a \times (\text{KLOC})^b \times C \quad [\text{uomini/mese}]$$
  $$\text{Duration} = c \times (\text{Effort})^d \quad [\text{mesi}]$$
- Modelli di organizzazione dei team: approccio democratico vs capo-programmatore; distinzione tra *Team Leader* (tecnico) e *Team Manager* (gestionale).

---

### 7. Principi Fondamentali di Progettazione (OOD)
*(Fonte: `08-Progetto`, `09-OOD`)*

Principi cardine:
1. **Stepwise Refinement** (raffinamento progressivo)
2. **Information Hiding** (incapsulamento e occultamento dell'informazione)
3. **Massima Coesione**: preferire coesione *funzionale* e *informativa*; evitare coesione *coincidente* o *logica*.
4. **Minimo Accoppiamento (Coupling)**: preferire accoppiamento *sui dati* (data coupling); evitare *content* o *common coupling*.

---

### 8. Architetture Software & Case Study di Riferimento
*(Fonte: `09-OOD`, `09a-SOA_casestudy`)*

- Pattern architetturali: **Layered (a livelli)**, **Client-Server**, **SOA (Service-Oriented Architecture)**.
- Diagrammi di implementazione: **Component Diagram** e **Deployment Diagram**.
- Il case study `09a-SOA_casestudy` (*Web-based Online Shopping System*) rappresenta il modello di riferimento del docente per la transizione tra Use Case, Activity, Sequence, Class e Component Diagrams.

---

### 9. Catalogo dei Design Pattern Richiesti
*(Fonte: `10-Design patterns`, `11-Design Patterns - Esempi`)*

Per l'appendice è obbligatorio applicare **almeno 2 design pattern**, scelti tra:
- **Creazionali**: Factory Method, Abstract Factory, Singleton, Builder, Prototype.
- **Strutturali**: Adapter, Bridge, Composite, Decorator, Facade, Proxy.
- **Comportamentali**: Observer, Strategy, State, Command, Template Method, Iterator.

---

### 10. Metriche di Qualità & Testing
*(Fonte: `12-Metriche di struttura`, `13-Qualità del Software`, `14-Testing`)*

- **Metriche OO di Chidamber & Kemerer**: CBO (Coupling Between Objects), DIT (Depth of Inheritance Tree), NOC (Number of Children), WMC (Weighted Methods per Class), LCOM (Lack of Cohesion in Methods), RFC (Response For a Class).
- **Complessità Ciclomatica di McCabe**: $V(G) = E - N + 2P$.
- **Standard ISO/IEC 25010** (SQuaRE): Funzionalità, Affidabilità, Usabilità, Efficienza, Manutenibilità, Portabilità.
- **Testing**: Tecniche Black-box (Equivalence Partitioning, Boundary Value Analysis) e White-box (Statement, Branch, Basis Path Testing).

---

## 📝 PARTE 3: Checklist Operativa per la Relazione del Progetto

### Documento di Specifica (PDF)
- [ ] **Frontespizio**: Titolo del progetto, componenti del gruppo con matricola, anno accademico e corso di laurea.
- [ ] **Capitolo 1 - Introduzione e Problem Statement**: Descrizione del dominio applicativo, contesto e obiettivi del sistema.
- [ ] **Capitolo 2 - Glossario**: Tabella con la definizione univoca di tutti i termini di dominio per evitare ambiguità.
- [ ] **Capitolo 3 - Definizione dei Requisiti Utente**: Elenco strutturato di Requisiti Funzionali, Non Funzionali e di Dominio.
- [ ] **Capitolo 4 - Verificabilità dei Requisiti**: Metriche, criteri di accettazione e metodi di collaudo per ciascun requisito.
- [ ] **Capitolo 5 - Specifica Software (OOA)**:
  - [ ] Use Case Diagrams complessivi e suddivisi per attore.
  - [ ] Schede dettagliate dei casi d'uso (Attori, Precondizioni, Flusso Principale, Flussi Alternativi, Postcondizioni).
  - [ ] Sequence Diagrams per i casi d'uso più rilevanti.
  - [ ] Class Diagram iniziale (**Unrefined Class Diagram**).
  - [ ] Eventuali Statechart / Activity Diagrams per logiche complesse.
- [ ] **Appendice - Progettazione con Design Pattern**:
  - [ ] Descrizione motivata della scelta di almeno due pattern (es. Factory Method, Singleton, Strategy, Observer, State).
  - [ ] **Refined Class Diagram** aggiornato con le classi del pattern, metodi, visibilità e tipi.
  - [ ] Sequence Diagram di dettaglio che mostra l'interazione degli oggetti tramite il pattern.

### Consegna & File Sorgente
- [ ] Archivio compresso contenente tutti i progetti **Visual Paradigm** (`.vpp`).
- [ ] File PDF finale denominato secondo la convenzione del gruppo (es. `Progetto_Cognome1_Cognome2.pdf`).
- [ ] Invio via email a `dambro@uniroma2.it` almeno **5 giorni lavorativi prima dell'appello**.

---

## 📊 PARTE 4: Mappatura delle 21 Slide Ufficiali Analizzate

| Slide | Titolo / Argomento | Pagine | Rilevanza per il Progetto |
|---|---|---|---|
| `01-Introduzione` | Introduzione e ciclo di vita | 39 | Definizione prodotto SW, fasi del ciclo di vita |
| `02-Processo software p1` | Modelli di processo tradizionali | 60 | Waterfall, V, Spirale, Synch-and-Stabilize |
| `02-Processo software p2` | Modelli agili e SCRUM | 19 | Principi agili e gestione iterativa |
| `03-Requisiti software` | Requisiti funzionali e non funzionali | 25 | Classificazione e definizione requisiti |
| `04-Req Engineering` | Processo di Requirements Engineering | 38 | Elicitazione, specifica SRS, validazione |
| `05-Richiami OOP` | Concetti cardine object-oriented | 15 | Ereditarietà, polimorfismo, incapsulamento |
| `05a-OOA` | Object Oriented Analysis & UML | 96 | Use Case, Class, Sequence, State, Activity |
| `05b-OOA_esercizio` | Esercitazione pratica OOA | 10 | Esempio applicativo di modellazione |
| `07-Pianificazione` | SPMP, COCOMO, Organizzazione | 45 | Standard IEEE 1058, stima effort e tempi |
| `08-Progetto` | Principi di progettazione software | 35 | Coesione, accoppiamento, information hiding |
| `09-OOD` | Object Oriented Design | 124 | Transizione OOA → OOD, Component/Deployment |
| `09a-SOA_casestudy` | Case Study Online Shopping | 41 | Esempio completo end-to-end |
| `10-Design patterns` | Catalogo Design Pattern GoF | 94 | Pattern Creazionali, Strutturali, Comportamentali |
| `11-Design Patterns - Esempi` | Applicazioni pratiche dei Pattern | 74 | Esempi di implementazione e diagrammi UML |
| `12-Metriche di struttura` | Metriche Object-Oriented | 49 | Chidamber & Kemerer, complessità ciclomatica |
| `13-Qualità del Software` | Standard di qualità | 29 | Modello ISO/IEC 25010 (SQuaRE) |
| `14-Testing` | Tecniche di test funzionale e strutturale | 84 | Black-box, White-box, Basis Path |
| `15-BPM` | Business Process Management | 45 | Gestione e modellazione dei processi |
| `16-BPMN` | Notazione BPMN standard | 50 | Diagrammi dei processi aziendali |
| `17-M&S Intro` | Modellazione e simulazione | 99 | Principi di simulazione a eventi discreti |
| `18-BP simulation` | Simulazione di processi aziendali | 89 | Analisi quantitativa dei processi |
| **TOTALE** | | **1210** | |
