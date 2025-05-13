import pyzx as zx

circ = zx.Circuit(2)
circ.add_gate("HAD", 0)
circ.add_gate("CNOT", 0, 1)
circ.add_gate("HAD", 1)

print("Original circuit:")
print(circ)

diagram = circ.to_graph()
print("\nConverted to ZX-graph:")
zx.draw(diagram)

zx.simplify.full_reduce(diagram)

print("\nAfter simplification:")
zx.draw(diagram)

optimized = zx.extract.extract_circuit(diagram.copy())
print("\nOptimized circuit:")
print(optimized)
