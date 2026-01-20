# Few-Shot Learning

Interaktywny notebook edukacyjny wprowadzający do technik Few-Shot Learning.

## 📋 Opis projektu

Ten projekt zawiera materiały dydaktyczne w formie Jupyter Notebook, które krok po kroku wprowadzają w:

1. **Few-Shot Learning** - uczenie się z bardzo małej liczby przykładów
2. **Metric-Based Methods** - Prototypical Networks, Matching Networks
3. **Meta-Learning** - MAML (Model-Agnostic Meta-Learning)

## 🗂️ Struktura projektu

```
miniproject/
├── notebook1.ipynb      # Główny notebook z tutorialem
├── requirements.txt     # Zależności Python (pip)
├── environment.yml      # Środowisko Conda
├── README.md           # Ten plik
└── data/               # Dane (pobierane automatycznie)
```

## 🚀 Instalacja

### Opcja 1: Conda (zalecane)

```bash
conda env create -f environment.yml
conda activate fsl-notebook
```

### Opcja 2: pip

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# lub: venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

## 💻 Uruchomienie

```bash
jupyter notebook notebook1.ipynb
```

## 📚 Zawartość notebooka

### Sekcja 1: Few-Shot Learning - Wprowadzenie
- Czym jest Few-Shot Learning?
- Dlaczego jest przydatne?
- Kluczowe pojęcia: N-way K-shot, Support Set, Query Set

### Sekcja 2: Metric-Based Few-Shot Learning
- Prototypical Networks - teoria i implementacja
- Przykład na danych syntetycznych 2D
- Przykład na CIFAR-10 z pretrenowanym ResNet-18
- Wizualizacje t-SNE

### Sekcja 3: Matching Networks
- Porównanie z Prototypical Networks
- Attention-weighted prediction

### Sekcja 4: Meta-Learning (MAML)
- Czym jest meta-learning?
- Inner loop vs Outer loop
- Implementacja MAML od podstaw
- Porównanie z metodami metric-based

### Ćwiczenia
- **Ćwiczenie 1:** Implementacja Prototypical Networks
- **Ćwiczenie 2:** Implementacja Inner-Loop Adaptation (MAML)
- **Zadanie opcjonalne:** Porównanie metod

## 🛠️ Wymagania

- Python >= 3.10
- PyTorch >= 2.0.0
- torchvision >= 0.15.0
- matplotlib >= 3.7.0
- scikit-learn >= 1.2.0
- numpy >= 1.24.0

## 📖 Bibliografia

- [Prototypical Networks for Few-shot Learning](https://arxiv.org/abs/1703.05175) (Snell et al., 2017)
- [Matching Networks for One Shot Learning](https://arxiv.org/abs/1606.04080) (Vinyals et al., 2016)
- [Model-Agnostic Meta-Learning (MAML)](https://arxiv.org/abs/1703.03400) (Finn et al., 2017)

## 👥 Autorzy

Miłosz Adamczyk i Piotr Bednarski
