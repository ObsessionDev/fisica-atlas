# fisica-atlas — il programma di Fisica come mappa di studio (Ing. Informatica, Sapienza)

Il programma dello scritto di Fisica in **12 capitoli e 84 argomenti**, con le dipendenze tra gli
argomenti, le priorità ricavate dagli ultimi 8 scritti (giugno 2025 – luglio 2026) e i percorsi di
studio disegnati. Si usa da solo come mappa, oppure con un agente AI come piano di studio personale
che tiene traccia di dove sei.

## Cosa c'è nella dashboard

- **Il tuo piano** — ore che servono, in base a quello che hai già fatto, contro le ore che hai fino all'appello.
- **Quadro d'insieme** — peso di ogni capitolo all'esame, priorità, ore stimate, avanzamento.
- **Percorsi di studio** — tre diagrammi (meccanica, termodinamica, elettromagnetismo) con una fascia
  per capitolo, le dipendenze, lo stato a colori e il **percorso critico** in blu. Zoom con pizzico o
  ⌘/Ctrl + rotella, spostamento trascinando; clic su un argomento per vedere cosa richiede e cosa sblocca.
- **Capitoli** — tutti gli argomenti, filtrabili per priorità, stato e percorso critico.

## Setup

Requisiti: un browser. Per il piano personale anche **Python 3.8+** e un agente
(Claude Code, Codex, Gemini CLI, Cursor o simili).

```
git clone https://github.com/ObsessionDev/fisica-atlas.git
cd fisica-atlas
```

Oppure scarica lo zip (*Code → Download ZIP*) ed estrailo.

Per vedere la dashboard basta aprire `dashboard.html` con un doppio clic. Funziona offline.

## Configurazione

Tutto sta in `PROGRAMMA.md`, l'**unico file che cambia**. Due parti sono tue.

**Profilo** (in cima al file)

| Campo | Esempio | A cosa serve |
|---|---|---|
| `Nome` | Giulia | facoltativo |
| `Appello` | 20/01/2027 | data dello scritto, per il conto dei giorni |
| `Inizio` | 01/10/2026 | da quando studi; vuoto = oggi |
| `Ore al giorno` | 3 | per il conto delle ore disponibili |
| `Obiettivo` | ≥ 24 | testo libero, lo usa l'agente |
| `Priorità incluse` | S, A | togli B e C se hai poco tempo |
| `Ore extra (teoria e simulazioni)` | 40 | ore oltre allo studio degli argomenti |

**Stato** (colonna delle tabelle dei capitoli): vuoto = da valutare · `✖` mai studiato ·
`◐` visto, non verificato · `⚠` lacuna · `✓` verificato (fatto senza aiuti).

Si possono modificare a mano o farli modificare all'agente. Dopo ogni modifica si rigenera la pagina:

```
python3 strumenti/genera_programma_html.py
```

## Uso con un agente

1. Apri l'agente **in questa cartella** (`claude`, `codex`, `gemini`, oppure la cartella in Cursor).
2. Scrivi `iniziamo`. L'agente legge `AGENTS.md`, ti chiede appello e ore al giorno, ti guida
   nell'autovalutazione capitolo per capitolo e aggiorna la dashboard.
3. Poi, quando vuoi:
   - `cosa studio adesso?` — propone 1–3 argomenti con i prerequisiti a posto, partendo dal percorso critico
   - `studiamo 6.3` — spiegazione mirata, un esercizio, correzione e aggiornamento dello stato
   - `interrogami sul capitolo 8` — cinque domande, una alla volta
   - `l'appello è il 20/01, ho 2 ore al giorno` — aggiorna profilo e piano

`AGENTS.md` lo leggono da soli Codex, Cursor e altri; `CLAUDE.md` e `GEMINI.md` rimandano lì per
Claude Code e Gemini CLI. Con altri strumenti basta dire: "leggi AGENTS.md e seguilo".

## Segnalare un problema

Hai trovato un errore nel programma, la dashboard non funziona o hai un'idea? Apri una
[issue](https://github.com/ObsessionDev/fisica-atlas/issues/new/choose) e scegli il modulo giusto:
**errore nel programma**, **problema di installazione o di uso**, **idea o miglioramento**.
Serve un account GitHub gratuito. Non incollare il tuo stato di studio né dati personali: le issue
sono pubbliche.

## Privacy

Il tuo stato resta in `PROGRAMMA.md`, sul tuo computer. Se fai un fork **pubblico** e ci spingi le
tue modifiche, anche il tuo stato diventa pubblico.

## File

- `PROGRAMMA.md` — programma, profilo e stato
- `dashboard.html` — la dashboard, generata da `PROGRAMMA.md` (non si modifica a mano)
- `AGENTS.md` — istruzioni per l'agente; `CLAUDE.md` e `GEMINI.md` rimandano qui
- `strumenti/` — il generatore (solo libreria standard di Python)
