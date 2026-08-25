# -*- coding: utf-8 -*-

import re

tex_path = r'MYAMA/PROGETTOFINALE/Latex PDF/sezioni/01_introduzione.tex'

with open(tex_path, 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

new_section = r'''\subsection{Classi di Utenza del Sistema}
Il servizio è accessibile alle seguenti classi di utenza (attori):
\begin{itemize}[leftmargin=*]
    \item \textbf{Utente di sistema:} è qualsiasi entità esterna che interagisce con il software per scambiare dati, richiedere un servizio o innescare uno specifico comportamento.
    
    \item \textbf{Utente non registrato:} è un generico individuo che ancora non possiede un account nella piattaforma MYAma. Esso può registrarsi e conseguentemente accedere al profilo personale provvisto di funzionalità specifiche in base al ruolo rivestito nella piattaforma.
    
    \item \textbf{Cittadino:} può consultare liberamente le informazioni generali sui servizi offerti, le tipologie di rifiuti ammesse, le sedi territoriali attive e le relative tariffe. Per procedere alla prenotazione di un servizio, può registrarsi fornendo i propri dati anagrafici e di contatto (nome, cognome, indirizzo, recapito telefonico e indirizzo e-mail). Inseguito alla registrazione può usufruire della piattaforma per richiedere un ritiro a domicilio o prenotare un conferimento diretto presso una sede AMA, specificando le caratteristiche del rifiuto (con eventuale caricamento foto), indicando l'indirizzo/CAP e selezionando una fascia oraria disponibile. Può inoltre monitorare lo stato di avanzamento delle proprie richieste, consultare lo storico, rilasciare valutazioni ed eventualmente annullare una prenotazione attiva entro i limiti temporali previsti.
    
    \item \textbf{Autista AMA:} tramite l'applicazione dedicata, consulta l'elenco dei ritiri assegnati per il proprio turno con i dettagli logistici (indirizzo, fascia oraria, tipologia di carico e capienza residua del mezzo), visualizza i recapiti per contattare il cittadino e registra l'esito dell'attività svolta (completato, cittadino assente, rifiuto non conforme).
    
    \item \textbf{Operatore di sede AMA:} gestisce le attività di accettazione presso il centro di raccolta, verificando le prenotazioni dei cittadini in arrivo, controllando la conformità dei rifiuti conferiti e registrando l'esito del servizio.
    
    \item \textbf{Amministratore di sede AMA:} gestisce l'organizzazione logistica della propria struttura: genera i codici di invito per il personale operativo (autisti e operatori) della sede, definisce le disponibilità di lavoratori e veicoli, imposta le fasce orarie e associa le sedi alle rispettive zone o CAP serviti.
    
    \item \textbf{Amministratore generale AMA:} opera a livello direttivo aziendale; è responsabile della gestione degli account degli Amministratori di sede (generazione codici di invito dedicati, abilitazione e revoca).
\end{itemize}'''

content = re.sub(
    r'\\subsection\{Classi di Utenza del Sistema\}.*?(?=\\subsection\{Perimetro del Sistema \(In-Scope e Out-of-Scope\)\})',
    lambda m: new_section + '\n\n',
    content,
    flags=re.DOTALL
)

with open(tex_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated 01_introduzione.tex")