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

    # Rysowanie punktów zbioru pomocniczego (support set)
    for c in range(n_way):
        ax.scatter(
            support_2d[support_y == c, 0],
            support_2d[support_y == c, 1],
            color=colors[c],
            s=120,
            label=f"Support {c}"
        )

    # Rysowanie punktów zapytań (query set)
    for i in range(len(query_2d)):
        cls = preds[i]
        correct = preds[i] == query_y[i].item()
        if correct:
            ax.scatter(
                query_2d[i, 0],
                query_2d[i, 1],
                marker='x',
                color=colors[preds[i]],
                s=120
            )
        else:
            ax.scatter(
                query_2d[i, 0],
                query_2d[i, 1],
                marker='o',
                facecolors='none',
                edgecolors=colors[cls],
                s=150,
                linewidths=2
            )

    # Rysowanie prototypów 
    if show_prototypes and prototypes_2d is not None:
        for c in range(n_way):
            ax.scatter(
                prototypes_2d[c, 0],
                prototypes_2d[c, 1],
                color=colors[c],
                marker='*',
                s=350,
                edgecolor='k',
                linewidth=1.5,
                label=f"Prototyp {c}"
            )

    # Dodajemy opisy osi
    ax.set_xlabel("t-SNE wymiar 1")
    ax.set_ylabel("t-SNE wymiar 2")
    
    ax.set_title(title)
    ax.grid(True)