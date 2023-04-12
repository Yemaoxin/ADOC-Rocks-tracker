1. Cgroup install in Ubuntu 
https://blog.csdn.net/wmdscjhdpy/article/details/123159308
sudo apt-get install cgroup-tools
sudo apt-get install libcgroup*
touch /etc/cgconfig.conf
touch /etc/cgrules.conf
cgconfigparser -l /etc/cgconfig.conf
sudo mkdir /etc/cgconfig.d
cgrulesengd

2. Cgroup v2和v1的区别
blkio全部要删除
sudo权限


3. base_background_compactions等三个参数不存在，所以你需要通过实际命令行对cgexec命令执行，才能发现背后的问题。

4. 记录暂时的一个信息
db_bench_runner DB_BENCH starting, with parameters:
/home/ymx/ADOC_N/db_bench
report qps in report.csv
sudo /usr/bin/cgexec -g io,cpu:test_group1 /home/ymx/ADOC_N/db_bench --db=/home/ymx/ssds_array --benchmarks=fillrandom,stats --num=1000000000 --key_size=16 --value_size=1000 --write_buffer_size=67108864 --target_file_size_base=67108864 --min_write_buffer_number_to_merge=1 --max_write_buffer_number=2 --level0_file_num_compaction_trigger=4 --level0_slowdown_writes_trigger=20 --threads=1 --bloom_bits=10 --compression_type=none --report_bg_io_stats=true --duration=14400 --report_interval_seconds=1 --core_num=20 --subcompactions=1 --histogram=True --FEA_enable=True --TEA_enable=True --num_levels=4 --max_background_jobs=2 --max_bytes_for_level_base=268435456 --report_file=/home/ymx/ssds_array/report.csv --level0_stop_writes_trigger=36
/home/ymx/ADOC_N/db_bench --db=/home/ymx/ssds_array --benchmarks=fillrandom,stats --num=1000000000 --key_size=16 --value_size=1000 --write_buffer_size=67108864 --target_file_size_base=67108864 --min_write_buffer_number_to_merge=1 --max_write_buffer_number=2 --level0_file_num_compaction_trigger=4 --level0_slowdown_writes_trigger=20 --threads=1 --bloom_bits=10 --compression_type=none --report_bg_io_stats=true --duration=14400 --report_interval_seconds=1 --core_num=20 --subcompactions=1 --histogram=True --FEA_enable=True --TEA_enable=True --num_levels=4 --max_background_jobs=2 --max_bytes_for_level_base=268435456 --report_file=/home/ymx/ssds_array/report.csv --level0_stop_writes_trigger=36 

5. 初步推测由于cgroup使用systemd 作为管理工具，所以导致默认打开文件有限制，暂时按该Github处理
Error: Too many open files
https://github.com/facebook/rocksdb/issues/4089