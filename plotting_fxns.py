import matplotlib.pyplot as plt

def make_counts(data):
    """Takes a string or list, returns a dictionary of counts."""
    d = dict()
    for item in data:
        d[item] = d.get(item, 0) + 1
    return d

def plot_histogram(data, bins=7):
    """Takes a list of numbers and plots a histogram."""
    plt.hist(data, bins=bins)
    plt.ylabel('Counts')
    plt.title('Histogram')
    plt.show()

def plot_bar(d):
    """Takes a dictionary and plots a bar chart. Returns nothing."""
    plt.bar(list(d.keys()), list(d.values()))
    plt.ylabel('Counts')
    plt.title('Frequency')
    plt.show()
