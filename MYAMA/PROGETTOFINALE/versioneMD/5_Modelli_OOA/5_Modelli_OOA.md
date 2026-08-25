# 5. System Architectural Models 

% =========================================================================
% 5.1 ACTIVITY DIAGRAMS
% =========================================================================
## Activity Diagrams

### Utente non registrato e Utente di sistema

Questi diagrammi modellano i flussi di base per l'ingresso nel sistema, dalla registrazione fino all'autenticazione.

![Activity Diagram — Registrarsi come cittadino](../figure/act_registrarsi_cittadino.jpg)

*Activity Diagram — Registrarsi come cittadino*


![Activity Diagram — Registrarsi tramite codice di invito](../figure/act_registrarsi_invito.jpg)

*Activity Diagram — Registrarsi tramite codice di invito*


![Activity Diagram — Effettuare accesso](../figure/act_effettuare_accesso.jpg)

*Activity Diagram — Effettuare accesso*


### Cittadino

I seguenti diagrammi illustrano le interazioni del cittadino per usufruire dei servizi AMA, dalla prenotazione fino alla valutazione finale.

![Activity Diagram — Richiesta ritiro a domicilio](../figure/act_richiesta_ritiro.jpg)

*Activity Diagram — Richiesta ritiro a domicilio*


![Activity Diagram — Prenotare conferimento in sede](../figure/act_prenota_conferimento.jpg)

*Activity Diagram — Prenotare conferimento in sede*


![Activity Diagram — Visualizzare prenotazioni attive](../figure/act_visualizzare_prenotazioni.jpg)

*Activity Diagram — Visualizzare prenotazioni attive*


![Activity Diagram — Annullare prenotazione](../figure/act_annullare_prenotazione.jpg)

*Activity Diagram — Annullare prenotazione*


![Activity Diagram — Valutare il servizio](../figure/act_valutare_servizio.jpg)

*Activity Diagram — Valutare il servizio*


### Autista e Operatore di Sede AMA

Questi diagrammi modellano il flusso di lavoro logistico del personale sul campo: lo svolgimento del servizio, i controlli di conformità e la registrazione dell'esito.

![Activity Diagram — Registrare esito del ritiro (Autista)](../figure/act_autista_registrare_esito.jpg)

*Activity Diagram — Registrare esito del ritiro (Autista)*


![Activity Diagram — Verificare prenotazione del cittadino (Operatore di Sede)](../figure/act_operatore_verificare.jpg)

*Activity Diagram — Verificare prenotazione del cittadino (Operatore di Sede)*


![Activity Diagram — Registrare esito del conferimento (Operatore di Sede)](../figure/act_operatore_esito_conferimento.jpg)

*Activity Diagram — Registrare esito del conferimento (Operatore di Sede)*


### Amministratori (di Sede e Generale)

I processi amministrativi consentono di gestire le risorse umane, i mezzi logistici e la configurazione strutturale delle sedi.

![Activity Diagram — Generare codice di invito (Amministratore Sede)](../figure/act_admin_sede_genera_codice.png)

*Activity Diagram — Generare codice di invito (Amministratore Sede)*


![Activity Diagram — Gestire disponibilità della sede e fasce orarie](../figure/act_admin_sede_gestire_fasce.png)

*Activity Diagram — Gestire disponibilità della sede e fasce orarie*


![Activity Diagram — Gestire disponibilità dei lavoratori](../figure/act_admin_sede_gestire_lavoratori.png)

*Activity Diagram — Gestire disponibilità dei lavoratori*


![Activity Diagram — Generare codice amministratore di sede (Amministratore Generale)](../figure/act_generare_codice_admin.jpg)

*Activity Diagram — Generare codice amministratore di sede (Amministratore Generale)*


![Activity Diagram — Gestire disponibilità dei veicoli](../figure/act_admin_sede_gestire_veicoli.png)

*Activity Diagram — Gestire disponibilità dei veicoli*


![Activity Diagram — Rimuovere lavoratori dalla sede](../figure/act_admin_sede_rimuovere_lavoratori.png)

*Activity Diagram — Rimuovere lavoratori dalla sede*


![Activity Diagram — Gestire associazioni tra sede e zone/CAP](../figure/act_admin_sede_gestire_associazioni.png)

*Activity Diagram — Gestire associazioni tra sede e zone/CAP*


![Activity Diagram — Rimuovere amministratore di sede](../figure/act_rimuovere_admin.jpg)

*Activity Diagram — Rimuovere amministratore di sede*


% =========================================================================
% 5.2 SEQUENCE DIAGRAMS
% =========================================================================

## Sequence Diagrams

### Utente non registrato e Utente di sistema


![Sequence Diagram — Registrarsi come cittadino](../figure/seq_Utente_non_Registrazione_cittadino.jpg)

*Sequence Diagram — Registrarsi come cittadino*


![Sequence Diagram — Registrarsi tramite codice di invito](../figure/seq_registrazione_Tramite_codice_invito.jpg)

*Sequence Diagram — Registrarsi tramite codice di invito*


![Sequence Diagram — Effettuare accesso](../figure/seq_EseguiAccesso.jpg)

*Sequence Diagram — Effettuare accesso*


### Cittadino


![Sequence Diagram — Richiedere ritiro a domicilio](../figure/seq_DiagramRichiedereRitiroADomicilio.jpg)

*Sequence Diagram — Richiedere ritiro a domicilio*


![Sequence Diagram — Prenotare conferimento presso sede AMA](../figure/seq_DiagramPrenotaConferimento.jpg)

*Sequence Diagram — Prenotare conferimento presso sede AMA*


![Sequence Diagram — Visualizzare prenotazioni attive](../figure/seq_DiagramVisualizzarePrenotazioniAttive.jpg)

*Sequence Diagram — Visualizzare prenotazioni attive*


![Sequence Diagram — Annullare prenotazione](../figure/seq_DiagramAnnullarePrenotazione.jpg)

*Sequence Diagram — Annullare prenotazione*


![Sequence Diagram — Visualizzare storico prenotazioni](../figure/seq_DiagramVisualizzaStorico.jpg)

*Sequence Diagram — Visualizzare storico prenotazioni*


![Sequence Diagram — Valutare il servizio](../figure/seq_DiagramValutarePrenotazione.jpg)

*Sequence Diagram — Valutare il servizio*


### Autista AMA


![Sequence Diagram — Visualizzare ritiri assegnati](../figure/seq_Visualizzare_ritiri_assegnati.jpg)

*Sequence Diagram — Visualizzare ritiri assegnati*


![Sequence Diagram — Registrare esito del ritiro](../figure/seq_Registrare_esito_ritiro.jpg)

*Sequence Diagram — Registrare esito del ritiro*


![Sequence Diagram — Chiamare cittadino](../figure/seq_Chiamare_cittadino.jpg)

*Sequence Diagram — Chiamare cittadino*


### Operatore di Sede AMA


![Sequence Diagram — Visualizzare prenotazioni della sede](../figure/seq_SequenceVisualizzarePrenotazioniSede.jpg)

*Sequence Diagram — Visualizzare prenotazioni della sede*


![Sequence Diagram — Verificare prenotazione del cittadino](../figure/seq_SequenceVerificarePrenotazioneCittadino.jpg)

*Sequence Diagram — Verificare prenotazione del cittadino*


![Sequence Diagram — Registrare esito del conferimento](../figure/seq_SequenceRegistrareEsitoConferimento.jpg)

*Sequence Diagram — Registrare esito del conferimento*


### Amministratore di Sede AMA


![Sequence Diagram — Generare codice invito](../figure/seq_SequenceGenerareCodiceInvitoPersonale.jpg)

*Sequence Diagram — Generare codice invito*


![Sequence Diagram — Gestire disponibilità dei lavoratori](../figure/seq_SequenceGestireDisponibilitaLavoratori.jpg)

*Sequence Diagram — Gestire disponibilità dei lavoratori*


![Sequence Diagram — Gestire disponibilità dei veicoli](../figure/seq_SequenceGestireDisponibilitaVeicoli.jpg)

*Sequence Diagram — Gestire disponibilità dei veicoli*


![Sequence Diagram — Gestire disponibilità della sede e fasce orarie](../figure/seq_SequenceGestireDisponibilitaSede.jpg)

*Sequence Diagram — Gestire disponibilità della sede e fasce orarie*


![Sequence Diagram — Gestire associazioni tra sede e zone/CAP](../figure/seq_SequenceGestireAssociazioniSedeZoneCAP.jpg)

*Sequence Diagram — Gestire associazioni tra sede e zone/CAP*


![Sequence Diagram — Rimuovere personale](../figure/seq_SequenceRimuoverePersonaleAMA.jpg)

*Sequence Diagram — Rimuovere personale*


### Amministratore Generale AMA


![Sequence Diagram — Generare codice amministratore di sede](../figure/seq_AmministratoreGeneraleGeneraCodici.jpg)

*Sequence Diagram — Generare codice amministratore di sede*


![Sequence Diagram — Rimuovere amministratore di sede AMA](../figure/seq_RimuovereAmministratoreDiSedeAMA.jpg)

*Sequence Diagram — Rimuovere amministratore di sede AMA*


% =========================================================================
% 5.3 CLASS DIAGRAMS
% =========================================================================
## Class Diagrams


### Class Diagram Unrefined 

![Class Diagram — Versione Unrefined ](../figure/class_CLASS_DIAGRAM_unrefined.jpg)
*Class Diagram — Versione Unrefined*



### Class Diagram Refined 

![Class Diagram — Versione Refined (BCE e Struttura Consolidata)](../figure/class_CLASS_DIAGRAM_refined.jpg)
*Class Diagram — Versione Refined*





---

