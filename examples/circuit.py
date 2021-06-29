fromfrom qiskit import QuantumCircuit, execute, Aer
from qiskit.visualization import plot_histogram,display
from user.index import Indexcircuit=QuantumCircuit(1,1)
try:
	Index["import"]qiskit)
except:
	print("Error: import is not defined or is inaccessible")
circuit.x(2)
circuit.h(0)
circuit.cx(0,1)
circuit.measure(0,1)
s=1024
backend=Aer.get_backend('qasm_simulator')
job=execute(circuit, backend, shots=s)
result=job.result()
counts=result.get_counts(circuit)
graph=plot_histogram(counts)
display(graph)
circuit.draw('mpl')

