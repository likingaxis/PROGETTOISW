# 📐 Guida Completa: Class Diagram Refined

> Basata sulla teoria del corso ISW (Prof. D'Ambrogio), sugli appunti Obsidian e sul progetto di riferimento **Buongiorno-Machowski** (Enjoy2Drive - Car Sharing).

---

## 1. Cos'è il Class Diagram Refined?

Il Class Diagram **Refined** è il modello statico **definitivo** del sistema, ottenuto **dopo** aver sviluppato i Sequence Diagram. Rappresenta l'evoluzione del Class Diagram Unrefined arricchito con:

- L'architettura **BCE (Boundary, Control, Entity)**
- Le **operazioni/metodi** estratte dai Sequence Diagram
- La **visibilità** (`+`, `-`, `#`) su attributi e metodi
- I **tipi di dato** formali e i **parametri tipizzati**
- Le **relazioni avanzate** (composizione, aggregazione, dipendenze)

```text
Requisiti / Use Case
        ↓
Class Diagram Unrefined  (solo Entity, attributi, associazioni)
        ↕
Activity + Sequence Diagram  (modello comportamentale con BCE)
        ↓
Class Diagram Refined  (modello strutturale completo e tipizzato)
        ↓
Applicazione Design Pattern  (GoF)
```

---

## 2. Unrefined vs Refined — Le Differenze

| Aspetto | Unrefined | Refined |
|---------|-----------|---------|
| **Classi presenti** | Solo **Entity** (dominio) | Entity + **Boundary** + **Control** |
| **Stereotipi UML** | Nessuno (o solo impliciti) | `<<entity>>`, `<<boundary>>`, `<<control>>`, `<<interface>>` |
| **Attributi** | Presenti, tipi ad alto livello | Presenti, **tipi formali** (String, int, Date, boolean…) |
| **Visibilità attributi** | Opzionale/assente | **Obbligatoria**: `-` private per tutti gli attributi Entity |
| **Operazioni/Metodi** | **Assenti** o minimali | **Completi**: derivati dai Sequence Diagram |
| **Firma dei metodi** | — | `+ nomeMetodo(param: Tipo): TipoRitorno` |
| **Relazioni** | Associazioni + molteplicità base | Associazioni + **Composizioni** ◆ + **Aggregazioni** ◇ + **Dipendenze** `<<use>>` |
| **Classi astratte** | Opzionali | In *corsivo*, con gerarchia completa |
| **Frecce tratteggiate** | Assenti | Presenti: **dipendenze BCE** |

> [!IMPORTANT]
> Il Refined **non si inventa da zero**: è la naturale evoluzione dell'Unrefined + tutto ciò che emerge dai Sequence Diagram.

---

## 3. L'Architettura BCE (Boundary - Control - Entity)

Questo è il **cuore** del passaggio Unrefined → Refined. Nel Refined, le classi sono organizzate in tre layer:

```text
┌─────────────────────────────────────────────────┐
│               BOUNDARY LAYER                     │
│  (Interfacce utente, form, schermate)            │
│  Stereotipo: <<boundary>>                        │
└────────────────────┬────────────────────────────┘
                     │  <<use>> (freccia tratteggiata)
                     ▼
┌─────────────────────────────────────────────────┐
│               CONTROL LAYER                      │
│  (Coordinatori UC, logica di business)           │
│  Stereotipo: <<control>>                         │
└────────┬──────────────────────────┬─────────────┘
         │  <<use>>                 │  <<use>>
         ▼                         ▼
┌──────────────────┐    ┌──────────────────────────┐
│  ALTRI CONTROL   │    │      ENTITY LAYER        │
│  (Factory, ecc.) │    │  (Dati dominio, CRUD)    │
└──────────────────┘    │  Stereotipo: <<entity>>  │
                        └──────────────────────────┘
```

### 3.1 Regole di Comunicazione BCE

> [!CAUTION]
> Queste regole sono **inviolabili** e il prof le controlla:

| Da → A | Boundary | Control | Entity |
|--------|----------|---------|--------|
| **Boundary** | ❌ | ✅ | ❌ |
| **Control** | ✅ (risposte) | ✅ | ✅ |
| **Entity** | ❌ | ✅ (risposte) | ✅ |

- **Boundary** → può invocare **solo** Control. **MAI direttamente Entity**.
- **Control** → può comunicare con altri Control e con Entity.
- **Entity** → non comunica mai con i Boundary; risponde solo ai Control.

### 3.2 Cosa sono in pratica?

| Tipo | Cosa rappresenta | Esempi (da Buongiorno-Machowski) | Esempi (MyAma) |
|------|-------------------|----------------------------------|-----------------|
| **Boundary** | Schermate/interfacce utente | `ModuloRegistrazione`, `SchermataLogin`, `SchermataMappaCliente`, `InterfacciaAdmin` | `HomeBookInterface`, `PannelloAutistaUI`, `PannelloSedeUI`, `RegistrationInterface` |
| **Control** | Coordinatori di logica | `RegistrazioneController`, `NoleggioController`, `FlottaController`, `TariffazioneController` | `GestoreRitiriController`, `AMAServiceController`, `AccettazioneController` |
| **Entity** | Dati persistenti del dominio | `Cliente`, `Veicolo`, `Prenotazione`, `Noleggio`, `Tariffa` | `Cittadino`, `Prenotazione`, `Rifiuto`, `SedeAMA`, `Veicolo` |

---

## 4. Tipi di Frecce e Relazioni — Guida Visiva

Questa è la parte più importante da sapere in Visual Paradigm:

### 4.1 Freccia Tratteggiata con Punta Aperta → **Dipendenza `<<use>>`**

```text
  Boundary - - - - - -> Control - - - - - -> Entity
             <<use>>              <<use>>
```

- **Quando usarla**: Per collegare classi BCE tra layer diversi
- **Significato**: "questa classe *usa/dipende da* quest'altra"
- **Direzione**: Dalla classe che dipende → verso la classe utilizzata
- **In Visual Paradigm**: "Dependency" con stereotipo `<<use>>`

> [!TIP]
> Le frecce tratteggiate `<<use>>` sono il **marchio di fabbrica** del Refined rispetto all'Unrefined. Se non le hai, non è un Refined.

### 4.2 Freccia Continua con Triangolo Vuoto → **Generalizzazione (Ereditarietà)**

```text
  AutistaAMA ───────▷ LavoratoreAMA (astratta, in corsivo)
  OperatoreSedeAMA ──▷ LavoratoreAMA
```

- **Quando usarla**: Relazione "è-un" (is-a), ereditarietà
- **Direzione**: Dalla sottoclasse → verso la superclasse
- **Regola**: La sottoclasse **eredita** attributi e operazioni → **NON ridichiarare** nella sottoclasse gli attributi/metodi ereditati (a meno di override)
- **Classi astratte**: Il nome va in *corsivo*. Non possono essere istanziate.

### 4.3 Linea Continua → **Associazione**

```text
  Cittadino ————————— Prenotazione
           1          0..*
```

- **Quando usarla**: Per relazioni strutturali tra Entity
- **Molteplicità obbligatoria** su entrambi gli estremi: `1`, `0..1`, `1..*`, `0..*`
- **Nome dell'associazione** opzionale (es. `effettua`, `gestisce`, `contiene`)
- **Role names** alle estremità (opzionali ma utili)

### 4.4 Rombo Pieno ◆ → **Composizione (Strong Containment)**

```text
  Prenotazione ◆————— Valutazione
               1       0..1
```

- **Quando usarla**: Quando il componente **non può esistere** senza il contenitore
- **Significato**: Se cancello `Prenotazione`, cancello anche `Valutazione`
- **Regola**: *Existence dependency* — il rombo pieno sta dal lato del "tutto"

### 4.5 Rombo Vuoto ◇ → **Aggregazione (Weak Containment)**

```text
  SedeAMA ◇————— Veicolo
          1       0..*
```

- **Quando usarla**: Quando il componente **può esistere** indipendentemente
- **Significato**: `Veicolo` esiste anche se `SedeAMA` viene eliminata
- **Regola**: Il rombo vuoto sta dal lato del "tutto"

### 4.6 Riepilogo Visivo Frecce

| Freccia | Stile Linea | Punta | Nome UML | Uso |
|---------|-------------|-------|----------|-----|
| `- - ->` | **Tratteggiata** | Aperta (>) | **Dipendenza** `<<use>>` | Boundary→Control, Control→Entity |
| `───▷` | **Continua** | Triangolo vuoto (▷) | **Generalizzazione** | Ereditarietà (sottoclasse→superclasse) |
| `─────` | **Continua** | Nessuna (o navigabilità) | **Associazione** | Relazione tra Entity |
| `◆────` | **Continua** | Rombo pieno | **Composizione** | Contenimento forte (vita dipendente) |
| `◇────` | **Continua** | Rombo vuoto | **Aggregazione** | Contenimento debole (vita indipendente) |
| `- -▷` | **Tratteggiata** | Triangolo vuoto | **Realizzazione** | Classe che implementa interfaccia |

---

## 5. Visibilità dei Membri

Nel Refined la visibilità è **obbligatoria** su ogni attributo e metodo:

| Simbolo | Significato | Quando usarlo |
|---------|-------------|---------------|
| `-` | **Private** | **Tutti gli attributi** delle Entity (Information Hiding!) |
| `+` | **Public** | **Metodi** invocati nei Sequence Diagram |
| `#` | **Protected** | Attributi/metodi ereditabili nelle gerarchie |
| `~` | **Package** | Stesso package (raro nei progetti d'esame) |

> [!WARNING]
> **Regola fondamentale**: Nel Refined, gli attributi delle Entity sono **sempre `private` (`-`)**. I metodi esposti sono **`public` (`+`)**. Non sbagliare, il prof ci tiene.

Esempio di classe Entity nel Refined:

```text
┌──────────────────────────────────┐
│        <<entity>>                │
│        Prenotazione              │  ← in corsivo se astratta
├──────────────────────────────────┤
│ - id: int                        │  ← tutti private
│ - dataCreazione: Date            │
│ - stato: String                  │
│ - indirizzo: String              │
├──────────────────────────────────┤
│ + getId(): int                   │  ← getter pubblici
│ + getStato(): String             │
│ + setStato(stato: String): void  │  ← setter pubblici
│ + aggiornaStato(esito: String): void │  ← metodo da Sequence
│ + calcolaCosto(): double         │  ← metodo di business
└──────────────────────────────────┘
```

---

## 6. Come Derivare le Operazioni (la Regola d'Oro)

> [!IMPORTANT]
> **Le operazioni del Refined NON si inventano**. Si estraggono meccanicamente dai Sequence Diagram.

### 6.1 Mappatura Messaggi → Metodi

Ogni **messaggio** nei Sequence Diagram diventa un **metodo pubblico** della classe destinataria:

```text
Sequence Diagram:                          Class Diagram Refined:
                                          
  :Control ──── modificaStato(esito) ────>  :Entity
                                           
  diventa:
                                          
  Entity:  + modificaStato(esito: String): void
```

$$\text{Messaggio in SD: } \texttt{areYouValid()} \longrightarrow \text{Metodo in CD: } \texttt{+ areYouValid(): boolean}$$

### 6.2 Criterio CRUD per le Entity

Oltre ai metodi dai Sequence, ogni Entity deve avere le operazioni CRUD di base:

| Operazione | Significato | Esempio |
|------------|-------------|---------|
| **Create** | Costruttore | `+ Prenotazione(data: Date, tipo: String)` |
| **Read** | Getter | `+ getId(): int`, `+ getStato(): String` |
| **Update** | Setter / modificatori | `+ setStato(stato: String): void` |
| **Delete** | Cancellazione | `+ eliminaPrenotazione(): void` |

### 6.3 Workflow Pratico

```text
1. Prendi un Sequence Diagram
2. Per ogni messaggio (freccia) che arriva a un oggetto:
   - Identifica la CLASSE destinataria
   - Il nome del messaggio = nome del METODO
   - I parametri del messaggio = parametri del METODO
   - Aggiungi il metodo come + (public) nella classe
3. Ripeti per TUTTI i Sequence Diagram
4. Alla fine, per ogni Entity aggiungi getter/setter/costruttore se mancanti
```

---

## 7. Checklist Pratica: Come Costruire il Refined

### Step 1 — Parti dall'Unrefined
- Copia tutte le Entity Class con i loro attributi e associazioni
- Aggiungi lo stereotipo `<<entity>>` a tutte

### Step 2 — Aggiungi i Boundary
- Una classe Boundary per ogni **interfaccia utente** (schermata, form, pagina) menzionata nei Sequence Diagram
- Stereotipo `<<boundary>>`
- Metodi: quelli che raccolgono input e mostrano output (es. `mostraErrore()`, `mostraConferma()`, `inserisciDati()`)

### Step 3 — Aggiungi i Control
- Un controller per ogni **area funzionale** o **Use Case principale**
- Stereotipo `<<control>>`
- Metodi: la logica di coordinamento (es. `verificaDisponibilita()`, `creaPrenotazione()`, `assegnaAutista()`)

### Step 4 — Estrai le Operazioni dai Sequence
- Per **ogni** Sequence Diagram, scorri tutti i messaggi
- Ogni messaggio → metodo pubblico nella classe destinataria
- Includi parametri e tipi di ritorno

### Step 5 — Aggiungi Visibilità e Tipi
- Tutti gli attributi Entity → `- private`
- Tutti i metodi invocati → `+ public`
- Tipizza ogni attributo: `String`, `int`, `Date`, `boolean`, `double`, ecc.
- Tipizza ogni parametro e ritorno dei metodi

### Step 6 — Disegna le Relazioni
- **Associazioni** (linea continua) tra Entity, con molteplicità
- **Composizioni** (◆) dove c'è dipendenza di esistenza
- **Aggregazioni** (◇) dove il componente può vivere da solo
- **Generalizzazioni** (▷) per le gerarchie (classi astratte in corsivo)
- **Dipendenze `<<use>>`** (tratteggiata) tra Boundary→Control e Control→Entity

### Step 7 — Verifica Coerenza
- ✅ Ogni messaggio dei Sequence è un metodo nel Refined
- ✅ Nessun arco diretto Boundary → Entity
- ✅ Classi astratte in corsivo
- ✅ Attributi ereditati NON ridichiarati nelle sottoclassi
- ✅ Molteplicità su tutte le associazioni
- ✅ Stereotipi su tutte le classi

---

## 8. Esempio dal Progetto Buongiorno-Machowski

Il progetto di riferimento (**Enjoy2Drive - Car Sharing**) ha questa struttura nel Refined:

### 8.1 Entity (Dominio)
- `Utente` (superclasse) → `Cliente`, `Operatore`, `OperatoreLogistica`, `Amministratore`
- `Veicolo`, `Prenotazione`, `Noleggio`, `Tariffa`, `AreaOperativa`, `Ticket`, `TaskIntervento`
- Tutti con attributi `private (-)` e metodi `public (+)`
- Metodi di business: `calcolaCostoTotale()`, `aggiornaStato()`, `verificaCoordinate()`

### 8.2 Boundary (Interfacce)
- `ModuloRegistrazione`, `SchermataLogin`, `InterfacciaAdmin`, `InterfacciaOperatore`, `SchermataMappaCliente`, `SchermataAreaPersonale`, `ModuloTicket`

### 8.3 Control (Coordinatori)
- `RegistrazioneController`, `AutenticazioneController`, `NoleggioController`, `FlottaController`, `TariffazioneController`, `PersonaleController`, `TaskController`, `TicketController`

### 8.4 Relazioni BCE
- Frecce **tratteggiate** `<<use>>` da ogni Boundary verso il rispettivo Controller
- Frecce **tratteggiate** `<<use>>` da ogni Controller verso le Entity che manipola
- **Nessun** arco diretto Boundary → Entity

---

## 9. Conteggio Classi Atteso (da MyAma come riferimento)

Un progetto ben fatto si aggira intorno a **40-50 classi** nel Refined:

| Tipo | Conteggio MyAma | Percentuale |
|------|-----------------|-------------|
| Entity | ~19 | ~41% |
| Boundary | ~14 | ~30% |
| Control | ~13 | ~28% |
| **Totale** | **~46** | 100% |

---

## 10. Errori Comuni da Evitare

> [!CAUTION]
> Il prof controlla queste cose:

| ❌ Errore | ✅ Corretto |
|-----------|-------------|
| Boundary che parla direttamente con Entity | Boundary → Control → Entity |
| Attributi senza visibilità | Sempre `-`, `+`, `#` |
| Metodi inventati senza base nel Sequence | Metodi estratti dai Sequence Diagram |
| Attributi ereditati ridichiarati nella sottoclasse | Solo nella superclasse |
| Frecce tratteggiate usate per associazioni | Tratteggiate = dipendenze; Continue = associazioni |
| Classe astratta non in corsivo | Corsivo obbligatorio |
| Molteplicità mancanti | Sempre su entrambi gli estremi |
| Nessuno stereotipo | `<<entity>>`, `<<boundary>>`, `<<control>>` su tutte le classi |
| Un unico mega-Controller per tutto | Un Controller per area funzionale / UC |

---

## 11. Glossario Rapido Notazione

| Termine | Significato |
|---------|-------------|
| `<<entity>>` | Classe dati persistente del dominio |
| `<<boundary>>` | Classe interfaccia utente |
| `<<control>>` | Classe coordinatrice di logica |
| `<<interface>>` | Contratto di metodi (usata nei Design Pattern) |
| `<<use>>` | Stereotipo sulla freccia tratteggiata di dipendenza |
| *NomeInCorsivo* | Classe astratta (non istanziabile) |
| `/attributo` | Attributo derivato (calcolato a runtime) |
| `$attributo` | Attributo statico (di classe, condiviso) |

---

> [!TIP]
> **Ricorda la sequenza logica**: prima fai i Sequence Diagram con BCE, poi costruisci il Refined estraendo meccanicamente i metodi. Non fare il contrario!
