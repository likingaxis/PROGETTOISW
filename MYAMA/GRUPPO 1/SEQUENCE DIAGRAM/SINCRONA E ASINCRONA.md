Sì. Nei sequence diagram di MyAma puoi usare questa regola:

- **Sincrona**: il mittente aspetta che il destinatario finisca l’operazione prima di continuare.
    
- **Asincrona**: il mittente invia il messaggio e può continuare senza aspettare.
    

Nel vostro progetto, **quasi tutti i messaggi sono sincroni**. Le chiamate asincrone hanno senso soprattutto per notifiche o comunicazioni esterne.

Ti riscrivo i messaggi principali con il tipo.

## 1. Registrarsi come cittadino

|Messaggio|Metodo|Classe|Tipo|
|---|---|---|---|
|`richiediRegistrazione()`|—|Interfaccia|Sincrona|
|`inserisciDatiPersonali(dati)`|`registrati(dati)`|`Cittadino`|Sincrona|
|`verificaEmail(email)`|`verificaEmail(email)`|`UtenteSistema`|Sincrona|
|`creaAccount(dati)`|`registrati(dati)`|`Cittadino`|Sincrona|
|`confermaRegistrazione()`|—|Interfaccia|Sincrona|

## 2. Registrarsi tramite codice invito

|Messaggio|Metodo|Classe|Tipo|
|---|---|---|---|
|`inserisciCodiceInvito(codice)`|—|Interfaccia|Sincrona|
|`verificaCodice(codice)`|`verificaValidita()`|`CodiceInvito`|Sincrona|
|`creaAccountLavoratore()`|`registratiConCodiceInvito()`|`LavoratoreAMA`|Sincrona|
|`marcaCodiceUtilizzato()`|`utilizza()`|`CodiceInvito`|Sincrona|

## 3. Effettuare accesso

|Messaggio|Metodo|Classe|Tipo|
|---|---|---|---|
|`inserisciCredenziali(email,password)`|`effettuaAccesso()`|`UtenteSistema`|Sincrona|
|`verificaCredenziali()`|`effettuaAccesso()`|`UtenteSistema`|Sincrona|
|`verificaAccountAbilitato()`|`isAbilitato()`|`UtenteSistema`|Sincrona|
|`accessoConsentito()`|—|Interfaccia|Sincrona|

## 4. Richiedere ritiro a domicilio

|Messaggio|Metodo|Classe|Tipo|
|---|---|---|---|
|`richiediRitiro()`|`richiediRitiro()`|`Cittadino`|Sincrona|
|`creaRifiuto(...)`|`creaRifiuto(...)`|`Rifiuto`|Sincrona|
|`aggiungiFoto(foto)`|`aggiungiFoto(foto)`|`Rifiuto`|Sincrona|
|`verificaCAP(cap)`|`verificaCAP(cap)`|`ZonaCAP`|Sincrona|
|`cercaDisponibilita()`|`verificaDisponibilita()`|`Disponibilita`|Sincrona|
|`prenotaSlot()`|`prenotaSlot()`|`Disponibilita`|Sincrona|
|`creaPrenotazione()`|`creaPrenotazione()`|`Prenotazione`|Sincrona|
|`creaRitiro()`|`creaRitiro()`|`RitiroDomicilio`|Sincrona|
|`inviaConfermaPrenotazione()`|eventuale metodo notifica|Sistema notifiche|**Asincrona**|

L'ultima può essere asincrona perché il sistema può salvare la prenotazione e poi inviare la notifica senza bloccare il processo.

## 5. Prenotare conferimento presso sede

|Messaggio|Metodo|Classe|Tipo|
|---|---|---|---|
|`prenotaConferimento()`|`prenotaConferimento()`|`Cittadino`|Sincrona|
|`creaRifiuto()`|`creaRifiuto()`|`Rifiuto`|Sincrona|
|`getSediCompatibili()`|`getSediCompatibili()`|`ZonaCAP`|Sincrona|
|`verificaCompatibilita()`|`verificaCompatibilita()`|`SedeAMA`|Sincrona|
|`verificaDisponibilita()`|`verificaDisponibilita()`|`Disponibilita`|Sincrona|
|`prenotaSlot()`|`prenotaSlot()`|`Disponibilita`|Sincrona|
|`creaPrenotazione()`|`creaPrenotazione()`|`Prenotazione`|Sincrona|
|`creaConferimento()`|`creaConferimento()`|`ConferimentoSede`|Sincrona|
|`inviaConferma()`|—|Sistema notifiche|**Asincrona**|

## 6. Visualizzare sedi compatibili

Tutti sincroni:

- `verificaCAP()`
    
- `getSediCompatibili()`
    
- `verificaCompatibilita()`
    
- `mostraSedi()`
    

Perché il cittadino aspetta il risultato prima di poter scegliere.

## 7. Visualizzare date e fasce

Tutti sincroni:

- `richiediDisponibilita()`
    
- `verificaDisponibilita()`
    
- `getFasceDisponibili()`
    
- `mostraFasce()`
    

## 8. Visualizzare prenotazioni attive

Tutti sincroni:

- `richiediPrenotazioniAttive()`
    
- `recuperaPrenotazioni()`
    
- `getDettagli()`
    
- `mostraDettagli()`
    

## 9. Annullare prenotazione

|Messaggio|Tipo|
|---|---|
|`richiediAnnullamento()`|Sincrona|
|`annulla()`|Sincrona|
|`liberaSlot()`|Sincrona|
|`modificaStato()`|Sincrona|
|`inviaNotificaAnnullamento()`|**Asincrona**|

## 10. Consultare storico

Tutti sincroni:

- `richiediStorico()`
    
- `recuperaPrenotazioniConcluse()`
    
- `getDettagli()`
    

## 11. Valutare servizio

Tutti sincroni:

- `selezionaPrenotazione()`
    
- `inserisciValutazione()`
    
- `creaValutazione()`
    

Un'eventuale:

`inviaConfermaValutazione()`

può essere asincrona, ma non è necessaria.

## 12. Visualizzare ritiri assegnati

Tutti sincroni:

- `richiediRitiriAssegnati()`
    
- `recuperaAssegnazioni()`
    
- `consultaDettagliRitiro()`
    
- `getDettagli()`
    

## 13. Registrare esito ritiro

|Messaggio|Tipo|
|---|---|
|`selezionaRitiro()`|Sincrona|
|`registraEsitoRitiro()`|Sincrona|
|`registraEsito()`|Sincrona|
|`modificaStato()`|Sincrona|
|`inviaNotificaEsito()`|**Asincrona**|

Qui l'asincrona ha molto senso: dopo aver salvato l'esito, il sistema può notificare il cittadino.

## 14. Chiamare cittadino

Qui farei attenzione.

- `consultaDettagliRitiro()` → Sincrona
    
- `recuperaRecapito()` → Sincrona
    
- `avviaChiamata()` → **Asincrona**
    

La chiamata telefonica non è un'operazione interna che deve terminare prima che il sistema possa fare altro.

## 15. Visualizzare prenotazioni della sede

Tutti sincroni:

- `richiediPrenotazioniSede()`
    
- `recuperaPrenotazioni()`
    
- `consultaDettagliConferimento()`
    
- `getDettagli()`
    

## 16. Verificare prenotazione

Tutti sincroni:

- `inserisciIdPrenotazione()`
    
- `verificaPrenotazione()`
    
- `cercaPrenotazione()`
    
- `verificaStato()`
    
- `prenotazioneValida()`
    

L'operatore deve aspettare l'esito della verifica.

## 17. Registrare esito conferimento

|Messaggio|Tipo|
|---|---|
|`selezionaConferimento()`|Sincrona|
|`registraEsitoConferimento()`|Sincrona|
|`registraEsito()`|Sincrona|
|`modificaStato()`|Sincrona|
|`inviaNotificaEsito()`|**Asincrona**|

### In pratica, su Visual Paradigm

Per MyAma userei:

**Freccia sincrona** per:  
`verifica...()`, `crea...()`, `recupera...()`, `modifica...()`, `annulla()`, `registra...()`, `get...()`.

Sono operazioni necessarie per continuare il flusso.

**Freccia asincrona** soprattutto per:  
`inviaNotifica()`, `inviaConferma()`, `inviaNotificaEsito()`, `inviaNotificaAnnullamento()`, `avviaChiamata()`.

Quindi non devi cercare di mettere chiamate asincrone per forza. Nel vostro progetto è del tutto normale avere un sequence diagram composto quasi interamente da **chiamate sincrone**. Il `project.xml` conferma che il dominio è basato soprattutto su operazioni di prenotazione, disponibilità, assegnazione ed esito.