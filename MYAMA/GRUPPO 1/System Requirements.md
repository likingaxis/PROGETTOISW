# 4. System Requirements

## 4.1 Requisiti Funzionali

Questa sezione descrive le funzioni che il sistema deve fornire, strutturate in base agli attori che interagiscono con MyAma. Sono stati estratti dai Use Case analizzati.

| Attore | ID | Requisito Funzionale | Descrizione / Criterio di Verifica |
|---|---|---|---|
| Utente non registrato | RF-01 | Registrazione cittadino | Il sistema deve consentire a un utente di registrarsi come cittadino fornendo i propri dati e accettando l'informativa privacy. |
| Utente non registrato | RF-02 | Registrazione tramite invito | Il sistema deve permettere la registrazione del personale (Amministratore o personale) tramite l'inserimento di un codice di invito valido. |
| Utente di sistema | RF-03 | Autenticazione | Il sistema deve permettere agli utenti registrati di effettuare l'accesso inserendo credenziali valide, reindirizzandoli alle funzionalità del proprio ruolo. |
| Cittadino | RF-04 | Richiesta ritiro a domicilio | Il sistema deve permettere al cittadino di prenotare un ritiro a domicilio fornendo indirizzo, CAP e i dettagli del rifiuto ingombrante. |
| Cittadino | RF-05 | Verifica zona coperta | Il sistema deve verificare che il CAP o la zona indicata dal cittadino per il ritiro a domicilio sia effettivamente coperta dal servizio e rispondere in caso contrario con un messaggio di errore. |
| Cittadino | RF-06 | Prenotazione conferimento | Il sistema deve permettere al cittadino di prenotare il conferimento del rifiuto presso una sede AMA compatibile con la propria zona. |
| Cittadino | RF-07 | Annullamento prenotazione | Il sistema deve consentire al cittadino di annullare una propria prenotazione precedentemente creata. |
| Autista AMA | RF-08 | Visualizzazione ritiri assegnati | Il sistema deve fornire all'autista l'elenco dei ritiri a domicilio assegnati per il proprio turno, con i dettagli dell'indirizzo e del rifiuto. |
| Autista AMA | RF-09 | Registrazione esito ritiro | Il sistema deve permettere all'autista di registrare l'esito (positivo o negativo) del ritiro a domicilio effettuato. |
| Operatore di Sede | RF-10 | Verifica e registrazione conferimento | Il sistema deve permettere all'operatore di verificare una prenotazione in sede e registrarne l'esito al momento dello scarico del rifiuto. |
| Amministratore Sede | RF-11 | Gestione risorse e disponibilità | Il sistema deve permettere all'amministratore di configurare le fasce orarie e la disponibilità di veicoli e personale. |
| Amministratore Sede | RF-12 | Generazione codici invito | Il sistema deve consentire a un'amministratore di generare codici di invito per registrare e abilitare nuovi operatori di sede e autisti. |
| Amministratore di sede | RF-13 | Rimuovere personale Ama | Il sistema deve permettere a un amministratore di rimuovere il profilo di operatori e autisti Ama. |
| Amministratore generale Sede | RF-14 | Generazione codici invito | Il sistema deve consentire all'amministratore di generare codici di invito per registrare e abilitare nuovi amministratori di sede. |
| Amministratore Generale | RF-15 | Rimuovere amministratori di Sede | Il sistema deve permettere all'amministratore generale di rimuovere il profilo di un amministratore di sede. |

---

## 4.2 Requisiti Non Funzionali

Questa sezione descrive i vincoli di qualità e le caratteristiche misurabili che il sistema deve rispettare.
| ID | Requisito | Descrizione|
|---|---|---|---|
| RNF-01 | Performance|Tutte le operazioni di manipolazione degli account sulla piattaforma(cancellazione, registrazione) assieme a quelle di notifica dell'esito del ritiro e annullamento di una prenotazione devono avvenire in un tempo strettamente minore ai 2 secondi. Per quanto riguarda invece la prenotazione di un servizio da parte dei cittadini e l'emissione di codici di invito i tempi di esecuzione hanno un upper bound di 3 secondi|
| RNF-02 | Scalabilità | Il sistema deve garantire l'operatività standard supportando fino a 2.000 utenti concorrenti attivi simultaneamente sulle operazioni di prenotazione. In caso di picchi improvvisi l'infrastruttura deve auto-scalare in tempi inferiori a 60 secondi per gestire fino a 15.000 utenti concorrenti. In quest'ultima fase i tempi di risposta alle interazioni tra cittadini e piattaforma non devono superare i 5 secondi. Infine, da un punto di vista aziendale, il sistema riesce a supportare fino a un massimo di 40 sedi operative con 20.000 utenze complessive. Inoltre, per scenari in cui c'è un picco di connessioni da parte del personale, i tempi di latenza di risposta non devono superare i 1.500 ms.|
| RNF-03 | Portabilità | Il prodotto deve essere utilizzabile su una vasta gamma di piattaforme e dispositivi. È fondamentale che sia disponibile sotto forma di app mobile per iOS e Android, ma anche accessibile tramite browser Web (compatibile con Chrome, Firefox, Safari, Microsoft Edge). Inoltre la piattaforma deve possedere un responsive design che le permette di adattare automaticamente il proprio layout e i propri contenuti alle dimensioni dello schermo devo viene visualizzata|
| RNF-04 | Affidabilità | La piattaforma deve garantire una disponibilità del servizio (uptime) pari al 99,9% su base annua, escludendo dal calcolo del disservizio gli interventi di manutenzione programmata che verranno eseguiti nella fascia notturna di minor traffico (02:00 - 04:00). Inoltre, in caso di crash improvvisi o anomalie di sistema, l'architettura deve assicurare la totale integrità dei dati, garantendo che i profili degli utenti e lo stato delle prenotazioni effettuate dai cittadini non subiscano alcuna perdita o corruzione. |
| RNF-05 | Manutenibilità | Il sistema deve essere strutturato secondo un'architettura modulare e disaccoppiata, supportata da una documentazione tecnica completa per facilitare futuri interventi di manutenzione. Inoltre, in caso di malfunzionamenti critici, le funzionalità del sistema dovranno poter essere ripristinate entro un tempo massimo di 3 ore.|
| RNF-06 | Disponibilità | |
| RNF-07 | Usabilità | Il sistema deve offrire un'interfaccia semplice, intuitiva e ad accessibilità immediata. La piattaforma deve consentire a un cittadino di portare a termine una prenotazione in un massimo di 5 passaggi guidati, integrando controlli per la prevenzione degli errori di inserimento e garantendo la compatibilità tra i dispositivi. Per il personale AMA, le funzionalità messe a disposizione devono assicurare una curva di apprendimento rapida, riducendo al minimo la necessità di formazione preliminare per il personale di sede.|
| RNF-08 | Sicurezza |Il sistema deve garantire la riservatezza e l'integrità dei dati personali dei cittadini e delle informazioni aziendali, operando in piena conformità con le normative vigenti sulla privacy. Tutte le comunicazioni di rete devono essere crittografate tramite protocolli sicuri e le password salvate tramite algoritmi di hashing. Inoltre, l'accesso agli account da parte del personale AMA deve essere regolamentato da un rigoroso sistema di controllo degli accessi basato sui ruoli, garantendo che ogni operatore possa visualizzare e modificare esclusivamente i dati e le pratiche della sede territoriale di propria competenza.|


---

## 4.3 Requisiti di Dominio

Questa sezione raccoglie le regole aziendali o logiche specifiche del contesto "AMA" (smaltimento rifiuti) che vincolano il funzionamento del software.

1. **RD-01 - Competenza Territoriale:** Una richiesta di ritiro a domicilio o la scelta di una sede per il conferimento sono vincolate dalla competenza territoriale e dalle fasce orarie operative disponibili delle sedi. Il sistema può accettare richieste solo se il CAP o la zona indicata dall'utente sono coperti e assegnati a una Sede AMA attiva.
2. **RD-02 - Vincolo di Capacità dei Veicoli:** Durante la pianificazione dei ritiri a domicilio, il sistema non può assegnare a un singolo veicolo un numero di prenotazioni il cui peso o volume stimato superi il carico massimo consentito (capacità) del veicolo stesso per quel turno.Inoltre il rifiuto è ritirabile solo se conforme a quanto dichiarato, e se la sede o il veicolo assegnato sono abilitati a gestirlo.
3. **RD-03 - Coerenza delle prenotazioni:** Il sistema deve impedire transizioni illecite, come l'annullamento di una prenotazione che risulta già in uno stato di completamento. 
4. **RD-04 - Validità del Codice di Invito:** Un codice di invito generato da un amministratore di sede o generale deve essere univoco, associato a un ruolo specifico e può essere monouso, per evitare la creazione fraudolenta di profili con privilegi elevati.
5. **RD-04 - Controllo degli Accessi basato sul Ruolo (RBAC):**Il sistema deve garantire che ogni utente possa accedere esclusivamente alle informazioni e alle funzionalità previste dal proprio ruolo. I dati personali del Cittadino, come informazioni anagrafiche, indirizzo e dati relativi alle prenotazioni, devono essere accessibili solo al personale AMA autorizzato e quando necessario allo svolgimento del servizio. Analogamente, gli Amministratori di sede devono poter operare solamente sui dati e sulle risorse delle sedi di propria competenza, mentre l'Amministratore Generale può accedere alle informazioni necessarie alla gestione complessiva del sistema.

