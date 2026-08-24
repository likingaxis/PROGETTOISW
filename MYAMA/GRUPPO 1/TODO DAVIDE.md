
# Scheda Use Case

## Cittadino Registrato - Richiedere ritiro a domicilio
***modifcare il flusso delle azioni in: ***
1. Il cittadino accede alla funzionalità per richiedere un ritiro a domicilio.
2. Il cittadino inserisce la tipologia e i dettagli del rifiuto ingombrante
3. Il cittadino invia la richiesta di ritiro da smaltire.
4. Viene eseguito il caso d'uso *Visualizzare sedi compatibili* per individure e fornire all'utente le sedi AMA compatibili.
5. Il sistema verifica la disponibilità delle risorse necessarie (lavoratori, veicoli e capacità di carico) per ogni sede compatibile.
6. Il sistema fornisce per ogni sede effettivamente disponibile, le fasce orarie possibili per il ritiro attraverso il caso d'uso *Visualizzare date e fasce orarie disponibili*.
7. Il sistema mostra il riepilogo della richiesta con le scelte possibili.
8. Il cittadino seleziona la sede, la data e la fascia oraria per confermare la richiesta di ritiro.
9. Il sistema crea la prenotazione e ne conferma l'avvenuta registrazione.

## Cittadino Registrato - Prenotare conferimento presso sede AMA
***modificare il flusso delle azioni in:***
1. Il cittadino seleziona la funzionalità per prenotare il conferimento di un rifiuto presso una sede AMA.
2. Il cittadino inserisce la tipologia e i dettagli del rifiuto da smaltire e carica una foto del rifiuto
3. Il cittadino invia la richiesta di conferimento.
4. Viene eseguito il caso d'uso *Visualizzare sedi compatibili* per individure e fornire all'utente le sedi AMA compatibili.
5. Il sistema verifica la disponibilità delle risorse necessarie (capacita di ricezione, e disponibilita oraria) per ogni sede compatibile.
6. Il sistema fornisce per ogni sede effettivamente disponibile, le fasce orarie possibili per il conferimento attraverso il caso d'uso *Visualizzare date e fasce orarie disponibili*.
7. Il sistema mostra il riepilogo della richiesta con le scelte possibili.
8. Il cittadino seleziona la sede, la data e la fascia oraria per confermare la richiesta di conferimento.
9. Il sistema crea la prenotazione e ne conferma l'avvenuta registrazione.

## Cittadino Registrato - Visualizzare sedi compatibli
***modificare il flusso delle azioni in: ***
1. Il Cittadino specifica il tipo di servizio richiesto tra conferimento o ritiro e con quale tipologia di rifiuto.
2. Durante la procedura di prenotazione per il servizio richiesto, il sistema acquisisce la zona o il CAP del cittadino.
3. Il sistema verifica quali sedi AMA possono accettare il servizio richiesto.
4. Il sistema mostra al cittadino l’elenco delle sedi compatibili disponibili.

## Cittadino Registrato - Visualizzare date e fasce orarie disponibili
***modificare il flusso delle azioni in:***
1. Il Cittadino specifica il tipo di servizio richiesto tra conferimento o ritiro e con quale tipologia di rifiuto.
2. Il Cittadino specifica un insieme di sedi da interrogare.
3. Il sistema mostra al cittadino le fasce orarie disponibili.

# 2 glossario dei termini di dominio
La sezione descrive i vari termini specialistici, gli attori e i concetti fondamentali usati per descriviere il sistema **MyAma**.

# 3 user requirements definition
La sezione descrive in dettaglio i requisiti utente e i casi d’uso del sistema MyAma. Ciascuna sottosezione comprende il relativo diagramma che descrive per ogni attore i relativi Use Case e la relativa documentazione sotto forma di tabella.

# 4
nun ce scrive un cazzo

# 5 System Architectural Models (Modelli OOA)
La sezione descrive i modelli dinamici e strutturali del sistema MyAma mediante i modelli di OOA

## 5.1
In questa sezione vengono presentati i diagrammi fondamentali, raggruppati per attore.

## 5.3.2
Il modello Refined integra e consolida l’architettura completa a oggetti del sistema MyAma, strutturando le classi secondo il pattern architetturale BCE (Boundary, Control, Entity). 
