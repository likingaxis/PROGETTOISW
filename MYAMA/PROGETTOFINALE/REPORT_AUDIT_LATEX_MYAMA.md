# Audit del progetto LaTeX e del PDF MyAma

**Repository analizzato:** `likingaxis/PROGETTOISW`  
**Commit analizzato:** `435ccdca0c01503b3bad41e3d500a023314e6aa0` del 24 agosto 2026  
**Area prioritaria:** `MYAMA/PROGETTOFINALE/Latex PDF/`  
**PDF verificato:** `main.pdf`, 81 pagine, generato il 24 agosto 2026 alle 15:03  
**Modalità:** solo audit; nessun sorgente del progetto è stato corretto.

## Valutazione sintetica

Il documento segue l'ordine usato con regolarità nei progetti Buongiorno, Hotel, Pesca, RistorApp e SteamPlatform: Introduzione, Glossario, User Requirements, System Requirements, modelli OOA e Design Pattern. La struttura generale è quindi riconoscibile e adeguata al corso.

Prima della consegna, tuttavia, vanno risolti alcuni problemi sostanziali:

1. il PDF non corrisponde più ai sorgenti LaTeX presenti nel repository;
2. alcuni servizi dichiarati nell'introduzione non sono tracciati nei casi d'uso e nei requisiti;
3. manca completamente la copertura dei requisiti dell'Amministratore generale AMA;
4. il ruolo Autista AMA è escluso per errore dal flusso di registrazione tramite invito;
5. testo e diagrammi dei due Design Pattern usano classi e metodi differenti;
6. il Class Diagram Refined è praticamente illeggibile nel PDF;
7. vari Activity e Sequence Diagram risultano ancora assenti rispetto ai casi d'uso documentati;
8. la sezione dei requisiti non fornisce criteri di verifica realmente completi per gran parte dei requisiti.

Nel PDF attuale **non sono state trovate pagine completamente bianche** e **non risultano fotografie o immagini estranee al progetto**. Sono però presenti pagine con molto spazio inutilizzato e diagrammi troppo piccoli o tagliati.

---

# 1. Correzioni bloccanti prima della consegna

## P0-01 — Il PDF è obsoleto rispetto ai sorgenti

**Posizione:**

- `Latex PDF/main.pdf`;
- `Latex PDF/sezioni/05_modelli_ooa.tex`, righe 113-129.

**Problema:** il PDF è stato generato alle 15:03, mentre il commit dei sorgenti è successivo. Nel `.tex` sono ora inclusi:

- Gestire disponibilità dei veicoli;
- Rimuovere lavoratori dalla sede;
- Rimuovere amministratore di sede.

Questi tre diagrammi non compaiono nel PDF attuale: l'elenco delle figure si ferma, per gli Activity Diagram, a «Generare codice amministratore di sede».

**Correzione richiesta:** ricompilare il documento dopo avere completato tutte le altre correzioni, eseguire almeno due passate e verificare nuovamente indice, elenco figure, elenco tabelle, numerazione e pagine finali.

## P0-02 — Registrazione tramite invito: manca il ruolo Autista AMA

**Posizioni:**

- `sezioni/03_user_requirements.tex`, righe 45-69, in particolare riga 53;
- `sezioni/04_system_requirements.tex`, riga 24;
- diagrammi di registrazione tramite invito;
- glossario e regole sui codici invito.

**Problema:** il documento afferma che il codice assegna il ruolo di «operatore di sede AMA o amministratore di sede AMA». Anche RF-02 parla solo di «Amministratore o Operatore». L'Autista AMA, però, è un utente del sistema e non esiste un'altra procedura con cui possa registrarsi.

**Correzione richiesta:** definire esplicitamente la gerarchia dei codici:

- Amministratore di sede AMA: può generare codici per Autista AMA e Operatore di sede AMA;
- Amministratore generale AMA: può generare codici per Amministratore di sede AMA;
- nessun ruolo può generare codici per ruoli gerarchicamente superiori.

Aggiornare coerentemente Use Case, RF-02, diagrammi, Activity, Sequence e classi legate a `CodiceInvito`.

## P0-03 — Definizione contraddittoria di «Utente di sistema»

**Posizioni:**

- `sezioni/02_glossario.tex`, riga 24;
- `sezioni/03_user_requirements.tex`, righe 92-113;
- Use Case Diagram dell'utente non registrato.

**Problema:** il glossario definisce l'Utente di sistema come un utente già autenticato. Lo stesso attore esegue però il caso d'uso «Effettuare accesso», quindi prima dell'autenticazione.

**Correzione richiesta:** scegliere una sola semantica. La soluzione più chiara è usare:

- **Utente registrato**: possiede un account e può effettuare l'accesso;
- **Utente autenticato / Utente di sistema**: ha completato l'accesso e accede alle funzionalità del proprio ruolo.

Aggiornare attori, generalizzazioni e precondizioni.

## P0-04 — Funzionalità dichiarate ma non specificate

**Posizioni principali:**

- `sezioni/01_introduzione.tex`, riga 9: consultazione di informazioni, sedi e tariffe da parte del visitatore;
- `sezioni/01_introduzione.tex`, righe 11 e 19: notifiche, report e statistiche;
- `sezioni/02_glossario.tex`: definizioni di Notifica e Report/Statistiche;
- capitoli 3 e 4.

**Problema:** queste funzionalità appartengono allo scope dichiarato, ma non hanno una catena completa Use Case → requisito → modelli OOA:

- Visualizzare informazioni pubbliche, tariffe e sedi;
- ricevere notifiche;
- consultare report e statistiche aggregate da parte dell'Amministratore generale.

**Correzione richiesta:** per ciascuna funzionalità decidere se è IN o OUT scope. Se resta nello scope, aggiungere Use Case, requisito funzionale, criterio di verifica e modelli necessari. Se è fuori scope, rimuoverla dall'introduzione e dalle descrizioni dei ruoli. Non lasciarla soltanto come promessa narrativa.

## P0-05 — Requisiti funzionali incompleti e Amministratore generale assente

**Posizione:** `sezioni/04_system_requirements.tex`, righe 22-46.

**Problema:** sono presenti 29 schede Use Case ma solo 13 requisiti funzionali molto aggregati. Nessun requisito è assegnato all'Amministratore generale AMA. Mancano o non sono distinguibili, tra gli altri:

- visualizzazione di sedi compatibili;
- visualizzazione di date e fasce disponibili;
- prenotazioni attive e storico;
- valutazione del servizio;
- consultazione dettagli e chiamate;
- gestione delle associazioni sede-zone/CAP;
- generazione del codice per amministratore di sede;
- rimozione dell'amministratore di sede;
- eventuali report/statistiche.

**Correzione richiesta:** creare una matrice di tracciabilità almeno con colonne `UC`, `RF`, `Activity`, `Sequence`, `Classi coinvolte`, `Test/Criterio`. Ogni Use Case deve essere coperto da almeno un RF oppure essere dichiarato esplicitamente parte di un RF aggregato, senza ambiguità.

## P0-06 — «Rimuovere personale» ha tre significati differenti

**Posizioni:**

- `sezioni/03_user_requirements.tex`, righe 598-623: viene rimossa soltanto l'associazione tra persona e sede;
- `sezioni/04_system_requirements.tex`, riga 46: viene rimosso l'account dal sistema;
- `sezioni/05_modelli_ooa.tex`, righe 119-123: didascalia «Rimuovere lavoratori dalla sede».

**Problema:** disassociare un lavoratore da una sede, revocargli il ruolo e cancellarne l'account sono operazioni diverse, con effetti e autorizzazioni diverse.

**Correzione richiesta:** scegliere l'operazione effettiva. Per l'Amministratore di sede è più coerente la disassociazione o disabilitazione presso la propria sede, non la cancellazione globale dell'account. Usare poi lo stesso nome e la stessa postcondizione in UC, RF, Activity, Sequence e Class Diagram.

## P0-07 — Observer: testo e diagramma descrivono modelli differenti

**Posizioni:**

- `sezioni/06_design_patterns.tex`, righe 69-79;
- `figure/pattern_observer.jpg`;
- glossario, riga 98.

**Nel testo:**

- `PrenotazioneObserver`;
- `EmailNotifier`;
- `DashboardAutistaNotifier`;
- `RegistroSedeObserver`;
- `update(prenotazione: Prenotazione)`.

**Nel diagramma:**

- `ObserverPrenotazione`;
- `NotificaCittadino`;
- `AggiornamentoAutista`;
- `AggiornamentoSede`;
- `update(stato: StatoPrenotazione)`.

**Correzione richiesta:** scegliere il modello definitivo e uniformare esattamente nomi, firme, tipi, attributi e partecipanti tra testo, diagramma del pattern, glossario e Refined Class Diagram.

## P0-08 — Strategy: testo e diagramma descrivono modelli differenti

**Posizioni:**

- `sezioni/06_design_patterns.tex`, righe 88-112;
- `figure/pattern_strategy.jpg`;
- glossario, riga 100.

**Nel testo:**

- `AssegnazioneStrategy`;
- `MaxCaricoStrategy`;
- `ProssimitaCAPStrategy`;
- `BilanciamentoCaricoStrategy`;
- `calcolaAssegnazione(richieste: List, mezzi: List)`.

**Nel diagramma:**

- `StrategiaAssegnazione`;
- `AssegnazionePerCapacita`;
- `AssegnazionePerZona`;
- nessuna strategia di bilanciamento;
- `assegna(ritiro: RitiroDomicilio): Assegnazione`.

**Correzione richiesta:** uniformare il modello. Se le strategie sono tre, devono comparire tutte e tre. Se sono due, eliminare dal testo la terza. La firma dell'interfaccia deve essere identica ovunque.

## P0-09 — I pattern non risultano integrati nel Class Diagram Refined principale

**Posizioni:**

- `figure/class_CLASS_DIAGRAM_refined.jpg`;
- `CLASS DIAGRAM/CLASS DIAGRAM REFINED/Class Refined.vpp`;
- capitolo 6 e `DESIGN PATTERN/Design Pattern.vpp`.

**Problema:** le classi specifiche di Observer e Strategy compaiono nei diagrammi separati del capitolo 6, ma non risultano nel modello Refined consolidato. Il docente chiede l'applicazione di almeno due pattern al Class Diagram ottenuto in fase di specifica.

**Correzione richiesta:** mostrare chiaramente l'evoluzione:

1. Refined precedente all'applicazione;
2. criticità individuate;
3. pattern applicati;
4. **Refined finale consolidato**, contenente le classi e le relazioni dei pattern.

In alternativa, dichiarare inequivocabilmente che i due diagrammi del capitolo 6 sono viste parziali del Refined finale e fornire comunque una vista finale completa.

## P0-10 — Class Diagram Refined illeggibile nel PDF

**Posizione PDF:** pagina numerata 71, pagina fisica 76.  
**Sorgente:** `sezioni/05_modelli_ooa.tex`, righe 303-310.

**Problema:** il diagramma ha proporzioni molto orizzontali ed è ridotto alla larghezza della pagina verticale. Occupa soltanto una fascia nella parte alta; nomi, attributi, metodi, molteplicità e relazioni non sono leggibili in stampa o a zoom normale.

**Correzione richiesta:** esportare in PDF/SVG vettoriale e inserirlo in pagina A4 orizzontale con `pdflscape`/`landscape`, oppure suddividerlo in più viste coerenti e aggiungere una tavola complessiva. Verificare la leggibilità al 100% e su stampa A4.

---

# 2. Diagrammi mancanti o non coperti

## P1-01 — Activity Diagram ancora assenti dal LaTeX

Le tre figure segnalate da Claude sono state inserite nel `.tex`, ma risultano ancora assenti almeno otto flussi per cui esistono già immagini nel progetto o una scheda Use Case esplicita:

| Flusso | Artefatto già presente fuori da `Latex PDF/figure` |
|---|---|
| Visualizzare sedi compatibili | `ACTIVITY DIAGRAM/FOTO ACTIVITY DIAGRAM DAVIDE/ActivityDiagramVisualizzareSediCompatibili.jpg` |
| Visualizzare date e fasce orarie disponibili | `.../ActivityDiagramVIsualizzareDataOraDisponibili.jpg` |
| Visualizzare storico prenotazioni | `.../ActivityDiagramVisualizzareStoricoPrenotazioni.jpg` |
| Chiamare Autista AMA | `.../ActivityDiagramChiamareAutista.jpg` |
| Visualizzare ritiri assegnati / Consultare dettagli | `ACTIVITY DIAGRAM/FOTO ACTIVITY DIAGRAM LUCA/Visualizzare ritiri assegnati _ Consultare dettagli del ritiro  .jpg` |
| Chiamare cittadino | `.../Chiamare cittadino.jpg` |
| Visualizzare prenotazioni della sede / Consultare dettagli | `.../Visualizzare prenotazioni della sede _ Consultare dettagli  .jpg` |
| Gestire associazioni tra sede e zone/CAP | `ACTIVITY DIAGRAM/FOTO ACTIVITY DIAGRAM ALFREDO/Gestire associazioni tra sede e zone cap.png` |

**Correzione richiesta:** includerli oppure motivare esplicitamente perché alcuni casi semplici sono assorbiti in un diagramma più ampio. La copertura deve essere dichiarata, non dedotta dal lettore.

## P1-02 — Sequence Diagram assenti

**Confronto tra schede Use Case, `LISTA SEQUENCE DIAGRAM.md` e capitolo 5:**

- Visualizzare sedi compatibili: non realizzato;
- Visualizzare date e fasce orarie disponibili: non realizzato;
- Chiamare Autista AMA: presente come Use Case ma privo di Sequence Diagram.

**Correzione richiesta:** realizzare i diagrammi o ricondurre formalmente i primi due al Sequence di «Prenotare conferimento». Per «Chiamare Autista AMA» decidere se il vero servizio software sia «Visualizzare recapito/Avviare chiamata»: se la telefonata è esterna a MyAma, il Sequence deve terminare al passaggio verso l'app Telefono.

## P1-03 — Diagramma Use Case del cittadino tagliato

**Posizione PDF:** pagina numerata 9, pagina fisica 14.  
**File:** `figure/uc_cittadino.jpg`.

**Problema:** sul bordo destro sono tagliate le relazioni `<<include>>` provenienti da «Prenotare conferimento» verso «Visualizzare sedi compatibili» e «Visualizzare date e fasce orarie disponibili». Una parte delle frecce e delle etichette esce dall'immagine.

**Correzione richiesta:** riesportare il diagramma con margini completi e verificare che nessun elemento tocchi il canvas. Preferire un formato vettoriale.

## P1-04 — Mancanza del confine del sistema nei Use Case Diagram

**Posizione:** tutte le sei immagini `uc_*.jpg`.

**Problema:** gli attori e i casi d'uso non sono racchiusi in un rettangolo di sistema denominato `MyAma`. Il confine non è sempre obbligatorio per la sintassi minima UML, ma qui è fortemente consigliato perché chiarisce cosa appartiene al software e cosa resta esterno, soprattutto per chiamate telefoniche, privacy e attori specializzati.

**Correzione richiesta:** aggiungere il system boundary e lasciare tutti gli attori all'esterno.

## P1-05 — Generalizzazione tra Amministratore generale e Amministratore di sede da verificare

**File:** `figure/uc_amministratore_generale.jpg`.

**Problema:** la freccia di generalizzazione rende l'Amministratore generale una specializzazione dell'Amministratore di sede; in UML ciò implica che erediti tutti i casi d'uso dell'amministratore di sede. Se l'amministratore generale non deve gestire lavoratori, veicoli e fasce di ogni sede, la relazione è semanticamente errata.

**Correzione richiesta:** mantenere la generalizzazione solo se l'ereditarietà completa dei privilegi è una regola voluta e documentata. Altrimenti collegare entrambi a un attore astratto comune, per esempio `Utente di sistema`, senza generalizzazione reciproca.

---

# 3. Requisiti e verificabilità

## P1-06 — La colonna «Descrizione / Criterio di verifica» non contiene veri criteri

**Posizione:** `sezioni/04_system_requirements.tex`, tabella RF, righe 13-47.

**Problema:** le celle ripetono in forma discorsiva ciò che il sistema deve fare, ma quasi mai specificano precondizioni di test, input, risultato atteso e regola di superamento. Il requisito del docente sulla verificabilità non è quindi soddisfatto in modo robusto.

**Correzione richiesta:** separare almeno:

- enunciato del requisito;
- metodo di verifica (`test funzionale`, `ispezione`, `misurazione`, `security test`);
- dati/precondizioni;
- risultato atteso misurabile.

## P1-07 — Requisiti non funzionali ancora vaghi

**Posizioni:** `sezioni/04_system_requirements.tex`, righe 67-81.

Da rendere verificabili:

- **RNF-01:** definire carico, hardware, rete, percentile e numero di utenti concorrenti per i 2/3 secondi;
- **RNF-02:** «senza compromettere» e «aggiunta di risorse» non indicano una soglia di scalabilità;
- **RNF-03:** specificare almeno versioni/browser supportati e criterio responsive;
- **RNF-04:** aggiungere frequenza massima di errore, RPO/RTO o scenari di recovery;
- **RNF-05:** «documentazione sufficiente» e «limitando l'impatto» non sono misurabili;
- **RNF-06:** precisare periodo di misura del 99,9%, modalità di monitoraggio e rapporto tra manutenzione esclusa e 24/7;
- **RNF-07:** «ridurre al minimo la formazione» non è verificabile;
- **RNF-08:** indicare standard/protocolli e politica password, evitando il generico «hashing sicuro».

## P1-08 — RD-04 è ambiguo

**Posizione:** `sezioni/04_system_requirements.tex`, riga 108.

**Problema:** «il codice ... può essere monouso» non stabilisce una regola. Un requisito non può lasciare opzionale una proprietà di sicurezza fondamentale.

**Correzione richiesta:** decidere se il codice **deve** essere monouso, quando scade, chi può revocarlo e quale ruolo/sede può assegnare.

## P1-09 — RD-03 non definisce il ciclo di vita

**Posizione:** `sezioni/04_system_requirements.tex`, riga 106.

**Problema:** viene fornito un solo esempio di transizione illecita, mentre il glossario elenca diversi stati della prenotazione.

**Correzione richiesta:** aggiungere una tabella o uno State Diagram con tutte le transizioni consentite e vietate tra `In attesa`, `Confermata`, `In corso`, `Completata`, `Annullata`, `Non eseguita`.

---

# 4. Struttura del documento e LaTeX

## P1-10 — Introduzione priva di Problem Statement e scope espliciti

**Posizione:** `sezioni/01_introduzione.tex`.

**Problema:** l'introduzione contiene una descrizione generale e l'elenco degli attori, ma non distingue chiaramente:

- problem statement;
- obiettivi;
- confine del sistema;
- funzionalità IN scope;
- funzionalità OUT of scope;
- assunzioni e vincoli principali.

Le guide interne indicano esplicitamente il Problem Statement come punto di partenza.

**Correzione richiesta:** aggiungere sottosezioni brevi e chiare. Questo risolve anche le funzionalità “promesse ma non modellate”.

## P1-11 — Le schede Use Case usano i campi in modo semanticamente invertito

**Posizione:** macro `\usecasetable` in `main.tex`, righe 62-87, e tutte le chiamate in `03_user_requirements.tex`.

**Problema:** il flusso numerato completo è inserito nel campo `Descrizione`, mentre `Scenario principale` contiene soltanto un riassunto. Normalmente la descrizione è sintetica e il flusso delle azioni costituisce lo scenario principale.

**Correzione richiesta:** spostare i passi numerati nel campo `Scenario principale`, lasciare in `Descrizione` una frase sull'obiettivo del caso d'uso e sostituire l'espressione grammaticalmente scorretta/ripetuta «Passo azione» con «Flusso principale» o «Sequenza delle azioni».

## P1-12 — Numerazione delle tabelle che parte da 2

**Posizione PDF:** Elenco delle tabelle, pagina romana IV.  
**Sorgente:** `sezioni/02_glossario.tex`, longtable senza didascalia.

**Problema:** il `longtable` del glossario incrementa il contatore, ma non ha una caption; la prima scheda Use Case appare quindi come «Tabella 2» e nell'elenco manca la Tabella 1.

**Correzione richiesta:** aggiungere una caption al glossario, per esempio «Glossario dei termini», oppure evitare che quel longtable consumi il contatore delle tabelle.

## P1-13 — Tabelle RNF/RD e Design Pattern oltre la larghezza utile

Con margini da 2,5 cm la larghezza utile è circa 16 cm. Alle larghezze `p{}` vanno aggiunti due `\tabcolsep` per colonna e le linee verticali.

| File e riga | Colonne dichiarate | Esito |
|---|---:|---|
| `02_glossario.tex:7` | 4,2 + 10,5 = 14,7 cm | rientra; il suggerimento originario di Claude non è più necessario |
| `04_system_requirements.tex:13` | 3,0 + 1,2 + 4,0 + 5,8 = 14,0 cm | rientra con le larghezze attuali |
| `04_system_requirements.tex:58` | 1,8 + 3,8 + 9,6 = 15,2 cm | supera la larghezza utile includendo il padding |
| `04_system_requirements.tex:93` | 1,8 + 3,8 + 9,6 = 15,2 cm | supera la larghezza utile includendo il padding |
| `06_design_patterns.tex:17` | 0,6 + 4,2 + 3,2 + 2,4 + 4,2 = 14,6 cm | supera la larghezza utile includendo il padding |

**Correzione richiesta:** preferire `tabularx`/`ltablex` con larghezza `\textwidth` e colonne elastiche. Se si mantengono misure fisse, ridurre la terza colonna RNF/RD a circa 9,0 cm e ridurre il totale della tabella dei pattern di almeno 0,8 cm.

## P1-14 — Uso eccessivo di `[H]` e grandi zone vuote

**Posizioni:** macro Use Case e quasi tutte le figure dei capitoli 3 e 5.

**Problema:** tabelle e figure sono rese non flottanti e indivisibili. Ne risultano molte pagine con una sola scheda e ampio spazio bianco; nel PDF attuale è evidente soprattutto tra le pagine numerate 20-29 e in varie pagine dei Sequence Diagram. Alla pagina numerata 43 il titolo 5.1.3 resta inoltre in fondo alla pagina, separato dalle figure successive.

**Correzione richiesta:**

- non inserire `\clearpage` prima di ogni sottosezione;
- usare selettivamente `[htbp]` e `\FloatBarrier` ai confini tra attori;
- usare `needspace` prima dei titoli per evitare intestazioni isolate;
- valutare tabelle spezzabili soltanto per schede particolarmente lunghe;
- controllare la resa dopo la compilazione definitiva.

## P1-15 — `\clearpage` generalizzato proposto da Claude: da non applicare

Inserire `\clearpage` prima di ogni `\subsection` e `\subsubsection` produrrebbe più pagine, non risolverebbe le tabelle indivisibili e aumenterebbe lo spazio bianco. Va usato soltanto per separare capitoli o blocchi che devono realmente iniziare su una nuova pagina.

## P2-01 — Label dei Use Case fragile, ma non “invalidità casuale”

**Posizione:** `main.tex`, riga 86: `\label{uc:#1}`.

Gli spazi nelle label sono una pratica fragile e rendono difficili i riferimenti, ma non è corretto affermare che provochino necessariamente compilazioni casualmente fallite. Il problema reale è che titolo visuale e identificatore tecnico coincidono.

**Correzione consigliata:** aggiungere un argomento separato e stabile, per esempio `uc:registrazione-cittadino`, oppure rimuovere le label se non vengono mai usate.

## P2-02 — Numeri non uniformemente in grassetto

**Posizione:** `sezioni/06_design_patterns.tex`, righe 30-40.

Le righe 3-8 hanno il numero non in grassetto, diversamente dalle righe 1-2. Uniformare lo stile. Problema confermato.

## P2-03 — Capitolo «Design Pattern» singolare e non presentato come appendice

**Posizione:** `sezioni/06_design_patterns.tex`, riga 1.

Sono descritti due pattern, quindi il titolo dovrebbe essere plurale: «Design Patterns» o «Pattern di progettazione». Le istruzioni del docente parlano di appendice; i benchmark spesso usano comunque un capitolo 6. La soluzione più aderente alle istruzioni è introdurre `\appendix` e presentare questa parte come appendice, oppure spiegare chiaramente che il capitolo 6 costituisce l'appendice progettuale.

## P2-04 — Istruzioni e sorgenti di consegna non allineati

**Posizioni:**

- `Latex PDF/README.md` parla di cartella `consegna/`, che non esiste;
- `Latex PDF/sorgenti_vpp/` contiene soltanto `.gitkeep`;
- `compile_pdf.py` usa `-aux-directory`, opzione legata soprattutto a MiKTeX, mentre il README cita anche TeX Live;
- la docstring dello script parla anch'essa di `consegna/`.

**Correzione richiesta:** aggiornare la documentazione e preparare un archivio autorevole dei `.vpp`. Non includere lock file `.lck`, backup `.bak_000f`, `project.xml` o duplicati se non necessari. Per compilazione multipiattaforma usare una procedura compatibile, per esempio `latexmk` con directory di output controllata.

## P2-05 — Fonte Markdown duplicata e non affidabile

**Posizione:** `Latex PDF/specifica_MyAma.md`, righe 10-14.

Il file contiene cinque placeholder `sbers` e diverge dalla specifica LaTeX e dal secondo `PROGETTOFINALE/specifica_MyAma.md`.

**Correzione richiesta:** dichiarare una sola fonte autorevole. Se il Markdown resta nel pacchetto, sincronizzarlo e rimuovere i placeholder; altrimenti archiviarlo fuori dalla cartella di consegna.

---

# 5. Immagini, leggibilità e impaginazione

## P1-16 — Diagrammi raster e testo troppo piccolo

Molti diagrammi sono JPEG/PNG esportati senza DPI dichiarati e vengono scalati fino a `\textwidth`. I casi più critici sono:

- `class_CLASS_DIAGRAM_refined.jpg`: illeggibile nel PDF;
- `seq_DiagramVisualizzarePrenotazioniAttive.jpg`: solo 535×396 px;
- `uc_autista.jpg`: 385×456 px;
- `act_valutare_servizio.jpg`: solo 263 px di larghezza;
- numerosi Sequence Diagram con molte lifeline e messaggi ridotti su pagina verticale.

**Correzione richiesta:** esportare i diagrammi da Visual Paradigm in PDF/SVG vettoriale. Per diagrammi larghi usare pagine landscape; per quelli molto grandi creare viste per sottosistema oltre alla vista complessiva. Verificare sempre a zoom 100% e su stampa A4.

## P1-17 — Sequence Diagram con molto spazio vuoto o scala non ottimale

**Esempi nel PDF attuale:** pagine numerate 55, 63, 68 e altre tavole a singolo diagramma.

**Problema:** `width=\textwidth,height=0.70\textheight,keepaspectratio` non garantisce una dimensione visiva coerente: diagrammi molto larghi restano bassi, diagrammi molto alti diventano stretti.

**Correzione richiesta:** scegliere caso per caso orientamento e scala; evitare un'unica regola per tutte le immagini. Ritagliare i margini bianchi dell'esportazione, senza tagliare elementi UML.

## Esito del controllo visivo generale

- Nessuna pagina completamente bianca rilevata nelle 81 pagine del PDF attuale.
- Nessuna immagine estranea al dominio MyAma.
- Copertina pertinente e correttamente a pagina intera.
- Font del PDF incorporati correttamente.
- PDF non ottimizzato e piuttosto pesante, circa 10,9 MB: comprimere soltanto dopo aver sostituito i diagrammi con versioni leggibili; non sacrificare la qualità.
- PDF non taggato per accessibilità: correzione facoltativa per l'esame, ma utile se si vuole una consegna più professionale.

---

# 6. Correzioni grammaticali, sintattiche e terminologiche

## Correzioni sistemiche

1. **«Passo azione»** in tutte le schede Use Case → `Flusso principale`, `Passi dello scenario principale` o `Sequenza delle azioni`.
2. Uniformare maiuscole/minuscole:
   - `Amministratore generale AMA`;
   - `Amministratore di sede AMA`;
   - `Operatore di sede AMA`;
   - `Cittadino`, `Autista`, `Veicolo` in maiuscolo solo quando indicano formalmente un attore o una classe.
3. Uniformare apostrofi ASCII e tipografici nel sorgente (`l'utente` / `l’utente`).
4. Uniformare i termini `personale`, `lavoratore`, `membro del personale` e scegliere quello coerente con il modello.
5. Uniformare `codice invito` e `codice di invito`; la seconda forma è grammaticalmente preferibile.
6. Uniformare `Class Diagram`, `Activity Diagram`, `Sequence Diagram` oppure usare sempre le forme italiane.

## Correzioni puntuali

| Posizione | Testo/problema | Correzione consigliata |
|---|---|---|
| `01_introduzione.tex:9` | «recapito telefonico ed email» | «recapito telefonico e indirizzo e-mail» |
| `01_introduzione.tex:17` | l'amministratore «registra il personale» | se la registrazione è autonoma tramite invito: «genera i codici e gestisce l'associazione del personale alla sede» |
| `03_user_requirements.tex:152` | «La zona o il CAP indicato non è servito» | «La zona o il CAP indicati non risultano coperti dal servizio» |
| `03_user_requirements.tex:164` | «foto dello stesso» | «una foto del rifiuto» |
| `03_user_requirements.tex:693` | «La zona o il CAP indicato non è valido» | «La zona o il CAP indicati non sono validi» oppure riformulare al singolare |
| `04_system_requirements.tex:67` | «operazioni di prenotazione ... e generazione» | «operazioni di prenotazione ... e di generazione» |
| `05_modelli_ooa.tex:3` | «architettura dinamica e strutturale» | in OOA è più preciso «modelli dinamici e strutturali» |
| `05_modelli_ooa.tex:291` | «I Class Diagram rappresentano» | «I diagrammi delle classi rappresentano» |
| `06_design_patterns.tex:1` | «Design Pattern» | plurale: «Design Patterns» / «Pattern di progettazione» |
| `06_design_patterns.tex:63` | «accoppiamento rigido e unidirezionale» | `tight coupling` non implica necessariamente unidirezionalità; usare «forte accoppiamento» |
| `06_design_patterns.tex:71-73` | maiuscola dopo i due punti («La classe», «L'interfaccia») | minuscola, salvo scelta editoriale uniforme |

---

# 7. Valutazione dei problemi segnalati da Claude

| Segnalazione | Esito dell'audit |
|---|---|
| Tre Activity Diagram mancanti | **Corretta per il vecchio PDF**, ma i tre blocchi sono già nel sorgente corrente. Serve ricompilare. Restano però altri otto Activity Diagram da includere o giustificare. |
| Tabelle oltre i margini | **Parzialmente corretta.** RNF, RD e tabella pattern sono ancora troppo larghe; glossario e tabella RF, con le misure correnti, rientrano. |
| Inserire `\clearpage` prima di ogni sottosezione | **Sconsigliato.** Aumenterebbe pagine e spazi vuoti. Usare `needspace`, float meno rigidi e `FloatBarrier` selettivo. |
| Spazi nelle label | **Problema di robustezza**, non sintassi necessariamente invalida o compilazione casuale. Meglio identificatore separato e senza spazi. |
| Numeri 3-8 non in grassetto | **Confermato.** |

---

# 8. Ordine operativo consigliato

1. Bloccare scope e gerarchia dei ruoli/codici invito.
2. Risolvere le contraddizioni nei Use Case: Utente di sistema, Autista, rimozione personale, report/notifiche.
3. Completare RF e matrice di tracciabilità/verificabilità.
4. Completare o giustificare Activity e Sequence mancanti.
5. Uniformare testo e diagrammi di Observer e Strategy.
6. Integrare i pattern nel Refined finale.
7. Riesportare Use Case cittadino, Refined e diagrammi poco leggibili in vettoriale/landscape.
8. Sistemare macro Use Case, tabelle larghe, numerazione e gestione dei float.
9. Eseguire revisione grammaticale e terminologica globale.
10. Preparare l'archivio `.vpp` pulito e autorevole.
11. Ricompilare il PDF definitivo.
12. Controllare pagina per pagina: indice, liste, margini, tagli, leggibilità al 100%, pagine bianche, numerazione e corrispondenza con i sorgenti.

## Criterio finale di accettazione

Il documento può considerarsi pronto quando ogni funzionalità dichiarata nello scope possiede una catena coerente:

`Attore → Use Case → Requisito verificabile → Activity/Sequence → Classi e operazioni → eventuale Pattern → Test di accettazione`.

Ogni nome, firma di metodo, ruolo e regola deve essere identico in testo, diagrammi e sorgenti Visual Paradigm.
