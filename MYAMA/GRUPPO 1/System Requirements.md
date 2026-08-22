# 4. System Requirements

## 4.1 Requisiti Funzionali

Questa sezione descrive le funzioni che il sistema deve fornire, strutturate in base agli attori che interagiscono con MyAma. Sono stati estratti dai Use Case analizzati.

| Attore | ID | Requisito Funzionale | Descrizione / Criterio di Verifica |
|---|---|---|---|
| Utente non registrato | RF-01 | Registrazione cittadino | Il sistema deve consentire a un utente di registrarsi come cittadino fornendo i propri dati e accettando l'informativa privacy. |
| Utente non registrato | RF-02 | Registrazione tramite invito | Il sistema deve permettere la registrazione del personale (Amministratore o Operatore) tramite l'inserimento di un codice di invito valido. |
| Utente di sistema | RF-03 | Autenticazione | Il sistema deve permettere agli utenti registrati di effettuare l'accesso inserendo credenziali valide, reindirizzandoli alle funzionalità del proprio ruolo. |
| Cittadino | RF-04 | Richiesta ritiro a domicilio | Il sistema deve permettere al cittadino di prenotare un ritiro a domicilio fornendo indirizzo, CAP e i dettagli del rifiuto ingombrante. |
| Cittadino | RF-05 | Verifica zona coperta | Il sistema deve verificare che il CAP o la zona indicata dal cittadino per il ritiro a domicilio sia effettivamente coperta dal servizio. |
| Cittadino | RF-06 | Prenotazione conferimento | Il sistema deve permettere al cittadino di prenotare il conferimento del rifiuto presso una sede AMA compatibile con la propria zona. |
| Cittadino | RF-07 | Annullamento prenotazione | Il sistema deve consentire al cittadino di annullare una propria prenotazione precedentemente creata. |
| Autista AMA | RF-08 | Visualizzazione ritiri assegnati | Il sistema deve fornire all'autista l'elenco dei ritiri a domicilio assegnati per il proprio turno, con i dettagli dell'indirizzo e del rifiuto. |
| Autista AMA | RF-09 | Registrazione esito ritiro | Il sistema deve permettere all'autista di registrare l'esito (es. positivo o negativo) del ritiro a domicilio effettuato. |
| Operatore di Sede | RF-10 | Verifica e registrazione conferimento | Il sistema deve permettere all'operatore di verificare una prenotazione in sede e registrarne l'esito al momento dello scarico del rifiuto. |
| Amministratore Sede | RF-11 | Gestione risorse e disponibilità | Il sistema deve permettere all'amministratore di configurare le fasce orarie e la disponibilità di veicoli e lavoratori. |
| Amministratore Sede | RF-12 | Generazione codici invito | Il sistema deve consentire all'amministratore di generare codici di invito per registrare e abilitare nuovi operatori di sede. |

---

## 4.2 Requisiti Non Funzionali

Questa sezione descrive i vincoli di qualità e le caratteristiche misurabili che il sistema deve rispettare.

| ID | Requisito | Descrizione e Metriche (Criterio di verifica) |
|---|---|---|
| RNF-01 | Sicurezza (Autenticazione e Privacy) | Il sistema deve garantire che le password siano salvate tramite algoritmi di hashing sicuri. L'accesso a dati personali e funzioni sensibili è consentito solo previa autenticazione e in base ai permessi del ruolo (RBAC). |
| RNF-02 | Performance (Tempi di risposta) | Il sistema deve restituire l'elenco delle sedi compatibili o delle fasce orarie disponibili in un tempo massimo di 2 secondi nel 95% delle richieste, per garantire una user-experience fluida. |
| RNF-03 | Usabilità | L'interfaccia utente deve essere intuitiva. La prenotazione di un ritiro o di un conferimento da parte di un cittadino deve potersi concludere in non più di 5 passaggi (click o schermate). |
| RNF-04 | Disponibilità (Availability) | Il sistema lato cittadino deve garantire un uptime del 99.5% su base mensile, permettendo la prenotazione dei servizi 24 ore su 24, 7 giorni su 7. |

---

## 4.3 Requisiti di Dominio

Questa sezione raccoglie le regole aziendali o logiche specifiche del contesto "AMA" (smaltimento rifiuti) che vincolano il funzionamento del software.

1. **RD-01 - Competenza Territoriale:** Una richiesta di ritiro a domicilio o la scelta di una sede per il conferimento sono vincolate dalla competenza territoriale. Il sistema può accettare richieste solo se il CAP o la zona indicata dall'utente sono coperti e assegnati a una Sede AMA attiva.
2. **RD-02 - Vincolo di Capacità dei Veicoli:** Durante la pianificazione dei ritiri a domicilio, il sistema non può assegnare a un singolo veicolo un numero di prenotazioni il cui peso o volume stimato superi il carico massimo consentito (capacità) del veicolo stesso per quel turno.
3. **RD-03 - Ciclo di Vita della Prenotazione:** Ogni prenotazione deve rispettare rigorosamente una macchina a stati definita (es. _Creata_, _Assegnata_, _Completata_, _Annullata_). Il sistema deve impedire transizioni illecite, come l'annullamento di una prenotazione che risulta già in stato _Completata_.
4. **RD-04 - Validità del Codice di Invito:** Un codice di invito generato da un amministratore deve essere univoco, associato a un ruolo specifico (es. Operatore o Amministratore) e può essere monouso, per evitare la creazione fraudolenta di profili con privilegi elevati.
