import numpy as np
import matplotlib.pyplot as plt
plt.style.use('default')
import glob
import os
import re

# Test types to plot
tests = ["latency", "bw"]

# Marker and style configs
markers = ['o', 's', '^', 'd', 'x', '*']
linestyles = ['-', '--', '-.', ':', (0, (3, 5, 1, 5)), (0, (5, 10))]

def plot_gen(name):
    # Search for .out files across systems (aion and iris)
    file_list = glob.glob(f'output/*/batch/eessi/osu_{name}_*/*.out')
    if len(file_list) == 0:
        raise ValueError(
            f"No .out files found in output/*/batch/eessi/osu_{name}_*/\n"
            "Check ReFrame output directory or test names."
        )

    def read_data(filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        data = np.loadtxt(lines[4:], delimiter=None)
        return data[:, 0], data[:, 1]

    plt.figure(figsize=(8, 6))

    for i, file in enumerate(file_list):
        x, y = read_data(file)

        # Extract system name (aion or iris) and test config
        match = re.search(r'output/([^/]+)/batch/eessi/osu_' + name + r'_(.*?)/', file)
        if match:
            system_name, config = match.groups()
            label = f'{system_name}:{config}'
        else:
            label = f'Unknown{i}'

        plt.loglog(x, y, label=label,
                   marker=markers[i % len(markers)],
                   linestyle=linestyles[i % len(linestyles)])

    # Set plot labels and title
    plt.xlabel("Message Size (Bytes)")
    plt.ylabel("Latency (us)" if name == "latency" else "Bandwidth (MB/s)")
    plt.title(f'OSU MPI {name.capitalize()} Comparison (Aion vs IRIS)')
    plt.legend()
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)

    # Save plot
    os.makedirs("results", exist_ok=True)
    plt.savefig(f'results/osu_{name}_comparison.png')
    plt.show()

# Generate plots for all test types
for test in tests:
    plot_gen(test)

