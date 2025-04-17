# MPI Benchmarking on ULHPC with ReFrame

This project evaluates the latency and bandwidth performance of MPI using OSU Micro-Benchmarks v7.2 on the ULHPC clusters (Aion and Iris). It compares three approaches for sourcing the benchmarks:

- Local Compilation (from source)
- EasyBuild Module
- EESSI Environment

All tests are automated and managed using the [ReFrame](https://reframe-hpc.readthedocs.io/) regression testing framework.

---

## Objectives

- Benchmark `osu_latency` and `osu_bw` with controlled message sizes
- Run tests across different CPU/memory topologies (e.g., same core, cross-NUMA, inter-node)
- Compare performance across sourcing methods
- Automate test execution with ReFrame

---

## Repository Structure

## Collaborators
- Asal Ashraf
- Vaibhav Mangroliya
- Amin Ghavami


