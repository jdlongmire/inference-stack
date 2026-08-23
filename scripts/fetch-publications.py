#!/usr/bin/env python3
"""Regenerate docs/_data/publications.yml from Zenodo.

The publications page is rendered from that data file, so refreshing the index is a
re-run of this script rather than hand-editing a list. Queries by ORCID, keeps the
newest version of each work, and merges the two authors (every one of Micah's works
is co-authored with JD, so the union is deduplicated by concept id).

    python3 scripts/fetch-publications.py            # write docs/_data/publications.yml
    python3 scripts/fetch-publications.py --check    # report drift, write nothing
"""
import argparse, json, sys, time, urllib.parse, urllib.request
from pathlib import Path

AUTHORS = {
    "0009-0009-1383-7698": "James (JD) Longmire",
    "0009-0006-7608-9322": "Micah Longmire",
}
OUT = Path(__file__).resolve().parent.parent / "docs" / "_data" / "publications.yml"
API = "https://zenodo.org/api/records"

# Zenodo rejects size > 25 on this endpoint.
PAGE_SIZE = 25


def fetch(orcid):
    out, page = [], 1
    while True:
        qs = urllib.parse.urlencode({
            "q": f'metadata.creators.person_or_org.identifiers.identifier:"{orcid}"',
            "size": PAGE_SIZE, "page": page, "sort": "newest",
        })
        req = urllib.request.Request(f"{API}?{qs}",
                                     headers={"Accept": "application/json",
                                              "User-Agent": "inference-stack/publications"})
        data = json.loads(urllib.request.urlopen(req, timeout=60).read())
        hits = data["hits"]["hits"]
        out += hits
        if len(out) >= data["hits"]["total"] or not hits:
            return out
        page += 1
        time.sleep(0.4)


def resource_type(md):
    rt = md.get("resource_type") or {}
    title = rt.get("title")
    if isinstance(title, dict):
        return title.get("en") or rt.get("type")
    return title or rt.get("type")


def creator_name(cr):
    p = cr.get("person_or_org") or cr
    return p.get("name") or " ".join(
        filter(None, [p.get("given_name"), p.get("family_name")])) or "Unknown"


# Domain is assigned from title keywords, most specific first. The corpus spans four
# research programmes; only "technology" is published on this site, so a work landing in
# the wrong bucket either appears where it should not or vanishes from the index. The
# script keeps classifying all four so a future re-scope needs no re-derivation.
RULES = [
    ("geology", ("flood", "hydrotectonic", "continental", "deep time", "geolog",
                 "stratigraph", "radiometric")),
    ("theology", ("covenant", "biblical", "naturalism", "contingency", "transcendental",
                  "designism", "theistic", "creation model", "special creation",
                  "existential inertia", "necessity argument", "duality argument",
                  "godelian", "gödelian", "seventh day", "consilience")),
    ("physics", ("quantum", "qft", "logic realism", "born rule", "fock", "spacetime",
                 "entanglement", "packet", "physical logic", "logic field",
                 "triadic reality", "viscosity", "it from bit", "logical emergence",
                 "renormalization", "information-geometric", "meta-theory of everything")),
]


# Keyword rules get these two wrong, so they are named explicitly. "Logic Packets"
# matches the physics rule on "packet" but is a critique of LLM optimism; the
# Transcendental Argument paper matches the theology rule but is Part I of the Logic
# Realism programme and belongs with it.
OVERRIDES = {
    "logic packets and the limits of derivation": "technology",
    "the transcendental argument for being": "physics",
}


def domain_of(title):
    t = (title or "").lower()
    for frag, dom in OVERRIDES.items():
        if frag in t:
            return dom
    for name, keys in RULES:
        if any(k in t for k in keys):
            return name
    return "technology"


def collect():
    by_concept = {}
    for orcid in AUTHORS:
        for rec in fetch(orcid):
            cid = str((rec.get("parent") or {}).get("id")
                      or rec.get("conceptrecid") or rec["id"])
            prev = by_concept.get(cid)
            newer = (rec["metadata"].get("publication_date") or "")
            if not prev or newer > (prev["metadata"].get("publication_date") or ""):
                by_concept[cid] = rec
    works = []
    for cid, rec in by_concept.items():
        md = rec["metadata"]
        works.append({
            "id": str(rec["id"]),
            "title": " ".join((md.get("title") or "").split()),
            "date": md.get("publication_date"),
            "type": resource_type(md),
            "doi": rec.get("doi") or md.get("doi"),
            "url": (rec.get("links") or {}).get("self_html")
                   or f"https://zenodo.org/records/{rec['id']}",
            "creators": [creator_name(c) for c in (md.get("creators") or [])],
            "domain": domain_of(md.get("title")),
        })
    works.sort(key=lambda w: (w["date"] or ""), reverse=True)
    return works


def to_yaml(works):
    def esc(s):
        return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"') + '"'
    lines = ["# Generated by scripts/fetch-publications.py. Do not edit by hand.",
             f"# Source: Zenodo, by ORCID ({', '.join(AUTHORS)}).", ""]
    for w in works:
        lines.append(f"- id: {esc(w['id'])}")
        for k in ("title", "date", "type", "doi", "url", "domain"):
            lines.append(f"  {k}: {esc(w[k]) if w[k] is not None else '~'}")
        lines.append("  creators:")
        lines += [f"    - {esc(c)}" for c in w["creators"]]
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="report drift, write nothing")
    args = ap.parse_args()
    works = collect()
    text = to_yaml(works)
    if args.check:
        old = OUT.read_text() if OUT.exists() else ""
        status = "up to date" if old == text else "DRIFTED"
        print(f"{len(works)} works on Zenodo; {OUT.name} is {status}")
        return 0 if old == text else 1
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text)
    counts = {}
    for w in works:
        counts[w["domain"]] = counts.get(w["domain"], 0) + 1
    print(f"wrote {OUT} with {len(works)} works")
    for k, v in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"  {k:10} {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
