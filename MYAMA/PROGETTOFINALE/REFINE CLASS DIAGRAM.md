# REFINED CLASS DIAGRAM — MyAma

> Documento di analisi completo per il Class Diagram Refined.
> Estratto dai 5 file `project.xml` dei Sequence Diagram + Class Diagram Unrefined.

---

## 1. CLASSI ENTITY (dal Class Diagram Unrefined + operazioni dai Sequence Diagram)

### 1.1 UtenteSistema (abstract)
**Stereotipo:** `<<entity>>`

| Attributo | Tipo | Visibilità |
|-----------|------|------------|
| id | int | - (private) |
| nome | String | - |
| cognome | String | - |
| email | String | - |
| password | String | - |

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| new UtenteSistema(data) | data | UtenteSistema | Davide - SequenceRegistrarsiTramiteCodiceInvito |

**Sottoclassi (generalizzazione):**
- Cittadino
- AmministratoreSedeAMA
- AmministratoreGeneraleAMA
- AutistaAMA (tramite LavoratoreAMA)
- OperatoreSedeAMA (tramite LavoratoreAMA)

---

### 1.2 Cittadino
**Stereotipo:** `<<entity>>`
**Generalizza:** UtenteSistema

| Attributo | Tipo | Visibilità |
|-----------|------|------------|
| codiceFiscale | String | - |
| telefono | String | - |
| indirizzo | String | - |
| CAP | String | - |

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| new Cittadino(email, passHash, username) | email: String, passHash: String, username: String | Cittadino | Davide - SequenceRegistrarsiComeCittadino |
| new cittadino(email, passHash, username) | email: String, passHash: String, username: String | Cittadino | Valerio - Registrazione cittadino |
| getTelefono() | — | String | Alfredo - SequenceChiamareCittadino (implicito) |

---

### 1.3 LavoratoreAMA (abstract)
**Stereotipo:** `<<entity>>`
**Generalizza:** UtenteSistema

| Attributo | Tipo | Visibilità |
|-----------|------|------------|
| idDipendente | String | - |
| telefono | String | - |

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| new personaleAMA(userName, passHash, email, role) | userName: String, passHash: String, email: String, role: String | LavoratoreAMA | Valerio - SequenceRegistrarsiTramiteCodiceInvito |
| getDettagli(idLavoratore) | idLavoratore: String | dettagli | Luca - SequenceGestireDisponibilitaLavoratori |

**Sottoclassi:**
- AutistaAMA
- OperatoreSedeAMA

---

### 1.4 AutistaAMA
**Stereotipo:** `<<entity>>`
**Generalizza:** LavoratoreAMA

| Attributo | Tipo | Visibilità |
|-----------|------|------------|
| (eredita da LavoratoreAMA) | | |

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| getRitiriAssegnati() | — | List | Alfredo - SequenceVisualizzareRitiriAssegnati (implicito via richiediRitiriAssegnati) |

---

### 1.5 OperatoreSedeAMA
**Stereotipo:** `<<entity>>`
**Generalizza:** LavoratoreAMA

| Attributo | Tipo | Visibilità |
|-----------|------|------------|
| (eredita da LavoratoreAMA) | | |

---

### 1.6 AmministratoreSedeAMA
**Stereotipo:** `<<entity>>`
**Generalizza:** UtenteSistema

| Attributo | Tipo | Visibilità |
|-----------|------|------------|
| (eredita da UtenteSistema) | | |

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| getSedeAssociata() | — | SedeAMA | Luca - SequenceGestireDisponibilitaLavoratori, Samuele - SequenceGestireDisponibilitaVeicoli |

---

### 1.7 AmministratoreGeneraleAMA
**Stereotipo:** `<<entity>>`
**Generalizza:** UtenteSistema

| Attributo | Tipo | Visibilità |
|-----------|------|------------|
| (eredita da UtenteSistema) | | |

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| getElencoAdminSede() | — | List | Alfredo - SequenceRimuovereAmministratoreSede |
| getDettagli(idAdminSede) | idAdminSede: String | dettagli | Alfredo - SequenceRimuovereAmministratoreSede |

---

### 1.8 Prenotazione (abstract)
**Stereotipo:** `<<entity>>`

| Attributo | Tipo | Visibilità |
|-----------|------|------------|
| idPrenotazione | int | - |
| data | LocalDate | - |
| fasciaOraria | String | - |
| stato | String | - |

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| destroyEntity() | — | status: boolean | Davide - SequenceAnnullarePrenotazione |
| setValutazione(data) | data | void | Davide - SequenceValutareServizio |
| modificaStato(esito) | esito: String | void | Alfredo - SequenceRegistrareEsitoRitiro |
| aggiornaStato(esito) | esito: String | void | Luca - SequenceRegistrareEsitoConferimento |
| verificaValidita(sede, data, fasciaOraria, stato) | sede: SedeAMA, data: LocalDate, fasciaOraria: String, stato: String | boolean | Luca - SequenceVerificarePrenotazioneCittadino |

**Sottoclassi (generalizzazione):**
- RitiroDomicilio
- ConferimentoSede

---

### 1.9 RitiroDomicilio
**Stereotipo:** `<<entity>>`
**Generalizza:** Prenotazione

| Attributo | Tipo | Visibilità |
|-----------|------|------------|
| indirizzoRitiro | String | - |

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| new RitiroADomicilio(in: data) | data | RitiroDomicilio | Davide - SequenceRichiedereRitiroADomicilio |

---

### 1.10 ConferimentoSede
**Stereotipo:** `<<entity>>`
**Generalizza:** Prenotazione

| Attributo | Tipo | Visibilità |
|-----------|------|------------|
| (eredita da Prenotazione) | | |

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| new ConferimentoSede(in: data) | data | ConferimentoSede | Davide - SequencePrenotareConferimentoSedeAMA |

---

### 1.11 Valutazione
**Stereotipo:** `<<entity>>`

| Attributo | Tipo | Visibilità |
|-----------|------|------------|
| voto | int | - |
| commento | String | - |

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| new Valutazione() | — | Valutazione | Davide - SequenceValutareServizio |

---

### 1.12 Rifiuto
**Stereotipo:** `<<entity>>`

| Attributo | Tipo | Visibilità |
|-----------|------|------------|
| descrizione | String | - |
| pesoStimato | double | - |
| volumeStimato | double | - |
| foto | String | - |

---

### 1.13 TipologiaRifiuto
**Stereotipo:** `<<entity>>`

| Attributo | Tipo | Visibilità |
|-----------|------|------------|
| idTipologia | int | - |
| nome | String | - |
| descrizione | String | - |

---

### 1.14 SedeAMA
**Stereotipo:** `<<entity>>`

| Attributo | Tipo | Visibilità |
|-----------|------|------------|
| idSede | int | - |
| nome | String | - |
| indirizzo | String | - |
| CAP | String | - |

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| recuperaPrenotazioniSede(idSede) | idSede: int | List\<Prenotazione\> | Luca - SequenceVisualizzarePrenotazioniSede |
| recuperaLavoratori() | — | List\<LavoratoreAMA\> | Luca - SequenceGestireDisponibilitaLavoratori |
| recuperaVeicoli() | — | List\<Veicolo\> | Luca/Samuele - SequenceGestireDisponibilitaVeicoli |
| recuperaZoneCAPAssociate() | — | List\<ZonaCAP\> | Luca - SequenceGestireAssociazioniSedeZoneCAP |
| associaZonaCAP(zonaCAP) | zonaCAP: ZonaCAP | void | Luca - SequenceGestireAssociazioniSedeZoneCAP |
| rimuoviZonaCAP(zonaCAP) | zonaCAP: ZonaCAP | void | Luca - SequenceGestireAssociazioniSedeZoneCAP |

---

### 1.15 Veicolo
**Stereotipo:** `<<entity>>`

| Attributo | Tipo | Visibilità |
|-----------|------|------------|
| idVeicolo | int | - |
| targa | String | - |
| capacitaPeso | double | - |
| capacitaVolume | double | - |

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| recuperaDisponibilita() | — | List\<Disponibilita\> | Samuele - SequenceGestireDisponibilitaVeicoli |

---

### 1.16 Disponibilita
**Stereotipo:** `<<entity>>`

| Attributo | Tipo | Visibilità |
|-----------|------|------------|
| data | LocalDate | - |
| oraInizio | LocalTime | - |
| oraFine | LocalTime | - |

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| inserisciDisponibilita(data, oraInizio, oraFine) | data: LocalDate, oraInizio: LocalTime, oraFine: LocalTime | void | Luca/Samuele |
| aggiornaDisponibilita(data, oraInizio, oraFine) | data: LocalDate, oraInizio: LocalTime, oraFine: LocalTime | Disponibilita | Luca/Samuele |

---

### 1.17 CodiceInvito
**Stereotipo:** `<<entity>>`

| Attributo | Tipo | Visibilità |
|-----------|------|------------|
| codice | String | - |
| ruoloAssociato | String | - |
| valido | boolean | - |
| utilizzato | boolean | - |

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| creaCodice(ruolo) | ruolo: String | CodiceInvito | Luca - SequenceGenerareCodiceInvitoPersonale |

---

### 1.18 ZonaCAP (NUOVA — emersa dai Sequence Diagram)
**Stereotipo:** `<<entity>>`

| Attributo | Tipo | Visibilità |
|-----------|------|------------|
| cap | String | - |
| nomeZona | String | - |

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| cercaZonaCAP(cap) | cap: String | ZonaCAP | Luca - SequenceGestireAssociazioniSedeZoneCAP |

---

### 1.19 Assegnazione (NUOVA — emersa dai Sequence Diagram)
**Stereotipo:** `<<entity>>`

| Attributo | Tipo | Visibilità |
|-----------|------|------------|
| idAssegnazione | int | - |
| dataAssegnazione | LocalDate | - |

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| — | — | — | Alfredo - SequenceVisualizzareRitiriAssegnati (lifeline esplicita) |

---

## 2. CLASSI BOUNDARY (emerse dai Sequence Diagram)

### 2.1 RegistrationInterface
**Stereotipo:** `<<boundary>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| richiediRegistrazione(in: email, passHash, username) | email: String, passHash: String, username: String | void | Davide |
| mostraInterfacciaRegistrazione() | — | void | Davide |
| mostraInterfacciaLogin() | — | void | Davide |
| showRegistrationInterface(errorData) | errorData | void | Valerio |
| showRegistrationInterface(errorValidationCode) | errorValidationCode | void | Valerio |
| redirectToLogin() | — | void | Davide |

---

### 2.2 InvitationRegistrationInterface
**Stereotipo:** `<<boundary>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| richiediRegistrazione(in: code, role, email, passHash, username) | code: String, role: String, email: String, passHash: String, username: String | void | Davide |

---

### 2.3 LoginInterface
**Stereotipo:** `<<boundary>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| richiediLogin(in: email, passHash, username) | email: String, passHash: String, username: String | void | Davide |
| showLoginInterface(errorData) | errorData | void | Valerio |
| forwardLoginData(out: sessionID, role) | — | sessionID, role | Davide |

---

### 2.4 HomeBookInterface
**Stereotipo:** `<<boundary>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| getAvailability(in: data) | data | void | Davide - RitiroDomicilio |
| richiediRitiroADomicilio(in: data) | data | void | Davide |
| return(out: availabilityList) | — | availabilityList | Davide |
| prenotazioneConfermata() | — | void | Davide |
| fasciaOrariaNonDisponibile() | — | void | Davide |

---

### 2.5 WasteDisposalInterface
**Stereotipo:** `<<boundary>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| getAvailability(in: data) | data | void | Davide - Conferimento |
| richiediConferimento(in: data) | data | void | Davide |
| return(out: availabilityList) | — | availabilityList | Davide |
| prenotazioneConfermata() | — | void | Davide |
| fasciaOrariaNonDisponibile() | — | void | Davide |

---

### 2.6 BookingHistory
**Stereotipo:** `<<boundary>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| getStoricoPrenotazioni(in: userData, filter) | userData, filter: String | void | Davide |
| mostraStoricoPrenotazioni(out: bookList) | bookList | void | Davide |
| annullaPrenotazione(in: data) | data | void | Davide |
| monstraCancellazioneEffettuata() | — | void | Davide |
| mostraErroreCancellazione() | — | void | Davide |
| valutaPrenotazione(in: data, valutazione) | data, valutazione | void | Davide |
| confermaValutazione() | — | void | Davide |
| mostraErroreValutazione() | — | void | Davide |

---

### 2.7 PannelloAutistaUI
**Stereotipo:** `<<boundary>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| richiediRitiriAssegnati() | — | void | Alfredo |
| mostraRitiri() | — | void | Alfredo |
| inserisciEsito(esito) | esito: String | void | Alfredo |
| mostraConferma() | — | void | Alfredo |
| mostraMessaggioErrore() | — | void | Alfredo |
| mostraChiamata() | — | void | Alfredo |
| mostraInformazione() | — | void | Alfredo |

---

### 2.8 PannelloSedeUI
**Stereotipo:** `<<boundary>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| richiediPrenotazioniSede() | — | void | Luca |
| mostraPrenotazioni(listaPrenotazioni) | listaPrenotazioni: List | void | Luca |

---

### 2.9 ControlloVarcoUI
**Stereotipo:** `<<boundary>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| inserisciIdPrenotazione(id) | id: int | void | Luca |
| mostraDettagliConferimento(dettagli) | dettagli | void | Luca |
| mostraPrenotazioneNonTrovata() | — | void | Luca |
| mostraEsitoVerifica(OK) | — | void | Luca |

---

### 2.10 GestioneConferimentoUI
**Stereotipo:** `<<boundary>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| selezionaPrenotazione(id) | id: int | void | Luca |
| inserisciEsito(esito) | esito: String | void | Luca |
| confermaRegistrazione(id, esito) | id: int, esito: String | void | Luca |
| mostraDettagliConferimento(dettagliConferimento) | dettagliConferimento | void | Luca |
| segnalaErroreEsito() | — | void | Luca |

---

### 2.11 GestioneCodiciUI
**Stereotipo:** `<<boundary>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| richiediCodiceAdminSede() | — | void | Alfredo |
| mostraCodiceGenerato() | — | void | Alfredo |
| mostraElencoAdminSede() | — | void | Alfredo |
| richiediDettagli(idAdminSede) | idAdminSede: String | void | Alfredo |
| mostraDettagli() | — | void | Alfredo |
| richiediRimozione() | — | void | Alfredo |
| richiediConferma() | — | void | Alfredo |
| confermaRimozione() | — | void | Alfredo |
| annullaOperazione() | — | void | Alfredo |

---

### 2.12 GestionePersonaleUI
**Stereotipo:** `<<boundary>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| accedeGestionePersonale() | — | void | Luca |
| richiediGenerazioneCodice() | — | void | Luca |
| mostraCodiceInvito(codiceGenerato) | codiceGenerato: String | void | Luca |
| richiediLavoratoriSede() | — | void | Luca |
| mostraLavoratori(listaLavoratori) | listaLavoratori: List | void | Luca |
| selezionaLavoratore(idLavoratore) | idLavoratore: String | void | Luca |
| mostraInformazioni(dettagliLavoratore) | dettagliLavoratore | void | Luca |
| richiediRimozione() | — | void | Luca |
| confermaRimozione() | — | void | Luca |
| mostraConfermaOperazione() | — | void | Luca |
| mostraPersonale(listaPersonale) | listaPersonale: List | void | Luca |
| mostraErroreLavoratore() | — | void | Luca |
| mostraErroreAutorizzazione() | — | void | Luca |

---

### 2.13 GestioneSedeUI
**Stereotipo:** `<<boundary>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| richiediDisponibilitaSede() | — | void | Luca |
| richiediGestioneDisponibilitaSede() | — | void | Luca |
| mostraDisponibilita(disponibilitaAttuali) | disponibilitaAttuali: List | void | Luca |
| mostraConfermaAggiornamento() | — | void | Luca |
| mostraErroreDisponibilita() | — | void | Luca |
| mostraRichiestaConferma() | — | void | Luca |
| richiediGestioneZoneCAP() | — | void | Luca |
| mostraZoneCAPAssociate(zoneCAPAssociate) | zoneCAPAssociate: List | void | Luca |
| mostraErroreCAP() | — | void | Luca |
| mostraErroreAssociazione() | — | void | Luca |

---

### 2.14 GestioneVeicoliUI
**Stereotipo:** `<<boundary>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| richiediGestioneDisponibilitaVeicoli() | — | void | Luca/Samuele |
| richiediVeicoliSede() | — | void | Luca/Samuele |
| mostraVeicoli(listaVeicoli) | listaVeicoli: List | void | Luca/Samuele |
| selezionaVeicolo(idVeicolo) | idVeicolo: int | void | Samuele |
| mostraDisponibilita(disponibilitaAttuali) | disponibilitaAttuali: List | void | Samuele |
| mostraConfermaAggiornamento() | — | void | Samuele |
| mostraErroreDisponibilita() | — | void | Samuele |
| mostraRichiestaConferma() | — | void | Samuele |

---

## 3. CLASSI CONTROL (emerse dai Sequence Diagram)

### 3.1 UserAccessEndpoint
**Stereotipo:** `<<control>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| registrationForward(in: userData) | userData | void | Davide/Valerio |
| registrationForward(in: role, userData) | role: String, userData | void | Davide |
| forwardCreateUserByRole(in: role, userData) | role: String, userData | void | Davide |
| loginForward(in: userData) | userData | void | Davide |
| loginTest(userData) | userData | result | Davide |
| forwardData(userData) | userData | void | Valerio |
| checkAccount(email, passHash, userName) | email: String, passHash: String, userName: String | accountStatus | Valerio |
| checkVCode(validationCode) | validationCode: String | codeStatus | Valerio |
| accessAccount() | — | void | Valerio |
| redirectLoginInterface() | — | void | Valerio |

---

### 3.2 AMAServiceController
**Stereotipo:** `<<control>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| forwardAvailabilityRequest(in: data) | data | void | Davide - Ritiro |
| forwardBookRequest(in: data) | data | void | Davide - Ritiro |
| requestAvailabilityCheck(in: data) | data | void | Davide - Conferimento |
| requestAvailabilityList(in: data) | data | void | Davide - Conferimento |
| forwardBookHistoryRequest(in: userData, filter) | userData, filter | void | Davide - Storico |
| forwardCancelRequest(in: data) | data | void | Davide - Annullamento |
| forwardCommentRequest(in: data, valutazione) | data, valutazione | void | Davide - Valutazione |
| forwardNotAvailable() | — | void | Davide |
| forwardAvailable() | — | void | Davide |
| forwardError() | — | void | Davide |
| forwardConfirm() | — | void | Davide |

---

### 3.3 GestoreRitiriController
**Stereotipo:** `<<control>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| visualizzaRitiriAssegnati() | — | List | Alfredo |
| registraEsitoRitiro(id, esito) | id: int, esito: String | void | Alfredo |

---

### 3.4 GestoreEsitoController
**Stereotipo:** `<<control>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| registraEsito(id, esito) | id: int, esito: String | void | Alfredo |

---

### 3.5 ContattoController
**Stereotipo:** `<<control>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| richiediDettagli(id) | id | dettagli | Alfredo - SequenceChiamareCittadino |
| getDettagli(id) | id | dettagli | Alfredo |

---

### 3.6 CodiciController
**Stereotipo:** `<<control>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| generaCodice("AmministratoreSedeAMA") | tipo: String | CodiceInvito | Alfredo |
| richiediCodiceAdminSede() | — | void | Alfredo |
| getElencoAdminSede() | — | List | Alfredo |
| richiediDettagli(idAdminSede) | idAdminSede: String | void | Alfredo |
| confermaRimozione() | — | void | Alfredo |

---

### 3.7 GestioneSedeController
**Stereotipo:** `<<control>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| recuperaPrenotazioniSede(idSede) | idSede: int | List | Luca |
| richiediDisponibilitaSede() | — | void | Luca |
| modificaDisponibilita(data, oraInizio, oraFine) | data, oraInizio, oraFine | void | Luca |
| modificaAssociazione(cap, operazione) | cap: String, operazione: String | void | Luca |
| richiediGestioneZoneCAP() | — | void | Luca |

---

### 3.8 AccettazioneController
**Stereotipo:** `<<control>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| cercaPrenotazione(id) | id: int | Prenotazione | Luca |
| verificaPrenotazione(id) | id: int | boolean | Luca |
| registraEsito(id, esito) | id: int, esito: String | void | Luca |
| verificaEsito(esito) | esito: String | boolean | Luca |

---

### 3.9 GestioneConferimentoController
**Stereotipo:** `<<control>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| selezionaPrenotazione(id) | id: int | Prenotazione | Luca |
| inserisciEsito(esito) | esito: String | void | Luca |
| confermaRegistrazione(id, esito) | id: int, esito: String | void | Luca |

---

### 3.10 GestionePersonaleController
**Stereotipo:** `<<control>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| generaCodiceInvito(ruolo) | ruolo: String | CodiceInvito | Luca |
| recuperaLavoratori() | — | List | Luca |
| richiediDettagli(idLavoratore) | idLavoratore: String | void | Luca |
| rimuoviPersonale(idLavoratore) | idLavoratore: String | void | Luca |
| richiediPersonaleSede() | — | List | Luca |
| modificaDisponibilita(idLavoratore, data, oraInizio, oraFine) | idLavoratore: String, data, oraInizio, oraFine | void | Luca |
| verificaAssociazione(lavoratore) | lavoratore: LavoratoreAMA | boolean | Luca |

---

### 3.11 GestioneVeicoliController
**Stereotipo:** `<<control>>`

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| recuperaVeicoli() | — | List | Samuele/Luca |
| modificaDisponibilita(idVeicolo, data, oraInizio, oraFine) | idVeicolo: int, data, oraInizio, oraFine | void | Samuele/Luca |
| confermaModifiche(idVeicolo) | idVeicolo: int | void | Samuele |
| selezionaVeicolo(idVeicolo) | idVeicolo: int | void | Samuele |

---

### 3.12 UserRegistry
**Stereotipo:** `<<control>>` (o service)

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| createUser(userData) | userData | UtenteSistema | Davide |
| createUserByRole(role, userData) | role: String, userData | UtenteSistema | Davide |
| getBookHistory(in: userData, filter) | userData, filter: String | List | Davide |
| cancelBook(in: data) | data | status: boolean | Davide |
| commentBook(in: data, valutazione) | data, valutazione | status | Davide |
| getHomeBookAvailabilityList(in: data) | data | List | Davide |
| checkHomeBookAvailability(in: data) | data | boolean | Davide |
| getAvailabilityList(in: data) | data | List | Davide |
| checkAvailability(in: data) | data | boolean | Davide |
| newHomeBookRequest(in: data) | data | RitiroDomicilio | Davide |
| newDisposalRequest(in: data) | data | ConferimentoSede | Davide |

> **Nota:** AMAServiceRegister è equivalente a UserRegistry per le operazioni di dominio. Nel Refined si può unificare o separare.

---

### 3.13 UserFactory
**Stereotipo:** `<<control>>` (factory)

| Operazione | Parametri | Ritorno | Fonte SD |
|------------|-----------|---------|----------|
| createUserByRole(role, userData) | role: String, userData | UtenteSistema | Davide |

---

## 4. RELAZIONI

### 4.1 Generalizzazioni (ereditarietà)
| Superclasse | Sottoclasse |
|-------------|-------------|
| UtenteSistema | Cittadino |
| UtenteSistema | LavoratoreAMA |
| UtenteSistema | AmministratoreSedeAMA |
| UtenteSistema | AmministratoreGeneraleAMA |
| LavoratoreAMA | AutistaAMA |
| LavoratoreAMA | OperatoreSedeAMA |
| Prenotazione | RitiroDomicilio |
| Prenotazione | ConferimentoSede |

### 4.2 Associazioni
| Classe A | Classe B | Molteplicità A | Molteplicità B | Note |
|----------|----------|----------------|----------------|------|
| Cittadino | Prenotazione | 1 | 0..* | Un cittadino può avere molte prenotazioni |
| Prenotazione | Rifiuto | 1..1 | 1..1 | Ogni prenotazione riguarda esattamente un rifiuto |
| Prenotazione | Valutazione | 1 | 0..1 | Una prenotazione può avere al più una valutazione |
| Rifiuto | TipologiaRifiuto | 0..* | 1..1 | Ogni rifiuto ha una tipologia |
| RitiroDomicilio | AutistaAMA | 0..* | 1..1 | Ogni ritiro è assegnato a un autista |
| AutistaAMA | Veicolo | 0..* | 1..1 | Un autista usa un veicolo |
| ConferimentoSede | SedeAMA | 0..* | 1..1 | Ogni conferimento è presso una sede |
| OperatoreSedeAMA | SedeAMA | 1..* | 1..1 | Più operatori presso una sede |
| AmministratoreSedeAMA | CodiceInvito | 1..1 | 1..* | Un admin gestisce i codici invito |
| LavoratoreAMA | Disponibilita | 0..* | 0..* | Lavoratori hanno disponibilità |
| Veicolo | Disponibilita | 0..* | 0..* | Veicoli hanno disponibilità |
| SedeAMA | ZonaCAP | 1..* | 0..* | Sedi servono zone CAP |
| RitiroDomicilio | Assegnazione | 1..1 | 0..* | Un ritiro ha assegnazioni |
| Assegnazione | AutistaAMA | 0..* | 1..1 | Assegnazione a un autista |

### 4.3 Dipendenze (Boundary → Control → Entity — pattern BCE)
| Boundary | Control |
|----------|---------|
| RegistrationInterface | UserAccessEndpoint |
| InvitationRegistrationInterface | UserAccessEndpoint |
| LoginInterface | UserAccessEndpoint |
| HomeBookInterface | AMAServiceController |
| WasteDisposalInterface | AMAServiceController |
| BookingHistory | AMAServiceController |
| PannelloAutistaUI | GestoreRitiriController |
| PannelloAutistaUI | GestoreEsitoController |
| PannelloAutistaUI | ContattoController |
| PannelloSedeUI | GestioneSedeController |
| ControlloVarcoUI | AccettazioneController |
| GestioneConferimentoUI | GestioneConferimentoController |
| GestioneCodiciUI | CodiciController |
| GestionePersonaleUI | GestionePersonaleController |
| GestioneSedeUI | GestioneSedeController |
| GestioneVeicoliUI | GestioneVeicoliController |

| Control | Entity |
|---------|--------|
| UserAccessEndpoint | UtenteSistema, Cittadino, LavoratoreAMA |
| UserRegistry | UtenteSistema, Cittadino, Prenotazione, Valutazione, RitiroDomicilio, ConferimentoSede |
| UserFactory | UtenteSistema, Cittadino |
| AMAServiceController | Prenotazione, RitiroDomicilio, ConferimentoSede, Valutazione |
| GestoreRitiriController | AutistaAMA, Prenotazione, Assegnazione |
| GestoreEsitoController | Prenotazione, RitiroDomicilio |
| ContattoController | Cittadino |
| CodiciController | AmministratoreGeneraleAMA, CodiceInvito |
| GestioneSedeController | SedeAMA, Prenotazione, Disponibilita, ZonaCAP |
| AccettazioneController | Prenotazione, OperatoreSedeAMA |
| GestioneConferimentoController | Prenotazione |
| GestionePersonaleController | LavoratoreAMA, CodiceInvito, AmministratoreSedeAMA, Disponibilita |
| GestioneVeicoliController | Veicolo, SedeAMA, Disponibilita, AmministratoreSedeAMA |

---

## 5. RIEPILOGO CLASSI TOTALI

| # | Classe | Stereotipo | Tipo |
|---|--------|------------|------|
| 1 | UtenteSistema | entity | abstract |
| 2 | Cittadino | entity | |
| 3 | LavoratoreAMA | entity | abstract |
| 4 | AutistaAMA | entity | |
| 5 | OperatoreSedeAMA | entity | |
| 6 | AmministratoreSedeAMA | entity | |
| 7 | AmministratoreGeneraleAMA | entity | |
| 8 | Prenotazione | entity | abstract |
| 9 | RitiroDomicilio | entity | |
| 10 | ConferimentoSede | entity | |
| 11 | Valutazione | entity | |
| 12 | Rifiuto | entity | |
| 13 | TipologiaRifiuto | entity | |
| 14 | SedeAMA | entity | |
| 15 | Veicolo | entity | |
| 16 | Disponibilita | entity | |
| 17 | CodiceInvito | entity | |
| 18 | ZonaCAP | entity | **NUOVA** |
| 19 | Assegnazione | entity | **NUOVA** |
| 20 | RegistrationInterface | boundary | |
| 21 | InvitationRegistrationInterface | boundary | |
| 22 | LoginInterface | boundary | |
| 23 | HomeBookInterface | boundary | |
| 24 | WasteDisposalInterface | boundary | |
| 25 | BookingHistory | boundary | |
| 26 | PannelloAutistaUI | boundary | |
| 27 | PannelloSedeUI | boundary | |
| 28 | ControlloVarcoUI | boundary | |
| 29 | GestioneConferimentoUI | boundary | |
| 30 | GestioneCodiciUI | boundary | |
| 31 | GestionePersonaleUI | boundary | |
| 32 | GestioneSedeUI | boundary | |
| 33 | GestioneVeicoliUI | boundary | |
| 34 | UserAccessEndpoint | control | |
| 35 | AMAServiceController | control | |
| 36 | GestoreRitiriController | control | |
| 37 | GestoreEsitoController | control | |
| 38 | ContattoController | control | |
| 39 | CodiciController | control | |
| 40 | GestioneSedeController | control | |
| 41 | AccettazioneController | control | |
| 42 | GestioneConferimentoController | control | |
| 43 | GestionePersonaleController | control | |
| 44 | GestioneVeicoliController | control | |
| 45 | UserRegistry | control/service | |
| 46 | UserFactory | control/factory | |

**Totale: 46 classi** (19 Entity + 14 Boundary + 13 Control)
