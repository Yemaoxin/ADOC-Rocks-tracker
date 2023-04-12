#
import os
import sys

work_path = os.getcwd()
os.chdir("../")
print(os.getcwd())
sys.path.insert(0, '.')

from db_bench_option import DEFAULT_DB_BENCH
from db_bench_option import load_config_file
from db_bench_option import set_parameters_to_env
from db_bench_runner import DB_launcher
from db_bench_runner import reset_CPUs
from parameter_generator import HardwareEnvironment
from parameter_generator import StorageMaterial
from db_bench_runner import clean_cgroup

os.chdir(work_path)
if __name__ == '__main__':
    env = HardwareEnvironment()
    # load config.json
    parameter_dict = load_config_file('config.json')
    
    set_parameters_to_env(parameter_dict, env)

    result_dir = "effect_testing/"
    #   use db_bench -help to see more detail
    #   after run this script, I found that I didn't set Write-Only,but I will redo this
    common_opt = {
            "duration":14400,
            "report_interval_seconds": 1,
            "value_size":1000,
            "key_size":16,
            "core_num":20,
            "subcompactions":1,
            "benchmarks":"fillrandom,stats",
            "report_bg_io_stats":"true",
            "histogram":True,
            "FEA_enable":True,
            "TEA_enable":True,
            "num_levels":4
    }
#   use db_bench -help to see more detail
    experiment_sets={
     "compa=1":{"max_background_compactions":1},
     "compa=2":{"max_background_compactions":2},
     "compa=4":{"max_background_compactions":4},
     "compa=8":{"max_background_compactions":8},
     "compa=16":{"max_background_compactions":16},
     "compa=32":{"max_background_compactions":32}
}
    # it will 
    for experiment in experiment_sets:
        print("experiment:",experiment)
        benchmark_opt =  common_opt
        benchmark_opt.update(experiment_sets[experiment])

        temp_result_dir = result_dir +experiment+"/"
        runner = DB_launcher(
            env, temp_result_dir, db_bench=DEFAULT_DB_BENCH, extend_options=benchmark_opt)
        runner.run()
        
        
    reset_CPUs()
    clean_cgroup()
