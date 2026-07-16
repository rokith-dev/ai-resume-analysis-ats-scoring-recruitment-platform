import matplotlib.pyplot as plt


def build_sample_chart() -> plt.Figure:
    fig, ax = plt.subplots()
    ax.set_title("Sample Chart")
    ax.plot([1, 2, 3], [2, 3, 5])
    return fig
