# 📋 Registro delle Decisioni e Convenzioni — *MyAma*

Questo documento raccoglie le decisioni concordate dal gruppo (Fase 0 di [`divisione-compiti.md`](../../guide/divisione-compiti.md) e [`guida-operativa.md`](../../guide/guida-operativa.md)) per garantire coerenza terminologica e formale in tutta la specifica.

---

## 🏷️ 1. Terminologia Standard del Dominio

Per evitare ambiguità nella stesura dei requisiti e dei diagrammi, useremo i seguenti termini standard:

| Concetto | Termine Concordato | Termini da Evitare / Sinonimi | Note |
|---|---|---|---|
| Utente finale del servizio | **Cliente** (o **Cittadino Registrato**) | *User*, *Fruitore*, *Persona* | Identifica chi prenota il ritiro o conferimento |
| Luogo fisico di raccolta | **Sede AMA** / **Centro di Raccolta** | *Isola ecologica*, *Discarica* | Struttura presidiata con varchi e orari |
| Operatore che guida il mezzo | **Autista AMA** | *Guidatore*, *Fattorino* | Addetto ai ritiri a domicilio |
| Addetto al varco in sede | **Operatore di Sede** | *Guardiano*, *Controllore* | Addetto alla verifica e convalida scarico |
| Amministrazione & Logistica | **Responsabile AMA** / **Amministratore** | *Admin*, *Gestore* | Assegna turni, monitora zone e tariffari |

---

## 🔢 2. Convenzioni di Numerazione e Identificativi (ID)

### Use Case:
- `UC-CLI-xx`: Casi d'uso relativi all'attore **Cliente / Cittadino** (es. `UC-CLI-01: Richiesta Ritiro a Domicilio`)
- `UC-AUT-xx`: Casi d'uso relativi all'attore **Autista AMA** (es. `UC-AUT-01: Consultazione Itinerario`)
- `UC-OPS-xx`: Casi d'uso relativi all'attore **Operatore di Sede** (es. `UC-OPS-01: Convalida Conferimento`)
- `UC-ADM-xx`: Casi d'uso relativi all'attore **Responsabile / Amministratore** (es. `UC-ADM-01: Gestione Sedi e Zone`)

### Requisiti:
- `RF-xx`: Requisito Funzionale Utente / Sistema (es. `RF-01: Prenotazione Ritiro a Domicilio`)
- `RNF-xx`: Requisito Non Funzionale (es. `RNF-01: Tempo di Risposta Calcolo Tariffa`)
- `RD-xx`: Requisito di Dominio (es. `RD-01: Vincolo di Capacità Massima del Veicolo`)

---

## 💻 3. File Visual Paradigm & Asset Grafici

- **File Principale UML**: `visual-paradigm/MyAma.vpp`
- **Esportazione Diagrammi**: Formato `.png` (ad alta risoluzione) salvati in `visual-paradigm/diagrammi/`
- **Convenzione Nomi Diagrammi**:
  - `UCD_Generale.png`, `UCD_Cliente.png`, `UCD_Autista.png`
  - `AD_RitiroDomicilio.png`, `AD_ConferimentoSede.png`
  - `SD_RichiestaRitiro.png`, `SD_ConvalidaConferimento.png`
  - `CD_Unrefined.png`, `CD_Refined.png`
