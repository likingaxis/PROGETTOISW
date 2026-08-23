# MyAma — Refined Class Diagram: note di costruzione

## Fonti usate
- `MYAMA/PROGETTOFINALE/CLASS DIAGRAM/class diagram unrefined.vpp` + relativo JPG come baseline.
- `MYAMA/PROGETTOFINALE/SEQUENCE DIAGRAM/LISTA SEQUENCE DIAGRAM.md`.
- `MYAMA/GRUPPO 1/SEQUENCE DIAGRAM/METODI.md`.
- `MYAMA/GRUPPO 1/SEQUENCE DIAGRAM/METODI ASSOCIATI A MESSAGGI.md`.
- `MYAMA/PROGETTOFINALE/SYSTEM REQUIREMENTS/System Requirements.md`.
- `MYAMA/PROGETTOFINALE/USE CASE DIAGRAM/User requirements definition.md`.
- `MYAMA/PROGETTOFINALE/glossario.md`.

## Criterio
Il modello conserva le 19 classi esplicitamente elencate nell'analisi dell'Unrefined e aggiunge soprattutto le operazioni emerse dai Sequence Diagram. Non sono state introdotte come classi autonome entità presenti soltanto nel glossario (es. Notifica, Report, Tariffa, Itinerario) perché non risultano parte della baseline Unrefined fornita.

## Punti da verificare visivamente in Visual Paradigm
1. Nomi/tipi esatti degli attributi già presenti nel `.vpp` originale: il file XMI usa tipi ragionevoli e coerenti con requisiti e glossario quando il testo non esponeva il dettaglio del `.vpp`.
2. Cardinalità `SedeAMA—ZonaCAP`: impostata molti-a-molti perché i requisiti parlano di associazioni sede/zone/CAP; se il vostro Unrefined usa un vincolo più stretto, mantenere quello.
3. `AmministratoreSedeAMA`: modellato come specializzazione diretta di `UtenteSistema`, separata da `LavoratoreAMA`.
4. `Valutazione`: una prenotazione può avere al massimo una valutazione (`0..1`).
5. `Assegnazione`: collegata a un solo `RitiroDomicilio`, un `AutistaAMA` e un `Veicolo`; la prenotazione può non essere ancora assegnata (`0..1`).
6. `Disponibilita`: associata alla sede e alla prenotazione; la prenotazione usa un singolo slot.
