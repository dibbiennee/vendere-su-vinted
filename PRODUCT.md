# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Persone che vendono, o vogliono iniziare a vendere, abbigliamento usato su Vinted in Italia. Tre situazioni confermate dai contenuti della guida:

- chi svuota l'armadio e ricava 50-200 € al mese, senza metodo;
- chi vende già con regolarità (20-50 articoli al mese) e non capisce perché gli articoli restano fermi;
- chi vuole trasformare l'attività in un lavoro e deve affrontare sourcing, magazzino e posizione fiscale.

Il contesto d'uso è mobile: leggono e vendono dal telefono, spesso in ritagli di tempo.

## Product Purpose

Vendere una guida operativa a pagamento (95 pagine, 15 capitoli, ~19.100 parole) che insegna a vendere su Vinted con un metodo verificabile, e nel frattempo raccogliere una lista di persone interessate a un futuro strumento software per venditori Vinted.

Successo della landing: l'acquisto della guida al prezzo di lancio, con l'email come meccanismo di conversione.

## Positioning

La guida è costruita su accuratezza verificabile, non su promesse di guadagno. Tre elementi che un concorrente non può copiare onestamente:

- dati di mercato con fonte (risultati finanziari Vinted 2025) invece di statistiche inventate;
- correzione di errori diffusi nelle guide gratuite: il denaro resta nel Saldo Vinted e il bonifico va richiesto; la Protezione acquisti (0,70 € + 5%) la paga il compratore ma alza il prezzo finale;
- distinzione esplicita, nel capitolo sull'algoritmo, tra ciò che è certo, osservato e ipotizzato.

## Operating Context

Il prodotto è un file (DOCX e PDF) consegnato dopo l'acquisto. La landing è il solo punto di contatto commerciale. Il pubblico arriverà prevalentemente da mobile.

## Capabilities and Constraints

- Prezzo di lancio confermato: **29 €**, prezzo pieno di riferimento 49 €.
- Nessun sistema di pagamento attivo: la landing raccoglie **solo l'email**, il pagamento avviene manualmente al lancio. Il form non ha ancora un backend: serve un segnaposto sostituibile.
- Il software futuro è **deliberatamente non specificato**: in pagina va comunicato come teaser, senza elencare funzioni non ancora costruite. Chi acquista ora avrà un prezzo riservato al lancio.
- Nome del software: **Cartellino** (proposto e accettato).
- **Offerta, rivista ad agosto 2026:** i 29 € comprendono la guida **e** Cartellino, il software con gli strumenti, il cui accesso è incluso al lancio senza costi aggiuntivi. Pagamento unico, nessun abbonamento.
- **Upsell separato: il generatore di scontrini, 4,90 € al mese**, disdicibile. Resta provabile in pagina senza pagare e senza registrazione: l'abbonamento serve per salvare, numerare e ritrovare le ricevute. Il piano di abbonamento non è ancora attivo: la pagina raccoglie interesse, non incassa.
- **Limite deliberato sul generatore di ricevute:** riproduce l'estetica dello scontrino termico (carattere, colonne, blocco pagamenti, codice a barre, formato 80/58 mm) ma **non** la dicitura "documento commerciale", la matricola RT o l'esposizione IVA. Quelli appartengono al documento fiscale emesso da registratore telematico: generarli con dati arbitrari produrrebbe un falso documento fiscale. In fondo a ogni ricevuta resta "Non valida ai fini fiscali".
- Lingua: italiano.

## Brand Commitments

- Titolo confermato: "Vendere su Vinted", sottotitolo "La guida completa per trasformare l'armadio in un business".
- Identità visiva esistente e vincolante: copertina in `copertina.png`, verde-petrolio profondo (#0E4A52), accento acqua (#7FC7CE), crema (#F2EDE3), cartellino prezzo come elemento grafico, titoli Trebuchet, testo Georgia.
- Voce: diretta e operativa, senza toni da guru. **Vietati i trattini lunghi (—)** e le sezioni di contesto non operative.
- Nessuna promessa di guadagno facile: è una scelta di posizionamento, non solo di stile.
- **Formato della landing, deciso dall'utente ad agosto 2026: pagina di vendita verticale a colonna unica, pensata per il telefono, con tono persuasivo.** Struttura: promessa, problema riconoscibile, cosa cambia, prove, indice, per chi sì e per chi no, strumento, riepilogo dell'offerta, domande. Azione sempre raggiungibile con barra fissa in basso. Due direzioni espressive sono state provate e rifiutate: il minimalismo editoriale su fondo scuro ("spenta e povera") e la copertina di rivista ("troppo strana"); anche la scheda prodotto e-commerce è stata superata perché poco persuasiva. Vale come vincolo permanente.
- **La persuasione resta ancorata ai fatti**: nessuna testimonianza, nessun contatore di copie vendute, nessuna promessa di guadagno, nessuna scadenza inventata. Le leve ammesse sono quelle vere: il prezzo di lancio che torna a 49 €, i dati verificabili con capitolo e pagina, la sezione che dice a chi la guida non serve.

## Evidence on Hand

- Il prodotto reale esiste: `GUIDA_COMPLETA_VINTED_2026.docx` e `.pdf`, 95 pagine, indice di 140 voci verificate.
- Contenuti sorgente in `build/capitoli/*.md`: da qui si possono estrarre estratti reali da mostrare in pagina.
- Copertina reale ad alta risoluzione in `copertina.png`.
- **Assenze da non inventare:** nessun cliente, nessuna recensione, nessun numero di copie vendute, nessun caso studio, nessuna testimonianza. Il prodotto non è ancora stato venduto a nessuno.

## Product Principles

1. La prova è il contenuto stesso: mostrare estratti veri della guida vale più di qualsiasi affermazione su di essa.
2. Non fabbricare prova sociale. In assenza di clienti, la credibilità viene da accuratezza e trasparenza.
3. Ogni promessa deve essere verificabile dal lettore, come le promesse che la guida insegna a scrivere nelle inserzioni.
4. Mobile prima di tutto: il pubblico vive su telefono.
5. Il software resta una promessa sobria finché non esiste.

## Accessibility & Inclusion

Nessun requisito specifico dichiarato. Vale lo standard: contrasto adeguato, tocco comodo su mobile, form utilizzabile da tastiera e screen reader.
