from plot import plot_confusion_matrix

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
    plt = plot_confusion_matrix(true, pred, data_labels, show_labels)
    # Show the plot
    plt.tight_layout() 
    plt.show()
    plt.close()

if __name__=="__main__":
    true = [0, 1, 2, 1]
    pred = [0, 2, 2, 1]
    data_labels = [0, 1, 2]
    show_labels = ['very good', 'good', 'bad']
    show_confusion_matrix(true, pred, data_labels, show_labels)