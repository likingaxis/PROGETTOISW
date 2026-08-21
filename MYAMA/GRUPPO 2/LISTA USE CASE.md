# UTENTE SBERS non registrato 
- Si registra come cittadino (extend(accetta dati sulla privacy))
	- accetta dati sulla privacy
- Si registra come amministratore di sede (mediante codice invito)
- Si registra come operatore di sede (mediante codice invito)
- Visualizza tariffe e informazioni

# Cittadino
1.  Richiedere ritiro a domicilio (**include**[3,4,7,11] **extends**[12,14]) ## per punto 10 consultare tutti
2.  Prenotare conferimento presso sede AMA(**include**[3,5,6,7,11] **extends**[12,14])
3.  Inserire le informazioni sul rifiuto
4.  Indicare indirizzo / zona / CAP
5. Visualizzare sedi compatibili
6. Visualizzare date e fasce orarie disponibili
7. Creare prenotazione //schioppo pure questo per mettere prenota conferimento e prenota ritiro a domicilio
8. Annullare prenotazione
9. Visualizzare prenotazioni attive(**extends**[8])
10. Ricevere notifiche / Chiamate
11. Caricare foto del rifiuto
12. Visualizzare eventuale costo del servizio
13. Consultare storico prenotazioni
14. Valutare il servizio

# Autista AMA
1. Visualizzare ritiri assegnati (**include**[2])
2. Consultare dettagli del ritiro
3. Registrare esito del ritiro
4. Chiamare Cittadino

# Operatore di sede AMA
1. Visualizzare prenotazioni della sede (**include**[2,3])
2. Consultare dettagli del conferimento
3. Verificare prenotazione del cittadino
4. Registrare esito del conferimento

# Amministratore sede AMA
1.  Gestisce la registrazione del personale AMA
2.  Gestisce disponibilità dei lavoratori
3.  Gestisce disponibilità dei veicoli
4.  gestisce disponibilità di sedi e fasce orarie (**include**[5])
5.  gestisce associazione tra sedi e zone/CAP
6. genera codice invito
7. rimuove operatori di sede AMA

# Amministratore generale AMA
- genera codice invito
- rimuove amministratori