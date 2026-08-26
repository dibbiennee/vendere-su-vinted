# Vendere su Vinted

Guida operativa alla vendita su Vinted e **Cartellino**, gli strumenti che la accompagnano.

## Cosa c'e' dentro

| Cartella | Contenuto |
|---|---|
| `app/` | Cartellino: sei strumenti in una pagina sola, senza account e senza server |
| `landing/` | La pagina di vendita della guida |
| `build/` | I sorgenti della guida in markdown e lo script che genera il DOCX |
| `riferimenti/` | Materiali di riferimento per il design |
| `GUIDA_COMPLETA_VINTED_2026.docx` / `.pdf` | La guida completa, 95 pagine e 15 capitoli |

## Cartellino

Sei strumenti per chi vende abbigliamento usato:

- **Metro** calcola quanto paga davvero il cliente e quanto ti resta, con la regola del 4x sul costo di acquisto
- **Diagnosi** legge visualizzazioni e preferiti di un articolo fermo e dice se il problema e' il titolo, la foto o il prezzo
- **Etichetta** genera titolo e descrizione pronti da copiare, misure comprese
- **Armadio** e' il magazzino: codice, posizione, costo, stato
- **Bilancia** calcola tasso di vendita, margine medio, ricavo orario e le soglie DAC7
- **Scontrino** genera ricevute di vendita fra privati, con logo e codice a barre

I dati restano nel browser di chi usa l'app: nessun account, nessun database, nessuna telemetria.

## Come si usa

Sono pagine HTML autonome: si aprono con un doppio clic o si caricano su qualsiasi hosting statico.

```
app/index.html        Cartellino
landing/index.html    la pagina di vendita
```

Per rigenerare il DOCX della guida dai sorgenti markdown:

```bash
cd build && python3 build_docx.py
```

L'indice ha i numeri di pagina reali: dopo aver modificato i capitoli va rigenerata la mappa delle pagine, altrimenti i rimandi si disallineano.

## Nota sulle ricevute

Lo strumento Scontrino produce **ricevute di vendita fra privati**, non documenti fiscali. Non genera la dicitura "documento commerciale", la matricola del registratore telematico o l'esposizione IVA: quelli appartengono ai documenti emessi da un RT certificato. Ogni ricevuta riporta in fondo "Non valida ai fini fiscali".

## Dati

I dati di mercato citati nella guida provengono dai risultati finanziari Vinted 2025 e sono verificati a meta' 2026. Commissioni, soglie fiscali e regole della piattaforma cambiano: la guida indica sempre a quale data ogni dato e' verificato.

Le indicazioni fiscali hanno finalita' informativa e non sostituiscono un commercialista. Progetto indipendente, non affiliato ne' approvato da Vinted.
