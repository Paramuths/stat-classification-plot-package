import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from einops import reduce

"""
helper function for plotting confusion matrix
"""
def plot_confusion_matrix(true, pred, data_labels, show_labels):
    cm = confusion_matrix(true, pred, labels=data_labels)
    percentage = reduce(cm, 'a b -> a', 'sum')
    correct_predict = np.trace(cm)
    num_data = np.sum(cm)

    # Create figure and axes
    _, ax = plt.subplots()

    # Plot confusion matrix as an image
    im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)

    # Customize axes
    ax.set(xticks=np.arange(cm.shape[1]),
        yticks=np.arange(cm.shape[0]),
        xticklabels=show_labels,
        yticklabels=show_labels,
        xlabel='Predicted label',
        ylabel='True label')

    # Add percentage to each cell
    thresh = cm.max() / 2.0
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, f"{cm[i,j]} ({(100 * cm[i, j]) / percentage[i]:.2f}%)",
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")

    # Add a colorbar
    ax.figure.colorbar(im, ax=ax)

    # Adding accuracy at the upper left corner
    ax.text(1, -0.8, f"accuracy = {correct_predict/num_data:.6f}", bbox=dict(facecolor='#87CEFA', edgecolor='black'), ha='center', va='center', color='black')

    return plt