# 3. User Requirements Definition


La presente sezione descrive in dettaglio i requisiti utente e i casi d'uso del sistema **MyAma**, organizzati e strutturati in base alle differenti classi di attori che interagiscono con la piattaforma. Ciascuna sottosezione comprende il relativo diagramma Use Case esportato e le relative schede descrittive tabellari conformi allo standard di specifica dei requisiti.

% =========================================================================
% 3.1 UTENTE NON REGISTRATO E UTENTE DI SISTEMA
% =========================================================================
## Use Case Utente non registrato e Utente di sistema


### Diagramma
\begin{figure}[H]
    \centering
    \includegraphics[width=0.75\textwidth]{figure/uc_utente_non_registrato.jpg}
    \caption{Use Case Diagram — Utente non registrato e Utente di sistema}
    \label{fig:uc_utente_non_registrato}
\end{figure}

### Documentazione


| **Use Case** | **Registrarsi come cittadino** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Utente non registrato |
| **Precondizioni** | L'utente non possiede ancora un account nel sistema. |
| **Scenario principale** | L'utente inserisce correttamente i dati richiesti, accetta l'informativa sulla privacy e completa la registrazione come cittadino. |
| **Scenari alternativi** |  |
| **Post-condizioni** | L'utente risulta registrato nel sistema con il ruolo di cittadino e dispone di un account utilizzabile per accedere alle funzionalità riservate. |




| **Use Case** | **Registrarsi tramite codice di invito** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Utente non registrato |
| **Precondizioni** | L'utente non possiede ancora un account nel sistema e ha ricevuto un codice di invito valido. |
| **Scenario principale** | L'utente inserisce un codice di invito valido e i dati richiesti, accetta l'informativa sulla privacy e completa la registrazione. Il sistema gli assegna il ruolo previsto dal codice. |
| **Scenari alternativi** |  |
| **Post-condizioni** | L'utente risulta registrato nel sistema con il ruolo associato al codice di invito e dispone di un account utilizzabile per accedere alle funzionalità previste per tale ruolo. |




| **Use Case** | **Accettare dati sulla privacy** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Utente non registrato |
| **Precondizioni** | L'utente ha avviato una procedura di registrazione (come cittadino o tramite codice di invito) e non ha ancora completato la creazione dell'account. |
| **Scenario principale** | Il sistema presenta l'informativa sulla privacy, l'utente la consulta e accetta il trattamento dei dati richiesto. Il sistema registra il consenso e permette di proseguire con la registrazione. |
| **Scenari alternativi** | L'utente non accetta l'informativa sulla privacy: il sistema non consente di proseguire con la registrazione. |
| **Post-condizioni** | L'accettazione dell'informativa sulla privacy risulta registrata e l'utente può proseguire con la procedura di registrazione in corso. |




| **Use Case** | **Effettuare accesso** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Utente registrato |
| **Precondizioni** | L'utente possiede un account registrato nel sistema. |
| **Scenario principale** | L'utente inserisce credenziali valide. Il sistema le verifica correttamente e consente l'accesso alle funzionalità associate al suo ruolo. |
| **Scenari alternativi** |  |
| **Post-condizioni** | L'utente risulta autenticato nel sistema e può utilizzare le funzionalità previste per il proprio ruolo. |



% =========================================================================
% 3.2 CITTADINO REGISTRATO
% =========================================================================
## Use Case Cittadino registrato


### Diagramma
\begin{figure}[H]
    \centering
    \includegraphics[width=0.85\textwidth]{figure/uc_cittadino.jpg}
    \caption{Use Case Diagram — Cittadino registrato}
    \label{fig:uc_cittadino}
\end{figure}

### Documentazione


| **Use Case** | **Richiedere ritiro a domicilio** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Cittadino registrato |
| **Precondizioni** | Il cittadino ha effettuato l’accesso al sistema ed è abilitato all’utilizzo delle funzionalità di prenotazione. |
| **Scenario principale** | Il cittadino inserisce correttamente le informazioni sul rifiuto e sull’indirizzo, il sistema verifica la copertura territoriale, individua una o più disponibilità e il cittadino conferma la richiesta specificando la sede compatibile e la fascia oraria. La prenotazione viene registrata. |
| **Scenari alternativi** |  |
| **Post-condizioni** | La richiesta di ritiro a domicilio è registrata nel sistema come prenotazione e contiene le informazioni relative al cittadino, al rifiuto, al luogo del ritiro e alla disponibilità assegnata. |




| **Use Case** | **Prenotare conferimento presso sede AMA** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Cittadino registrato |
| **Precondizioni** | Il cittadino ha effettuato l’accesso al sistema. |
| **Scenario principale** | Il cittadino inserisce correttamente le informazioni e la foto del rifiuto, seleziona una sede compatibile e una disponibilità valida, e conferma il conferimento. Il sistema registra la prenotazione. |
| **Scenari alternativi** | Le informazioni relative al rifiuto (o la foto caricata) sono incomplete o non valide: il sistema richiede al cittadino di correggerle prima di procedere. |
| **Post-condizioni** | La prenotazione del conferimento presso la sede AMA risulta registrata nel sistema con le informazioni relative al cittadino, al rifiuto, alla sede scelta e alla data e fascia oraria selezionate. |




| **Use Case** | **Visualizzare sedi compatibili** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Cittadino registrato |
| **Precondizioni** | Il cittadino ha avviato la procedura di prenotazione per il conferimento o per il ritiro, ed ha inserito le informazioni sul rifiuto. |
| **Scenario principale** | Il sistema individua una o più sedi compatibili con la zona del cittadino e le mostra all’utente. |
| **Scenari alternativi** | Non sono presenti sedi compatibili con la zona indicata: il sistema informa il cittadino che non è possibile effettuare il servizio. |
| **Post-condizioni** | Il cittadino ha selezionato una sede AMA compatibile da utilizzare per la prenotazione. |




| **Use Case** | **Visualizzare date e fasce orarie disponibili** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Cittadino registrato |
| **Precondizioni** | Il cittadino ha avviato la procedura di prenotazione per il conferimento o per il ritiro e ha selezionato una sede compatibile. |
| **Scenario principale** | Il sistema individua le disponibilità compatibili con la sede scelta per il servizio richiesto (tra conferimento o ritiro) e le mostra al cittadino. |
| **Scenari alternativi** | Non sono presenti date o fasce orarie disponibili per la sede selezionata: il sistema richiede di scegliere un'altra sede o di riprovare in un altro momento. |
| **Post-condizioni** | Il cittadino ha selezionato una data e una fascia oraria disponibili da utilizzare per la prenotazione. |




| **Use Case** | **Annullare prenotazione** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Cittadino registrato |
| **Precondizioni** | Il cittadino possiede almeno una prenotazione attiva che può essere annullata. |
| **Scenario principale** | Il cittadino seleziona una prenotazione attiva, ne richiede l’annullamento e conferma l’operazione. Il sistema aggiorna lo stato della prenotazione. |
| **Scenari alternativi** |  |
| **Post-condizioni** | La prenotazione risulta annullata nel sistema. |




| **Use Case** | **Visualizzare prenotazioni attive** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Cittadino registrato |
| **Precondizioni** | Il cittadino ha effettuato l’accesso al sistema. |
| **Scenario principale** | Il cittadino accede all'elenco delle prenotazioni e visualizza i dettagli di quelle attive. |
| **Scenari alternativi** | Il cittadino non possiede prenotazioni attive: il sistema informa che non sono presenti prenotazioni da visualizzare. |
| **Post-condizioni** | Il cittadino ha consultato l’elenco e i dettagli delle proprie prenotazioni attive. |




| **Use Case** | **Visualizzare storico prenotazioni** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Cittadino registrato |
| **Precondizioni** | Il cittadino ha effettuato l’accesso al sistema. |
| **Scenario principale** | Il cittadino accede allo storico e visualizza l'elenco e i dettagli delle proprie prenotazioni passate. |
| **Scenari alternativi** | Il cittadino non possiede prenotazioni concluse o annullate: il sistema informa che lo storico è vuoto. |
| **Post-condizioni** | Il cittadino ha consultato lo storico delle proprie prenotazioni (nessuna modifica allo stato del sistema). |




| **Use Case** | **Valutare il servizio** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Cittadino registrato |
| **Precondizioni** | Il cittadino dispone di almeno una prenotazione conclusa che può essere valutata. |
| **Scenario principale** | Il cittadino seleziona una prenotazione conclusa, inserisce la propria valutazione e la conferma. Il sistema registra correttamente la valutazione. |
| **Scenari alternativi** | Il cittadino interrompe l’operazione prima della conferma: nessuna valutazione viene registrata. |
| **Post-condizioni** | La valutazione del cittadino risulta registrata e associata alla prenotazione conclusa. |




| **Use Case** | **Chiamare Autista AMA** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Cittadino registrato |
| **Precondizioni** | Il cittadino possiede una prenotazione di ritiro a domicilio in stato assegnato o in corso, con un autista AMA associato. |
| **Scenario principale** | Il cittadino accede ai dettagli del ritiro, il sistema mostra il recapito telefonico dell'autista assegnato e il cittadino avvia la chiamata in autonomia tramite il proprio dispositivo. |
| **Scenari alternativi** | Le informazioni di contatto non sono disponibili o l'autista non è ancora stato associato: il sistema segnala l'impossibilità di effettuare la chiamata. |
| **Post-condizioni** | Il cittadino ha visualizzato il recapito telefonico dell'autista AMA e ha avuto la possibilità di avviare la chiamata. |



% =========================================================================
% 3.3 AUTISTA AMA
% =========================================================================
## Use Case Autista AMA


### Diagramma
\begin{figure}[H]
    \centering
    \includegraphics[width=0.75\textwidth]{figure/uc_autista.jpg}
    \caption{Use Case Diagram — Autista AMA}
    \label{fig:uc_autista}
\end{figure}

### Documentazione


| **Use Case** | **Visualizzare ritiri assegnati** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Autista AMA |
| **Precondizioni** | L’autista AMA ha effettuato l’accesso al sistema ed è associato ad almeno un ritiro. |
| **Scenario principale** | L’autista accede alla propria area e visualizza correttamente l’elenco dei ritiri che gli sono stati assegnati. |
| **Scenari alternativi** | Non risultano ritiri assegnati all’autista: il sistema informa che non sono presenti attività da visualizzare. |
| **Post-condizioni** | L’autista ha visualizzato l'elenco dei ritiri assegnati (nessuna modifica allo stato del sistema). |




| **Use Case** | **Consultare dettagli del ritiro** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Autista AMA |
| **Precondizioni** | L’autista AMA ha effettuato l’accesso al sistema e ha selezionato un ritiro assegnato. |
| **Scenario principale** | L’autista seleziona un ritiro e il sistema mostra correttamente tutte le informazioni necessarie per svolgere il servizio. |
| **Scenari alternativi** | Le informazioni relative al ritiro non sono disponibili o risultano incomplete: il sistema segnala il problema all’autista. |
| **Post-condizioni** | L’autista ha consultato i dettagli del ritiro senza modificare lo stato della prenotazione. |




| **Use Case** | **Registrare esito del ritiro** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Autista AMA |
| **Precondizioni** | L’autista AMA ha effettuato l’accesso al sistema ed è associato al ritiro di cui deve registrare l’esito. |
| **Scenario principale** | L’autista seleziona il ritiro effettuato, registra correttamente l’esito del servizio e conferma l’operazione. Il sistema aggiorna lo stato della prenotazione. |
| **Scenari alternativi** |  |
| **Post-condizioni** | L’esito del ritiro risulta registrato nel sistema e lo stato della prenotazione viene aggiornato di conseguenza. |




| **Use Case** | **Chiamare cittadino** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Autista AMA |
| **Precondizioni** | L’autista AMA ha effettuato l’accesso al sistema ed è associato al ritiro relativo al cittadino da contattare. |
| **Scenario principale** | L’autista seleziona il ritiro, il sistema mostra il recapito telefonico e l'autista avvia la chiamata in autonomia tramite il proprio dispositivo. |
| **Scenari alternativi** | Le informazioni di contatto non sono disponibili: il sistema segnala la mancanza del recapito all’autista, impedendogli di effettuare la chiamata. |
| **Post-condizioni** | L’autista ha visualizzato il contatto telefonico del cittadino e ha avuto la possibilità di avviare la chiamata. |



% =========================================================================
% 3.4 OPERATORE DI SEDE AMA
% =========================================================================
## Use Case Operatore di sede AMA


### Diagramma
\begin{figure}[H]
    \centering
    \includegraphics[width=0.75\textwidth]{figure/uc_operatore_sede.jpg}
    \caption{Use Case Diagram — Operatore di sede AMA}
    \label{fig:uc_operatore_sede}
\end{figure}

### Documentazione


| **Use Case** | **Visualizzare prenotazioni della sede** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Operatore di sede AMA |
| **Precondizioni** | L’operatore di sede AMA ha effettuato l’accesso al sistema ed è associato a una sede AMA. |
| **Scenario principale** | L’operatore accede alla propria area e visualizza correttamente l’elenco delle prenotazioni associate alla sede. |
| **Scenari alternativi** | Non risultano prenotazioni associate alla sede: il sistema informa l’operatore che non sono presenti conferimenti da visualizzare. |
| **Post-condizioni** | L’operatore ha visualizzato l'elenco delle prenotazioni della sede (nessuna modifica allo stato delle prenotazioni). |




| **Use Case** | **Consultare dettagli del conferimento** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Operatore di sede AMA |
| **Precondizioni** | L’operatore di sede AMA ha effettuato l’accesso al sistema e ha selezionato una prenotazione associata alla propria sede. |
| **Scenario principale** | L’operatore seleziona una prenotazione e il sistema mostra correttamente tutte le informazioni necessarie relative al conferimento. |
| **Scenari alternativi** | Le informazioni relative al conferimento non sono disponibili o risultano incomplete: il sistema segnala il problema all’operatore. |
| **Post-condizioni** | L’operatore ha consultato i dettagli del conferimento senza modificare lo stato della prenotazione. |




| **Use Case** | **Verificare prenotazione del cittadino** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Operatore di sede AMA |
| **Precondizioni** | Il cittadino possiede una prenotazione per il conferimento presso la sede AMA e si presenta per usufruire del servizio. |
| **Scenario principale** | L’operatore individua la prenotazione del cittadino, ne verifica la validità e conferma che il conferimento possa essere effettuato. |
| **Scenari alternativi** |  |
| **Post-condizioni** | La prenotazione del cittadino risulta verificata e, se valida, il conferimento può essere effettuato. |




| **Use Case** | **Registrare esito del conferimento** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Operatore di sede AMA |
| **Precondizioni** | L’operatore di sede AMA ha effettuato l’accesso al sistema e il conferimento associato alla prenotazione è stato verificato e gestito. |
| **Scenario principale** | L’operatore seleziona la prenotazione, registra correttamente l’esito del conferimento e conferma l’operazione. Il sistema aggiorna lo stato della prenotazione. |
| **Scenari alternativi** |  |
| **Post-condizioni** | L’esito del conferimento risulta registrato nel sistema e lo stato della prenotazione viene aggiornato di conseguenza. |



% =========================================================================
% 3.5 AMMINISTRATORE DI SEDE AMA
% =========================================================================
## Use Case Amministratore di sede AMA


### Diagramma
\begin{figure}[H]
    \centering
    \includegraphics[width=0.75\textwidth]{figure/uc_amministratore_sede.jpg}
    \caption{Use Case Diagram — Amministratore di sede AMA}
    \label{fig:uc_amministratore_sede}
\end{figure}

### Documentazione


| **Use Case** | **Generare codice invito** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Amministratore di sede AMA |
| **Precondizioni** | L’amministratore di sede AMA ha effettuato l’accesso al sistema e dispone dei permessi per generare codici invito per i ruoli di propria competenza. |
| **Scenario principale** | L’amministratore seleziona un ruolo autorizzato e il sistema genera correttamente un codice invito utilizzabile per la registrazione del nuovo utente. |
| **Scenari alternativi** |  |
| **Post-condizioni** | È stato generato un codice invito valido, associato al ruolo selezionato e utilizzabile da un utente non registrato per completare la relativa procedura di registrazione. |




| **Use Case** | **Gestire disponibilità dei lavoratori** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Amministratore di sede AMA |
| **Precondizioni** | L’amministratore ha effettuato l’accesso al sistema e il lavoratore interessato risulta associato alla sede amministrata. |
| **Scenario principale** | L’amministratore seleziona un lavoratore, modifica correttamente le relative disponibilità e conferma l’operazione. Il sistema registra le nuove informazioni. |
| **Scenari alternativi** |  |
| **Post-condizioni** | Le disponibilità del lavoratore risultano aggiornate nel sistema e possono essere utilizzate per la pianificazione dei servizi. |




| **Use Case** | **Rimuovere personale** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Amministratore di sede AMA |
| **Precondizioni** | L’amministratore ha effettuato l’accesso al sistema e il membro del personale selezionato risulta associato alla sede amministrata. |
| **Scenario principale** | L’amministratore seleziona un membro del personale, ne richiede la rimozione e conferma l’operazione. Il sistema aggiorna correttamente l’associazione. |
| **Scenari alternativi** |  |
| **Post-condizioni** | Il membro del personale non risulta più associato alla sede AMA amministrata. |




| **Use Case** | **Gestire disponibilità dei veicoli** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Amministratore di sede AMA |
| **Precondizioni** | L’amministratore ha effettuato l’accesso al sistema e il veicolo selezionato risulta associato alla sede. |
| **Scenario principale** | L’amministratore seleziona un veicolo, modifica correttamente la sua disponibilità e conferma l’operazione. |
| **Scenari alternativi** |  |
| **Post-condizioni** | La disponibilità del veicolo risulta aggiornata nel sistema e può essere utilizzata per la pianificazione dei ritiri. |




| **Use Case** | **Gestire disponibilità della sede e fasce orarie** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Amministratore di sede AMA |
| **Precondizioni** | L’amministratore ha effettuato l’accesso al sistema ed è associato alla sede da configurare. |
| **Scenario principale** | L’amministratore modifica correttamente i giorni o le fasce orarie disponibili per i conferimenti e conferma l’operazione. |
| **Scenari alternativi** | Le fasce orarie inserite non sono valide o presentano incongruenze: il sistema segnala l’errore e richiede una correzione. |
| **Post-condizioni** | Le disponibilità della sede e le relative fasce orarie risultano aggiornate e possono essere utilizzate dal sistema per le prenotazioni dei cittadini. |




| **Use Case** | **Gestire associazioni tra sede e zone/CAP** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Amministratore di sede AMA |
| **Precondizioni** | L’amministratore ha effettuato l’accesso al sistema ed è associato alla sede da configurare. |
| **Scenario principale** | L’amministratore modifica correttamente le zone o i CAP associati alla propria sede e conferma l’operazione. |
| **Scenari alternativi** |  |
| **Post-condizioni** | Le associazioni tra la sede AMA e le relative zone o CAP risultano aggiornate e possono essere utilizzate dal sistema per determinare le sedi compatibili con le richieste dei cittadini. |



% =========================================================================
% 3.6 AMMINISTRATORE GENERALE AMA
% =========================================================================
## Use Case Amministratore generale AMA


### Diagramma
\begin{figure}[H]
    \centering
    \includegraphics[width=0.75\textwidth]{figure/uc_amministratore_generale.jpg}
    \caption{Use Case Diagram — Amministratore generale AMA}
    \label{fig:uc_amministratore_generale}
\end{figure}

### Documentazione


| **Use Case** | **Generare codice amministratore di sede** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Amministratore generale AMA |
| **Precondizioni** | L’amministratore generale AMA ha effettuato l’accesso al sistema e dispone dei permessi necessari per generare codici invito destinati alla registrazione di amministratori di sede AMA. |
| **Scenario principale** | L’amministratore generale richiede la generazione di un nuovo codice invito per un amministratore di sede. Il sistema verifica i permessi, genera correttamente il codice e lo rende disponibile all’amministratore generale. |
| **Scenari alternativi** |  |
| **Post-condizioni** | È stato generato un codice invito valido associato al ruolo di amministratore di sede AMA, utilizzabile da un utente non registrato per completare la relativa procedura di registrazione. |




| **Use Case** | **Rimuovere amministratori di sede AMA** |
| :--- | :--- |
| **Descrizione** | **Flusso delle azioni** |
| **Attori** | Amministratore generale AMA |
| **Precondizioni** | L’amministratore generale AMA ha effettuato l’accesso al sistema e l’amministratore di sede selezionato risulta registrato e attivo nel sistema. |
| **Scenario principale** | L’amministratore generale seleziona un amministratore di sede, ne richiede la rimozione e conferma l’operazione. Il sistema aggiorna correttamente le informazioni relative al ruolo dell’utente. |
| **Scenari alternativi** |  |
| **Post-condizioni** | L’utente selezionato non risulta più abilitato a operare come amministratore di sede AMA nel sistema. |



---
