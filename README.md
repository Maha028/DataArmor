# 🛡️ DataArmor

**DataArmor** is a Python-based data anonymization tool that uses the Mondrian algorithm to achieve **k-anonymity** on structured datasets. Designed with a simple GUI, it allows users to protect sensitive information by anonymizing quasi-identifiers through generalization and intelligent partitioning.

---

## 📌 Features

- ✅ Mondrian algorithm for multi-dimensional k-anonymity
- ✅ Intuitive GUI using Tkinter
- ✅ Supports numeric and categorical quasi-identifiers
- ✅ Easy CSV input and anonymized output
- ✅ Suitable for research and educational purposes

---

## GUI Overview

- Load your dataset (CSV format)
- Select:
  - Explicit Identifier (EID)
  - Quasi-Identifiers (QIDs): Numeric and Non-numeric
  - Desired value of **k**
- Click **"Anonymize"** to apply k-anonymity
- View and save the anonymized dataset

---

## How It Works

DataArmor uses the Mondrian multi-dimensional partitioning algorithm:
1. **Partitioning**: Recursively splits the dataset based on QID values.
2. **Validation**: Ensures each partition has at least *k* records.
3. **Generalization**: Applies generalization or suppression to satisfy anonymity requirements.

---

## File Structure

| File               | Description                                      |
|--------------------|--------------------------------------------------|
| DataArmor_GUI.py   | Main script with Tkinter GUI                     |
| k_Anonymity.py     | Mondrian algorithm implementation                |
| data1.csv          | Sample dataset                                   |
| README.md          | Project documentation                            |

---

## Requirements

- Python 3.x
- `pandas`
- `tkinter` (standard with Python)
- `csv` (built-in)

Install dependencies (if needed):

pip install pandas

## Getting Started

1. Clone the repository:

git clone https://github.com/Maha028/DataArmor.git
cd DataArmor

2. Run the GUI:

python DataArmor_GUI.py

3. Follow the GUI steps to load your dataset and apply k-anonymity.


## Sample Dataset

The repository includes `data1.csv`, a sample dataset for testing. You can replace it with your own structured CSV files.
