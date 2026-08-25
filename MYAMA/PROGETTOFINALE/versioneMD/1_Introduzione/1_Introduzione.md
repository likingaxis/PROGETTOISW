# 1. Introduzione


## Problem Statement e Obiettivi del Progetto

La gestione dello smaltimento dei rifiuti urbani ingombranti e speciali nella città di Roma presenta storicamente complessità logistiche legate al coordinamento tra cittadini, centri di raccolta territoriali (isole ecologiche) e squadre operative di raccolta su strada. I canali tradizionali non integrati comportano spesso tempi di attesa elevati per l'utenza, difficoltà nella stima preventiva dei carichi e rischi di saturazione non controllata dei mezzi e delle sedi.

La piattaforma **MyAma** si propone come soluzione software integrata volta a digitalizzare e ottimizzare l'intero ciclo di vita delle richieste di smaltimento dei rifiuti ingombranti. L'obiettivo primario del sistema è duplice:

    * **Per la cittadinanza:** fornire un canale digitale trasparente, accessibile e guidato per prenotare in autonomia sia il *ritiro a domicilio* sia il *conferimento programmato in sede*, consentendo il tracciamento in tempo reale dello stato del servizio ed evitando code e disservizi.
    * **Per l'azienda (AMA):** fornire strumenti di pianificazione logistica per l'allocazione ottimizzata dei turni, il rispetto della capacità massima di carico dei veicoli, il contingentamento degli accessi ai centri di raccolta e il monitoraggio puntuale degli esiti operativi.


## Classi di Utenza del Sistema

Il servizio è accessibile alle seguenti classi di utenza (attori):
     
     * **Utente di sistema:** è qualsiasi entità esterna che interagisce con il software per scambiare dati, richiedere un servizio o innescare uno specifico comportamento.


     * **Utente non registrato:** è un generico individuo che ancora non possiede un account nella piattaforma MYAma. Esso può registrarsi e conseguentemente accedere al profilo personale provvisto di funzionalità specifiche in base al ruolo rivestito nella piattaforma.


    * **Cittadino:** può consultare liberamente le informazioni generali sui servizi offerti, le tipologie di rifiuti ammesse, le sedi territoriali attive e le relative tariffe. Per procedere alla prenotazione di un servizio, può registrarsi fornendo i propri dati anagrafici e di contatto (nome, cognome, indirizzo, recapito telefonico e indirizzo e-mail). In seguito alla registrazione può usufruire della piattaforma per richiedere un ritiro a domicilio o prenotare un conferimento diretto presso una sede AMA, specificando le caratteristiche del rifiuto (con eventuale caricamento foto), indicando l'indirizzo/CAP e selezionando una fascia oraria disponibile. Può inoltre monitorare lo stato di avanzamento delle proprie richieste, consultare lo storico, rilasciare valutazioni ed eventualmente annullare una prenotazione attiva entro i limiti temporali previsti.

    
    * **Autista AMA:** tramite l'applicazione dedicata, consulta l'elenco dei ritiri assegnati per il proprio turno con i dettagli logistici (indirizzo, fascia oraria, tipologia di carico e capienza residua del mezzo), visualizza i recapiti per contattare il cittadino e registra l'esito dell'attività svolta (completato, cittadino assente, rifiuto non conforme).
    

    * **Operatore di sede AMA:** gestisce le attività di accettazione presso il centro di raccolta, verificando le prenotazioni dei cittadini in arrivo, controllando la conformità dei rifiuti conferiti e registrando l'esito del servizio.
    

    * **Amministratore di sede AMA:** gestisce l'organizzazione logistica della propria struttura: genera i codici di invito per il personale operativo (autisti e operatori) della sede, definisce le disponibilità di lavoratori e veicoli, imposta le fasce orarie e associa le sedi alle rispettive zone o CAP serviti.
    
    
    * **Amministratore generale AMA:** opera a livello direttivo aziendale; è responsabile della gestione degli account degli Amministratori di sede (generazione codici di invito dedicati, abilitazione e revoca).


## Perimetro del Sistema (In-Scope e Out-of-Scope)

Al fine di delimitare con precisione i requisiti e i modelli OOA sviluppati nel presente documento:

    * **Funzionalità In-Scope:** autenticazione e registrazione basata su ruoli; gestione completa delle prenotazioni di ritiro a domicilio e conferimento in sede; verifica territoriale vincolata a sede e CAP; gestione delle disponibilità e della capacità dei mezzi; tracciamento e registrazione degli esiti di servizio; consultazione dello storico e rilascio feedback; gestione amministrativa di sedi, personale, veicoli e codici di invito.
    * **Funzionalità Out-of-Scope (future estensioni):** integrazione diretta con gateway di pagamento elettronico per tariffe extra-franchigia (gestite in questa fase a livello di preventivo informativo); autenticazione federata SPID/CIE; tracciamento GPS in tempo reale dei veicoli; gestione di reportistica analitica avanzata di Business Intelligence.


---
