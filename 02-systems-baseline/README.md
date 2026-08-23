# 02-systems-baseline/

The **apparatus**: what the thing must do and how its parts fit, distinct from the thing itself.

- `2.1-requirements/` — numbered, traceable. A design decision with no requirement behind it
  is needs-capture masquerading as design.
- `2.2-architecture/` — structure and its rationale
- `2.3-behavior/` — how it acts, including failure behaviour
- `2.4-interfaces/` — **MOSA lives here.** Every module declares what it *provides* and what it
  *consumes*, so the dependency graph is explicit and checkable for cycles, and replacing a
  module shows exactly what breaks. Undeclared coupling is the failure this directory prevents.
- `2.5-verification/` — how any claim of "done" is proven
