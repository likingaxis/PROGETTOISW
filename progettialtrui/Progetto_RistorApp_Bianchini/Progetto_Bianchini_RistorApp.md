# 📄 Specifica di Progetto: RistorApp

> **Autori**: Massimo Bianchini, Mattia Corsetti, Nicolò Mazzenga  
> **Pagine totali**: 80  
> **Trascrizione**: Estratta dal documento originale per consultazione testuale diretta.

---


<!-- Pagina PDF 1 -->
## 📑 Pagina 1

    RistorApp
Massimo  Bianchini  0339736
Mattia  Corsetti  0343167
Nicolò  Mazzenga  0308288


---

<!-- Pagina PDF 2 -->
## 📑 Pagina 2

 1.  PREFAZIONE ..................................................................................................................................................... 4 2.  INTRODUZIONE ............................................................................................................................................... 5 3.  GLOSSARIO ....................................................................................................................................................... 6 4.  USER  REQUIREMENTS  DEFINITION ......................................................................................................... 8 4.1.  Use  Case  Utente .......................................................................................................................................... 8 4.1.1.  Diagramma ....................................................................................................................................... 8 4.1.2.  Documentazione ............................................................................................................................... 8 4.2.  Use  Case  Personale ................................................................................................................................... 13 4.2.1.  Diagramma ..................................................................................................................................... 13 4.2.2.  Documentazione ............................................................................................................................. 13 4.3.  Use  Case  Cliente ....................................................................................................................................... 16 4.3.1.  Diagramma ..................................................................................................................................... 16 4.3.2.  Documentazione ............................................................................................................................. 16 4.4.  Use  Case  Cameriere .................................................................................................................................. 20 4.4.1.  Diagramma ..................................................................................................................................... 20 4.4.2.  Documentazione ............................................................................................................................. 20 4.5.  Use  Case  Cuoco ........................................................................................................................................ 24 4.5.1.  Diagramma ..................................................................................................................................... 24 4.5.2.  Documentazione ............................................................................................................................. 24 4.6.  Use  Case  Manager .................................................................................................................................... 26 4.6.1.  Diagramma ..................................................................................................................................... 26 4.6.2.  Documentazione ............................................................................................................................. 26 5.  REQUISITI  DI  SISTEMA ............................................................................................................................... 30 5.1.  Requisiti  funzionali ................................................................................................................................... 30 5.2.  Requisiti  non  funzionali ............................................................................................................................ 33 5.3.  Requisiti  di  dominio ................................................................................................................................. 35 6.  SYSTEM  ARCHITECTURAL  MODEL ....................................................................................................... 36 6.1.  Activity  Diagrams ..................................................................................................................................... 36 6.1.1.  Activity  Diagrams  Utente ............................................................................................................... 36 6.1.2.  Activity  Diagrams  Personale .......................................................................................................... 41 6.1.3.  Activity  Diagrams  Cliente .............................................................................................................. 43 6.1.4.  Activity  Diagrams  Cameriere ......................................................................................................... 48 6.1.5.  Activity  Diagrams  Cuoco ............................................................................................................... 52 6.1.6.  Activity  Diagrams  Manager ........................................................................................................... 54 6.2.  Sequence  Diagrams .................................................................................................................................. 60 6.2.1.  Sequence  Diagram  Utente .............................................................................................................. 60 6.2.2.  Sequence  Diagrams  Personale ........................................................................................................ 64 6.2.3.  Sequence  Diagrams  Cliente ............................................................................................................ 66 6.2.4.  Sequence  Diagrams  Cameriere ....................................................................................................... 69 6.2.5.  Sequence  Diagrams  Cuoco ............................................................................................................. 72 6.2.6.  Sequence  Diagrams  Manager ......................................................................................................... 74 6.3.  Class  Diagrams ......................................................................................................................................... 78 6.3.1.  Class  Diagram  Unrefined ............................................................................................................... 78 6.3.2.  Class  Diagram  Refined ................................................................................................................... 79 7.  DESIGN  PATTERN .......................................................................................................................................... 80 7.1.  Observer .................................................................................................................................................... 80 7.2.  Factory  method ......................................................................................................................................... 81


---

<!-- Pagina PDF 3 -->
## 📑 Pagina 3

1.  PREFAZIONE   Il  documento  di  specifica  dei  requisiti  che  segue  è  costruito  per  essere  consultato  da  diverse  categorie
di
destinatari:
 ●  Stakeholder  e  Utenti  Finali:  I  manager,  i  cuochi  e  i  camerieri  del  ristorante,  i  quali
utilizzeranno
questo
documento
per
verificare
che
i
requisiti
definiti
soddisfino
pienamente
le
loro
necessità
operative
 ●  Progettisti  e  Sviluppatori:  Il  team  tecnico  incaricato  di  utilizzare  questa  specifica  come  linea
guida
fondamentale
per
comprendere
cosa
deve
essere
sviluppato
e
per
pianificare
la
progettazione
e
la
codifica
del
sistema.
 ●  Ingegneri  di  Collaudo:  Il  personale  addetto  alla  Qualità  e  al  Testing,  che  sfrutterà  i  requisiti
qui
delineati
per
sviluppare
casi
di
test
e
validare
la
correttezza
del
software.
 ●  Ingegneri  Manutentori:  Le  figure  che  interverranno  sul  software  in  futuro,  alle  quali  il
documento
fornirà
una
chiara
comprensione
del
sistema
e
delle
relazioni
tra
le
sue
componenti.


---

<!-- Pagina PDF 4 -->
## 📑 Pagina 4

2.  INTRODUZIONE   Il  software  è  progettato  per  facilitare  la  gestione  operativa  di  un'attività  di  ristorazione  moderna,
automatizzando
la
presa
in
carico
degli
ordini
e
le
attività
amministrative
al
fine
di
ridurre
il
rischio
di
errori
e
ottimizzare
l'efficienza
del
personale
di
sala
e
di
cucina.
Il
ristorante
opera
gestendo
flussi
di
lavoro
eterogenei,
come
le
ordinazioni
ai
tavoli
fisici,
l'asporto
e
il
delivery,
coinvolgendo
diversi
attori
con
ruoli
ben
definiti.
 I  clienti,  tramite  il  portale  o  l'applicazione,  possono  effettuare  ordinazioni  direttamente  dal  proprio
tavolo,
oppure
prenotare
ordini
per
l'asporto
e
la
consegna
a
domicilio
selezionando
le
pietanze
dal
menù
digitale.
Una
volta
confermato
l'ordine,
il
sistema
consente
al
cliente
di
seguirne
lo
stato
di
preparazione
e
di
effettuare
il
pagamento
digitale.
Al
termine
del
pasto,
il
cliente
può
lasciare
una
recensione
pubblica
consultabile
da
altri
utenti.
 Parallelamente,  il  personale  del  ristorante  svolge  attività  operative  distinte:  i  camerieri  gestiscono
l'assegnazione
dei
tavoli,
inseriscono
ordini
manualmente
per
i
clienti
sprovvisti
di
smartphone
e
monitorano
lo
stato
delle
comande;
i
cuochi
ricevono
e
processano
gli
ordini
direttamente
sui
monitor
in
cucina,
dove
le
comande
vengono
smistate
e
ordinate
per
priorità
e
tipologia;
i
manager
supervisionano
l'intera
infrastruttura
gestionale,
aggiornando
il
menù,
coordinando
i
turni
del
personale
e
analizzando
l'andamento
economico
tramite
un
modulo
di
reportistica.
 Il  sistema  supporta  anche  la  gestione  degli  account  interni  per  i  dipendenti  e  garantisce  comunicazioni
tempestive
tramite
notifiche,
inviate
per
avvisare,
ad
esempio,
i
camerieri
o
i
clienti
quando
un
ordine
è
pronto
per
essere
servito
o
ritirato.
Gli
utenti
non
registrati
possono
consultare
il
menù
e
le
informazioni
pubbliche
del
locale,
mentre
gli
utenti
autenticati
hanno
accesso
a
funzionalità
avanzate
come
lo
storico
degli
ordini
e
la
gestione
dei
pagamenti
rapidi.
 L'obiettivo  finale  del  sistema  è  semplificare  la  gestione  della  ristorazione,  offrire  un  servizio  rapido  e
innovativo
ai
clienti
e
fornire
al
personale
uno
strumento
centralizzato
per
migliorare
la
qualità
del
lavoro.
   Il  prodotto  prevede  l'interazione  e  l'integrazione  con  sistemi  esterni:  ●  Gateway  di  Pagamento  Elettronico  (es.  PayPal,  Stripe  o  circuiti  bancari):  Interfacciamento
necessario
per
processare
in
modo
sicuro
i
pagamenti
digitali
effettuati
dai
clienti
per
gli
ordini
al
tavolo,
l'asporto
e
il
delivery,
delegando
a
tali
sistemi
esterni
la
validazione
e
la
transazione
economica.
 ●  Gateway  di  Comunicazione  (Email/SMS):  Interazione  con  server  SMTP  e  provider  di
telecomunicazioni
per
l'invio
automatizzato
di
notifiche
push,
messaggi
di
conferma
ordine
e
avvisi
sullo
stato
della
consegna
diretti
ai
clienti.
 ●  Servizi  di  Mapping  e  Geolocalizzazione  (es.  Google  Maps  API):  Integrazione  impiegata  per  la
validazione
degli
indirizzi
inseriti
dagli
utenti
e
per
l'ottimizzazione
dei
percorsi
di
consegna
a
domicilio
(delivery).
 ●  Sistemi  Fiscali  e  Registratori  di  Cassa  Telematici:  Collegamento  con  i  sistemi  di  fatturazione
elettronica
e
registratori
di
cassa
hardware
presenti
fisicamente
nel
locale
per
l'emissione
automatica
di
scontrini
e
ricevute
fiscali
al
momento
del
pagamento.
 ●  Piattaforme  Esterne  di  Delivery:  L'interfacciamento  con  servizi  di  terze  parti  per  la  gestione
logistica
delle
consegne
a
domicilio.
Il
software
gestisce
la
ricezione
dell'ordine
e
la
preparazione
interna,
delegando
a
questi
applicativi
esterni
il
trasporto
fisico,
l'assegnazione
del
fattorino
e
l'aggiornamento
finale
dello
stato
in
"Consegnato"
verso
il
cliente.


---

<!-- Pagina PDF 5 -->
## 📑 Pagina 5

3.  GLOSSARIO    Termine  Descrizione
Sistema  L'applicazione  software  progettata  per  la  gestione  automatizzata  e  completa  del  ristorante.
Portale  /  Applicazione  L'interfaccia  web  o  mobile  tramite  la  quale  gli  utenti  (clienti  e  personale)  interagiscono  con  il  sistema.
Utente  (Generico)  Entità  astratta  che  rappresenta  una  qualsiasi  persona  che  interagisce  con  il  sistema.  Funge  da  attore  base  da  cui  derivano  le  tipologie  specializzate  (Registrato  e  Non  Registrato),  raggruppando  le  interazioni  comuni.
Utente  (Non  Registrato)  Persona  che  accede  al  portale  senza  possedere  o  utilizzare  un  account,  limitandosi  a  consultare  le  informazioni  pubbliche  (es.  menù,  orari).
Utente  Registrato  Utente  che  ha  creato  un  account  nel  sistema,  ottenendo  l'accesso  a  funzionalità  avanzate  (es.  storico  ordini,  gestione  metodi  di  pagamento).
Cliente  Utente  (autenticato  o  al  tavolo)  che  effettua  ordini,  procede  ai  pagamenti  digitali,  monitora  lo  stato  della  propria  comanda  e  può  rilasciare  recensioni.
Personale  Categoria  astratta  che  racchiude  tutti  i  dipendenti  del  ristorante  (Cuoco,  Cameriere,  Manager).  Rappresenta  l'utente  interno  autorizzato  ad  accedere  alle  funzionalità  riservate  del  sistema,  distinto  dall'utenza  esterna  (Clienti).  Funge  da  attore  base  per  l'ereditarietà  dei  permessi  e  delle  funzioni  di  autenticazione  operativa.
Cameriere  Membro  del  personale  di  sala  (utente  con  privilegi  specifici)  responsabile  dell'assegnazione  dei  tavoli,  dell'inserimento  manuale  degli  ordini  e  della  consegna  ai  tavoli.
Cuoco  Membro  del  personale  di  cucina  che  interagisce  con  i  monitor  del  sistema  per  ricevere  le  comande,  prepararle  secondo  la  priorità  e  aggiornarne  lo  stato  (es.  "In  preparazione",  "Pronto").
Manager  Amministratore  del  locale  che  utilizza  il  sistema  per  gestire  l'infrastruttura,  aggiornare  il  menù,  coordinare  i  turni  del  personale  e  analizzare  la  reportistica  finanziaria.
Comanda  /  Ordine  La  richiesta  formale  di  pietanze  effettuata  dal  Cliente  o  dal  Cameriere.  Viene  processata  dal  sistema,  smistata  alla  cucina  e  fatturata  al  momento  del  pagamento.
Menù  Lista  digitale  delle  pietanze  e  delle  bevande  offerte  dal  ristorante,  aggiornabile  in  tempo  reale  dal  Manager.


---

<!-- Pagina PDF 6 -->
## 📑 Pagina 6

Asporto  (Take-away)  Modalità  di  ordinazione  in  cui  il  Cliente  prenota  le  pietanze  tramite  il  sistema  per  poi  ritirarle  fisicamente  presso  il  ristorante.
Delivery  Servizio  di  consegna  a  domicilio.  La  preparazione  è  gestita  interamente  dalla  cucina  del  ristorante,  mentre  la  presa  in  carico  fisica  del  pasto,  il  calcolo  dei  percorsi  e  il  trasporto  al  domicilio  del  Cliente  sono  delegati  a  una  Piattaforma  Esterna  di  Delivery  dedicata.
Recensione  Feedback  pubblico  inserito  dal  Cliente  al  termine  del  pasto,  visibile  agli  altri  utenti  del  portale.
Gateway  di  Pagamento  Sistema  esterno  (es.  PayPal,  circuiti  bancari)  con  cui  il  software  interagisce  per  delegare  ed  elaborare  in  sicurezza  le  transazioni  economiche  digitali.
Gateway  di  Comunicazione  Sistema  esterno  (server  SMTP/SMS)  utilizzato  per  inoltrare  notifiche  automatizzate  ai  clienti  (es.  conferma  ordine,  stato  consegna).
Sistema  Fiscale  Apparato  hardware/software  esterno  (es.  Registratore  di  Cassa  Telematico)  integrato  con  il  sistema  per  l'emissione  legale  di  scontrini  e  fatture  elettroniche.


---

<!-- Pagina PDF 7 -->
## 📑 Pagina 7

4.  USER  REQUIREMENTS  DEFINITION
 4.1.  Use  Case  Utente  4.1.1.  Diagramma
4.1.2.  Documentazione
 Use  Case  Visualizza  menù  pubblico
Descrizione  Passo  Azione  1.  L’utente  accede  all’area  riservata  al  menù   2.  L’utente  visualizza  il  menù   3.  L’utente  effettua  eventuali  click  sulle  pietanze  per  vedere  gli  allergeni
Attori   Utente  (registrato  o  non  registrato)
Precondizioni  Nessuna  precondizione  particolare
Scenario  Principale  L’Utente  apre  l’app  e  prende  visione  del  menù


---

<!-- Pagina PDF 8 -->
## 📑 Pagina 8

Scenari  alternativi  Il  Manager  sta  effettuando  un  aggiornamento  massivo  del  menù  in  quel  momento;  il  sistema  mostra  un  banner  temporaneo  indicando  che  i  prezzi  o  i  piatti  potrebbero  subire  variazioni  a  breve.
Post  -  condizioni  L'utente  ottiene  le  informazioni  desiderate  sulle  pietanze  offerte.   Use  Case  Effettua  registrazione
Descrizione  Passo  Azione   1.   L'utente  accede  alla  sezione  "Registrati"    2.  inserisce  le  informazioni  richieste  (nome,  cognome,  email,  password)   3.  Il  sistema  valida  i  dati    4.  Se  tutto  è  corretto,  viene  creato  un  account  con  relative  credenziali  di  accesso.    5.  Il  sistema  conferma  la  registrazione
Attori   Utente  non  registrato
Precondizioni  L'utente  deve  fornire  il  consenso  per  il  trattamento  dei  dati  personali
Scenario  Principale  L'utente  si  registra  al  sistema  per  poter  accedere  alle  funzionalità  avanzate
Scenari  alternativi  Il  sistema  rileva  degli  errori  nei  dati  inseriti  oppure  trova  che  la  email  è  collegata  ad  un  altro  account
Post  -  condizioni   L'utente  ha  un  nuovo  account,  viene  aggiunto  al  database  e  diventa  un  "Utente  Registrato"   Use  Case  Effettua  accesso
Descrizione  Passo  Azione   1.   L'utente  richiede  la  pagina  di  login.   2.  Inserisce  la  propria  email  e  la  password.   3.   Il  sistema  verifica  le  credenziali     4.  Se  corrette,  l'utente  accede  alla  propria  area  personale.
Attori   Utente  Registrato


---

<!-- Pagina PDF 9 -->
## 📑 Pagina 9

Precondizioni  L'utente  deve  aver  completato  in  precedenza  la  registrazione  ed  essere  in  possesso  di  credenziali  valide.
Scenario  Principale  L'utente  si  autentica  per  sbloccare  le  varie  funzionalità
Scenari  alternativi  L’utente  sbaglia  le  credenziali  e  si  trova  a  leggere  un  messaggio  di  errore  oppure  chiede  di  recuperare  la  password.
Post  -  condizioni  L'utente  è  autenticato  e  il  sistema  carica  l'interfaccia   Use  Case  Modifica  Dati  Personali
Descrizione  Passo  Azione   1.   L'utente  accede  alla  sezione  "Profilo  personale"   2.  Seleziona  il  campo  da  modificare  (es.  numero  di  telefono,  intolleranze  alimentari,  password).   3.  Inserisce  i  nuovi  dati  e  conferma  la  modifica.     4.  Il  sistema  aggiorna  le  informazioni.
Attori   Utente  Registrato
Precondizioni  L'utente  deve  aver  effettuato  l'accesso  con  successo.
Scenario  Principale  L'utente  mantiene  aggiornate  le  proprie  informazioni  di  contatto  o  di  preferenza  all'interno  dell'applicativo
Scenari  alternativi  L'utente  lascia  dei  campi  obbligatori  vuoti  o  inserisce  un  formato  non  valido;  il  sistema  blocca  il  salvataggio  e  segnala  l'errore
Post  -  condizioni  I  dati  personali  risultano  aggiornati  nel  database  del  sistema.   Use  Case  Cancellazione  Account
Descrizione  Passo  Azione  1.  L'utente  accede  alla  sezione  "Gestione  Account"    2.  L’utente  seleziona  elimina  account   3.   Il  sistema  chiede  una  conferma  di  sicurezza   4.  L'utente  conferma  l'intenzione   5.  Il  sistema  disattiva  l'account


---

<!-- Pagina PDF 10 -->
## 📑 Pagina 10

Attori   Utente  registrato
Precondizioni  L'utente  deve  aver  effettuato  l'accesso  al  sistema.  Non  ci  devono  essere  ordini  in  corso  o  pendenze  economiche  attive.
Scenario  Principale  L'utente  decide  di  non  voler  più  usufruire  di  RistorApp  e  richiede  la  rimozione  del  proprio  profilo.
Scenari  alternativi  Non  ci  sono  scenari  alternativi  particolari
Post  -  condizioni  L'account  viene  chiuso,  l'utente  viene  disconnesso   Use  Case  Visualizza  Storico  Ordini
Descrizione  Passo  Azione   1.  L'utente  accede  alla  propria  area  personale.   2.  Seleziona  la  sezione  "Storico  Ordini"   3.  .  Il  sistema  restituisce  l'elenco  degli  ordini  precedenti  (con  dettagli  su  data,  pietanze,  costo  totale  e  stato)
Attori   Utente  Registrato
Precondizioni  L'utente  deve  aver  effettuato  l'accesso  con  successo.
Scenario  Principale  L'utente  consulta  l'elenco  delle  proprie  ordinazioni  passate  per  vederne  dettagli  o  ripetere  un  ordine  gradito.
Scenari  alternativi  L'utente  non  ha  ancora  mai  effettuato  un  ordine  all'interno  del  sistema;  la  pagina  viene  caricata  mostrando  un  messaggio  di  assenza  ordini
Post  -  condizioni  L'utente  visualizza  correttamente  le  informazioni  richieste  relative  al  suo  storico  personale   Use  Case  Gestisci  metodo  di  pagamento
Descrizione  Passo  Azione   1.   L'utente  accede  alla  sezione  "Metodi  di  Pagamento"  nel  proprio  profilo.   2.   Sceglie  di  aggiungere,  modificare  o  rimuovere  i  dati  di  una  carta  di  credito/debito.   3.   Inserisce  i  dati  richiesti  e  conferma  l'operazione..


---

<!-- Pagina PDF 11 -->
## 📑 Pagina 11

4.  Il  sistema  valida  e  salva  le  informazioni  .
Attori  Utente  Registrato
Precondizioni  L'utente  deve  aver  effettuato  l'accesso  con  successo.
Scenario  Principale  L'utente  configura  in  anticipo  un  metodo  di  pagamento  predefinito  per  rendere  più  rapido  il  processo  di  ordinazione
Scenari  alternativi  I  dati  della  carta  inserita  risultano  scaduti  o  non  validi  al  momento  del  controllo  di  sicurezza
Post  -  condizioni  Il  nuovo  metodo  di  pagamento  viene  aggiornato  e  associato  in  modo  sicuro  all'account  dell'utente.   Use  Case  Recupera  password
Descrizione  Passo  Azione   1.   Dalla  pagina  di  login,  l'utente  seleziona  "Password  dimenticata?"   2.   Inserisce  il  proprio  indirizzo  email.   3.    Il  sistema  verifica  l'esistenza  dell'account  e  invia  un  link  temporaneo  di  ripristino  tramite  email.    4.  L'utente  clicca  sul  link,  digita  la  nuova  password  e  la  conferma.
Attori  Utente  Registrato
Precondizioni   L'utente  ha  dimenticato  le  credenziali  ma  possiede  un  account  esistente  nel  sistema.
Scenario  Principale  L'utente  ripristina  autonomamente  l'accesso  al  proprio  profilo  tramite  un  il  codice  inviato  alla  propria  email
Scenari  alternativi  L'indirizzo  email  inserito  non  è  presente  nel  database,  quindi  non  viene  inviata  alcuna  mail
Post  -  condizioni  La  vecchia  password  viene  sovrascritta  nel  database  e  l'utente  può  effettuare  nuovamente  l'accesso  con  la  nuova  password.


---

<!-- Pagina PDF 12 -->
## 📑 Pagina 12

4.2.  Use  Case  Personale  4.2.1.  Diagramma
4.2.2.  Documentazione   Use  Case  Effettua  Accesso  Personale
Descrizione  Passo  Azione   1.   Il  dipendente  avvia  l'applicazione   2.   Inserisce  le  proprie  credenziali  aziendali    3.   Il  sistema  verifica  le  credenziali  e  identifica  il  ruolo   4.  Il  sistema  carica  l'interfaccia  operativa  specifica  per  quel  ruolo
Attori  Personale
Precondizioni   L'account  del  dipendente  deve  essere  stato  registrato  dal  Manager  ed  essere  attivo  nel  sistema  aziendale
Scenario  Principale  Il  dipendente  accede  correttamente  al  sistema  di  gestione  interno  per  iniziare  il  proprio  turno  di  lavoro


---

<!-- Pagina PDF 13 -->
## 📑 Pagina 13

Scenari  alternativi  Le  credenziali  sono  errate  e  il  sistema  chiede  di  riprovare  oppure  l’account  è  stato  sospeso  dal  manager
Post  -  condizioni  La  sessione  di  lavoro  è  avviata  e  le  funzionalità  specifiche  del  ruolo  sono  abilitate   Use  Case  Visualizza  Bacheca  Avvisi
Descrizione  Passo  Azione   1.  Il  dipendente  accede  alla  propria  dashboard  principale.   2.  Seleziona  la  sezione  "Bacheca  Avvisi"   3.  Il  sistema  mostra  l'elenco  delle  comunicazioni  aziendali  non  ancora  lette
Attori  Personale
Precondizioni  Il  dipendente  deve  aver  effettuato  correttamente  l'accesso  al  sistema
Scenario  Principale   Il  dipendente  consulta  la  bacheca  per  rimanere  informato  su  comunicazioni  di  servizio,  cambi  di  turno  o  direttive  del  Manager
Scenari  alternativi  Non  c'è  alcun  avviso  presente  nel  database  per  quel  dipendente:  il  sistema  mostra  una  pagina  vuota  con  il  messaggio  "Nessuna  nuova  comunicazione"
Post  -  condizioni  Gli  avvisi  visualizzati  vengono  registrati  come  "letti"  dal  sistema   Use  Case  Gestisci  Profilo  Personale
Descrizione  Passo  Azione   1.  Il  dipendente  accede  alla  sezione  "Profilo"   2.  Modifica  i  dati  autorizzati  (es.  recapito  telefonico  o  password  personale).   3.  Salva  le  modifiche.   4.  Il  sistema  valida  i  dati  e  aggiorna  il  database  del  personale
Attori  Personale
Precondizioni  Il  dipendente  deve  aver  effettuato  correttamente  l'accesso  al  sistema


---

<!-- Pagina PDF 14 -->
## 📑 Pagina 14

Scenario  Principale   Il  dipendente  aggiorna  autonomamente  le  proprie  informazioni  per  la  reperibilità  aziendale
Scenari  alternativi  Il  formato  dei  dati  inseriti  non  è  valido  e  il  sistema  lo  segnala  l’errore  e  non  salva  le  modifiche
Post  -  condizioni  I  dati  del  dipendente  risultano  aggiornati  nel  sistema   Use  Case  Recupera  Password  Aziendale
Descrizione  Passo  Azione   1.  Dalla  schermata  di  login,  il  dipendente  seleziona  "Password  dimenticata?"   2.  Inserisce  il  proprio  indirizzo  email  aziendale.   3.  Il  sistema  invia  un  link  temporaneo  per  reimpostare  le  credenziali.   4.  Il  dipendente  inserisce  e  conferma  la  nuova  password.
Attori  Personale
Precondizioni  Il  dipendente  deve  avere  un  account  creato  dal  Manager  associato  a  un'email  valida.
Scenario  Principale  Il  dipendente  smarrisce  la  password  e  cerca  di  cambiarla  tramite  la  procedura  password  dimenticata
Scenari  alternativi  L'email  inserita  non  corrisponde  a  nessun  dipendente  registrato  e  il  sistema  mostra  un  messaggio  di  errore
Post  -  condizioni   La  password  viene  aggiornata  e  il  dipendente  può  effettuare  l'accesso.


---

<!-- Pagina PDF 15 -->
## 📑 Pagina 15

4.3.  Use  Case  Cliente  4.3.1.  Diagramma
  4.3.2.  Documentazione   Use  Case  Effettua  Ordinazione
Descrizione  Passo  Azione   1.   Il  cliente  accede  al  menù  digitale   2.   Seleziona  la  modalità  desiderata    3.   Aggiunge  le  pietanze  desiderate  al  carrello.   4.  Conferma  l'ordine  e  lo  invia  al  sistema.


---

<!-- Pagina PDF 16 -->
## 📑 Pagina 16

Attori  Cliente
Precondizioni  Il  cliente  ha  effettuato  l'accesso  al  sistema
Scenario  Principale   Il  cliente  consulta  il  menù,  seleziona  i  prodotti  e  invia  una  nuova  ordinazione  al  ristorante.
Scenari  alternativi  Una  o  più  pietanze  selezionate  terminano  la  disponibilità  in  cucina  prima  della  conferma  e  quindi  il  sistema  avverte  il  cliente
Post  -  condizioni   L'ordine  viene  registrato  nel  database  del  sistema,  smistato  alla  cucina  e  associato  al  cliente/tavolo.   Use  Case  Monitora  Stato  Ordine
Descrizione  Passo  Azione   1.  Il  cliente  accede  alla  schermata  degli  ordini  attivi.   2.  Visualizza  lo  stato  di  avanzamento  in  tempo  reale
Attori  Cliente
Precondizioni   Il  cliente  deve  aver  effettuato  e  confermato  almeno  un  ordine.
Scenario  Principale  Il  cliente  controlla  a  che  punto  è  la  preparazione  del  suo  pasto  per  sapere  quando  verrà  servito  o  quando  potrà  ritirarlo.
Scenari  alternativi  L'ordine  subisce  un  ritardo  imprevisto  in  cucina  e  il  sistema  lo  segnala  al  cliente
Post  -  condizioni   Il  cliente  è  informato  correttamente  e  in  tempo  reale  sulla  situazione  della  propria  comanda.   Use  Case  Effettua  Pagamento
Descrizione  Passo  Azione   1.  Il  cliente  accede  alla  sezione  di  riepilogo  del  proprio  ordine/tavolo   2.  Seleziona  la  voce  per  richiedere  il  conto   3.  Sceglie  il  metodo  di  pagamento  digitale  desiderato   4.  Il  sistema  processa  la  transazione  delegandola  al  Gateway
Attori  Cliente,  Gateway  di  Pagamento


---

<!-- Pagina PDF 17 -->
## 📑 Pagina 17

Precondizioni  Il  cliente  ha  un  ordine  completato  e  un  conto  da  pagare.
Scenario  Principale  l  cliente  paga  in  autonomia  il  proprio  conto
Scenari  alternativi   La  transazione  viene  rifiutata  dal  Gateway  di  Pagamento  e  il  sistema  avvisa  di  questo  fatto  con  un  errore
Post  -  condizioni  L'ordine  viene  marcato  come  pagato,  si  genera  la  ricevuta/scontrino  e  la  comanda  viene  chiusa.   Use  Case  Lascia  Recensione
Descrizione  Passo  Azione   1.   Il  cliente  accede  alla  sezione  "Recensioni"  dell'applicazione.   2.  Assegna  un  voto  e  inserisce  un  commento  testuale  sulla  sua  esperienza.   3.  Il  sistema  salva  e  pubblica  la  recensione.
Attori  Cliente
Precondizioni   Il  cliente  deve  essere  un  Utente  Registrato  e  aver  completato  e  pagato  almeno  un  ordine  all'interno  del  locale
Scenario  Principale  Il  cliente  valuta  positivamente  o  negativamente  il  pasto  e  il  servizio  offerto
Scenari  alternativi   Il  cliente  cerca  di  lasciare  una  recensione  senza  aver  mai  effettuato  una  consumazione  e  il  sistema  lo  blocca,  mostrando  un  messaggio  con  le  azioni  richieste  per  poter  effettuare  questa  azione.
Post  -  condizioni  La  recensione  viene  salvata  nel  database  ed  è  visibile  agli  altri  utenti  e  al  Manager.   Use  Case  Gestione  Reclami
Descrizione  Passo  Azione   1.  Il  cliente  accede  alla  sezione  dedicata  all'assistenza  o  ai  propri  ordini  attivi   2.  Seleziona  l'opzione  per  aprire  un  ticket/reclamo   3.  Compila  il  modulo  descrivendo  il  problema  e  lo  invia.


---

<!-- Pagina PDF 18 -->
## 📑 Pagina 18

4.  Il  sistema  registra  il  reclamo,  avvisa  il  Manager  e  invia  una  notifica  di  presa  in  carico  al  cliente  tramite  il  Gateway  di  Comunicazione.
Attori  Cliente,  Manager,  Gateway  di  Comunicazione
Precondizioni  Il  cliente  deve  aver  effettuato  l'accesso  e  aver  riscontrato  un'anomalia  nel  servizio.
Scenario  Principale   Il  cliente  segnala  un  problema  per  ottenere  rapidamente  assistenza
Scenari  alternativi  Il  cliente  non  compila  i  campi  obbligatori  per  la  descrizione  del  problema;  il  sistema  mostra  un  messaggio  di  errore  e  blocca  l'invio  del  ticket.
Post  -  condizioni  Il  reclamo  viene  registrato  nel  database  con  stato  "Aperto"  ed  è  in  attesa  di  essere  gestito  dal  personale.


---

<!-- Pagina PDF 19 -->
## 📑 Pagina 19

4.4.  Use  Case  Cameriere  4.4.1.  Diagramma
  4.4.2.  Documentazione   Use  Case  Assegna  Tavolo
Descrizione  Passo  Azione   1.   Il  cameriere  accoglie  i  clienti  e  verifica  la  disponibilità  dei  tavoli  tramite  il  sistema   2.  Seleziona  un  tavolo  libero  con  capienza  adeguata   3.  Aggiorna  lo  stato  del  tavolo  in  "Occupato"  nel  sistema
Attori  Cameriere.
Precondizioni  Il  cameriere  ha  effettuato  il  login  al  sistema.  Ci  sono  clienti  fisicamente  in  attesa  di  un  tavolo.
Scenario  Principale  Il  cameriere  assegna  un  tavolo  fisico  a  un  gruppo  di  clienti  appena  arrivato  nel  locale.


---

<!-- Pagina PDF 20 -->
## 📑 Pagina 20

Scenari  alternativi  Non  ci  sono  tavoli  liberi  o  con  capienza  sufficiente  e  il  sistema  lo  notifica  al  cameriere
Post  -  condizioni   Il  tavolo  risulta  occupato  nel  database  e  pronto  per  ricevere  le  ordinazioni   Use  Case  Inserisce  Ordine  Manuale
Descrizione  Passo  Azione   1.  Il  cameriere  seleziona  il  tavolo  corrispondente  nel  sistema   2.  Ascolta  le  richieste  dei  clienti  e  seleziona  le  pietanze  dal  menù  digitale   3.  Aggiunge  eventuali  note  per  la  cucina   4.   Invia  la  comanda  al  sistema.
Attori  Cameriere.
Precondizioni  Il  tavolo  deve  risultare  occupato  nel  sistema  e  i  clienti  devono  aver  deciso  cosa  ordinare
Scenario  Principale  Il  cameriere  prende  la  comanda  al  tavolo  e  la  trasmette  alla  cucina
Scenari  alternativi  Una  pietanza  richiesta  non  è  più  disponibile  in  tempo  reale
Post  -  condizioni   L'ordine  viene  registrato  nel  database,  smistato  ai  monitor  della  cucina  e  associato  al  conto  di  quel  tavolo   Use  Case  Monitora  Stato  Ordine
Descrizione  Passo  Azione   1.  Il  cameriere  accede  alla  schermata  panoramica  dei  tavoli  attivi  sul  proprio  terminale   2.  Visualizza  lo  stato  di  avanzamento  delle  comande  inviate  in  cucina
Attori  Cameriere.
Precondizioni  Ci  sono  ordini  in  corso  associati  ai  tavoli  gestiti  dal  cameriere
Scenario  Principale  Il  cameriere  controlla  quali  piatti  sono  pronti  in  cucina  per  poterli  prendere  e  servire  ai  tavoli  corretti


---

<!-- Pagina PDF 21 -->
## 📑 Pagina 21

Scenari  alternativi  Un  piatto  subisce  un  forte  ritardo  segnalato  dalla  cucina;  il  sistema  comunica  l'ordine  al  cameriere,  che  si  reca  al  tavolo  per  avvisare  i  clienti.
Post  -  condizioni   Il  cameriere  è  costantemente  aggiornato  sulla  situazione  per  gestire  il  servizio  in  sala   Use  Case  Chiudi  Comanda
Descrizione  Passo  Azione   1.  Il  cameriere  seleziona  il  tavolo  da  chiudere   2.  Richiede  la  chiusura  della  comanda   3.  Il  sistema  verifica  che  non  vi  siano  ordini  pendenti  per  quel  tavolo   4.  Il  sistema  calcola  il  totale  parziale  e  finale,  includendo  eventuali  sconti  o  costi  di  coperto   5.  Il  tavolo  passa  allo  stato  "In  attesa  di  pagamento"
Attori  Cameriere.
Precondizioni  I  clienti  al  tavolo  hanno  terminato  la  consumazione  e  la  comanda  è  in  stato  "Aperto"
Scenario  Principale  Il  cameriere  blocca  la  possibilità  di  inserire  nuovi  ordini  per  il  tavolo  selezionato  e  ottiene  il  riepilogo  dei  costi  da  presentare  al  cliente
Scenari  alternativi  Ordini  ancora  "In  preparazione":  il  sistema  avvisa  il  cameriere  che  non  è  possibile  chiudere  la  comanda  finché  la  cucina  non  ha  completato  tutte  le  portate
Post  -  condizioni   La  comanda  è  bloccata  e  il  totale  è  calcolato  e  memorizzato  nel  sistema   Use  Case  Gestisci  Pagamento
Descrizione  Passo  Azione   1.  Il  cameriere  seleziona  il  tavolo/comanda  da  saldare  dal  proprio  terminale   2.  Seleziona  la  modalità  di  pagamento  scelta  dal  cliente


---

<!-- Pagina PDF 22 -->
## 📑 Pagina 22

3.  Il  sistema  processa  il  pagamento    4.  Il  sistema  invia  i  dati  al  Sistema  Fiscale  per  l'emissione  dello  scontrino/fattura
Attori   Cameriere,  Gateway  di  Pagamento,  Sistema  Fiscale
Precondizioni  La  comanda  deve  essere  stata  precedentemente  chiusa  e  trovarsi  nello  stato  "In  attesa  di  pagamento"
Scenario  Principale  Il  cameriere  gestisce  l'incasso  effettivo,  emettendo  il  documento  fiscale  e  liberando  il  tavolo  per  nuovi  clienti
Scenari  alternativi  Ci  possono  essere  errori  di  rete  e  quindi  ci  sono  problemi  alla  cassa  oppure  il  pagamento  viene  rifiutato
Post  -  condizioni  Il  pagamento  è  registrato,  il  documento  fiscale  è  emesso  e  il  tavolo  torna  allo  stato  "Libero"  nel  sistema


---

<!-- Pagina PDF 23 -->
## 📑 Pagina 23

4.5.  Use  Case  Cuoco  4.5.1.  Diagramma
 4.5.2.  Documentazione   Use  Case  Visualizza  Comande  in  Coda
Descrizione  Passo  Azione   1.   Il  cuoco  osserva  il  monitor  touch  in  cucina   2.  Il  sistema  mostra  la  lista  degli  ordini  in  entrata,  ordinati  dinamicamente  per  orario  di  arrivo,  priorità  e  modalità
Attori   Cuoco
Precondizioni  Il  sistema  è  attivo  e  ci  sono  ordini  confermati  non  ancora  consegnati
Scenario  Principale  Il  personale  di  cucina  consulta  in  tempo  reale  i  piatti  da  preparare  in  base  all'ordine  di  arrivo  stabilito  dal  sistema
Scenari  alternativi  Avviene  un  intoppo  in  cucina  e  quindi  il  cuoco  decide  se  mettere  la  comanda  in  "Stato  di  Sospensione"  oppure  comunicare  il  ritardo
Post  -  condizioni  Il  cuoco  sa  quali  pietanze  preparare  e  in  quale  ordine  procedere   Use  Case  Aggiorna  Stato  Comanda
Descrizione  Passo  Azione  1.  l  cuoco  seleziona  una  comanda  specifica  dal  monitor


---

<!-- Pagina PDF 24 -->
## 📑 Pagina 24

2.  Ne  aggiorna  lo  stato  in  "In  preparazione"  non  appena  inizia  a  cucinare  i  piatti   3.  Al  termine  della  preparazione,  aggiorna  lo  stato  in  "Pronto  da  servire/ritirare"
Attori   Cuoco,  Gateway  di  Comunicazione
Precondizioni  Deve  esserci  almeno  una  comanda  "In  coda"  visibile  sul  monitor  della  cucina
Scenario  Principale  Il  cuoco  notifica  al  sistema  l'avanzamento  della  preparazione  dei  piatti
Scenari  alternativi  Avviene  un  intoppo  in  cucina  e  quindi  il  cuoco  decide  se  mettere  la  comanda  in  "Stato  di  Sospensione"  oppure  comunicare  il  ritardo
Post  -  condizioni  Lo  stato  dell'ordine  cambia  nel  database.  Se  lo  stato  è   "Pronto",  il  sistema  comunica  al  cameriere  che  deve  ritirarlo   Use  Case  Segnala  Indisponibilità  Piatto
Descrizione  Passo  Azione   1.   Il  cuoco  accede  a  una  sezione  dedicata  del  monitor  (esempio  "Gestione  Scorte")    2.  Seleziona  un  piatto  o  un  ingrediente  specifico  dal  menù  del  giorno   3.  Ne  segnala  l'esaurimento   4.   Il  sistema  aggiorna  il  database  e  disabilita  l'ordinazione  di  quel  piatto
Attori   Cuoco
Precondizioni  l  cuoco  conferma  l'esaurimento  fisico  degli  ingredienti  necessari  per  preparare  una  specifica  pietanza
Scenario  Principale  Il  cuoco  comunica  al  sistema  che  un  piatto  non  può  più  essere  preparato  per  il  resto  del  turno,  bloccandone  le  ordinazioni  future
Scenari  alternativi  Avviene  un  intoppo  in  cucina  e  quindi  il  cuoco  decide  se  mettere  la  comanda  in  "Stato  di  Sospensione"  oppure  comunicare  il  ritardo
Post  -  condizioni  Il  cuoco  segna  come  "esaurito"  un  piatto  che  però  è  già  presente  in  una  comanda  non  ancora  elaborata;  il  sistema  avvisa  il  cuoco  e  invia  una  notifica  automatica  ai  camerieri  per  quel  tavolo


---

<!-- Pagina PDF 25 -->
## 📑 Pagina 25

4.6.  Use  Case  Manager  4.6.1.  Diagramma
4.6.2.  Documentazione   Use  Case  Aggiorna  Menù
Descrizione  Passo  Azione   1.  Il  manager  accede  all'area  dedicata  alla  gestione  dell'offerta  gastronomica   2.  Seleziona  il  menù  da  modificare.   3.   Effettua  le  modifiche  desiderate   4.  Salva  le  modifiche,  rendendo  visibile  la  versione  aggiornata
Attori   Manager
Precondizioni   Il  manager  ha  effettuato  il  login  al  sistema  con  i  privilegi  di  amministrazione
Scenario  Principale  Il  manager  mantiene  aggiornata  la  lista  dei  piatti  offerti  dal  ristorante


---

<!-- Pagina PDF 26 -->
## 📑 Pagina 26

Scenari  alternativi  Le  modifiche  inserite  presentano  errori  formali;  il  sistema  mostra  un  messaggio  di  errore  e  blocca  il  salvataggio
Post  -  condizioni  l  menù  viene  aggiornato  nel  database  ed  è  immediatamente  visibile  sui  dispositivi  dei  Clienti  e  del  personale   Use  Case  Monitora  Attività  e  Reportistica
Descrizione  Passo  Azione   1.  Il  manager  accede  alla  dashboard  di  monitoraggio  del  sistema   2.  Seleziona  il  tipo  di  statistica  e  applica  i  filtri  desiderati    3.   Il  sistema  mostra  i  dati  aggregati  e  aggiornati  in  forma  grafica
Attori   Manager
Precondizioni   Il  manager  ha  effettuato  il  login  al  sistema  con  i  privilegi  di  amministrazione
Scenario  Principale  Il  manager  analizza  l'andamento  della  struttura  per  poter  prendere  delle  decisioni
Scenari  alternativi  Se  i  dati  per  il  periodo  selezionato  non  sono  disponibili,  il  sistema  segnala  l'anomalia  con  un  relativo  avviso
Post  -  condizioni  Il  manager  ha  consultato  con  successo  i  dati    Use  Case  Gestisci  Personale
Descrizione  Passo  Azione   1.  Il  manager  accede  all'area  "Risorse  Umane"  del  sistema   2.  Seleziona  l'opzione  per  aggiungere  un  nuovo  dipendente  o  modificarne  uno  esistente   3.  Inserisce  i  dati  anagrafici  e  assegna  il  ruolo  specifico    4.  Il  sistema  salva  i  dati,  genera  le  credenziali  di  accesso  e  invia  una  notifica  automatica  al  dipendente  tramite  il  Gateway  di  Comunicazione
Attori   Manager,  Gateway  di  Comunicazione


---

<!-- Pagina PDF 27 -->
## 📑 Pagina 27

Precondizioni  Il  manager  è  autenticato  al  sistema.  È  stato  assunto  un  nuovo  dipendente  o  vi  è  la  necessità  di  aggiornare  i  dati  di  uno  esistente
Scenario  Principale  Il  manager  crea  e  abilita  gli  account  necessari  affinché  il  nuovo  personale  operativo  possa  accedere  all'applicazione
Scenari  alternativi  Il  sistema  rileva  che  l'indirizzo  email  inserito  per  il  nuovo  dipendente  è  già  presente  nel  database;  blocca  la  creazione  e  chiede  al  manager  di  utilizzare  un  indirizzo  univoco.
Post  -  condizioni  Il  profilo  del  dipendente  è  attivo,  configurato  correttamente  e  pronto  per  essere  utilizzato   Use  Case  Pianificazione  Turni
Descrizione  Passo  Azione   1.  Il  manager  accede  alla  sezione  "Calendario  Turni"   2.  Visualizza  la  griglia  settimanale  e  la  lista  del  personale   3.  Assegna  i  dipendenti  alle  varie  fasce  orarie   4.  Salva  e  pubblica  il  calendario
Attori   Manager
Precondizioni  Il  manager  è  autenticato.  Devono  esistere  account  di  personale  attivi  nel  sistema
Scenario  Principale  Il  manager  organizza  la  copertura  del  servizio  per  la  settimana  entrante,  garantendo  la  presenza  di  personale  sufficiente
Scenari  alternativi  Il  manager  fa  un  errore  nell’assegnare  i  turni,  il  sistema  vedendo  il  conflitto  impedisce  il  salvataggio
Post  -  condizioni  Il  calendario  viene  aggiornato  e  reso  visibile  nelle  bacheche  personali  di  tutti  i  dipendenti  interessati   Use  Case  Sospende  Account
Descrizione  Passo  Azione   1.  Il  manager  accede  all'anagrafica  del  Personale  o  dei  Clienti.   2.  Seleziona  l'utente  specifico  e  clicca  su  "Sospendi/Disattiva  Account".


---

<!-- Pagina PDF 28 -->
## 📑 Pagina 28

 3.  Inserisce  la  motivazione  (opzionale)  e  conferma  l'azione   4.  Il  sistema  disabilita  le  credenziali  dell'utente  preso  in  considerazione
Attori   Manager
Precondizioni  Il  manager  è  autenticato.  L'account  bersaglio  deve  esistere  all'interno  del  sistema.
Scenario  Principale  Il  manager  inibisce  l'accesso  a  un  dipendente  non  più  in  servizio  o  a  un  cliente  che  ha  violato  delle  regole  del  locale
Scenari  alternativi  Il  manager  tenta  di  sospendere  il  proprio  account;  il  sistema  riconosce  l'operazione  non  valida  e  la  blocca
Post  -  condizioni   L'account  bersaglio  cambia  stato  in  "Sospeso"  e  non  può  più  effettuare  il  login  all'applicazione.   Use  Case  Gestisci  Consegne  Delivery
Descrizione  Passo  Azione   1.   Il  manager  accede  alla  sezione  "Ordini  in  Consegna"   2.  Visualizza  un  ordine  delivery  completato  dalla  cucina  e  in  attesa  di  ritiro.    3.  Affida  fisicamente  i  pacchi  al  corriere  della  piattaforma  esterna   4.  Seleziona  l'ordine  e  ne  aggiorna  lo  stato  in  "Affidato  al  corriere".
Attori   Manager,  Piattaforma  Esterna  di  Delivery
Precondizioni  L'ordine  di  tipo  "Delivery"  deve  essere  stato  completato  dalla  cucina  e  trovarsi  nello  stato  "Pronto  da  ritirare".
Scenario  Principale  Il  manager  coordina  il  passaggio  di  consegne  logistico  tra  la  cucina  del  ristorante  e  il  fattorino  esterno.
Scenari  alternativi  Il  corriere  esterno  non  si  presenta  entro  il  tempo  limite  stimato;  il  manager  contatta  l'assistenza  dell'applicativo  esterno  e  imposta  l'ordine  in  "Attesa  di  ritiro  prolungato".
Post  -  condizioni  Lo  stato  dell'ordine  cambia  in  "Affidato  al  corriere"


---

<!-- Pagina PDF 29 -->
## 📑 Pagina 29

5.  REQUISITI  DI  SISTEMA
 5.1.  Requisiti  funzionali
Soggetto  ID  Requisito  funzionale
Descrizione
Utente  (Generico)  F1.1  Visualizza  menu  pubblico
Il  sistema  deve  permettere  la  consultazione  dell'offerta  gastronomica  (pietanze,  prezzi,  allergeni)  senza  autenticazione.
Utente  non  registrato  F1.2  Registrazione  account
Il  sistema  deve  consentire  la  creazione  di  un  profilo  raccogliendo  dati  anagrafici,  contatti  e  consenso  al  trattamento  dei  dati  (GDPR).
Utente  non  registrato  F1.3  Assegnazione  ID  Utente
In  fase  di  registrazione,  il  sistema  deve  generare  e  associare  all'utente  un  identificatore  univoco  (Client_ID).
Utente  registrato  F2.1  Autenticazione  (Login)
Il  sistema  deve  verificare  le  credenziali  (email/password)  interfacciandosi  con  il  database  per  caricare  il  profilo  corrispondente.
Utente  registrato  F2.2  Recupero  password  Il  sistema  deve  fornire  una  procedura  per  l'invio  di  un  link  di  reset  all'indirizzo  email  associato  all'account  in  caso  di  smarrimento.
Utente  registrato  F2.3  Gestione  profilo  e  dati
Il  sistema  deve  permettere  la  visualizzazione,  modifica  o  cancellazione  definitiva  dei  dati  personali  e  delle  preferenze.
Utente  registrato  F2.4  Visualizzazione  storico
Il  sistema  deve  fornire  una  lista  rintracciabile  di  tutti  gli  ordini  passati,  inclusi  dettagli,  date  e  importi  pagati.
Utente  registrato  F2.5  Scrittura  recensione  Il  sistema  deve  consentire  l'inserimento  di  un  feedback  pubblico  (voto  da  1  a  5  e  testo)  per  gli  ordini  regolarmente  completati.
Personale  (Generico)  F3.1  Accesso  area  riservata
Il  personale  (cuochi,  camerieri)  deve  accedere  all'interfaccia  operativa  tramite  credenziali  dedicate  fornite  dal  manager.
Personale  (Generico)  F3.2  Visualizzazione  avvisi
Il  sistema  deve  fornire  una  bacheca  centralizzata  per  la  consultazione  di  comunicazioni  interne  e  turni  di  servizio.


---

<!-- Pagina PDF 30 -->
## 📑 Pagina 30

Cliente  F4.1  Creazione  ordine  Il  sistema  deve  gestire  la  selezione  dei  piatti,  l'applicazione  di  note  (es.  allergeni)  e  il  calcolo  automatico  del  totale.
Cliente  F4.2  Validazione  indirizzo  Per  gli  ordini  con  consegna  a  domicilio,  il  sistema  deve  interfacciarsi  con  API  di  mapping  esterne  per  validare  l'indirizzo  inserito.
Cliente  F4.3  Identificazione  ordine
Ad  ogni  nuova  comanda  inviata,  il  sistema  deve  generare  un  identificatore  univoco  (Order_ID)  per  la  tracciabilità.
Cliente  F4.4  Monitoraggio  stato  Il  sistema  deve  permettere  la  visualizzazione  in  tempo  reale  dell'avanzamento  dell'ordine  (in  preparazione,  pronto,  in  consegna).
Cliente  F4.5  Apertura  ticket  Il  sistema  deve  permettere  l'apertura  di  ticket,  e  permettere  la  gestione  dei  reclami  effettuati.
Cliente  F4.6  Notifiche  automatiche
Il  sistema  deve  inviare  comunicazioni  automatiche  (Email/SMS)  di  conferma  ordine  e  avvenuta  consegna  tramite  gateway  esterni.
Cliente  F4.7  Pagamento  digitale  Il  sistema  deve  delegare  la  transazione  economica  a  un  Gateway  di  Pagamento  esterno  (es.  PayPal,  Stripe)  gestendo  i  messaggi  di  conferma  o  errore.
Cameriere  F5.1  Gestione  stato  tavoli  Il  sistema  deve  permettere  l'aggiornamento  dello  stato  dei  tavoli  fisici  nel  database  (libero,  occupato,  in  attesa  di  pagamento).
Cameriere  F5.2  Inserimento  manuale  ordini
Il  sistema  deve  consentire  al  cameriere  di  inserire  manualmente  ordini  per  i  clienti  sprovvisti  di  dispositivo  digitale.
Cameriere  F5.3  Chiusura  comanda  Il  sistema  deve  bloccare  l'aggiunta  di  nuove  portate  a  un  ordine  e  generare  il  riepilogo  finale  dei  costi  comprensivo  di  tasse.
Cameriere  F5.4  Integrazione  fiscale  Il  sistema  deve  inviare  i  dati  della  transazione  al  Sistema  Fiscale  per  l'emissione  automatica  di  scontrini  o  fatture  elettroniche.
Cuoco  F6.1  Gestione  coda  comande
Il  sistema  deve  mostrare  sui  monitor  della  cucina  le  comande  in  entrata,  ordinate  dinamicamente  per  orario  e  priorità.


---

<!-- Pagina PDF 31 -->
## 📑 Pagina 31

Cuoco  F6.2  Aggiornamento  stato  preparazione
Il  sistema  deve  permettere  al  cuoco  di  notificare  l'avanzamento  della  preparazione,  attivando  i  trigger  per  le  notifiche  alla  sala.
Cuoco  F6.3  Segnalazione  scorte  Il  sistema  deve  consentire  al  cuoco  di  marcare  un  piatto  come  "Esaurito",  disabilitandolo  istantaneamente  nel  menù  digitale.
Manager  F7.1  Configurazione  menù
Il  sistema  deve  permettere  l'inserimento,  la  modifica  dei  prezzi  e  la  rimozione  di  pietanze  dall'offerta  digitale.
Manager  F7.2  Gestione  account  staff
Il  sistema  deve  permettere  al  manager  di  creare,  sospendere  o  eliminare  gli  account  del  personale  operativo.
Manager  F7.3  Pianificazione  turni  Il  sistema  deve  fornire  strumenti  per  la  creazione  e  la  pubblicazione  del  calendario  settimanale  del  personale.
Manager  F7.4  Reportistica  analitica  Il  sistema  deve  generare  report  grafici  e  aggregati  sugli  incassi  e  sulle  performance  operative  (piatti  più  venduti,  tempi  medi  di  preparazione,  ecc.).


---

<!-- Pagina PDF 32 -->
## 📑 Pagina 32

5.2.  Requisiti  non  funzionali
ID   Requisito  Categoria  Descrizione
NF1  Performance  Requisiti  di  prodotto
Il  sistema  deve  garantire  tempi  di  risposta  rapidi  per  tutte  le  principali  operazioni,  come  visualizzazione  del  menù,  invio  di  un  ordine,  aggiornamento  dello  stato,  e  login.  In  particolare,  il  tempo  massimo  di  risposta  previsto  per  ogni  richiesta  dell’utente  deve  essere  inferiore  a  2  secondi,  anche  in  condizioni  di  traffico  sostenuto  (  come  nel  caso  di  ristorante  pieno).  L’applicazione  deve  essere  in  grado  di  gestire  almeno  150  utenti  simultaneamente  (tra  clienti  al  ristorante,  che  ordinano  al  delivery  e  chi  semplicemente  vuole  vedere  il  menù  o  accedere  all’app.
NF2  Affidabilità   Requisiti  di  prodotto
Il  sistema  deve  essere  stabile  e  funzionare  in  modo  continuo  per  il  95%  del  tempo.  In  caso  di  crash  o  di  malfunzionamento,  questi  devono  essere  gestiti  tramite  una  notifica  all’utente.  È  appropriato  avere  dei  salvataggi  automatici  per  evitare  perdite  di  dati  in  caso  di  interruzione.
NF3  Disponibilità   Requisiti  di  prodotto
Il  sistema  deve  essere  attivo  e  disponibile  agli  utenti  per  gran  parte  del  tempo,  soprattutto  negli  orari  di  punta  come  pranzo  o  cena.  Sono  tollerate  interruzioni  nei  momenti  in  cui  il  ristorante  è  chiuso  o  ci  sono  poche  persone.
NF4  Usabilità  Requisiti  di  prodotto
Usabilità  L'interfaccia  del  sistema  deve  essere  progettata  per  minimizzare  lo  sforzo  richiesto  per  l'apprendimento,  l'operatività  e  la  preparazione  degli  input  da  parte  di  utenti  anche  non  esperti.  Per  garantire  la  verificabilità  del  requisito,  vengono  definiti  i  seguenti  obiettivi  di  produttività  e  tempi  medi  di  apprendimento  (training  time):  Profilo  Cliente:  Un  utente  senza  esperienza  pregressa  con  l'applicativo  deve  essere  in  grado  di  completare  con  successo  le  funzionalità  principali  (es.  ricerca  ristorante  e  invio  di  un  ordine)  in  un  tempo  inferiore  a  10  minuti  dopo  la  consultazione  di  una  breve  guida  introduttiva.  Profilo  Gestore  del  Personale:  Deve  essere  in  grado  di  completare  la  schedulazione  dei  turni  e  la  visualizzazione  delle  notifiche  critiche  in  meno  di  15  minuti.
NF5  Scalabilità  Requisiti  di  prodotto
Il  sistema  dovrà  essere  progettato  per  gestire  carichi  crescenti,  ben  oltre  le  capacità  del  ristorante,  con  tempi  di  risposta  inferiori  a  2s  per  l'80%  delle  richieste.  L’aggiunta  di  nuove  funzionalità  (es.  integrazione  con  sistemi  di  valutazione  esterna)  dovrà  essere  possibile  tramite  moduli  indipendenti,  integrabili  nel  minor  tempo  possibile.
NF6  Portabilità  Requisiti  di  prodotto
L’applicazione  deve  essere  utilizzabile  su  una  vasta  gamma  di  dispositivi  e  piattaforme.  In  particolare,  deve  essere  disponibile  sotto  forma  di  app  mobile  per  Android  e  iOS  ma  anche  accessibile  tramite  browser  web  (compatibile  con  Chrome,  Firefox,  Safari).  Il  design  responsivo  deve  garantire  la  corretta  visualizzazione  e  usabilità  sia  su  desktop  che  su  dispositivi  mobili  o  tablet.
NF7  Design  responsivo  Requisiti  di  prodotto
L’applicazione  deve  essere  in  grado  di  applicarsi  a  diverse  dimensioni  dello  schermo,  in  modo  da  essere  utilizzata  da  tutti  anche  da  chi  non  ha  uno  specifico  dispositivo.


---

<!-- Pagina PDF 33 -->
## 📑 Pagina 33

NF8  Standard  di  documentazione
Requisiti  organizzativi
I  documenti  di  specifica  e  di  progetto  devono  essere  conformi  allo  standard  IEEE  830-1998  o  ISO/IEC  25010
NF9  Manutenibilità  Requisiti  organizzativi
Il  codice  deve  essere  strutturato  in  moduli  facilmente  aggiornabili  e  documentati.  In  tal  modo  la  manutenibilità  sarà  più  semplice,  in  questo  senso  è  particolarmente  importante  quella  perfettiva  in  quanto  possiamo  prevedere  che  si  possano  aggiungere  in  futuro  nuove  funzionalità.  In  caso  di  guasti  ci  si  aspetta  che  il  sistema  torni  a  funzionare  correttamente  entro  il  minor  tempo  possibile.
NF10  Privacy  e  sicurezza  Requisiti  esterni  I  dati  personali  e  sensibili  devono  essere  protetti  mediante  protocolli  di  sicurezza.  Il  sistema  deve  prevedere  l’autenticazione  tramite  username  e  password,  e  opzionalmente  autenticazione  a  due  fattori.  L’accesso  alle  funzioni  critiche  deve  essere  riservato  agli  utenti  autorizzati  secondo  un  sistema  di  ruoli  ben  definito.  Devono  essere  previsti  backup  periodici  dei  dati  ogni  due  settimane.
NF11  Conformità  legislativa
Requisiti  esterni  Il  sistema  deve  rispettare  le  normative  sulla  protezione  dei  dati  personali  secondo  il  GDPR.
NF12  Tracciabilità  Requisiti  esterni  Il  sistema  deve  supportare  il  tracciamento  delle  attività  utente  (audit  log)  per  garantire  la  rintracciabilità.


---

<!-- Pagina PDF 34 -->
## 📑 Pagina 34

5.3.  Requisiti  di  dominio
ID  Requisito  Descrizione
RD1  Conformità  legislativa  (GDPR)
L'applicazione  deve  essere  conforme  al  Regolamento  generale  sulla  protezione  dei  dati  (Regolamento  UE  2016/679).  Il  sistema  deve  garantire  che  il  trattamento,  la  conservazione  e  la  protezione  dei  dati  raccolti  avvengano  secondo  i  principi  di  liceità,  trasparenza  e  minimizzazione.  Link  di  riferimento:  https://eur-lex.europa.eu/eli/reg/2016/679/oj?locale=it
RD2  Tutela  della  Privacy  e  Gestione  Dati  Personali
Il  sistema  deve  permettere  agli  utenti  (Clienti  e  Personale)  di  esercitare  pienamente  i  propri  diritti  sui  dati  registrati,  inclusi  l'accesso,  la  rettifica  e  la  cancellazione  definitiva  (diritto  all'oblio).  L'utilizzo  di  dati  sensibili  legati  alla  posizione  (es.  indirizzi  per  il  servizio  di  Delivery)  deve  avvenire  esclusivamente  per  finalità  contrattuali  legate  alla  consegna.  Link  di  riferimento:   https://www.garanteprivacy.it/
RD3  Trasparenza  Tariffaria  e  Pagamenti  Sicuri
In  ottemperanza  alle  direttive  europee  (es.  PSD2)  e  al  Codice  del  Consumo,  il  sistema  deve  esporre  in  modo  inequivocabile  tutti  i  costi  prima  della  conferma  dell'ordine,  separando  in  modo  chiaro  il  prezzo  delle  pietanze,  eventuali  costi  di  coperto/servizio  e  le  tariffe  di  consegna  a  domicilio.  I  pagamenti  digitali  devono  essere  demandati  a  Gateway  sicuri  e  certificati.  Link  di  riferimento:  https://www.mimit.gov.it/it/per-il-cittadino/tutela
RD4  Trasparenza  Menù  e  Sicurezza  Alimentare
Il  menù  digitale  offerto  dal  sistema  deve  fornire  informazioni  chiare  e  precise  sugli  ingredienti  di  ogni  pietanza.  In  ottemperanza  al  Regolamento  (UE)  N.  1169/2011,  è  fatto  obbligo  di  indicare  in  modo  esplicito  la  presenza  di  eventuali  allergeni  per  tutelare  la  salute  e  la  sicurezza  del  consumatore.  Link  di  riferimento:  https://eur-lex.europa.eu/eli/reg/2011/1169/oj?locale=it


---

<!-- Pagina PDF 35 -->
## 📑 Pagina 35

6.  SYSTEM  ARCHITECTURAL  MODEL  6.1.  Activity  Diagrams  6.1.1.  Activity  Diagrams  Utente
 -  Eliminazione  account  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 36 -->
## 📑 Pagina 36

 -  Visualizzazione  del  menu  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
 -  Registrazione  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 37 -->
## 📑 Pagina 37

-  Visualizza  storico  ordini  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  –
 -  Modifica  dati  personali  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 38 -->
## 📑 Pagina 38

-  Effettua  accesso  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
 -  Gestisci  metodo  di  pagamento  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 39 -->
## 📑 Pagina 39

-  Recupero  password  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 40 -->
## 📑 Pagina 40

6.1.2.  Activity  Diagrams  Personale   -  Effettua  accesso  personale  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
 -  Gestisci  profilo  personale  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 41 -->
## 📑 Pagina 41

-  Visualizza  bacheca  avvisi  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
 -  Recupero  password  aziendale  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 42 -->
## 📑 Pagina 42

6.1.3.  Activity  Diagrams  Cliente   -  Effettua  ordinazione  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 43 -->
## 📑 Pagina 43

-  Effettua  pagamento  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 44 -->
## 📑 Pagina 44

-  Lascia  recensione  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 45 -->
## 📑 Pagina 45

-  Gestione  reclami  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 46 -->
## 📑 Pagina 46

-  Monitora  stato  ordine  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 47 -->
## 📑 Pagina 47

6.1.4.  Activity  Diagrams  Cameriere   -  Assegna  tavolo  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
 -  Monitora  stato  ordini  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 48 -->
## 📑 Pagina 48

-  Gestione  pagamento  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 49 -->
## 📑 Pagina 49

-  Inserisce  ordine  manuale  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 50 -->
## 📑 Pagina 50

-  Chiudi  la  comanda  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 51 -->
## 📑 Pagina 51

6.1.5.  Activity  Diagrams  Cuoco   -  Gestione  stato  comanda  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 52 -->
## 📑 Pagina 52

-  Segnala  indisponibilità  piatto  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
 -  Visualizza  comande  in  coda  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 53 -->
## 📑 Pagina 53

6.1.6.  Activity  Diagrams  Manager   -  Gestione  reclami  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 54 -->
## 📑 Pagina 54

-  Aggiorna  menù  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
 -  Gestisci  consegne  delivery  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 55 -->
## 📑 Pagina 55

-  Sospende  account  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 56 -->
## 📑 Pagina 56

-  Pianificazione  turni  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 57 -->
## 📑 Pagina 57

-  Monitora  attività  e  reportistica  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 58 -->
## 📑 Pagina 58

-  Gestisci  personale  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 59 -->
## 📑 Pagina 59

6.2.  Sequence  Diagrams  6.2.1.  Sequence  Diagram  Utente
 -  Elimina  account  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
 -  Registrazione  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 60 -->
## 📑 Pagina 60

-  Visualizza  menù  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
 -  Visualizza  Storico  ordini  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 61 -->
## 📑 Pagina 61

-  Gestisci  metodo  di  pagamento  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
 -  Effettua  accesso  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 62 -->
## 📑 Pagina 62

 -  Modifica  dati  personali  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
 -  Recupero  password  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 63 -->
## 📑 Pagina 63

6.2.2.  Sequence  Diagrams  Personale
 -  Effettua  accesso  personale  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
 -  Visualizza  bacheca  avvisi  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 64 -->
## 📑 Pagina 64

-  Gestione  profilo  personale  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
 -  Recupero  password  aziendale  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 65 -->
## 📑 Pagina 65

6.2.3.  Sequence  Diagrams  Cliente
 -  Effettua  ordinazione  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
 -  Effettua  pagamento  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 66 -->
## 📑 Pagina 66

-  Lascia  recensione  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
 -  Gestisci  reclami  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 67 -->
## 📑 Pagina 67

-  Monitora  stato  ordine  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 68 -->
## 📑 Pagina 68

6.2.4.  Sequence  Diagrams  Cameriere
 -  Assegna  tavolo  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
 -  Inserisce  ordine  manuale  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 69 -->
## 📑 Pagina 69

-  Gestisci  pagamento  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 70 -->
## 📑 Pagina 70

 -  Chiudi  comanda  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
 -  Monitora  Stato  Ordini  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
—


---

<!-- Pagina PDF 71 -->
## 📑 Pagina 71

6.2.5.  Sequence  Diagrams  Cuoco
 -  Segnala  indisponibilità  Piatto  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
 -  Gestione  stato  comanda  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 72 -->
## 📑 Pagina 72

-  Visualizza  comande  in  coda  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 73 -->
## 📑 Pagina 73

6.2.6.  Sequence  Diagrams  Manager   -  Gestisci  consegne  delivery  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
 -  Aggiorna  Menù  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 74 -->
## 📑 Pagina 74

-  Pianificazione  turni  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
 -  Gestione  reclami  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 75 -->
## 📑 Pagina 75

-  Gestione  Attività  e  reportistica  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —
 -  Sospende  account  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 76 -->
## 📑 Pagina 76

-  Gestisci  personale  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —  —


---

<!-- Pagina PDF 77 -->
## 📑 Pagina 77

6.3.  Class  Diagrams  6.3.1.  Class  Diagram  Unrefined


---

<!-- Pagina PDF 78 -->
## 📑 Pagina 78

6.3.2.  Class  Diagram  Refined


---

<!-- Pagina PDF 79 -->
## 📑 Pagina 79

7.  DESIGN  PATTERN  7.1.  Observer
 Secondo  il  caso  d'uso  "Aggiorna  Stato  Comanda",  quando  il  Cuoco  termina  un  piatto  e  aggiorna  lo
stato
su
"Pronto
da
servire/ritirare",
il
sistema
deve
comunicarlo
al
Cameriere.
Senza
questo
pattern,
i
terminali
dei
camerieri
dovrebbero
interrogare
continuamente
il
database
per
chiedere
lo
stato
dell’ordine
(approccio
non
scalabile
e
che
sovraccarica
il
sistema).
 Grazie  al  Design  Pattern  Observer,  è  l'oggetto  Ordine  stesso  che,  appena  cambia  stato,  notifica
proattivamente
tutti
i
dispositivi
dei
camerieri
registrati.


---

<!-- Pagina PDF 80 -->
## 📑 Pagina 80

7.2.  Factory  method
 Il  Manager  ha  la  possibilità  di  registrare  nuovi  dipendenti  (es.  Cuoco  o  Cameriere).  Il
GestorePersonale
(che
funge
da
Client
del
pattern)
ha
la
necessità
di
creare
questi
oggetti,
ma
non
è
in
grado
di
sapere
in
anticipo
le
classi
di
oggetti
che
deve
creare
finché
il
Manager
non
seleziona
il
ruolo
dall'interfaccia.
 Invece  di  collegare  nel  Controller  una  serie  di  istruzioni  condizionali  (if-else)  con  le  chiamate  dirette  a
new
Cuoco()
o
new
Cameriere(),
la
classe
delega
la
responsabilità
di
creazione
a
una
Factory.
 In  questo  modo,  il  Controller  rimane  disaccoppiato  dalle  implementazioni  specifiche  del  personale.


---