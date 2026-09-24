# Programma di Fisica — capitoli, dipendenze, priorità

Fisica per Ingegneria Informatica (Sapienza). Aggiornato il 24/09/2026.
Fonti: programma svolto del corso, dispense degli argomenti aggiuntivi 2026 (§1–13),
analisi degli 8 scritti da giugno 2025 a luglio 2026.

Com'è fatto lo scritto: 3 ore, 5 quesiti da 6 punti, sufficienza 18. Tre esercizi
(meccanica, termodinamica, elettromagnetismo) e due domande di teoria (una di E/M, una di
meccanica/fluidi/termo). La struttura è stata identica in tutti gli 8 scritti.

Questo file è la **mappa** del programma e il posto dove si tiene il **proprio stato**.
La pagina `dashboard.html` si genera da qui: vedi `README.md` e `AGENTS.md`.

---

## Profilo

<!-- Da compilare. Date nel formato gg/mm/aaaa. -->
- Nome:
- Appello:
- Inizio:
- Ore al giorno:
- Obiettivo:
- Priorità incluse: S, A, B, C
- Ore extra (teoria e simulazioni): 40

---

## Come si legge

**ID** — `capitolo.paragrafo`. Le dipendenze usano questi ID.

**Priorità**
- **S** — esce quasi a ogni esame, oppure è prerequisito diretto di qualcosa che esce. Va saputo *fare*.
- **A** — uscito almeno una volta, o teoria candidata forte (dispense 2026). Va saputo.
- **B** — in programma, raro. Basta saperlo esporre a livello di definizione + formula chiave.
- **C** — cultura del programma. Una riga, se capita.

**Slot** — dove pesa all'esame: `E1` esercizio meccanica · `E2` esercizio termo · `E3` esercizio E/M ·
`T-EM` teoria E/M · `T-MT` teoria mecc/fluidi/termo. Tra parentesi quante volte è uscito sugli 8 scritti.

**Stato** — lo tiene aggiornato chi studia (vuoto = da valutare)
- ✖ mai studiato · ◐ visto, non ancora verificato · ⚠ lacuna (provato e non saputo) · ✓ verificato (fatto senza aiuti)

---

## Quadro d'insieme

| Cap | Titolo | Peso all'esame | Priorità | Ore stimate |
|---|---|---|---|---|
| 0 | Strumenti matematici | trasversale (E3, T-EM) | S | 2 |
| 1 | Cinematica del punto | E1 (2/8) | A | 1,5 |
| 2 | Dinamica del punto | E1, T-MT (2/8) | S | 4 |
| 3 | Sistemi e corpo rigido | E1 (4/8), T-MT (2/8) | **S** | 7 |
| 4 | Fluidi | T-MT (2/8) | A | 2,5 |
| 5 | Termodinamica | **E2 (8/8)**, T-MT (2/8) | **S** | 8 |
| 6 | Elettrostatica nel vuoto | E3 (4/8) | **S** | 8 |
| 7 | Correnti | E3 (2/8), T-EM (2/8) | S | 3 |
| 8 | Magnetismo e induzione | E3 (2/8), T-EM (3/8) | **S** | 9 |
| 9 | Equazioni di Maxwell e onde | T-EM (3/8) | S | 4 |
| 10 | Campo elettrico nella materia | T-EM (candidata) | A | 3 |
| 11 | Campo magnetico nella materia | T-EM (1/8) | A | 3 |
| | **Totale** | | | **≈ 55 h** |

Le ore sono di studio + 1–2 esercizi per capitolo, senza carte di teoria e simulazioni. Sono una stima
per chi parte da zero: la pagina le scala in base al proprio stato (sezione "Il tuo piano").

**Dove stanno i punti** (30 in tutto):
- Cap 6–11 (elettromagnetismo): **≈ 12 punti** — tutto E3 + tutta T-EM.
- Cap 5 (termo): **6–9 punti** — E2 ogni volta, a volte anche la teoria.
- Cap 1–4 (meccanica e fluidi): **6–9 punti** — E1 + a volte la teoria.

---

## Grafo delle dipendenze tra capitoli

```
                 ┌──────────────► 1 Cinematica ──► 2 Dinamica ──┬──► 3 Sistemi e corpo rigido
                 │                                              │
                 │                                              ├──► 4 Fluidi
                 │                                              │
 0 Strumenti ────┤                                              └──► 5 Termodinamica  (serve solo 2.6 lavoro)
 matematici      │
                 │                  ┌──► 10 Materia (E)
                 └──► 6 Elettrostat ┤
                                    └──► 7 Correnti ──► 8 Magnetismo ──┬──► 9 Maxwell e onde
                                                           ▲           └──► 11 Materia (B)
                              2.10 oscillatore smorzato ───┘ (solo per 8.9 RLC)
```

Due rami quasi indipendenti: **meccanica + termo** (1→2→3/4/5) ed **elettromagnetismo** (0→6→7→8→9, con 10 e 11 laterali).
Si possono studiare in parallelo, un blocco al giorno per ramo.

**Catena critica** — tutto E3 e tutta la teoria E/M passano di qui:

```
0.4–0.5 flusso, circuitazione, div/Stokes
  → 6.3–6.5 Gauss, I Maxwell, potenziale
    → 6.9–6.10 condensatori, energia
      → 7.3–7.4 FEM, RC
        → 8.3–8.5 Biot-Savart, Ampère
          → 8.6–8.8 Faraday, induttanza, RL
            → 9.1–9.3 Ampère-Maxwell, Maxwell, onde
              → 11.1 M e H
```

---

## Capitolo 0 — Strumenti matematici

Richiamo mirato a quello che serve in elettromagnetismo.

| ID | Argomento | P | Dipende da | Slot | Stato |
| --- | --- | --- | --- | --- | --- |
| 0.1 | Vettori: componenti, prodotto scalare e vettoriale, derivata di un vettore | S | — | tutto |   |
| 0.2 | Coordinate polari, cilindriche, sferiche; elementi dl, dS, dV (dV = 4πr²dr, dV = 2πrL dr) | S | 0.1 | E3, E1 (momenti d'inerzia) |   |
| 0.3 | EDO lineari: 1° ordine (RC, RL), 2° ordine omogenee e forzate, metodo dei complessi | S | — | E3, T-EM, T-MT |   |
| 0.4 | Integrali di linea e di superficie; flusso e circuitazione di un campo | S | 0.2 | E3, T-EM |   |
| 0.5 | Gradiente, divergenza, rotore; **teorema della divergenza** (disp. §6), **teorema di Stokes / della circuitazione** (disp. §7) | S | 0.4 | T-EM (FEM/Stokes 1/8) |   |

---

## Capitolo 1 — Cinematica del punto

| ID | Argomento | P | Dipende da | Slot | Stato |
| --- | --- | --- | --- | --- | --- |
| 1.1 | Posizione, spostamento, velocità e accelerazione medie e istantanee; moto uniforme e uniformemente accelerato, equazioni orarie, grafici | A | 0.1 | E1 |   |
| 1.2 | Moto dei gravi, proiettile | B | 1.1 | E1 |   |
| 1.3 | Moto circolare; velocità e accelerazione angolare; accelerazione tangenziale e normale; **raggio di curvatura**; moto vario | A | 1.1 | E1 (2/8 "cinematica con calcolo") |   |
| 1.4 | Moto nel piano in coordinate polari, **accelerazione di Coriolis** (disp. §1) | A | 1.3, 0.2 | T-MT candidata |   |
| 1.5 | Moto armonico (cinematica) | B | 1.3 | — |   |
| 1.6 | Moti relativi, trasformazioni di Galileo | B | 1.1 | — |   |
| 1.7 | Galileo, metodo scientifico, principio di inerzia e di relatività, grandezze fisiche | C | — | — |   |

---

## Capitolo 2 — Dinamica del punto

| ID | Argomento | P | Dipende da | Slot | Stato |
| --- | --- | --- | --- | --- | --- |
| 2.1 | Leggi di Newton, forze di vincolo, peso, principio di equivalenza | S | 1.1 | E1 |   |
| 2.2 | Attrito statico e dinamico, piano inclinato | S | 2.1 | E1 (2/8 "punto con attrito/vincoli") |   |
| 2.3 | Forza elastica, moto armonico semplice; soluzione per **serie di potenze** (disp. §2) | A | 2.1, 0.3 | T-MT candidata |   |
| 2.4 | Pendolo semplice (piccole oscillazioni) | B | 2.3 | — |   |
| 2.5 | Riferimenti non inerziali, forze apparenti, principio di equivalenza forte | B | 2.1, 1.6 | — |   |
| 2.6 | Lavoro, **potenza**, teorema dell'energia cinetica | S | 2.1, 0.4 | E1 (potenza costante) |   |
| 2.7 | Forze conservative, energia potenziale (peso, gravitazione, elastica), conservazione dell'energia meccanica | S | 2.6 | E1 |   |
| 2.8 | Momento di una forza, momento angolare, momento assiale, teorema del momento angolare e conservazione | S | 2.1, 0.1 | E1 (1/8) |   |
| 2.9 | Gravitazione universale, **orbite**, Keplero, velocità areolare, **velocità di fuga**, forza centrale conservativa | A | 2.7, 2.8 | T-MT (1/8) |   |
| 2.10 | **Oscillatore smorzato**: sotto-critico, critico, sovra-critico (disp. §3) | A | 2.3, 0.3 | T-MT (1/8) |   |
| 2.11 | Oscillazioni forzate, numeri complessi, risonanza (disp. §4) | A | 2.10 | T-MT candidata |   |

---

## Capitolo 3 — Sistemi di punti e corpo rigido

Il cluster più frequente di E1 (rotolamento + carrucola 3/8). Da sapere a memoria: momenti d'inerzia dei corpi standard e vincolo v = ωR.

| ID | Argomento | P | Dipende da | Slot | Stato |
| --- | --- | --- | --- | --- | --- |
| 3.1 | Centro di massa e suo moto, quantità di moto del sistema, **I equazione cardinale**, conservazione di p | A | 2.1 | E1 |   |
| 3.2 | **II equazione cardinale**, conservazione del momento angolare nei sistemi | S | 3.1, 2.8 | E1, T-MT |   |
| 3.3 | Teorema dell'energia cinetica nei sistemi, **teorema di König** (K e L), energia potenziale e conservazione per sistemi | S | 3.1, 3.2, 2.7 | T-MT (1/8), E1 |   |
| 3.4 | **Urti** centrali, elastici e anelastici; **pendolo balistico** | A | 3.1, 2.7 (3.2 se il bersaglio ruota) | T-MT (1/8, luglio 2026) |   |
| 3.5 | **Momento d'inerzia** di corpi estesi (asta, anello, disco, cilindro, sfera), Huygens-Steiner, assi perpendicolari | S | 3.2, 0.2 | E1 |   |
| 3.6 | Dinamica del corpo rigido: rotazione ad asse fisso, τ = Iα, L = Iω, lavoro del momento, K di rotazione; **carrucole massive**, Atwood | S | 3.5 | E1 (3/8) |   |
| 3.7 | Statica, sistemi equivalenti di forze, coppia di forze | B | 3.6 | — |   |
| 3.8 | Pendolo composto | B | 3.6, 2.3 | — |   |
| 3.9 | **Rotolamento puro**: vincolo v = ωR, attrito statico, metodo energetico e dinamico; effetto giroscopico | S | 3.6, 3.3 | E1 (3/8) |   |

---

## Capitolo 4 — Fluidi

Piccolo, autonomo, due teorie già uscite. Buon rapporto resa/ore.

| ID | Argomento | P | Dipende da | Slot | Stato |
| --- | --- | --- | --- | --- | --- |
| 4.1 | Pressione e sua isotropia; equazione della statica dei fluidi (forze conservative, fluidi pesanti) | A | 2.1, 2.7 | T-MT |   |
| 4.2 | **Stevino**, atmosfera isoterma, paradosso idrostatico, **Pascal**, pressa idraulica, misura delle pressioni | A | 4.1 | T-MT (1/8) |   |
| 4.3 | **Archimede**, misura delle densità | A | 4.2 | T-MT (stessa domanda) |   |
| 4.4 | Dinamica: conservazione della massa (**continuità**), **Bernoulli** con esempi | A | 4.1, 2.6 | T-MT (1/8) |   |

---

## Capitolo 5 — Termodinamica

6 punti **a ogni esame** (E2 in 8 scritti su 8), sempre lo stesso schema. Da sapere a memoria:
lavoro, calore ed entropia per ogni tipo di trasformazione, relazioni dell'adiabatica.

| ID | Argomento | P | Dipende da | Slot | Stato |
| --- | --- | --- | --- | --- | --- |
| 5.1 | Principio zero, temperatura, termometri | B | — | — |   |
| 5.2 | Calore, capacità termica, calori specifici, **calorimetria**, equivalente meccanico della caloria | A | 5.1 | E2 (2/8) |   |
| 5.3 | Trasmissione del calore: conduzione, convezione, irraggiamento | C | 5.2 | — |   |
| 5.4 | Sistemi termodinamici, variabili di stato intensive/estensive, trasformazioni quasi statiche, **reversibili e irreversibili**, lavoro nelle reversibili | S | 5.1, 2.6 | E2 |   |
| 5.5 | **I principio**, energia interna come funzione di stato | S | 5.4 | E2 |   |
| 5.6 | Gas perfetti: equazione di stato, R, Dalton; energia interna (esperienza di Joule); c_V, c_p, Mayer, γ mono/biatomico | S | 5.5 | E2 |   |
| 5.7 | **Trasformazioni**: isocora, isobara, isoterma, **adiabatica** (pV^γ, TV^(γ−1), T^γ p^(1−γ)), politropica e suo calore specifico — Q, L, ΔU di ognuna | S | 5.6 | E2 |   |
| 5.8 | **Cicli**: bilancio Q/L/ΔU per tratto, rendimento, macchine frigorifere e COP | S | 5.7 | E2 (6/8) |   |
| 5.9 | Teoria cinetica: pressione cinetica, interpretazione cinetica di T, equipartizione, dipendenza di c_V da T | B | 5.6 | — |   |
| 5.10 | **II principio**: Kelvin-Planck, Clausius, **equivalenza dei due enunciati** | S | 5.8 | T-MT (1/8) |   |
| 5.11 | Ciclo di Carnot, **teorema di Carnot**, temperatura termodinamica | S | 5.10 | T-MT (1/8), E2 |   |
| 5.12 | Integrale di Clausius, **disuguaglianza di Clausius**, entropia come funzione di stato, entropia nei sistemi isolati | S | 5.11 | T-MT candidata |   |
| 5.13 | **ΔS nei calcoli**: gas perfetto per ogni trasformazione, **tratti irreversibili** (percorso reversibile equivalente), **sorgenti**, ΔS dell'universo | S | 5.12, 5.7 | E2 (ΔS 3/8) |   |
| 5.14 | Entropia e disordine, interpretazione statistica, entropia e informazione, III principio | C | 5.12 | — |   |

Trappola già vista: adiabatica = isoentropica **solo se reversibile**.

---

## Capitolo 6 — Elettrostatica nel vuoto

| ID | Argomento | P | Dipende da | Slot | Stato |
| --- | --- | --- | --- | --- | --- |
| 6.1 | Carica, elettroscopio, **Coulomb**, ε₀, campo E, sovrapposizione | S | 0.1 | E3 |   |
| 6.2 | **Distribuzioni continue**: anello (asse), disco, **bacchetta finita** (disp. §5), filo infinito, piano infinito | S | 6.1, 0.4 | E3 (2/8), T-EM candidata |   |
| 6.3 | Flusso, **teorema di Gauss**, simmetria sferica/cilindrica/piana, anche **ρ(r) non uniforme** | S | 6.1, 0.2, 0.4 | E3 (2/8) |   |
| 6.4 | Teorema della divergenza, **I equazione di Maxwell** in forma integrale e differenziale | S | 6.3, 0.5 | T-EM candidata |   |
| 6.5 | Conservatività di E, **potenziale** (carica, anello, da E con integrale di linea), energia elettrostatica di un sistema di cariche | S | 6.1, 2.7 | E3 |   |
| 6.6 | **Dipolo**: potenziale, campo in cartesiane e polari, momento ed energia di un dipolo in campo esterno | B | 6.5 | serve a 10 |   |
| 6.7 | Quadrupolo, **sviluppo in multipoli** (disp. §8) | B | 6.6 | T-EM candidata |   |
| 6.8 | **Conduttori** in equilibrio: proprietà, gabbia di Faraday, effetto delle punte, forza su conduttori carichi, coefficienti di potenziale e di induzione | A | 6.3, 6.5 | E3 |   |
| 6.9 | **Capacità**: conduttore isolato, condensatore piano e sferico, serie e parallelo | A | 6.8 | E3, serve a 7.4, 9.1 |   |
| 6.10 | Energia del condensatore, **densità di energia del campo** (caso piano e caso generale, disp. §9) | A | 6.9 | T-EM candidata |   |

---

## Capitolo 7 — Correnti (campi lentamente variabili)

Il cuore è la parte "di campo" (J, forma locale, circuitazione), non solo i circuiti.

| ID | Argomento | P | Dipende da | Slot | Stato |
| --- | --- | --- | --- | --- | --- |
| 7.1 | Densità e intensità di corrente, **equazione di continuità** | A | 6.1 | serve a 9.1 |   |
| 7.2 | Legge di Ohm (anche locale J = σE), resistenza, resistività, potenza, effetto Joule, serie e parallelo | A | 7.1, 6.5 | E3 |   |
| 7.3 | **Forza elettromotrice**, circuitazione di E, generatori, Kirchhoff — FEM vs ddp | S | 7.2, 0.5 | T-EM (1/8) |   |
| 7.4 | **Carica e scarica del condensatore (RC)**, bilancio energetico | S | 7.3, 6.10, 0.3 | E3 (RC/RL 2/8), T-EM (1/8) |   |

---

## Capitolo 8 — Magnetismo e induzione

Il capitolo che pesa di più sulla teoria E/M.

| ID | Argomento | P | Dipende da | Slot | Stato |
| --- | --- | --- | --- | --- | --- |
| 8.1 | Campo B, **forza di Lorentz**, moto di una carica in campo uniforme, spettrometro di massa | A | 2.1, 1.3 | E3 |   |
| 8.2 | **II formula di Laplace**: forza su un filo, spira in campo uniforme, **momento magnetico**, momento torcente | A | 8.1 | serve a 8.4, 11 |   |
| 8.3 | **I formula di Laplace (Biot-Savart)**: spira circolare sull'asse, **filo rettilineo**, **solenoide** | S | 7.1, 0.4 | E3, T-EM |   |
| 8.4 | **Azioni tra correnti**, definizione dell'Ampère | S | 8.2, 8.3 | T-EM (1/8) |   |
| 8.5 | Solenoidalità di B (II Maxwell), **legge di Ampère**, anche con J(r) | S | 8.3, 0.5 | E3 (1/8) |   |
| 8.6 | **Faraday-Neumann-Lenz**: esperienze, fem di movimento (via Lorentz), giustificazione relativistica, circuitazione di E e **III Maxwell** | S | 8.5, 7.3, 8.1 | E3 (filo-spira 1/8), T-EM candidata |   |
| 8.7 | Mutua induzione e autoinduzione, **induttanza del solenoide** | S | 8.6, 8.3 | T-EM (1/8, luglio 2026) |   |
| 8.8 | **Circuito RL**, energia dell'induttore, **densità di energia del campo B** | S | 8.7, 7.4, 0.3 | E3, T-EM |   |
| 8.9 | **RLC** e analogia con l'oscillatore smorzato | A | 8.8, 2.10 | T-EM (1/8, con RC) |   |

---

## Capitolo 9 — Equazioni di Maxwell e onde

| ID | Argomento | P | Dipende da | Slot | Stato |
| --- | --- | --- | --- | --- | --- |
| 9.1 | Limite della legge di Ampère (condensatore in carica), continuità, **corrente di spostamento, Ampère-Maxwell** | S | 8.5, 7.1, 6.9, 6.4 | T-EM (2/8) |   |
| 9.2 | **Equazioni di Maxwell complete**, forma integrale e differenziale | S | 9.1, 6.4, 8.6 | T-EM |   |
| 9.3 | Equazione delle onde, soluzione, **onde piane** e sferiche: trasversalità, E ⊥ B, E = cB, c = 1/√(ε₀μ₀) | A | 9.2, 0.5 | T-EM (1/8) |   |
| 9.4 | **Vettore di Poynting**, intensità (disp. §13) | A | 9.3, 6.10, 8.8 | T-EM candidata |   |

---

## Capitolo 10 — Campo elettrico nella materia

| ID | Argomento | P | Dipende da | Slot | Stato |
| --- | --- | --- | --- | --- | --- |
| 10.1 | Dielettrici: **P**, σ_p = P·n, ρ_p = −∇·P (disp. §10), suscettività, ε_r, vettore **D**, Gauss per D | A | 6.4, 6.6, 6.9 | T-EM candidata |   |
| 10.2 | Polarizzazione per **deformazione**, polarizzabilità (disp. §11) | B | 10.1, 6.6 | T-EM candidata |   |
| 10.3 | Polarizzazione per **orientamento**, funzione di Langevin (disp. §12.1) | B | 10.1, 6.6 | T-EM candidata |   |

---

## Capitolo 11 — Campo magnetico nella materia

| ID | Argomento | P | Dipende da | Slot | Stato |
| --- | --- | --- | --- | --- | --- |
| 11.1 | Magnetizzazione **M**, campo **H**, suscettività, μ_r, correnti di magnetizzazione, **Ampère nella materia** | A | 8.5, 8.2 | T-EM (1/8) |   |
| 11.2 | Diamagnetismo: modello | B | 11.1 | T-EM candidata |   |
| 11.3 | **Paramagnetismo**: orientamento, Langevin, legge di Curie (disp. §12.2) | B | 11.1, 10.3 | T-EM candidata |   |
| 11.4 | **Ferromagnetismo**: domini di Weiss, campo locale, temperatura di Curie, isteresi (disp. §12.3) | B | 11.3 | T-EM candidata |   |

---
## Ordine di studio consigliato

Topologico (nessun argomento prima dei suoi prerequisiti), poi per priorità. Da adattare al proprio stato:
chi ha già basi solide in un capitolo lo verifica e passa oltre.

1. **Autovalutazione** — segnare lo stato di ogni argomento (con l'agente, ~30 min). Senza, il piano è una stima.
2. **Termodinamica** — 5.4–5.8, poi 5.10–5.13. ~8 h. Rende 6 punti a ogni esame con uno schema sempre uguale.
3. **Catena E/M, parte statica** — 0.4–0.5 → 6.1–6.5 → 6.8–6.10 → 7.1–7.4. ~11 h.
4. **Catena E/M, parte magnetica** — 8.1–8.8 → 9.1–9.3. ~12 h. Qui nascono 5 delle 8 teorie E/M uscite.
5. **Corpo rigido** — 3.5, 3.6, 3.9, poi 3.2–3.4. ~6 h. È il cluster più frequente di E1.
6. **Teorie A a basso costo** — 11.1, 8.9, 9.4, 10.1, 4.1–4.4, 2.9, 2.10, 5.10–5.12.
7. **B e C** solo se avanza tempo: 6.6–6.7, 10.2–10.3, 11.2–11.4, 2.3 (serie di potenze), 2.11, 1.4.

I due rami (meccanica/termo ed E/M) sono indipendenti: si possono alternare, un blocco al giorno per ramo.

---

## Il conto del tempo

- Studio S + A da zero: ≈ 45 h. Tutto il programma: ≈ 55 h.
- Teoria: una scheda per ogni domanda già uscita o candidata (una trentina), ≈ 1 h l'una tra stesura e prova a tempo.
- Simulazioni d'esame a tempo, con correzione: ≈ 4–5 h l'una, almeno 3.
- Il campo "Ore extra (teoria e simulazioni)" del Profilo vale 40 h di default: si cambia a piacere.
- La sezione "Il tuo piano" della pagina fa il conto con il proprio Profilo e il proprio stato.
