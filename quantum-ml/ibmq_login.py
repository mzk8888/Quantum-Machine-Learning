from qiskit_ibm_runtime import QiskitRuntimeService

# IBM Quantum に接続
service = QiskitRuntimeService(
    channel="ibm_quantum_platform",
    token="B3QJtC4quW4P-coUN7SMN5K6l6G3jrjKaA-ax1iVjxZw",   # setx で保存してあるなら省略可能
    instance="my-quantum-instance"  # ここが大事！
)

# 利用可能なバックエンド一覧を表示
print(service.backends())

