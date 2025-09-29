import sys

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

if len(sys.argv) > 1:
    if sys.argv[1].isdecimal():
        numOfRegisters = int(sys.argv[1])
else:
    print("You can provide a custom number of qubits by setting " \
          "the first CLI parameter to the desired number of qubits.")
    numOfRegisters = 8

if numOfRegisters > 64:
    print(":0")

print(f"Selected number of qubits: {numOfRegisters}")

def sort_result(e):
    return e[1]

qc = QuantumCircuit(numOfRegisters, numOfRegisters)

for index in range(numOfRegisters):
    qc.h(index)

qc.measure_all(add_bits=False)

backend = AerSimulator()

job = backend.run(qc)
job.wait_for_final_state()

result = list(job.result().get_counts().items())
result.sort(reverse=True, key=sort_result)
print(f"Result {int(result[0][0], 2)}")
