# MyAma — PlantUML Refined corretti

Questi file sono una baseline operativa ottenuta incrociando:
- Class Diagram Unrefined;
- Refined attuale;
- Activity Diagram (26 flussi);
- Sequence Diagram e mappatura messaggio→metodo;
- System Requirements;
- Glossario;
- GUIDA_COLLEGAMENTI_UML.md.

## File
1. `01_ENTITY_MODEL.puml` — modello Entity completo, da usare come riferimento principale.
2. `02_REGISTRAZIONE_ACCESSO.puml` — registrazione, invito, login.
3. `03_CITTADINO_PRENOTAZIONI.puml` — cittadino, ritiri, conferimenti, storico, valutazione.
4. `04_AUTISTA_RITIRI.puml` — ritiri assegnati, esito, contatto cittadino.
5. `05_OPERATORE_SEDE.puml` — prenotazioni sede, verifica, esito conferimento.
6. `06_AMMINISTRAZIONE.puml` — admin sede/generale, personale, mezzi, disponibilità, CAP, codici.

## Correzioni già incorporate
- `RitiroDomicilio` e `ConferimentoSede` sono entrambi sottoclassi di `Prenotazione`.
- Eliminata la relazione permanente diretta `AutistaAMA—Veicolo`.
- L'allocazione del ritiro passa tramite `Assegnazione`.
- Aggiunta `Assegnazione—Veicolo`.
- Corrette le cardinalità principali `TipologiaRifiuto—Rifiuto`, `ConferimentoSede—SedeAMA`, `OperatoreSedeAMA—SedeAMA`.
- `CodiceInvito` può essere 0..* per amministratore.
- `Disponibilita` è raffinata in Lavoratore/Veicolo/Sede per evitare una composizione ambigua many-to-many.
- `password` raffinata in `passwordHash`.
- `StatoPrenotazione`, `EsitoServizio`, `RuoloUtente` modellati come enum.
- BCE organizzato in diagrammi separati per area.

## Decisioni progettuali ancora da confermare
- `SedeAMA—ZonaCAP` è lasciata many-to-many (`0..* ↔ 0..*`) perché i documenti confermano l'associazione ma non impongono in modo univoco che un CAP appartenga a una sola sede.
- `RitiroDomicilio—Assegnazione` è `0..1`, interpretando `Assegnazione` come allocazione corrente. Se volete conservare lo storico delle riassegnazioni, cambiare a `0..*`.
- `AmministratoreSedeAMA—SedeAMA` è `0..1 ↔ 1`: ogni admin di sede amministra una sede; una sede può temporaneamente non avere admin o averne uno. Se il requisito vuole esattamente un admin sempre presente, usare `1 ↔ 1`.
