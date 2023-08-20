from plot import plot_confusion_matrix, plot_roc, plot_pr, plot_prf

"""
function to show confusion matrix

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

"""
function to show roc curve

true: a list of true labels
prob: a list of predicted probabilities for each label, corresponding to true
data_labels: a list of data that the labels are stored in, corresponding to the order in prob
positive_label: label to choose as positive

ex. true = [1, 2, 0, 0]
    prob = [[0.1, 0.1, 0.8],
            [0.2, 0.3, 0.5],
            [0.8, 0.1, 0.1],
            [0.5, 0.4, 0.1]]
    data_labels = [0, 1, 2]
    show_labels = ['very good', 'good', 'bad']
    positive_label = 1
"""
def show_roc(true, prob, data_labels, show_labels, positive_labels):
    plt = plot_roc(true, prob, data_labels, show_labels, positive_labels)
    # Save the plot
    plt.tight_layout() 
    plt.show()
    plt.close()

"""
function to show pr curve

true: a list of true labels
prob: a list of predicted probabilities for each label, corresponding to true
data_labels: a list of data that the labels are stored in, corresponding to the order in prob
positive_label: label to choose as positive

ex. true = [1, 2, 0, 0]
    prob = [[0.1, 0.1, 0.8],
            [0.2, 0.3, 0.5],
            [0.8, 0.1, 0.1],
            [0.5, 0.4, 0.1]]
    data_labels = [0, 1, 2]
    show_labels = ['very good', 'good', 'bad']
    positive_label = 1
"""
def show_pr(true, prob, data_labels, show_labels, positive_labels):
    plt = plot_pr(true, prob, data_labels, show_labels, positive_labels)
    # Save the plot
    plt.tight_layout() 
    plt.show()
    plt.close()

"""
function to show precision, recall, f1 graph

true: a list of true labels
prob: a list of predicted probabilities for each label, corresponding to true
data_labels: a list of data that the labels are stored in, corresponding to the order in prob
positive_label: label to choose as positive

ex. true = [1, 2, 0, 0]
    prob = [[0.1, 0.1, 0.8],
            [0.2, 0.3, 0.5],
            [0.8, 0.1, 0.1],
            [0.5, 0.4, 0.1]]
    data_labels = [0, 1, 2]
    show_labels = ['very good', 'good', 'bad']
    positive_label = 1
"""
def show_prf(true, prob, data_labels, show_labels, positive_labels):
    plt = plot_prf(true, prob, data_labels, show_labels, positive_labels)
    # Save the plot
    plt.tight_layout() 
    plt.show()
    plt.close()

if __name__=="__main__":
    # true = [0, 1, 2, 1]
    # pred = [0, 2, 2, 1]
    # data_labels = [0, 1, 2]
    # show_labels = ['very good', 'good', 'bad']
    # show_confusion_matrix(true, pred, data_labels, show_labels)

    true = [1, 2, 0, 0]
    prob = [[0.1, 0.1, 0.8],
            [0.2, 0.3, 0.5],
            [0.8, 0.1, 0.1],
            [0.5, 0.4, 0.1]]
    data_labels = [0, 1, 2]
    show_labels = ['very good', 'good', 'bad']
    positive_label = 1
    show_prf(true, prob, data_labels, show_labels, positive_label)