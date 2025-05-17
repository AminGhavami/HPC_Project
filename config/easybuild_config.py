site_configuration = {
    'systems': [
        {
            'name': 'aion',
            'descr': 'ULHPC Aion Cluster',
            'hostnames': [r'aion-[\d]+'],
            'modules_system': 'lmod',
            'partitions': [
                {
                    'name': 'batch',
                    'descr': 'Aion batch partition',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': ['--partition=batch', '--qos=normal'],
                    'environs': ['easybuild'],
                    'max_jobs': 10,
                },
            ]
        },
        {
            'name': 'iris',
            'descr': 'ULHPC IRIS Cluster',
            'hostnames': [r'iris-[\d]+'],
            'modules_system': 'lmod',
            'partitions': [
                {
                    'name': 'batch',
                    'descr': 'IRIS compute nodes',
                    'scheduler': 'slurm',
                    'launcher': 'srun',
                    'access': ['--partition=batch', '--qos=normal'],
                    'environs': ['easybuild'],
                    'max_jobs': 10
                }
    
            ]
        }
    ],
    'environments': [
        {
            'name': 'easybuild',
            'modules': [
                'env/testing/2023b',
                'perf/OSU-Micro-Benchmarks/7.2-gompi-2023b',
                'toolchain/foss/2023b',
                'mpi/OpenMPI/4.1.6-GCC-13.2.0',
                'toolchain/gompi/2023b'


            ],
            'cc': 'mpicc',
            'cxx': 'mpicxx',
            'ftn': 'mpif90'
        }
    ]
}


