### Record the related db_bench command

record the command to check
FEAT_usage_4h:
sudo /usr/bin/cgexec -g io,cpu:test_group1 /home/ymx/ADOC_N/db_bench --db=/home/ymx/ssds_array --benchmarks=fillrandom,stats --num=1000000000 --key_size=16 --value_size=1000 --write_buffer_size=67108864 --target_file_size_base=67108864 --min_write_buffer_number_to_merge=1 --max_write_buffer_number=2 --level0_file_num_compaction_trigger=4 --level0_slowdown_writes_trigger=20 --threads=1 --bloom_bits=10 --compression_type=none --report_bg_io_stats=true --duration=14400 --report_interval_seconds=1 --core_num=20 --subcompactions=1 --histogram=True --FEA_enable=True --TEA_enable=True --num_levels=4 --max_background_jobs=2 --max_bytes_for_level_base=268435456 --report_file=/home/ymx/ssds_array/report.csv --level0_stop_writes_trigger=36