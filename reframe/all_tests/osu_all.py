import reframe as rfm
import reframe.utility.sanity as sn
from reframe.core.pipeline import RunOnlyRegressionTest
# from reframe.core.decorators import run_before


class BaseOsuTest(RunOnlyRegressionTest):
    valid_systems = ['aion:batch', 'iris:batch']
    valid_prog_environs = ['easybuild','eessi','local']
    time_limit = '10m'
    exclusive_access = True

    @run_before('run')
    def set_prerun_env(self):
        self.prerun_cmds = [
            'unset SLURM_CPUS_PER_TASK',
            'unset SLURM_TRES_PER_TASK',
            'echo SLURM_CPUS_PER_TASK=$SLURM_CPUS_PER_TASK',
            'echo SLURM_TRES_PER_TASK=$SLURM_TRES_PER_TASK'
        ]


@rfm.simple_test
class osu_latency_same_core(BaseOsuTest):
    descr = 'OSU Latency Test (Same Core)'
    executable = 'osu_latency'

    @run_before('run')
    def set_job_opts(self):
        self.job.options = ['--nodes=1', '--ntasks=2', '--ntasks-per-node=2', '--cpus-per-task=1']
        self.prerun_cmds += ['numactl -C 0,0 -l']  # Pin both to same core


    @sanity_function
    def validate_output(self):
        return sn.assert_found(r'# OSU MPI Latency Test', self.stdout)

    @performance_function('us')
    def latency(self):
        return sn.extractsingle(r'^512\s+(\S+)', self.stdout, 1, float)


@rfm.simple_test
class osu_latency_same_numa(BaseOsuTest):
    descr = 'OSU Latency Test (Same NUMA)'
    executable = 'osu_latency'

    @run_before('run')
    def set_job_opts(self):
        self.job.options = ['--nodes=1', '--ntasks=2', '--cpus-per-task=1']
        self.prerun_cmds += ['numactl -C 0,1 -l']

    @sanity_function
    def validate_output(self):
        return sn.assert_found(r'# OSU MPI Latency Test', self.stdout)

    @performance_function('us')
    def latency(self):
        return sn.extractsingle(r'^512\s+(\S+)', self.stdout, 1, float)


@rfm.simple_test
class osu_latency_cross_numa(BaseOsuTest):
    descr = 'OSU Latency Test (Cross NUMA)'
    executable = 'osu_latency'


    @run_before('run')
    def set_job_opts(self):
        self.job.options = ['--nodes=1', '--ntasks=2', '--cpus-per-task=1']
        self.prerun_cmds += ['numactl -C 0,16']

    @sanity_function
    def validate_output(self):
        return sn.assert_found(r'# OSU MPI Latency Test', self.stdout)
    @performance_function('us')
    def latency(self):
        return sn.extractsingle(r'^512\s+(\S+)', self.stdout, 1, float)


@rfm.simple_test
class osu_latency_inter_node(BaseOsuTest):
    descr = 'OSU Latency Test (Inter-node)'
    executable = 'osu_latency'

    @run_before('run')
    def set_job_opts(self):
        self.job.options = ['--nodes=2', '--ntasks=2', '--ntasks-per-node=1', '--cpus-per-task=1']

    @sanity_function
    def validate_output(self):
        return sn.assert_found(r'# OSU MPI Latency Test', self.stdout)

    @performance_function('us')
    def latency(self):
        return sn.extractsingle(r'^512\s+(\S+)', self.stdout, 1, float)
####
@rfm.simple_test
class osu_bw_same_core(BaseOsuTest):
    descr = 'OSU Bandwidth Test (Same Core)'
    executable = 'osu_bw'

    @run_before('run')
    def set_job_opts(self):
        self.job.options = ['--nodes=1', '--ntasks=2', '--ntasks-per-node=2', '--cpus-per-task=1']
        self.prerun_cmds += ['numactl -C 0,0 -l']  # Pin both to same core


    @sanity_function
    def validate_output(self):
        return sn.assert_found(r'# OSU MPI Bandwidth Test', self.stdout)

    @performance_function('MB/s')
    def bandwidth(self):
        return sn.extractsingle(r'^1048576\s+(\S+)', self.stdout, 1, float)


@rfm.simple_test
class osu_bw_same_numa(BaseOsuTest):
    descr = 'OSU Bandwidth Test (Same NUMA)'
    executable = 'osu_bw'

    @run_before('run')
    def set_job_opts(self):
        self.job.options = ['--nodes=1', '--ntasks=2', '--cpus-per-task=1']
        self.prerun_cmds += ['numactl -C 0,1 -l']

    @sanity_function
    def validate_output(self):
        return sn.assert_found(r'# OSU MPI Bandwidth Test', self.stdout)

    @performance_function('MB/s')
    def bandwidth(self):
        return sn.extractsingle(r'^1048576\s+(\S+)', self.stdout, 1, float)


@rfm.simple_test
class osu_bw_cross_numa(BaseOsuTest):
    descr = 'OSU Bandwidth Test (Cross NUMA)'
    executable = 'osu_bw'

    @run_before('run')
    def set_job_opts(self):
        self.job.options = ['--nodes=1', '--ntasks=2', '--cpus-per-task=1']
        self.prerun_cmds += ['numactl -C 0,16']

    @sanity_function
    def validate_output(self):
        return sn.assert_found(r'# OSU MPI Bandwidth Test', self.stdout)

    @performance_function('MB/s')
    def bandwidth(self):
        return sn.extractsingle(r'^1048576\s+(\S+)', self.stdout, 1, float)


@rfm.simple_test
class osu_bw_inter_node(BaseOsuTest):
    descr = 'OSU Bandwidth Test (Inter-node)'
    executable = 'osu_bw'

    @run_before('run')
    def set_job_opts(self):
        self.job.options = ['--nodes=2', '--ntasks=2', '--ntasks-per-node=1', '--cpus-per-task=1']

    @sanity_function
    def validate_output(self):
        return sn.assert_found(r'# OSU MPI Bandwidth Test', self.stdout)

    @performance_function('MB/s')
    def bandwidth(self):
        return sn.extractsingle(r'^1048576\s+(\S+)', self.stdout, 1, float)

