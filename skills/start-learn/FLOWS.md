# Flows — dettaglio Scenario A e Scenario B

Riferimento per la **logica di flusso** di `/start-learn`. Il SKILL.md rimanda qui dopo l'auto-detection.

## Auto-detection

L'agente legge la risposta dell'utente e inferisce il flusso:

| Segnali Scenario A | Segnali Scenario B |
|---|---|
| Menziona un file, PR, repo, diff | Menziona un topic, linguaggio, skill nuova |
| "capire questo codice", "cosa fa questo" | "imparare da zero", "non so niente di X" |
| Contesto: codebase attiva aperta | Contesto: nessun artefatto esistente |

Se ambiguo, l'agente dichiara l'assunzione e prosegue:
> *"Parto dall'ipotesi che tu voglia imparare X da zero — dimmi se sbaglio."*

---

## Scenario A — Understand existing code/topic

**Trigger**: l'utente menziona codice esistente o vuole approfondire qualcosa in un progetto attivo.

### Protocollo

1. **Dichiara assunzione** ("Scenario A: stai lavorando su codice esistente") e chiedi conferma in una parola se ambiguo.
2. **Stima il livello** dalla risposta: ha già una base? è esperto? usa quello per filtrare la skill-mapping table.
3. **Proponi** usando la tabella qui sotto. Aspetta sempre che l'utente confermi.
4. **Baseline handoff**: dichiara esplicitamente il livello stimato così `/assess` potrà misurare il delta in futuro.

### Skill-mapping table

| Goal dell'utente | Skill proposta |
|---|---|
| Verificare di aver capito davvero | `/explain-and-check <file-o-topic>` |
| Testare cosa ricorda | `/quiz-me <file-o-topic>` |
| Ancorare a conoscenze precedenti | `/connect-to-what-you-know <file-o-topic>` |
| Catturare note durature | `/linked-notes <file-o-topic>` |
| Catturare flashcard | `/flashcards <file-o-topic>` |
| Praticare con esercizi | `/learn-by-doing <file-o-topic>` |
| Solo domande, niente risposte | `/ask-me-questions <file-o-topic>` |

---

## Scenario B — Learn from scratch

**Trigger**: l'utente vuole imparare qualcosa di nuovo senza artefatti esistenti.

### Protocollo

#### Passo 1 — Workspace
Chiedi in plain text (nessun tool):
> *"Dove vuoi creare la workspace? (es. `~/learning/chess/` o `~/Documenti/rust-ownership/`)"*

Crea la cartella e scrivi `MISSION.md` (3–5 righe: perché, successo, vincoli, fuori scope). Mostra all'utente e aspetta conferma o correzione.

#### Passo 2 — Curriculum
Genera un curriculum di 8–12 lezioni ordinate per difficoltà crescente. Mostra la lista all'utente e aspetta approvazione/modifiche prima di scrivere `CURRICULUM.md`.

Formato `CURRICULUM.md`:
```markdown
# Curriculum: <topic>
- [ ] Lezione 1 — <titolo>
- [ ] Lezione 2 — <titolo>
...
```

L'utente può riordinare, tagliare o aggiungere lezioni liberamente.

#### Passo 3 — Risorse
Cerca via web search fonti autorevoli per il topic. Scrivi `RESOURCES.md` con due sezioni:
- `## Knowledge` — docs ufficiali, libri, corsi
- `## Wisdom` — community, forum, classi locali

Fallback se web search non disponibile: nomi di fonti note senza URL inventati, con flag *"verifica il link"*.

#### Passo 4 — Prima lezione on-demand
Di' all'utente: *"Curriculum pronto. Di' 'prossima lezione' quando vuoi iniziare."*

Quando l'utente chiede la prima lezione:
1. Leggi la prima riga `[ ]` in `CURRICULUM.md`.
2. Cerca la fonte primaria del topic (web search o docs).
3. Genera il file HTML seguendo il template in [LESSON-FORMAT.md](LESSON-FORMAT.md).
4. Segna `[x]` la lezione in `CURRICULUM.md`.
5. Aggiorna `reference/glossario.html` con i termini nuovi della lezione.
6. Indica all'utente come aprire il file HTML.

Ripeti dal punto 1 per ogni lezione successiva.

#### Regole Scenario B

- **Non generare tutte le lezioni upfront** — solo quella richiesta dall'utente, così ogni lezione può adattarsi ai learning-records accumulati.
- **Ogni lezione parte dalla fonte primaria** — nessun contenuto da memoria parametrica senza citazione verificabile.
- **Il glossario si costruisce incrementalmente** — aggiungi solo i termini introdotti nella lezione corrente.
- **Non auto-dispatcher altre skill** — se l'utente vuole fare `/quiz-me` o `/linked-notes` sulla lezione appena letta, proponi il comando ma non lo invocare automaticamente.
