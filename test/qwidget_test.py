from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QCheckBox, QHBoxLayout

app = QApplication([])
from PySide6.QtCore import Qt
window = QWidget()
layout = QVBoxLayout()

table = QTableWidget(3, 3)
table.setHorizontalHeaderLabels(["Seç", "Ad", "Soyad"])

for row in range(3):
    # 1. Widget oluştur
    checkbox_widget = QWidget()
    checkbox = QCheckBox()

    # 2. Checkbox'ı ortalamak için layout ekle
    layout_box = QHBoxLayout(checkbox_widget)
    layout_box.addWidget(checkbox)
    layout_box.setAlignment(Qt.AlignCenter)  # Ortala
    layout_box.setContentsMargins(0, 0, 0, 0)  # Kenar boşluklarını kaldır

    # 3. Hücreye widget olarak ekle
    table.setCellWidget(row, 0, checkbox_widget)

    # Diğer sütunlara veri ekleyelim
    table.setItem(row, 1, QTableWidgetItem(f"Ad {row + 1}"))
    table.setItem(row, 2, QTableWidgetItem(f"Soyad {row + 1}"))

layout.addWidget(table)
window.setLayout(layout)

window.show()
app.exec()