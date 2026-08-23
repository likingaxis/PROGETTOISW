# 🎨 Prompt Immagine — Cover Page MyAma

> File di riferimento per ricreare o modificare la cover page del progetto MyAma.  
> Utilizzabile su: **Antigravity (Nano Banana)**, Midjourney, DALL·E, Ideogram, Leonardo AI, etc.

---

## 📐 Impostazioni generali

| Parametro       | Valore                  |
|-----------------|-------------------------|
| Aspect Ratio    | `3:4` (verticale, A4)   |
| Stile           | Flat/Corporate premium  |
| Sfondo          | Bianco `#FFFFFF`        |
| Colore primario | Giallo AMA `#F5C518`    |
| Colore secondario | Porpora AMA `#9B1B30` |
| Testo           | Dark charcoal `#1A1A2E` |

---

## ✏️ Prompt completo (Versione Minimale & Compatta)

```
Design an elegant university project cover page for "MyAma", portrait oriented (A4 document page).

Background design:
- Clean white background (#FFFFFF)
- Abstract flowing ribbon-like wave shapes sweeping across the page diagonally 
  from top-right to bottom-left
- The ribbons use AMA Roma's official colors: golden yellow (#F5C518) and 
  deep porpora/amaranth (#9B1B30)
- The yellow and porpora ribbons intertwine, twist and overlap each other 
  creating a dynamic flowing effect with depth and subtle shadows
- Two main groups of ribbons: one cluster in the upper-right area, 
  one cluster in the lower-left area, framing the central content
- Ribbons are smooth, glossy, 3D-like with soft lighting
- No recycling symbols or extra icons

Content layout (top to bottom, all text in dark charcoal #1A1A2E):

1. TOP HEADER (clean and modern):
   - Top-left: Small green seal/logo of Università degli Studi di Roma "Tor Vergata"
   - Top area: "Progetto di Ingegneria del Software" in elegant medium sans-serif font

2. CENTER OF THE PAGE — MyAma logo (large and prominent):
   - A stylized icon above the text: a golden yellow (#F5C518) leaf shape with a 
     porpora (#9B1B30) hand silhouette inside it
   - Below the icon: "MyAma" wordmark, "My" in golden yellow, 
     "Ama" in porpora/amaranth, bold modern sans-serif font

3. BELOW THE LOGO (subtitle):
   - "Specifica dei Requisiti Software" in dark charcoal, 
     elegant medium-weight font, centered

4. BOTTOM AREA — Authors in alphabetical order (by last name):
   - Line 1: "Valerio Bernardi • Samuele De Santis"
   - Line 2: "Alfredo Grande • Luca Gugliotta • Davide Luci"

5. VERY BOTTOM:
   - "A.A. 2025/2026" in smaller dark charcoal text

Style: modern, premium, sleek, minimalist academic document cover. 
The intertwining ribbons in yellow and porpora add dynamism without 
cluttering the central area which remains clean and readable on the 
white background. Overall mood is institutional, polished and high-end.
```

---

## 🔧 Come modificare

### Cambiare il corso / anno
Modifica le righe nella sezione **Top center**:
```
"Progetto di Ingegneria del Software"  →  "Progetto di [Nome Corso]"
"2025/2026"                            →  "20XX/20XX"
```

### Cambiare gli autori
Modifica la riga nella sezione **Bottom area**, mantenendo l'ordine alfabetico per cognome:
```
"Nome1 Cognome1 • Nome2 Cognome2 • ..."
```

### Cambiare il sottotitolo del progetto
Modifica la riga nella sezione **Below the logo**:
```
"Gestione prenotazioni per rifiuti ingombranti"  →  "[Nuovo sottotitolo]"
```

### Cambiare lo sfondo
- **Sfondo nero**: sostituire `white background (#FFFFFF)` con `dark charcoal background (#1A1A2E)` e cambiare il colore del testo da `dark charcoal` a `white (#FFFFFF)`
- **Sfondo colorato**: specificare il colore desiderato

### Cambiare i colori delle ribbon
Sostituire i codici colore:
```
golden yellow (#F5C518)     →  [nuovo colore primario]
porpora/amaranth (#9B1B30)  →  [nuovo colore secondario]
```

### Aggiungere icone extra
Aggiungere nella sezione desiderata, ad esempio:
```
- Add a small stylized [descrizione icona] icon in [colore], placed [posizione]
```

---

## 🛠️ Parametri per piattaforme specifiche

| Piattaforma   | Suffisso / Impostazione consigliata                        |
|---------------|-------------------------------------------------------------|
| Midjourney    | `--ar 3:4 --style raw --s 250`                             |
| Ideogram      | Stile: "Graphic Design" / "Typography"                     |
| Leonardo AI   | Modello: "Kino XL", Preset: "Creative"                     |
| DALL·E        | Nessun suffisso necessario, specificare "portrait oriented" |
| Antigravity   | AspectRatio: `3:4`                                          |

---

## 📝 Note

- Il testo generato dall'AI potrebbe avere piccole imperfezioni tipografiche. 
  Per la versione definitiva del documento, è consigliabile:
  1. Usare solo lo **sfondo con le ribbon** come immagine di fondo
  2. Sovrapporre **logo ritagliato** e **testo reale** tramite Word, LaTeX, Canva o Figma
- I colori giallo e porpora sono i colori ufficiali di **AMA Roma S.p.A.** 
  (Azienda Municipale Ambiente), ispirati ai colori storici della città di Roma
