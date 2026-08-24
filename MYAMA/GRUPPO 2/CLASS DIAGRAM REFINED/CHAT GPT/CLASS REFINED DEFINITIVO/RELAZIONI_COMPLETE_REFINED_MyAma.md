# MyAma — Lista completa dei collegamenti del Refined Class Diagram

Questa lista è stata ricavata direttamente da `00_REFINED_COMPLETO.puml` e verificata riga per riga.

## Formato usato

- `Cittadino 1 — Association — 0..* Prenotazione`
- `Prenotazione 1 — Composition — 1 Rifiuto`
- `Cittadino — Generalization — UtenteSistema`
- `RegistrationInterface — Usage — UserAccessEndpoint`

Per `Generalization`, la classe a sinistra è la **sottoclasse** e quella a destra è la **superclasse**.
Per `Usage` e `Create` non sono indicate molteplicità perché non si applicano.

## Controllo di completezza

- Collegamenti totali: **95**
- Generalization: **11**
- Association: **12**
- Composition: **6**
- Aggregation: **1**
- Usage: **63**
- Create: **2**

## GENERALIZZAZIONI VALERIO INIZIA

- Cittadino — Generalization — UtenteSistema
- LavoratoreAMA — Generalization — UtenteSistema
- AutistaAMA — Generalization — LavoratoreAMA
- OperatoreSedeAMA — Generalization — LavoratoreAMA
- AmministratoreSedeAMA — Generalization — UtenteSistema
- AmministratoreGeneraleAMA — Generalization — UtenteSistema
- RitiroDomicilio — Generalization — Prenotazione
- ConferimentoSede — Generalization — Prenotazione
- DisponibilitaLavoratore — Generalization — Disponibilita
- DisponibilitaVeicolo — Generalization — Disponibilita
- DisponibilitaSede — Generalization — Disponibilita

## ASSOCIAZIONI / COMPOSIZIONI / AGGREGAZIONI

- Cittadino 1 — Association — 0..* Prenotazione
- Prenotazione 1 — Composition — 1 Rifiuto
- TipologiaRifiuto 1 — Association — 0..* Rifiuto
- Prenotazione 1 — Composition — 0..1 Valutazione
- ConferimentoSede 0..* — Association — 1 SedeAMA
- OperatoreSedeAMA 0..* — Association — 1 SedeAMA
- AmministratoreSedeAMA 0..1 — Association — 1 SedeAMA
- SedeAMA 0..* — Association — 0..* ZonaCAP

VALERIO FINISCE

ALFREDO INIZIA
- SedeAMA 1 — Aggregation — 0..* Veicolo
- SedeAMA 1 — Association — 0..* LavoratoreAMA
- LavoratoreAMA 1 — Composition — 0..* DisponibilitaLavoratore
- Veicolo 1 — Composition — 0..* DisponibilitaVeicolo
- SedeAMA 1 — Composition — 0..* DisponibilitaSede
- RitiroDomicilio 1 — Composition — 0..1 Assegnazione
- Assegnazione 0..* — Association — 1 AutistaAMA
- Assegnazione 0..* — Association — 1 Veicolo
- AmministratoreSedeAMA 1 — Association — 0..* CodiceInvito
- AmministratoreGeneraleAMA 1 — Association — 0..* CodiceInvito
- DisponibilitaSede 1 — Association — 0..* Prenotazione

## BOUNDARY → CONTROL

- RegistrationInterface — Usage — UserAccessEndpoint
- InvitationRegistrationInterface — Usage — UserAccessEndpoint
- LoginInterface — Usage — UserAccessEndpoint
- HomeBookInterface — Usage — AMAServiceController
- WasteDisposalInterface — Usage — AMAServiceController
- BookingHistory — Usage — AMAServiceController
- PannelloAutistaUI — Usage — GestoreRitiriController
- PannelloAutistaUI — Usage — GestoreEsitoController

ALFREDO FINISCE
SAMUELE INIZIA
- PannelloAutistaUI — Usage — ContattoController
- PannelloSedeUI — Usage — GestioneSedeController
- ControlloVarcoUI — Usage — AccettazioneController
- GestioneConferimentoUI — Usage — GestioneConferimentoController
- GestioneCodiciUI — Usage — CodiciController
- GestionePersonaleUI — Usage — GestionePersonaleController
- GestioneSedeUI — Usage — GestioneSedeController
- GestioneVeicoliUI — Usage — GestioneVeicoliController

## CONTROL → CONTROL

- UserAccessEndpoint — Usage — UserRegistry
- UserAccessEndpoint — Usage — UserFactory
- AMAServiceController — Usage — UserRegistry

## CONTROL → ENTITY

- UserAccessEndpoint — Usage — UtenteSistema
- UserAccessEndpoint — Usage — Cittadino
- UserAccessEndpoint — Usage — LavoratoreAMA
- UserAccessEndpoint — Usage — CodiceInvito
- UserRegistry — Usage — UtenteSistema
- UserRegistry — Usage — Cittadino
- UserRegistry — Usage — Prenotazione
- UserRegistry — Usage — Valutazione
SAMUELE FINISCE
LUCA INIZIA
- UserRegistry — Usage — RitiroDomicilio
- UserRegistry — Usage — ConferimentoSede
- UserFactory — Create — UtenteSistema
- UserFactory — Create — Cittadino
- AMAServiceController — Usage — Prenotazione
- AMAServiceController — Usage — RitiroDomicilio
- AMAServiceController — Usage — ConferimentoSede
- AMAServiceController — Usage — Rifiuto
- AMAServiceController — Usage — SedeAMA
- AMAServiceController — Usage — ZonaCAP
- AMAServiceController — Usage — DisponibilitaSede
- AMAServiceController — Usage — Valutazione
- GestoreRitiriController — Usage — AutistaAMA
- GestoreRitiriController — Usage — Prenotazione
- GestoreRitiriController — Usage — RitiroDomicilio
- GestoreRitiriController — Usage — Assegnazione
- GestoreEsitoController — Usage — Prenotazione
- GestoreEsitoController — Usage — RitiroDomicilio
- ContattoController — Usage — Cittadino
LUCA FINISCE
DAVIDE INIZIA
- GestioneSedeController — Usage — SedeAMA
- GestioneSedeController — Usage — Prenotazione
- GestioneSedeController — Usage — DisponibilitaSede
- GestioneSedeController — Usage — ZonaCAP
- GestioneSedeController — Usage — AmministratoreSedeAMA
- AccettazioneController — Usage — Prenotazione
- AccettazioneController — Usage — OperatoreSedeAMA
- GestioneConferimentoController — Usage — Prenotazione
- GestioneConferimentoController — Usage — ConferimentoSede
- CodiciController — Usage — AmministratoreGeneraleAMA
- CodiciController — Usage — CodiceInvito
- GestionePersonaleController — Usage — LavoratoreAMA
- GestionePersonaleController — Usage — CodiceInvito
- GestionePersonaleController — Usage — AmministratoreSedeAMA
- GestionePersonaleController — Usage — DisponibilitaLavoratore
- GestioneVeicoliController — Usage — Veicolo
- GestioneVeicoliController — Usage — SedeAMA
- GestioneVeicoliController — Usage — DisponibilitaVeicolo
- GestioneVeicoliController — Usage — AmministratoreSedeAMA
DAVIDE FINISCE

## Verifica finale

La lista contiene **95 collegamenti**, esattamente quanti quelli presenti nel file `00_REFINED_COMPLETO.puml`.
Non sono stati aggiunti collegamenti esterni al file e non ne sono stati rimossi.