
## Attori

Gli attori attualmente individuati sono:

- **cittadino**, che utilizza il sistema per richiedere il servizio;
- **utente registrato**, figura ancora da valutare in relazione alle modalità di accesso al sistema;
- **autista AMA**, coinvolto nell'esecuzione dei ritiri a domicilio;
- **impiegato / operatore AMA**, coinvolto nella gestione dei conferimenti presso le sedi;
- **amministratore AMA**, il cui ruolo operativo dovrà essere definito con maggiore precisione nelle fasi successive.

Anche la modalità di registrazione o autenticazione dell'utente non viene definita in questa fase. È sufficiente stabilire l'eventuale necessità di identificare il cittadino, senza entrare per ora nella scelta della tecnologia utilizzata.

---

## Funzionalità principali
Le funzionalità principali individuate riguardano innanzitutto la possibilità per il cittadino di prenotare lo smaltimento di un rifiuto ingombrante.

Il sistema deve permettere di scegliere tra **ritiro a domicilio** e **conferimento presso una sede AMA**, inserendo le informazioni relative al rifiuto e indicando l'indirizzo, la zona o il CAP di riferimento.

Sulla base di queste informazioni, MyAma deve verificare quali servizi siano effettivamente compatibili con la richiesta. Nel caso del conferimento, il sistema deve individuare le sedi AMA compatibili con la zona del cittadino; in entrambi i casi deve mostrare soltanto date e fasce orarie realmente disponibili.

Una volta individuata una possibilità valida, il cittadino deve poter creare la prenotazione e, quando consentito, modificarla oppure annullarla.

Dal lato AMA, il sistema deve supportare l'organizzazione delle risorse necessarie all'esecuzione del servizio. Deve quindi gestire la disponibilità dei lavoratori e dei veicoli e permettere l'assegnazione del personale e dei mezzi ai ritiri in base al **ruolo**, alla **disponibilità** e alla **capacità del veicolo**.

Il sistema deve inoltre supportare le attività dell'autista AMA e dell'operatore della sede AMA e deve consentire la registrazione dell'esito del servizio. La prenotazione deve avere uno stato che permetta di distinguere, almeno, tra un servizio **completato**, **annullato** o **non eseguito**.

L'invio di **notifiche al cittadino** è considerato utile, ma deve ancora essere valutato nel dettaglio prima di essere confermato come funzionalità principale.

---

## Funzionalità secondarie / candidate

Sono state individuate anche alcune funzionalità che potrebbero essere utili, ma che non vengono considerate obbligatorie in questa fase.

Tra queste rientrano:

- caricamento di una **foto del rifiuto**;
- calcolo di un eventuale **costo del servizio**, che potrebbe successivamente essere promosso a funzionalità principale;
- gestione dello **storico delle prenotazioni**;
- possibilità di lasciare una **valutazione del servizio**;
- eventuali funzionalità aggiuntive relative alla **gestione operativa AMA**, ancora da definire.

Queste funzionalità restano quindi candidate e non devono essere trattate come requisiti certi finché il gruppo non ne approva formalmente l'inclusione.

---

## Cosa rientra nello scope

Rientra nello scope di MyAma tutto ciò che è direttamente necessario per gestire il seguente processo:

**richiesta del cittadino → prenotazione → organizzazione AMA → esecuzione del servizio → registrazione dell'esito.**

Il perimetro comprende quindi:

- gestione dei rifiuti ingombranti;
- gestione delle richieste del cittadino;
- ritiro a domicilio;
- conferimento presso una sede AMA;
- sedi AMA disponibili nella zona del cittadino;
- CAP e zone servite;
- disponibilità temporali;
- prenotazioni;
- lavoratori AMA coinvolti nel servizio;
- autisti;
- operatori di sede;
- veicoli;
- capacità dei veicoli;
- assegnazione delle risorse;
- controllo della disponibilità delle risorse;
- esecuzione del ritiro;
- esecuzione del conferimento;
- stato ed esito della prenotazione.

Il sistema non deve quindi limitarsi alla sola prenotazione lato cittadino, ma deve consentire ad AMA di organizzare le risorse necessarie per soddisfare correttamente la richiesta.

---

## Cosa resta fuori scope per ora

Restano fuori dallo scope tutte le funzionalità interne ad AMA che non sono direttamente necessarie alla gestione dello smaltimento dei rifiuti ingombranti.

In particolare, non rientrano per ora nel progetto:

- gestione interna completa dei dipendenti AMA, come stipendi, contratti e altri aspett;
- gestione generale dei mezzi, come acquisti, manutenzione o navigazione GPS;
- gestione generale di tutti i servizi AMA;
- gestione di tutti i tipi di rifiuti;
- gestione delle discariche o degli impianti di trattamento;
- gestione completa della raccolta urbana;
- gestione amministrativa generale dei cittadini;
- qualsiasi altra funzionalità non direttamente collegata alla prenotazione e all'esecuzione del servizio MyAma.

Non rientrano inoltre nello scope funzionale di questa fase le decisioni tecniche e progettuali, come:

- database da utilizzare;
- linguaggio di programmazione;
- framework;
- architettura software;
- Design Pattern;
- struttura delle classi;
- API;
- tecnologie di autenticazione.

Questi aspetti verranno affrontati nelle fasi successive del progetto.

---

## Riassunto principale

| Stato          | Funzionalità                  |
| -------------- | ----------------------------- |
| 🟢 IN          | Ritiro a domicilio            |
| 🟢 IN          | Conferimento in sede          |
| 🟢 IN          | Gestione prenotazione         |
| 🟢 IN          | Compatibilità CAP/zona        |
| 🟢 IN          | Gestione disponibilità        |
| 🟢 IN          | Assegnazione risorse          |
| 🟢 IN          | Gestione veicolo/capacità     |
| 🟢 IN          | Registrazione esito           |
| 🟡 DA DECIDERE | Foto del rifiuto              |
| 🟡 DA DECIDERE | Costo                         |
| 🟡 DA DECIDERE | Notifiche (opterei come IN)   |
| 🟡 DA DECIDERE | Storico                       |
| 🟡 DA DECIDERE | Valutazioni                   |
| 🟡 DA DECIDERE | Statistiche/report            |
| 🟡 DA DECIDERE | Registrazione utente          |
| 🔴 OUT         | Contabilità AMA               |
| 🔴 OUT         | Stipendi                      |
| 🔴 OUT         | Manutenzione mezzi            |
| 🔴 OUT         | Gestione interna AMA completa |

### Riassunto del perimetro

Il concetto centrale può essere espresso così:

> **MyAma deve permettere al cittadino di richiedere lo smaltimento di un rifiuto ingombrante, tramite ritiro a domicilio o conferimento presso una sede AMA, e deve permettere ad AMA di organizzare le risorse necessarie per eseguire correttamente il servizio.**

---

## Checklist di revisione

- [ ] Si capisce qual è il problema che MyAma vuole risolvere?
- [ ] Sono presenti **ritiro a domicilio** e **conferimento in sede**?
- [ ] È presente il cittadino?
- [ ] È presente l'autista?
- [ ] È presente l'operatore di sede?
- [ ] È presente l'organizzazione delle risorse AMA?
- [ ] Si parla di sedi e CAP/zone?
- [ ] Si parla delle disponibilità?
- [ ] Si considerano lavoratori e veicoli?
- [ ] È chiaro che il veicolo deve essere adeguato al rifiuto/carico?
- [ ] È prevista la registrazione dell'esito?
- [ ] Il cittadino vede solo opzioni compatibili con la propria zona?
- [ ] Sono state introdotte funzioni non presenti in `idea.md`?
- [ ] Le funzioni “da valutare” sono state trattate erroneamente come certe?
- [ ] Sono state introdotte tecnologie, database o pattern prematuramente?
- [ ] Il progetto è rimasto focalizzato sullo **smaltimento dei rifiuti ingombranti**?
