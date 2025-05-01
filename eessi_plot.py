import numpy as np
import matplotlib.pyplot as plt
plt.style.use('default')
import glob
import os

# Test types to plot
tests = ["latency", "bw"]

# Marker and style configs
markers = ['o', 's', '^', 'd', 'x', '*']
linestyles = ['-', '--', '-.', ':', (0, (3, 5, 1, 5)), (0, (5, 10))]


def plot_gen(name):
    # Find relevant ReFrame output files
    file_list = glob.glob(f'output/*/batch/eessi/osu_{name}_*/*.out')
    if len(file_list) == 0:
        raise ValueError(f"There is no .out file in output/aion/batch/eessi/osu_{name}_*/\n" \
        "or Defined the right searching style to find .out files")

    def read_data(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        # Data starts after the header lines
        data = np.loadtxt(lines[4:], delimiter=None)
        return data[:, 0], data[:, 1]

    plt.figure(figsize=(8, 6))

    for i, file in enumerate(file_list):
        x, y = read_data(file)
        label = os.path.splitext(os.path.dirname(file))[0].replace("output/aion/batch/eessi/osu_", "")
        # print(os.path.splitext(os.path.dirname(file))[0].replace("project/osu_", ""))
        plt.loglog(x, y, label=label,
                   marker=markers[i % len(markers)],
                   linestyle=linestyles[i % len(linestyles)])

    # Set plot labels and title
    plt.xlabel("Message Size (Bytes)")
    plt.ylabel("Latency (us)" if name == "latency" else "Bandwidth (MB/s)")
    plt.title(f'OSU MPI {name.capitalize()} Comparison (Aion)')
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)

    # Save plot
    plt.savefig(f'osu_{name}_comparison.png')
    plt.show()


# Generate plots for all test types
for test in tests:
    plot_gen(test)

