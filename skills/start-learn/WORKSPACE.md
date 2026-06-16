# Workspace — struttura e scopo dei file

Riferimento per la **Scenario B workspace** creata da `/start-learn`. Il percorso è scelto dall'utente in plain text; l'accesso nelle sessioni successive avviene con `cd` nella cartella.

## Struttura

```
workspace-root/
  MISSION.md            ← perché l'utente vuole imparare questo topic
  CURRICULUM.md         ← roadmap delle lezioni, editabile a mano
  NOTES.md              ← preferenze dell'utente, note dell'agente
  RESOURCES.md          ← fonti Knowledge + community Wisdom
  lessons/
    0001-nome.html      ← lezioni generate on-demand
    0002-nome.html
  reference/
    glossario.html      ← glossario auto-costruito lezione per lezione
  learning-records/
    0001-slug.md        ← progress record dopo ogni assessment
  notes/                ← atomic notes da /linked-notes (workspace mode)
  flashcards/           ← card files da /flashcards (workspace mode)
  exercises/            ← exercise files da /learn-by-doing (workspace mode)
```

## File chiave

**`CURRICULUM.md`** — roadmap editabile. Formato:
```markdown
# Curriculum: <topic>
- [ ] Lezione 1 — Titolo
- [x] Lezione 2 — Titolo   ← già generata
- [ ] Lezione 3 — Titolo
```
L'agente segna `[x]` quando genera il file HTML. L'utente può riordinare, aggiungere o rimuovere righe liberamente.

**`MISSION.md`** — goal in 3–5 righe: perché, cosa conta come successo, vincoli, fuori scope. Scritto dall'agente dopo il primo scambio, confermato dall'utente.

**`RESOURCES.md`** — popolato via web search. Due sezioni: `## Knowledge` (docs ufficiali, libri) e `## Wisdom` (community, forum, corsi). Fallback se web search non disponibile: nomi senza URL + flag "verifica il link".

**`reference/glossario.html`** — ogni lezione aggiunge automaticamente i termini nuovi. Il file è una pagina HTML stampabile, aggiornata incrementalmente.

## Workspace detection

Qualsiasi skill (assess, linked-notes, flashcards, learn-by-doing) rileva la workspace controllando la presenza di `CURRICULUM.md` nella directory corrente. Se presente → workspace mode. Se assente → legacy mode (percorsi `learn/` come prima).

## Regola del `cd`

L'utente deve essere dentro la workspace prima di invocare qualsiasi skill workspace-aware. Non esiste routing automatico: è responsabilità dell'utente navigare nella cartella giusta.
