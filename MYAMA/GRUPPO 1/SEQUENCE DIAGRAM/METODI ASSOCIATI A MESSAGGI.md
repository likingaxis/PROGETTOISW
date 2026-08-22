Certo. Ti conviene organizzarlo così: **Sequence Diagram → Messaggio → Metodo della classe associato**.

Quando il messaggio è solo di interfaccia, tipo `mostraForm()`, non lo considero un metodo del dominio.

## 1. Registrarsi come cittadino

|Messaggio|Metodo associato|Classe|
|---|---|---|
|`richiediRegistrazione()`|—|Interfaccia|
|`inserisciDatiPersonali(dati)`|`registrati(datiPersonali)`|`Cittadino`|
|`verificaEmail(email)`|`verificaEmail(email)`|`UtenteSistema`|
|`creaAccount(dati)`|`registrati(datiPersonali)`|`Cittadino`|
|`confermaRegistrazione()`|—|Interfaccia|

Metodi coinvolti:

- `Cittadino.registrati(datiPersonali)`
    
- `UtenteSistema.verificaEmail(email)`
    

---

## 2. Registrarsi tramite codice invito

|Messaggio|Metodo associato|Classe|
|---|---|---|
|`inserisciCodiceInvito(codice)`|`verificaValidita()`|`CodiceInvito`|
|`verificaCodice(codice)`|`verificaValidita()`|`CodiceInvito`|
|`inserisciDatiLavoratore(dati)`|`registratiConCodiceInvito(codice)`|`LavoratoreAMA`|
|`creaAccountLavoratore()`|`registratiConCodiceInvito(codice)`|`LavoratoreAMA`|
|`marcaCodiceUtilizzato()`|`utilizza()`|`CodiceInvito`|

Metodi:

- `CodiceInvito.verificaValidita()`
    
- `CodiceInvito.utilizza()`
    
- `LavoratoreAMA.registratiConCodiceInvito(codice)`
    

---

## 3. Effettuare accesso

|Messaggio|Metodo associato|Classe|
|---|---|---|
|`inserisciCredenziali(email,password)`|`effettuaAccesso(email,password)`|`UtenteSistema`|
|`verificaCredenziali()`|`effettuaAccesso(email,password)`|`UtenteSistema`|
|`verificaAccountAbilitato()`|`isAbilitato()`|`UtenteSistema`|
|`accessoConsentito()`|—|Interfaccia|
|`mostraErroreAccesso()`|—|Interfaccia|

Metodi:

- `UtenteSistema.effettuaAccesso(email,password)`
    
- `UtenteSistema.isAbilitato()`
    

---

# 4. Richiedere ritiro a domicilio

|Messaggio|Metodo associato|Classe|
|---|---|---|
|`richiediRitiro()`|`richiediRitiro()`|`Cittadino`|
|`inserisciDatiRifiuto(...)`|`creaRifiuto(...)`|`Rifiuto`|
|`caricaFoto(foto)`|`aggiungiFoto(foto)`|`Rifiuto`|
|`inserisciIndirizzo(indirizzo,CAP)`|`impostaIndirizzoRitiro(indirizzo)`|`RitiroDomicilio`|
|`verificaCAP(cap)`|`verificaCAP(cap)`|`ZonaCAP`|
|`cercaDisponibilita(...)`|`verificaDisponibilita(...)`|`Disponibilita`|
|`selezionaDisponibilita(...)`|`prenotaSlot()`|`Disponibilita`|
|`confermaPrenotazione()`|`creaPrenotazione()`|`Prenotazione`|
|`creaRitiro()`|`creaRitiro(indirizzo)`|`RitiroDomicilio`|

Metodi:

- `Cittadino.richiediRitiro()`
    
- `Rifiuto.creaRifiuto(...)`
    
- `Rifiuto.aggiungiFoto(foto)`
    
- `RitiroDomicilio.impostaIndirizzoRitiro(indirizzo)`
    
- `ZonaCAP.verificaCAP(cap)`
    
- `Disponibilita.verificaDisponibilita(...)`
    
- `Disponibilita.prenotaSlot()`
    
- `Prenotazione.creaPrenotazione()`
    
- `RitiroDomicilio.creaRitiro(indirizzo)`
    

---

# 5. Prenotare conferimento presso sede AMA

|Messaggio|Metodo associato|Classe|
|---|---|---|
|`prenotaConferimento()`|`prenotaConferimento()`|`Cittadino`|
|`inserisciDatiRifiuto()`|`creaRifiuto()`|`Rifiuto`|
|`cercaSediCompatibili()`|`getSediCompatibili()`|`ZonaCAP`|
|`verificaCompatibilita()`|`verificaCompatibilita(...)`|`SedeAMA`|
|`richiediDisponibilita()`|`visualizzaDisponibilita()`|`SedeAMA`|
|`verificaDisponibilita()`|`verificaDisponibilita(...)`|`Disponibilita`|
|`selezionaSlot()`|`prenotaSlot()`|`Disponibilita`|
|`creaPrenotazione()`|`creaPrenotazione()`|`Prenotazione`|
|`creaConferimento()`|`creaConferimento(sede)`|`ConferimentoSede`|

---

# 6. Visualizzare sedi compatibili

|Messaggio|Metodo associato|Classe|
|---|---|---|
|`inserisciCAP(cap)`|`verificaCAP(cap)`|`ZonaCAP`|
|`richiediSediCompatibili()`|`getSediCompatibili()`|`ZonaCAP`|
|`verificaCompatibilita(rifiuto)`|`verificaCompatibilita(...)`|`SedeAMA`|
|`mostraSedi()`|—|Interfaccia|

Metodi:

- `ZonaCAP.verificaCAP(cap)`
    
- `ZonaCAP.getSediCompatibili()`
    
- `SedeAMA.verificaCompatibilita(...)`
    

---

# 7. Visualizzare date e fasce disponibili

|Messaggio|Metodo associato|Classe|
|---|---|---|
|`richiediDisponibilita()`|`visualizzaDisponibilita()`|`SedeAMA`|
|`cercaDisponibilita(data)`|`verificaDisponibilita(...)`|`Disponibilita`|
|`ottieniFasceDisponibili()`|`getFasceDisponibili()`|`Disponibilita`|
|`mostraFasce()`|—|Interfaccia|

---

# 8. Visualizzare prenotazioni attive

|Messaggio|Metodo associato|Classe|
|---|---|---|
|`richiediPrenotazioniAttive()`|`visualizzaPrenotazioniAttive()`|`Cittadino`|
|`recuperaPrenotazioni()`|`getDettagli()`|`Prenotazione`|
|`selezionaPrenotazione(id)`|`getDettagli()`|`Prenotazione`|
|`mostraDettagli()`|—|Interfaccia|

---

# 9. Annullare prenotazione

|Messaggio|Metodo associato|Classe|
|---|---|---|
|`selezionaPrenotazione(id)`|`getDettagli()`|`Prenotazione`|
|`richiediAnnullamento()`|`annullaPrenotazione(id)`|`Cittadino`|
|`annulla()`|`annulla()`|`Prenotazione`|
|`liberaDisponibilita()`|`liberaSlot()`|`Disponibilita`|
|`aggiornaStato()`|`modificaStato(stato)`|`Prenotazione`|

---

# 10. Consultare storico prenotazioni

|Messaggio|Metodo associato|Classe|
|---|---|---|
|`richiediStorico()`|`consultaStoricoPrenotazioni()`|`Cittadino`|
|`recuperaPrenotazioniConcluse()`|`getDettagli()`|`Prenotazione`|
|`selezionaPrenotazione()`|`getDettagli()`|`Prenotazione`|

---

# 11. Valutare il servizio

|Messaggio|Metodo associato|Classe|
|---|---|---|
|`selezionaPrenotazione()`|`getDettagli()`|`Prenotazione`|
|`inserisciValutazione(voto,commento)`|`valutaServizio(...)`|`Cittadino`|
|`creaValutazione(voto,commento)`|`creaValutazione(...)`|`Valutazione`|

---

# 12. Visualizzare ritiri assegnati / dettagli

|Messaggio|Metodo associato|Classe|
|---|---|---|
|`richiediRitiriAssegnati()`|`visualizzaRitiriAssegnati()`|`AutistaAMA`|
|`recuperaAssegnazioni()`|`getDettagliAssegnazione()`|`Assegnazione`|
|`selezionaRitiro(id)`|`consultaDettagliRitiro(id)`|`AutistaAMA`|
|`recuperaDettagliRitiro()`|`getDettagli()`|`Prenotazione`|

---

# 13. Registrare esito ritiro

|Messaggio|Metodo associato|Classe|
|---|---|---|
|`selezionaRitiro(id)`|`consultaDettagliRitiro(id)`|`AutistaAMA`|
|`inserisciEsito(esito)`|`registraEsitoRitiro(id,esito)`|`AutistaAMA`|
|`registraEsito(esito)`|`registraEsito(esito)`|`RitiroDomicilio`|
|`aggiornaStato()`|`modificaStato(stato)`|`Prenotazione`|

---

# 14. Chiamare cittadino

|Messaggio|Metodo associato|Classe|
|---|---|---|
|`selezionaRitiro()`|`consultaDettagliRitiro(id)`|`AutistaAMA`|
|`richiediContattoCittadino()`|`chiamaCittadino(idCittadino)`|`AutistaAMA`|
|`recuperaRecapito()`|eventualmente `getDettagli()`|`Cittadino`|
|`avviaChiamata()`|—|Sistema esterno/telefono|

Qui eviterei di mettere un vero `avviaChiamata()` dentro una classe del dominio.

---

# 15. Visualizzare prenotazioni della sede / dettagli

|Messaggio|Metodo associato|Classe|
|---|---|---|
|`richiediPrenotazioniSede()`|`visualizzaPrenotazioniSede()`|`OperatoreSedeAMA`|
|`recuperaPrenotazioni()`|`getDettagli()`|`Prenotazione`|
|`selezionaConferimento(id)`|`consultaDettagliConferimento(id)`|`OperatoreSedeAMA`|
|`recuperaDettagli()`|`getDettagli()`|`Prenotazione`|

---

# 16. Verificare prenotazione

|Messaggio|Metodo associato|Classe|
|---|---|---|
|`inserisciIdPrenotazione(id)`|`verificaPrenotazione(id)`|`OperatoreSedeAMA`|
|`cercaPrenotazione(id)`|`getDettagli()`|`Prenotazione`|
|`verificaStato()`|`getDettagli()` oppure `verificaStato()`|`Prenotazione`|
|`prenotazioneValida()`|—|Ritorno|

Io qui aggiungerei a `Prenotazione`:

- `verificaStato()`
    

perché emerge chiaramente dal sequence.

---

# 17. Registrare esito conferimento

|Messaggio|Metodo associato|Classe|
|---|---|---|
|`selezionaConferimento(id)`|`consultaDettagliConferimento(id)`|`OperatoreSedeAMA`|
|`inserisciEsito(esito)`|`registraEsitoConferimento(id,esito)`|`OperatoreSedeAMA`|
|`registraEsito(esito)`|`registraEsito(esito)`|`ConferimentoSede`|
|`aggiornaStato()`|`modificaStato(stato)`|`Prenotazione`|

---

## La distinzione più importante

Nel sequence puoi avere:

```text
Cittadino → Sistema: confermaPrenotazione()
```

ma questo **non significa necessariamente** che `Cittadino` debba avere:

```text
+ confermaPrenotazione()
```

Il vero metodo del dominio potrebbe essere:

```text
Prenotazione.creaPrenotazione()
```

Quindi:

**Messaggio dell'attore**  
`confermaPrenotazione()`

↓

**Sistema elabora**

↓

**Metodo della classe**  
`Prenotazione.creaPrenotazione()`

Questo è il collegamento che devi usare quando passerai dal **sequence diagram al refined class diagram**.