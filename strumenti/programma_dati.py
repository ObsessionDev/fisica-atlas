"""Legge PROGRAMMA.md e restituisce capitoli, argomenti e profilo come dati.

Le tabelle degli argomenti si leggono per nome di colonna: `Lezione` è facoltativa,
`Stato` vuoto vale `?` (da valutare).
"""
import re
from pathlib import Path

RADICE = Path(__file__).resolve().parent.parent
ID_RE = re.compile(r"\b(\d{1,2}\.\d{1,2})\b")
STATI = "✖⚠◐✓?"


def celle(riga):
    return [c.strip() for c in riga.strip().strip("|").split("|")]


def numero(t):
    m = re.search(r"\d+(?:[.,]\d+)?", t)
    return float(m.group().replace(",", ".")) if m else None


def leggi(percorso=RADICE / "PROGRAMMA.md"):
    testo = Path(percorso).read_text(encoding="utf-8")
    capitoli, argomenti, profilo = [], [], {}
    cap, sez, testa = None, None, None
    ore = {}
    for riga in testo.splitlines():
        m = re.match(r"^## (.+)$", riga)
        if m:
            sez, testa = m.group(1), None
            mc = re.match(r"^Capitolo (\d+) — (.+)$", sez)
            cap = {"n": int(mc.group(1)), "titolo": mc.group(2), "intro": []} if mc else None
            if cap:
                capitoli.append(cap)
            continue
        if sez == "Profilo":
            mp = re.match(r"^- ([^:]+):\s*(.*)$", riga)
            if mp:
                profilo[mp.group(1).strip()] = re.sub(r"<!--.*?-->", "", mp.group(2)).strip()
            continue
        if riga.startswith("|"):
            c = celle(riga)
            if re.match(r"^[-: ]+$", "".join(c)):
                continue
            if testa is None:
                testa = c
                continue
            r = dict(zip(testa, c))
            if sez == "Quadro d'insieme" and re.match(r"^\d+$", r.get("Cap", "")):
                col = next((k for k in testa if k.lower().startswith("ore")), None)
                if col:
                    ore[int(r["Cap"])] = numero(r[col])
            elif cap is not None and "ID" in r:
                stato = (r.get("Stato") or "?").strip() or "?"
                argomenti.append({
                    "id": r["ID"], "cap": cap["n"], "testo": r["Argomento"], "p": r["P"],
                    "dip": ID_RE.findall(r.get("Dipende da", "")), "dip_testo": r.get("Dipende da", ""),
                    "slot": r.get("Slot", ""),
                    "stato": stato[0] if stato[0] in STATI else "?", "stato_testo": stato,
                    "lezione": r.get("Lezione", ""),
                })
            continue
        testa = None
        if cap is not None and riga and not riga.startswith("---"):
            cap["intro"].append(riga)
    for c in capitoli:
        c["ore"] = ore.get(c["n"])
    return testo, capitoli, argomenti, profilo
