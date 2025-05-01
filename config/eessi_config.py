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
                    'environs': ['eessi'],
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
                    'environs': ['eessi'],
                    'max_jobs': 10
                }
            ]
        }
    ],
    'environments': [
        {
            'name': 'eessi',
            'modules': ['EESSI/2023.06'],
            'cc': 'gcc',
            'cxx': 'g++',
            'ftn': 'gfortran',
        },
    ]
}



