"""Genera dashboard.html da PROGRAMMA.md.

Uso: python3 strumenti/genera_programma_html.py [percorso/PROGRAMMA.md]
Senza argomenti usa il PROGRAMMA.md nella cartella sopra `strumenti/`.
La pagina (dashboard.html) si scrive accanto al PROGRAMMA.md. Solo libreria standard, Python 3.8+.
La fonte resta PROGRAMMA.md: la pagina si rigenera, non si modifica a mano.
"""
import html
import json
import re
import sys
from pathlib import Path

from programma_dati import RADICE, leggi

# Etichette brevi per i riquadri dei diagrammi.
ETICHETTE = {
    "0.1": "Vettori", "0.2": "Coordinate e dV", "0.3": "EDO lineari",
    "0.4": "Flusso e circuitazione", "0.5": "Div, rot, Stokes",
    "1.1": "Moti rettilinei", "1.3": "Moto circolare", "1.4": "Polari, Coriolis",
    "1.6": "Moti relativi",
    "2.1": "Newton, vincoli", "2.2": "Attrito", "2.3": "Moto armonico",
    "2.6": "Lavoro, potenza", "2.7": "Energia meccanica", "2.8": "Momento angolare",
    "2.9": "Gravitazione, orbite", "2.10": "Oscillatore smorzato",
    "2.11": "Oscillazioni forzate",
    "3.1": "Centro di massa", "3.2": "II cardinale", "3.3": "König",
    "3.4": "Urti, p. balistico", "3.5": "Momento d'inerzia",
    "3.6": "Corpo rigido, carrucole", "3.9": "Rotolamento puro",
    "4.1": "Statica dei fluidi", "4.2": "Stevino, Pascal", "4.3": "Archimede",
    "4.4": "Continuità, Bernoulli",
    "5.1": "Principio zero", "5.2": "Calorimetria", "5.4": "Rev. e irreversibili",
    "5.5": "I principio", "5.6": "Gas perfetti", "5.7": "Trasformazioni",
    "5.8": "Cicli, rendimento", "5.10": "II principio", "5.11": "Carnot",
    "5.12": "Clausius, entropia", "5.13": "ΔS e irreversibili",
    "6.1": "Coulomb, campo E", "6.2": "Distribuzioni continue", "6.3": "Gauss",
    "6.4": "I Maxwell", "6.5": "Potenziale", "6.6": "Dipolo", "6.8": "Conduttori",
    "6.9": "Capacità", "6.10": "Energia del campo E",
    "7.1": "Corrente, continuità", "7.2": "Ohm, Joule", "7.3": "FEM, Kirchhoff",
    "7.4": "Circuito RC",
    "8.1": "Lorentz", "8.2": "II Laplace", "8.3": "Biot-Savart",
    "8.4": "Azioni tra correnti", "8.5": "Ampère", "8.6": "Faraday-Lenz",
    "8.7": "Induttanza", "8.8": "RL, energia di B", "8.9": "RLC",
    "9.1": "Ampère-Maxwell", "9.2": "Maxwell complete", "9.3": "Onde piane",
    "9.4": "Poynting",
    "10.1": "P, D, dielettrici", "11.1": "M, H, Ampère materia",
}

# Blocchi dei diagrammi: fasce (una per capitolo) e percorso critico.
# Meccanica e termo sono separati: la termo dipende dalla meccanica solo per 2.6.
# L'E/M resta intero: circuiti e magnetismo si agganciano all'elettrostatica in troppi punti.
BLOCCHI = [
    {
        "id": "mecc", "titolo": "Meccanica",
        "fasce": [["Strumenti", [0]], ["Cinematica", [1]], ["Dinamica del punto", [2]],
                  ["Sistemi e corpo rigido", [3]], ["Fluidi", [4]]],
        "critico": ["2.1", "2.7", "2.8", "3.1", "3.2", "3.3", "3.5", "3.6", "3.9"],
        "nota": "Percorso critico: il corpo rigido, fino al rotolamento — il cluster più frequente "
                "dell'esercizio di meccanica (4 scritti su 8).",
    },
    {
        "id": "termo", "titolo": "Termodinamica",
        "fasce": [["Termodinamica", [5]]],
        "critico": ["5.4", "5.5", "5.6", "5.7", "5.8", "5.10", "5.11", "5.12", "5.13"],
        "nota": "Percorso critico: dalle trasformazioni all'entropia con irreversibili — "
                "l'esercizio che esce a ogni esame.",
    },
    {
        "id": "em", "titolo": "Elettromagnetismo",
        "fasce": [["Strumenti", [0]], ["Elettrostatica", [6]], ["Correnti", [7]],
                  ["Magnetismo e induzione", [8]], ["Maxwell e onde", [9]], ["Materia", [10, 11]]],
        "critico": ["0.4", "0.5", "6.3", "6.4", "6.5", "6.8", "6.9", "6.10", "7.3", "7.4",
                    "8.3", "8.5", "8.6", "8.7", "8.8", "9.1", "9.2", "9.3", "11.1"],
        "nota": "Da questa catena passano tutto l'esercizio E/M e tutta la teoria E/M, "
                "circa 12 punti su 30.",
    },
]


def inline(t):
    t = html.escape(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![*\w])\*([^*]+)\*(?!\w)", r"<em>\1</em>", t)
    return t


def md(blocco):
    """Markdown minimo: paragrafi, elenchi, tabelle. I blocchi ``` si saltano."""
    out, lista, tabella, codice, prec = [], None, [], False, False

    def chiudi():
        nonlocal lista, tabella
        if lista:
            out.append(f"</{lista}>")
            lista = None
        if tabella:
            righe = [r for r in tabella if not re.match(r"^\|[-| ]+\|$", r)]
            testa, *corpo = [[inline(c.strip()) for c in r.strip("|").split("|")] for r in righe]
            out.append('<div class="tabwrap"><table><thead><tr>'
                       + "".join(f"<th>{c}</th>" for c in testa) + "</tr></thead><tbody>"
                       + "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in corpo)
                       + "</tbody></table></div>")
            tabella = []

    for riga in blocco:
        if riga.startswith("```"):
            codice = not codice
            continue
        if codice:
            continue
        if riga.startswith("|"):
            if lista:
                out.append(f"</{lista}>")
                lista = None
            tabella.append(riga)
            continue
        m = re.match(r"^(\d+\.|-) (.*)$", riga)
        if m:
            tipo = "ol" if m.group(1)[0].isdigit() else "ul"
            if tabella:
                chiudi()
            if lista != tipo:
                if lista:
                    out.append(f"</{lista}>")
                out.append(f"<{tipo}>")
                lista = tipo
            out.append(f"<li>{inline(m.group(2))}</li>")
            continue
        chiudi()
        if riga.strip() and riga.strip() != "---" and not riga.startswith("<!--"):
            # righe consecutive dello stesso paragrafo si uniscono
            if out and out[-1].startswith("<p>") and prec:
                out[-1] = out[-1][:-4] + " " + inline(riga) + "</p>"
            else:
                out.append(f"<p>{inline(riga)}</p>")
        prec = bool(riga.strip()) and not riga.startswith("|")
    chiudi()
    return "\n".join(out)


def sezione(testo, titolo):
    m = re.search(rf"^## {re.escape(titolo)}\n(.*?)(?=^## |\Z)", testo, re.S | re.M)
    return m.group(1).strip().splitlines() if m else []


def main():
    sorgente = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else RADICE / "PROGRAMMA.md"
    testo, capitoli, argomenti, profilo = leggi(sorgente)
    for a in argomenti:
        a["breve"] = ETICHETTE.get(a["id"], re.sub(r"\*\*|\(.*", "", a["testo"])[:24].strip())
        a["html"] = inline(a["testo"])
    for c in capitoli:
        c["intro_html"] = md(c.pop("intro"))
    data = re.search(r"(?:Scritto|Aggiornato) il ([\d/]+)", testo)
    dati = {
        "capitoli": capitoli, "argomenti": argomenti, "blocchi": BLOCCHI, "profilo": profilo,
        "quadro": md(sezione(testo, "Quadro d'insieme")),
        "ordine": md(sezione(testo, "Ordine di studio consigliato")),
        "tempo": md(sezione(testo, "Il conto del tempo")),
        "data": data.group(1) if data else "",
    }
    modello = (Path(__file__).resolve().parent / "programma_modello.html").read_text(encoding="utf-8")
    uscita = modello.replace("__DATI__", json.dumps(dati, ensure_ascii=False).replace("</", "<\\/"))
    destinazione = sorgente.parent / "dashboard.html"
    destinazione.write_text(uscita, encoding="utf-8")
    print(f"{destinazione.name}: {len(argomenti)} argomenti, {len(capitoli)} capitoli")


if __name__ == "__main__":
    main()
