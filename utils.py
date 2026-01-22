import torch


def few_shot_comparison(baseline_name: str, method_name: str,
                        pre_acc: float, post_acc: float,
                        n_way: int, k_shot: int, n_query: int):

    print("Porównanie skuteczności Few-Shot Learning")
    print("----------------------------------------")
    print(f"Liczba klas (n-way): {n_way}, Liczba przykładów na klasę (k-shot): {k_shot}, Liczba zapytań na klasę: {n_query}\n")
    
    print(f"Dokładność (accuracy) przed few-shot ({baseline_name}): {pre_acc:.2f}")
    print(f"Dokładność (accuracy) po few-shot ({method_name}):      {post_acc:.2f}\n")
    
    print("Poprawa dzięki few-shot learning: "
          f"{post_acc - pre_acc:+.2f}")


def plot_tsne(ax, preds, title, n_way, support_2d, query_2d, support_y, query_y, show_prototypes=False, prototypes_2d=None):
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'orange', 'purple', 'brown'][:n_way]

    if isinstance(support_2d, torch.Tensor):
        support_2d = support_2d.cpu().numpy()
    if isinstance(query_2d, torch.Tensor):
        query_2d = query_2d.cpu().numpy()
    if isinstance(support_y, torch.Tensor):
        support_y = support_y.cpu().numpy()
    if isinstance(query_y, torch.Tensor):
        query_y = query_y.cpu().numpy()
    if isinstance(preds, torch.Tensor):
        preds = preds.cpu().numpy()


    # Rysowanie punktów zbioru pomocniczego (support set)
    for class_label in range(n_way):
        ax.scatter(
            support_2d[support_y == class_label, 0],
            support_2d[support_y == class_label, 1],
            color=colors[class_label],
            s=120,
            label=f"Support {class_label}"
        )               

    # Rysowanie punktów zapytań (query set)
    for class_idx in range(n_way):
        # dobrze sklasyfikowane punkty danej klasy
        correct_mask = (preds == class_idx) & (query_y == class_idx)
        ax.scatter(
            query_2d[correct_mask, 0],
            query_2d[correct_mask, 1],
            marker='x',
            color=colors[class_idx],
            s=120,
            label=f"Query {class_idx} dobrze sklasyfikowane"  # label dla legendy
        )
    
        # źle sklasyfikowane punkty danej klasy
        incorrect_mask = (preds == class_idx) & (query_y != class_idx)
        ax.scatter(
            query_2d[incorrect_mask, 0],
            query_2d[incorrect_mask, 1],
            marker='o',
            facecolors='none',
            edgecolors=colors[class_idx],
            s=150,
            linewidths=2,
            label=f"Query {class_idx} źle sklasyfikowane"  # label dla legendy
        )

    # Rysowanie prototypów 
    if show_prototypes and prototypes_2d is not None:
        for class_label in range(n_way):
            ax.scatter(
                prototypes_2d[class_label, 0],
                prototypes_2d[class_label, 1],
                color=colors[class_label],
                marker='*',
                s=350,
                edgecolor='k',
                linewidth=1.5,
                label=f"Prototyp {class_label}"
            )

    # Dodajemy opisy osi
    ax.set_xlabel("t-SNE wymiar 1")
    ax.set_ylabel("t-SNE wymiar 2")
    
    ax.set_title(title)
    ax.grid(True)
    ax.legend()  
