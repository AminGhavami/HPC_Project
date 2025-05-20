#!/bin/bash

module purge

echo -e "\033[36mLoading Local modules...\033[0m"

# Load EasyBuild toolchain and required software
module load env/testing/2023
module load perf/OSU-Micro-Benchmarks/7.2-gompi-2023b
module load devel/ReFrame/4.7.4-GCCcore-13.2.0
module load lang/Python/3.11.5-GCCcore-13.2.0

# Confirm module setup
echo "Modules loaded"

echo -e "\033[31mRunning ReFrame ...\033[0m"
reframe -C ./config/local_config.py -c ./reframe/local_c/osu_local.py -r

echo -e "\033[36mLoading EasyBuild modules...\033[0m"
module purge
module load env/testing/2023b
module load tools/EasyBuild/5.0.0
eb OSU-Micro-Benchmarks-7.2-gompi-2023b.eb
module use "${EASYBUILD_PREFIX}/modules/all"
module load perf/OSU-Micro-Benchmarks/7.2-gompi-2023b
module load devel/ReFrame/4.7.4-GCCcore-13.2.0
module load lang/Python/3.11.5-GCCcore-13.2.0

# Confirm module setup
echo "Loaded modules:"
reframe -C ./config/easybuild_config.py -c ./reframe/easybuild/osu_easybuild.py -r

echo -e "\033[31mRunning ReFrame ...\033[0m"

echo -e "\033[36mLoading EESSI modules...\033[0m"
module purge
# load old environment
module load env/deprecated/2020b
echo "load old env"
# load essensial modules
echo "loading EESSI"
module load EESSI

echo "loading OSU-Micro-Benchmarks"
module load OSU-Micro-Benchmarks/7.2-gompi-2023b
echo "lading OpenMPI"
module load OpenMPI/4.1.6-GCC-13.2.0
echo "leading ReFrame"
module load ReFrame/4.6.2
reframe --version
echo "loading python"
module load Python/3.11.5-GCCcore-13.2.0

echo -e "\033[31mRunning ReFrame ...\033[0m"
reframe -C ./config/eessi_config.py -c ./reframe/eessi/osu_eessi.py -r

echo -e "\033[31mProduce plots\033[0m"
module load lang/Anaconda3/2020.11
python results_plot.py
