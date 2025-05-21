#!/bin/bash

module purge

echo "Loading Local modules..."

# Load EasyBuild toolchain and required software
module load env/release/2023b
module load toolchain/foss/2023b
module load system/hwloc
#module load perf/OSU-Micro-Benchmarks/7.2-gompi-2023b
module load devel/ReFrame/4.7.4-GCCcore-13.2.0
#module load lang/Python/3.11.5-GCCcore-13.2.0

# Confirm module setup
echo "Loaded moduled"


echo "Running ReFrame..."
reframe -C ./config/local_config.py -c ./reframe/local_c/osu_local.py -r

# echo "Plotting results..."
# module load lang/Anaconda3/2020.11

# python easybuild_plot.py
#srun --ntasks=1 --ntasks-per-node=1 --cpus-per-task=1 bash -c 'unset SLURM_CPU_BIND SLURM_CPU_BIND_TYPE SLURM_CPU_BIND_VERBOSE SLURM_CPU_BIND_LIST
