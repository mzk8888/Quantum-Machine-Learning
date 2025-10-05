import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


import torch
import torch.nn as nn
import torch.optim as optim
import pennylane as qml


# 量子デバイス（2量子ビット）
n_qubits = 2
dev = qml.device("default.qubit", wires=n_qubits)

# 量子回路（量子レイヤー）
@qml.qnode(dev, interface="torch")
def quantum_circuit(inputs, weights):
    qml.AngleEmbedding(inputs, wires=range(n_qubits))
    qml.StronglyEntanglingLayers(weights, wires=range(n_qubits))
    return [qml.expval(qml.PauliZ(i)) for i in range(n_qubits)]

# Torchとの接続ラッパー
class QuantumLayer(nn.Module):
    def __init__(self, n_qubits, n_layers):
        super().__init__()
        weight_shapes = {"weights": (n_layers, n_qubits, 3)}
        self.qlayer = qml.qnn.TorchLayer(quantum_circuit, weight_shapes)

    def forward(self, x):
        return self.qlayer(x)

# ハイブリッドモデル
class HybridModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(4, 2)      # 入力: 4次元ベクトル
        self.q = QuantumLayer(n_qubits, 1)
        self.fc2 = nn.Linear(2, 2)      # 出力: 2クラス分類

    def forward(self, x):
        x = torch.tanh(self.fc1(x))
        x = self.q(x)
        x = self.fc2(x)
        return x

# メイン処理
if __name__ == "__main__":
    model = HybridModel()
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)

    # サンプルデータ（ランダム）
    X = torch.rand(20, 4)
    y = torch.randint(0, 2, (20,))

    # 学習ログを保存
    losses = []

    # 学習ループ
    for epoch in range(20):
        optimizer.zero_grad()
        out = model(X)
        loss = criterion(out, y)
        loss.backward()
        optimizer.step()
        losses.append(loss.item())
        print(f"Epoch {epoch + 1}: Loss={loss.item():.4f}")

    # === 可視化 ===（ループの外に配置！）
    import matplotlib.pyplot as plt

    plt.plot(losses, marker="o")
    plt.title("Hybrid Quantum-Classical Model Training")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.grid(True)

    plt.show()  # 画面にグラフを表示
