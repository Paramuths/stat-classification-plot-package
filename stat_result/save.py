import os

from plot import plot_confusion_matrix, plot_roc, plot_pr, plot_prf

"""
function to save confusion matrix

true: a list of true labels
pred: a list of predicted labels, corresponding to true
data_labels: a list of data that the labels are stored in 
show_labels: a list of string to show in the plot, corresponding to data_labels
path: path to destination folder

ex. true = [0, 1, 2, 1]
    pred = [0, 2, 2, 1]
    data_labels = [0, 1, 2]
    show_labels = ['very good', 'good', 'bad']
    path = "./stat_result"
"""
def save_confusion_matrix(true, pred, data_labels, show_labels, path):
    plt = plot_confusion_matrix(true, pred, data_labels, show_labels)
    # Save the plot
    plt.tight_layout() 
    plt.savefig(os.path.join(path, 'confusion_matrix.png'))
    plt.close()

"""
function to save roc curve

true: a list of true labels
prob: a list of predicted probabilities for each label, corresponding to true
data_labels: a list of data that the labels are stored in, corresponding to the order in prob
positive_label: label to choose as positive
path: path to destination folder

ex. true = [1, 2, 0, 0]
    prob = [[0.1, 0.1, 0.8],
            [0.2, 0.3, 0.5],
            [0.8, 0.1, 0.1],
            [0.5, 0.4, 0.1]]
    data_labels = [0, 1, 2]
    show_labels = ['very good', 'good', 'bad']
    positive_label = 1
    path = "./stat_result"
"""
def save_roc(true, prob, data_labels, show_labels, positive_labels, path):
    plt = plot_roc(true, prob, data_labels, show_labels, positive_labels)
    # Save the plot
    plt.tight_layout() 
    plt.savefig(os.path.join(path, 'roc.png'))
    plt.close()

"""
function to save pr curve

true: a list of true labels
prob: a list of predicted probabilities for each label, corresponding to true
data_labels: a list of data that the labels are stored in, corresponding to the order in prob
positive_label: label to choose as positive
path: path to destination folder

ex. true = [1, 2, 0, 0]
    prob = [[0.1, 0.1, 0.8],
            [0.2, 0.3, 0.5],
            [0.8, 0.1, 0.1],
            [0.5, 0.4, 0.1]]
    data_labels = [0, 1, 2]
    show_labels = ['very good', 'good', 'bad']
    positive_label = 1
    path = "./stat_result"
"""
def save_pr(true, prob, data_labels, show_labels, positive_labels, path):
    plt = plot_pr(true, prob, data_labels, show_labels, positive_labels)
    # Save the plot
    plt.tight_layout() 
    plt.savefig(os.path.join(path, 'pr.png'))
    plt.close()

"""
function to save precision, recall, f1 graph

true: a list of true labels
prob: a list of predicted probabilities for each label, corresponding to true
data_labels: a list of data that the labels are stored in, corresponding to the order in prob
positive_label: label to choose as positive
path: path to destination folder

ex. true = [1, 2, 0, 0]
    prob = [[0.1, 0.1, 0.8],
            [0.2, 0.3, 0.5],
            [0.8, 0.1, 0.1],
            [0.5, 0.4, 0.1]]
    data_labels = [0, 1, 2]
    show_labels = ['very good', 'good', 'bad']
    positive_label = 1
    path = "./stat_result"
"""
def save_prf(true, prob, data_labels, show_labels, positive_labels, path):
    plt = plot_prf(true, prob, data_labels, show_labels, positive_labels)
    # Save the plot
    plt.tight_layout() 
    plt.savefig(os.path.join(path, 'precision_recall_f1.png'))
    plt.close()

if __name__=="__main__":
    # true = [0, 1, 2, 1]
    # pred = [0, 2, 2, 1]
    # data_labels = [0, 1, 2]
    # show_labels = ['very good', 'good', 'bad']
    path = "./stat_result"
    # save_confusion_matrix(true, pred, data_labels, show_labels, path)

    true = [1, 2, 0, 0]
    prob = [[0.1, 0.1, 0.8],
            [0.2, 0.3, 0.5],
            [0.8, 0.1, 0.1],
            [0.5, 0.4, 0.1]]
    data_labels = [0, 1, 2]
    show_labels = ['very good', 'good', 'bad']
    positive_label = 1
    save_prf(true, prob, data_labels, show_labels, positive_label, path)