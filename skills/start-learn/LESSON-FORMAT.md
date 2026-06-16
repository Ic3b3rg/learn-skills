# Lesson format — template HTML e formati pratica

Riferimento per le lezioni Scenario B generate da `/start-learn`. Ogni lezione è un file HTML auto-contenuto in `lessons/`.

## Struttura fissa (ogni lezione)

```
1. Titolo + obiettivo della lezione
2. Spiegazione — l'agente insegna, con citazioni a fonti
3. Pratica adattiva — formato scelto in base al topic
4. Fonte primaria consigliata + link alla lezione successiva
```

La struttura è sempre questa. Il formato della sezione pratica varia.

## Formati pratica adattativi

### A-B-C-D (default)
Per linguaggi, teoria, nomenclatura. Domande a scelta multipla classiche. Ogni risposta deve avere lo stesso numero di caratteri — nessun indizio visivo sulla risposta corretta.

### SVG diagram
Per topic spaziali: scacchiera, flowchart, anatomia, circuiti. Il diagramma SVG inline precede la domanda. La domanda chiede di identificare, posizionare o ragionare sul diagramma.

### Code editor
Per programmazione. Un `<textarea>` con monospace + un pulsante "Verifica" con JS inline che confronta l'output. Il codice di verifica è incluso nel file HTML — nessuna dipendenza esterna.

### Sequence display
Per procedure: sequenze Rubik's, mosse yoga, algoritmi step-by-step. La sequenza è visualizzata, la domanda chiede di completarla o correggerla.

## Template HTML

```html
<!DOCTYPE html>
<html lang="<language>">
<head>
  <meta charset="UTF-8">
  <title><N>. <Titolo lezione></title>
  <style>
    /* stile Tufte: font serif, larghezza limitata, ampi margini */
    body { max-width: 640px; margin: 4rem auto; font-family: Georgia, serif;
           line-height: 1.7; color: #222; padding: 0 1.5rem; }
    h1 { font-size: 1.4rem; } h2 { font-size: 1.1rem; margin-top: 2rem; }
    .objective { color: #555; font-style: italic; margin-bottom: 2rem; }
    .practice { background: #f8f8f8; border-left: 3px solid #ccc;
                padding: 1rem 1.5rem; margin: 2rem 0; }
    .feedback { margin-top: 0.5rem; font-weight: bold; }
    .nav { margin-top: 3rem; border-top: 1px solid #eee; padding-top: 1rem;
           font-size: 0.9rem; }
    cite { font-size: 0.85rem; color: #666; }
  </style>
</head>
<body>
  <h1>Lezione <N> — <Titolo></h1>
  <p class="objective">Obiettivo: <una frase></p>

  <h2>Spiegazione</h2>
  <p><!-- contenuto didattico, con citazioni inline --></p>
  <cite>Fonte: <link a fonte autorevole></cite>

  <h2>Pratica</h2>
  <div class="practice">
    <!-- sezione pratica adattiva: A-B-C-D / SVG / code editor / sequence -->
  </div>

  <div class="nav">
    <strong>Fonte primaria:</strong> <a href="...">...</a><br>
    <!-- se esiste lezione successiva: -->
    <a href="000N-prossima.html">→ Lezione N+1</a>
  </div>
</body>
</html>
```

## Naming e numerazione

File: `lessons/000N-kebab-slug.html` dove N è il numero della lezione nel CURRICULUM.md (con zero-padding a 4 cifre). Slug derivato dal titolo.

## Regole

- **Nessuna dipendenza esterna** — niente CDN, niente script remoti. Il file deve aprirsi offline.
- **Stampabile** — lo stile Tufte (colonne strette, serif) è pensato per la stampa.
- **Risposte multiple uguali in lunghezza** — per A-B-C-D, pareggiare i caratteri per non dare indizi visivi.
- **Feedback immediato** — il JS inline mostra corretto/sbagliato al click, senza ricaricare la pagina.
