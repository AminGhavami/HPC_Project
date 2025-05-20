import numpy as np
import matplotlib.pyplot as plt
import glob
import os
import re

plt.style.use('default')

tests = ["latency", "bw"]

# The target message size (X value) to extract for each test
target_values = {
    'latency': 8192,
    'bw': 1048576
}

def plot_specific_point(test_type):
    # Find all .out files for this test type across all envs/systems
    file_list = glob.glob(f'output/*/batch/*/osu_{test_type}_*/*.out')

    if not file_list:
        raise ValueError(f"No matching output files found for {test_type}")

    target_x = target_values[test_type]
    data_points = []

    for file in file_list:
        with open(file, 'r') as f:
            lines = f.readlines()
        try:
            data = np.loadtxt(lines[4:], delimiter=None)
        except Exception as e:
            print(f"Error reading {file}: {e}")
            continue

        # Find the row where message size matches target_x
        row = data[np.where(data[:, 0] == target_x)]
        if row.size == 0:
            print(f"Skipping {file}, target value {target_x} not found.")
            continue

        y_value = row[0][1]

        # Extract environment and system for labeling
        match = re.search(r'output/([^/]+)/batch/([^/]+)/osu_' + test_type + r'_(.*?)/', file)
        if match:
            system, env, config = match.groups()
            label = f"{env}:{config} ({system})"
        else:
            label = os.path.basename(file)

        data_points.append((label, y_value))

    # Plotting
    plt.figure(figsize=(10, 6))
    labels, values = zip(*data_points)
    x_pos = np.arange(len(labels))

    plt.scatter(x_pos, values, color='blue', marker='o')
    plt.xticks(x_pos, labels, rotation=45, ha='right')
    plt.ylabel("Latency (us)" if test_type == "latency" else "Bandwidth (MB/s)")
    plt.title(f'OSU {test_type.capitalize()} at {target_x} Bytes')
    plt.grid(True, linestyle='--', axis='y')

    os.makedirs("results", exist_ok=True)
    plt.tight_layout()
    plt.savefig(f'results/osu_{test_type}_scatter.png')
    plt.show()


# Generate scatter plots for both latency and bw
for test in tests:
    plot_specific_point(test)

