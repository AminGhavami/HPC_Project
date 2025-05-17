#!/bin/bash

module purge

echo "Loading EasyBuild modules..."

# Load EasyBuild toolchain and required software
module load env/testing/2023
module load tools/EasyBuild/5.0.0
eb OSU-Micro-Benchmarks-7.2-gompi-2023b.eb
module load perf/OSU-Micro-Benchmarks/7.2-gompi-2023b
module load devel/ReFrame/4.7.4-GCCcore-13.2.0
module load lang/Python/3.11.5-GCCcore-13.2.0

# Confirm module setup
echo "Loaded modules:"
module list

echo "Running ReFrame..."
reframe -C ./config/easybuild_config.py -c ./reframe/easybuild/osu_easybuild.py -r

echo "Plotting results..."
# module load lang/Anaconda3/2020.11

python easybuild_plot.py

