# 🧠 Category Theory Meets Quantum Intuition

> Bridging abstract structure and quantum behavior through morphisms, composition, and diagrams.

---

## 🎯 Why This Exists
After beginning a deep-dive into category theory, I wanted to anchor some of these abstract concepts in my existing understanding of quantum computing. This is a personal exploration to see how categories, morphisms, and diagrammatic reasoning can help structure intuition around quantum gates, circuits, and computation.

---

## 🧩 Core Correspondences

| **Category Theory**             | **Quantum Computing**                            |
|--------------------------------|--------------------------------------------------|
| Objects                        | Quantum systems (e.g. qubits, registers)         |
| Morphisms                      | Unitary transformations (quantum gates)          |
| Composition                    | Sequential gate application                      |
| Identity morphism              | Identity gate (no-op)                            |
| Monoidal product               | Tensor product of quantum systems                |
| Diagrammatic reasoning (ZX)    | Visual rewrite rules for circuits                |
| Isomorphism                    | Reversible quantum operations                    |

---

## ✍️ Intuition Sketch

Quantum circuits are naturally **compositional**: we build them by chaining smaller operations (morphisms) into larger structures. The ZX-calculus abstracts this further—allowing us to **ignore the specific gates** and instead **manipulate the logic of information flow** directly.

In this view:
- **A ZX-diagram is a morphism.**
- **Rewriting a circuit = applying categorical equivalences.**
- The rules preserve *behavior* while changing *form*—just like category theory respects identity and composition.

---

## 🔄 Where This is Going

As I work through more ZX-calculus examples (via PyZX), I’ll update this page to show concrete diagrammatic transformations and how they relate to category-theoretic structure—especially around rewrite rules and completeness.

---

*“Category theory doesn’t explain what quantum computing is—it gives you a language to think about how it fits together.”*
