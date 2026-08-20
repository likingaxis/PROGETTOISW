# 🔗 Matrice di Tracciabilità — *MyAma*

Questo documento mappa la corrispondenza bidirezionale tra **Requisiti Utente (UR)**, **Use Case (UC)**, **System Requirements (SR)** e le **Classi OOA / Design Pattern** del sistema MyAma.

---

## 📊 Matrice Requisiti ↔ Use Case ↔ Diagrammi

| ID Requisito | Descrizione Sintetica | Use Case Associato | Sequence Diagram | Classi / Pattern Coinvolti |
|---|---|---|---|---|
| **RF-01** | Prenotazione ritiro a domicilio | `UC-CLI-01` | `SD_RichiestaRitiro` | `PrenotazioneDomicilio`, `Veicolo`, `Richiesta` |
| **RF-02** | Prenotazione conferimento in sede | `UC-CLI-02` | `SD_PrenotazioneSede` | `PrenotazioneSede`, `SedeAMA`, `SlotOrario` |
| **RF-03** | Calcolo preventivo e tariffa ritiro | `UC-CLI-03` | `SD_CalcoloTariffa` | Pattern *Strategy* (`CalcoloTariffaStrategy`) |
| **RF-04** | Consultazione itinerario e carichi autista | `UC-AUT-01` | `SD_ItinerarioAutista` | `Autista`, `Itinerario`, `Veicolo` |
| **RF-05** | Registrazione esito ritiro | `UC-AUT-02` | `SD_EsitoRitiro` | Pattern *State* (`StatoPrenotazione`) |
| **RF-06** | Convalida conferimento al varco | `UC-OPS-01` | `SD_ConvalidaVarco` | `OperatoreSede`, `Conferimento`, `SedeAMA` |
| **RF-07** | Gestione anagrafica mezzi e zone/CAP | `UC-ADM-01` | `SD_GestioneRisorse` | `Amministratore`, `ZonaCAP`, `Flotta` |

---

## 🧪 Matrice di Verificabilità & Test Case

| ID Requisito | Criterio di Accettazione | Metodo di Verifica (Inspection / Analysis / Test / Demo) |
|---|---|---|
| **RF-01** | La richiesta è confermata solo se il CAP è servito e il carico $\le$ limite veicolo. | Test Funzionale con input CAP valido/invalido e peso limite. |
| **RNF-01** | Il tempo di generazione del preventivo deve essere $\le 2.0$ secondi. | Test di Prestazione / Benchmark con carico simulato. |
| **RD-01** | Il peso totale assegnato a un mezzo non può superare la portata massima omologata. | Analisi statica dei vincoli di consistenza e invarianti di classe. |
