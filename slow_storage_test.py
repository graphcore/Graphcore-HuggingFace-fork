import os
import time
import subprocess

print("Slow storage test begin")

# 1. write out `env` to stdout (to get hostname)
env_vars = os.environ
print("Print env vars")
for env in env_vars:
    print(f"{env}: {env_vars[env]}")



file1, file2 = "13800232677581770137.popef", "9028179549235720115.popef"
dataset_folder = "/datasets/poplar-executables-hf-3-2/stablediffusion2_text2img"
tmp_folder = "/tmp/exe_cache/stablediffusion2_text2img"

# 2,3. Test first two read speed - /datasets
for i in [1, 2]:
    print(f"Read speed test {i} from /datasets - start")
    cmd = f"md5sum -b {dataset_folder}/{file1} {dataset_folder}/{file2}".split()
    start_time = time.time()
    output = subprocess.check_output(cmd)
    end_time = time.time()
    print("Duration(s): ", end_time - start_time)
    print(f"Read speed test {i} from /datasets - end")
    print("-"*20)

# 4. Test read speed - /tmp
print("Read speed test from /tmp - start")
cmd = f"md5sum -b {tmp_folder}/{file1} {tmp_folder}/{file2}".split()
start_time = time.time()
output = subprocess.check_output(cmd)
end_time = time.time()
print("Duration(s): ", end_time - start_time)
print("Read speed test from /tmp - end")