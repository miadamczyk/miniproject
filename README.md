# Few-Shot Learning

Interaktywny notebook edukacyjny wprowadzający do technik Few-Shot Learning.

## Opis projektu

Ten projekt zawiera materiały dydaktyczne w formie Jupyter Notebook, które krok po kroku wprowadzają w:

1. **Few-Shot Learning** - uczenie się z bardzo małej liczby przykładów
2. **Metric-Based Methods** - Prototypical Networks, Matching Networks, Siamese Networks
3. **Meta-Learning** - MAML (Model-Agnostic Meta-Learning)

## Struktura projektu

```
miniproject/
├── metric-based.ipynb      # Notebook z wprowadzeniem i metodami metric-based
├── meta-learning.ipynb     # Notebook z meta-learning
├── requirements.txt        # Zależności Python (pip)
├── environment.yml         # Środowisko Conda
├── README.md               # Ten plik
└── Images/                 # Folder ze zdjęciami wykorzysywanymi w notebookach
```

## Instalacja

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

## Uruchomienie

```bash
jupyter notebook metric-based.ipynb
```

```bash
jupyter notebook meta-learning.ipynb
```

## Zawartość notebooków

### Sekcja 1: Few-Shot Learning - Wprowadzenie
- Czym jest Few-Shot Learning?
- Dlaczego jest przydatne?
- Kluczowe pojęcia: N-way K-shot, Support Set, Query Set

### Sekcja 2: Metric-Based Few-Shot Learning
- Metody Metric-Based - podstawy

### Sekcja 3: Prototypical Networks, Matching Networks, Siamese Networks
- Teoria i implementacja
- Przykład na CIFAR-10 z pretrenowanym ResNet-18
- Wizualizacje t-SNE i prównanie z baseline - Nearest Neighbor

### Sekcja 4: Meta-Learning (MAML)
- Czym jest meta-learning?
- Inner loop vs Outer loop
- Implementacja MAML od podstaw
- Porównanie z metodami metric-based

### Ćwiczenia
- **Ćwiczenie 1:** Odpowieź na pytanie dotyczące wizualizacji TSNE
- **Ćwiczenie 2:** Implementacja Inner-Loop Adaptation (MAML)

## Wymagania

- Python >= 3.10
- PyTorch >= 2.0.0
- torchvision >= 0.15.0
- matplotlib >= 3.7.0
- scikit-learn >= 1.2.0
- numpy >= 1.24.0
- jupyter >= 1.0.0
- ipykernel >= 6.0.0


## Bibliografia

### Few-Shot Learning - Wprowadzenie
- [IBM: What is few-shot learning?](https://www.ibm.com/think/topics/few-shot-learning) (dostęp 21.01.2026)
- [Datacamp: What is Few-Shot Learning? Unlocking Insights with Limited Data](https://www.datacamp.com/blog/what-is-few-shot-learning) (dostęp 21.01.2026)
- [Jaimlr: Few-Shot Learning Strategies](https://jaimlr.github.io/Journal-of-Artificial-Intelligence-Machine-Learning-Research/few-shot-learning-strategies-by-loveleen-narang.html) (dostęp 21.01.2026)
- [MGX.dev: Few-Shot Learning: Foundational Principles, Methodologies, Applications, and Future Directions](https://mgx.dev/insights/few-shot-learning-foundational-principles-methodologies-applications-and-future-directions/125229aa85474e198eda6582b8847abc) (dostęp 21.01.2026)

### Metric-Based Methods
- [Snell et al., 2017 - Prototypical Networks for Few-shot Learning](https://arxiv.org/abs/1703.05175) (dostęp 21.01.2026)
- [Vinyals et al., 2016 - Matching Networks for One Shot Learning](https://arxiv.org/abs/1606.04080) (dostęp 21.01.2026)
- [Koch et al., 2015 - Siamese Neural Networks for One-shot Image Recognition](https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf) (dostęp 21.01.2026)

### Meta-Learning
- [Finn et al., 2017 - Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks (MAML)](https://arxiv.org/abs/1703.03400) (dostęp 21.01.2026)
- [Nichol et al., 2018 - On First-Order Meta-Learning Algorithms (Reptile)](https://arxiv.org/abs/1803.02999) (dostęp 21.01.2026)
- [Li et al., 2017 - Meta-SGD: Learning to Learn Quickly for Few-Shot Learning](https://arxiv.org/abs/1707.09835) (dostęp 21.01.2026)
- [Hospedales et al., 2021 - Meta-Learning in Neural Networks: A Survey](https://arxiv.org/abs/2004.05439) (dostęp 21.01.2026)

## Autorzy

Miłosz Adamczyk, Piotr Bednarski
