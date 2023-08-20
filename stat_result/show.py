import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.metrics import confusion_matrix
from einops import reduce

"""
true: a list of true labels
pred: a list of predicted labels, corresponding to true
data_labels: a list of data that the labels are stored in 
show_labels: a list of string to show in the plot, corresponding to data_labels

ex. true = [0, 1, 2, 1]
    pred = [0, 2, 2, 1]
    data_labels = [0, 1, 2]
    show_labels = ['very good', 'good', 'bad']
"""
def show_confusion_matrix(true, pred, data_labels, show_labels):
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

    # Save the plot
    plt.tight_layout() 
    plt.show()
    plt.close()

if __name__=="__main__":
    true = [0, 1, 2, 1]
    pred = [0, 2, 2, 1]
    data_labels = [0, 1, 2]
    show_labels = ['very good', 'good', 'bad']
    show_confusion_matrix(true, pred, data_labels, show_labels)