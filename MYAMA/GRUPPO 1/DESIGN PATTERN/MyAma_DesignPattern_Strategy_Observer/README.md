# MyAma — Design Pattern UML

## Strategy
Problema: separare l'algoritmo di scelta di Autista e Veicolo dal componente che coordina l'assegnazione del RitiroDomicilio.

Ruoli GoF:
- Context: `GestoreAssegnazione`
- Strategy: `StrategiaAssegnazione`
- ConcreteStrategy:
  - `StrategiaPerCapacita`
  - `StrategiaPerZona`
  - `StrategiaBilanciamentoCarico`

## Observer
Problema: permettere a più componenti di reagire al cambio di stato di `Prenotazione` senza accoppiare direttamente la prenotazione a tutte le classi concrete interessate.

Ruoli GoF:
- Subject: `SubjectPrenotazione`
- ConcreteSubject: `Prenotazione`
- Observer: `ObserverPrenotazione`
- ConcreteObserver:
  - `NotificaCittadinoObserver`
  - `AggiornamentoAutistaObserver`
  - `AggiornamentoSedeObserver`

Le classi specifiche dei pattern sono raffinazioni progettuali introdotte per risolvere i problemi individuati nel Refined Class Diagram.
