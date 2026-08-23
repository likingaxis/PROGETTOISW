# MyAma — Refined Class Diagram BCE completo

## Base usata

- `class_diagram_unrefined(1).json`: baseline di classi, attributi, generalizzazioni e relazioni del modello unrefined.
- `sequence_diagrams_parziale_aggiornato(1).json`: 23 sequence diagram disponibili.
- Refined precedente fornito nella cartella `CHAT GPT.zip`: usato solo come base per non perdere i metodi di dominio già ricavati in precedenza.

## Contenuto del modello

- **19 entity**
- **14 boundary**
- **11 control**
- **2 repository/register**
- **46 classi totali**
- **8 generalizzazioni**
- **18 associazioni di dominio**
- **51 dipendenze BCE/uso**

## Normalizzazioni applicate

- `RitiroADomicilio` → `RitiroDomicilio`.
- `PersonaleAMA` → `LavoratoreAMA`.
- L'entity `Operatore di Sede AMA` → `OperatoreSedeAMA`; l'attore resta `Operatore di Sede AMA`.
- `GestionePersonale Controller` → `GestionePersonaleController`.
- `Contatto controller` → `ContattoController`.
- `Account DB` → `AccountRepository` con stereotipo `repository`.
- `AMAServiceRegister` mantenuto come nome, ma classificato `repository`.
- Stereotipi `Boundary/Control/Entity` normalizzati in `boundary/control/entity`.
- `registraEdito(esito)` corretto in `registraEsito(esito)`.
- La registrazione cittadino usa `RegistrationInterface.validate(userData)` come self-validation, in accordo con la revisione fatta in chat; `UserAccessEndpoint` coordina la registrazione dopo la validazione.
- Nel sequence `RegistrareEsitoConferimento` la logica dell'ALT viene interpretata in modo coerente: esito non valido → errore; esito valido → richiesta di conferma e aggiornamento.
- Le relazioni dirette `AutistaAMA—Veicolo` e `AutistaAMA—RitiroDomicilio` dell'unrefined sono sostituite da `Assegnazione`, perché i sequence introducono esplicitamente questa entity.
- Le associazioni specifiche Autista/Operatore→Sede sono ricondotte alla relazione più generale `SedeAMA—LavoratoreAMA`.
- `ZonaCAP` e `Assegnazione` sono aggiunte perché compaiono esplicitamente nei sequence ma non nelle 17 classi del JSON unrefined.

## Relazioni di dominio riviste

Sono state mantenute le relazioni fondamentali del class diagram unrefined, ma sono state rese coerenti con i sequence:

- `Cittadino 1 — 0..* Prenotazione`
- `Prenotazione 1 *— 1 Rifiuto`
- `TipologiaRifiuto 1 — 0..* Rifiuto`
- `SedeAMA 1 — 0..* ConferimentoSede`
- `SedeAMA 1 — 0..* LavoratoreAMA`
- `SedeAMA 1 — 0..* Veicolo`
- `SedeAMA 1 — 1 AmministratoreSedeAMA`
- `SedeAMA 0..* — 0..* ZonaCAP`
- `SedeAMA/LavoratoreAMA/Veicolo — Disponibilita`
- `RitiroDomicilio 1 *— 0..1 Assegnazione`
- `AutistaAMA 1 — 0..* Assegnazione`
- `Veicolo 1 — 0..* Assegnazione`
- `Prenotazione 1 *— 0..1 Valutazione`
- `AmministratoreSedeAMA 1 — 0..* CodiceInvito`
- `AmministratoreGeneraleAMA 1 — 0..* CodiceInvito`

La relazione `Disponibilita 1 — 0..* Prenotazione` è una **inferenza di raffinamento**: serve a rappresentare lo slot scelto dalla prenotazione, anche se nei sequence cittadini la disponibilità passa attraverso `AMAServiceRegister`.

## Import in Visual Paradigm

1. `Project → Import → XMI...`
2. seleziona `CLASS-REFINED-COMPLETE-MyAma.xmi`
3. lascia `Matching: By Internal ID`
4. puoi attivare `Generate new ID for elements not found in current project`
5. dopo l'import crea/apri un Class Diagram e trascina le classi dal Model Explorer.

### Nota sugli stereotipi

L'XMI usa UML standard e salva `boundary`, `control`, `entity` e `repository` anche nella documentazione delle classi. La resa grafica automatica degli stereotipi dipende dall'importatore XMI di Visual Paradigm.  
Il file `.puml` mostra invece gli stereotipi esplicitamente come `<<boundary>>`, `<<control>>`, `<<entity>>`, `<<repository>>`.

## Limite attuale

Il JSON dei sequence è dichiarato `parziale_aggiornato` e contiene 23 diagrammi. Il modello è quindi completo **rispetto ai 23 sequence forniti**. Se arrivano altri sequence, vanno aggiunti i relativi metodi/dipendenze prima della consegna finale.
