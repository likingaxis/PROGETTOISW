## Attori
- cittadino
- FORSE UTENTE REGISTRATO
- autista ama
- impiegato ama 
- amministratore ama

## Funzionalità principali
- FORSE REGISTRAZIONE CON EMAIL E PASSWORD / SPID
- Prenotazione del **ritiro a domicilio** di rifiuti ingombranti.
- Prenotazione del **conferimento presso una sede AMA**.
- Inserimento delle informazioni relative al **rifiuto da smaltire**.
- Indicazione dell'**indirizzo, zona o CAP** del cittadino.
- Verifica della compatibilità tra **zona del cittadino e servizio disponibile**.
- Individuazione delle **sedi AMA compatibili** con la zona del cittadino.
- Visualizzazione delle **date e fasce orarie disponibili**.
- Creazione della **prenotazione**.
- Modifica o annullamento della prenotazione, quando consentito.
- Organizzazione delle **risorse AMA** necessarie per il servizio.
- Gestione della disponibilità dei **lavoratori AMA**.
- Assegnazione del personale e dei veicoli ai ritiri, in base a ruolo, disponibilità e capacità del mezzo.
- Gestione dei **veicoli AMA**.
- Verifica della capacità del veicolo rispetto al ritiro da effettuare.
- Gestione delle attività dell'**autista AMA**.
- Gestione delle attività dell'**operatore della sede AMA**.
- Registrazione dell'**esito del servizio**.
- Gestione dello **stato della prenotazione**, distinguendo almeno tra servizio completato, annullato o non eseguito.
- Mostrare al cittadino soltanto servizi e disponibilità **realmente compatibili** con la sua richiesta.
- Invio di **notifiche** al cittadino. (DA VEDERE BENE)


## Funzionalità secondarie / candidate
Queste sono funzionalità presenti nell'idea, ma che **non risultano ancora definite come obbligatorie**.

- Caricamento di una **foto del rifiuto**.
    
- Calcolo di un eventuale **costo del servizio**. (FORSE PRIMARIA)
    
- Gestione dello **storico delle prenotazioni**.
    
- Possibilità di lasciare una **valutazione del servizio**.
    
- Eventuali funzionalità aggiuntive della **gestione operativa AMA**, da definire meglio.

Queste non dovrebbero essere presentate come requisiti certi finché il gruppo non decide di includerle.


---

## Cosa rientra nello scope
Rientra nello scope tutto ciò che serve a gestire il processo:

**richiesta del cittadino → prenotazione → organizzazione AMA → esecuzione del servizio → registrazione dell'esito.**

In particolare:
- gestione dei rifiuti ingombranti;
- cittadino e sue richieste;
- ritiro a domicilio;
- conferimento presso sede;
- sedi AMA;
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

Il sistema quindi non deve occuparsi solo della prenotazione lato cittadino.
Deve anche permettere ad AMA di **organizzare le risorse necessarie per soddisfare la richiesta**.

---

## Cosa resta fuori scope per ora
Per ora lascerei fuori tutte le funzionalità che riguardano AMA ma che non sono necessarie alla gestione dello smaltimento degli ingombranti.

Quindi:
- gestione interna dei dipendenti ama (inteso come stipendi, contratti, ecc.)
- gestione generale dei mezzi (nuovi acquisti, manutenzione, navigazione gps, ecc.)
- gestione generale di tutti i servizi AMA;
- gestione di tutti i tipi di rifiuti;
- gestione delle discariche o degli impianti di trattamento;
- gestione completa della raccolta urbana;
- gestione amministrativa generale dei cittadini;
- qualunque funzionalità non direttamente collegata al processo di prenotazione ed esecuzione del servizio MyAma.

Inoltre, **per ora non fanno parte dello scope funzionale** neanche decisioni tecniche come:
- database da utilizzare;
- linguaggio di programmazione;
- framework;
- architettura software;
- Design Pattern;
- struttura delle classi;
- API;
- tecnologie di autenticazione.

Queste verranno affrontate nelle fasi successive.


## Riassunto principale

| Stato          | Funzionalità              |
| -------------- | ------------------------- |
| 🟢 IN          | Ritiro a domicilio        |
| 🟢 IN          | Conferimento in sede      |
| 🟢 IN          | Gestione prenotazione     |
| 🟢 IN          | Compatibilità CAP/zona    |
| 🟢 IN          | Gestione disponibilità    |
| 🟢 IN          | Assegnazione risorse      |
| 🟢 IN          | Gestione veicolo/capacità |
| 🟢 IN          | Registrazione esito       |
| 🟡 DA DECIDERE | Foto del rifiuto          |
| 🟡 DA DECIDERE | Costo                     |
| 🟡 DA DECIDERE | Notifiche                 |
| 🟡 DA DECIDERE | Storico                   |
| 🟡 DA DECIDERE | Valutazioni               |
| 🟡 DA DECIDERE | Statistiche/report        |
| 🟡 DA DECIDERE | Registrazione utente      |
| 🔴 OUT         | Contabilità AMA           |
| 🔴 OUT         | Stipendi                  |
| 🔴 OUT         | Manutenzione mezzi        |
| 🔴 OUT         | Gestione HR completa      |




### Riassunto del perimetro
Il concetto centrale può essere espresso così:

> **MyAma deve permettere al cittadino di richiedere lo smaltimento di un rifiuto ingombrante, tramite ritiro a domicilio o conferimento presso una sede AMA, e deve permettere ad AMA di organizzare le risorse necessarie per eseguire correttamente il servizio.**

Questa, secondo me, è la base migliore da portare come lavoro della coppia **D-E**.




## Checklist
- [ ]  Si capisce qual è il problema che MyAma vuole risolvere?
- [ ]  Sono presenti **ritiro a domicilio** e **conferimento in sede**?
- [ ]  È presente il cittadino?
- [ ]  È presente l'autista?
- [ ]  È presente l'operatore di sede?
- [ ]  È presente l'organizzazione delle risorse AMA?
- [ ]  Si parla di sedi e CAP/zone?
- [ ]  Si parla delle disponibilità?
- [ ]  Si considerano lavoratori e veicoli?
- [ ]  È chiaro che il veicolo deve essere adeguato al rifiuto/carico?
- [ ]  È prevista la registrazione dell'esito?
- [ ]  Il cittadino vede solo opzioni compatibili con la propria zona?
- [ ]  Sono state introdotte funzioni non presenti in `idea.md`?
- [ ]  Le funzioni “da valutare” sono state trattate erroneamente come certe?
- [ ]  Sono state introdotte tecnologie/database/pattern prematuramente?
- [ ]  Il progetto è rimasto focalizzato sullo **smaltimento dei rifiuti ingombranti**?
