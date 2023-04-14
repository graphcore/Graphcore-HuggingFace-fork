import os

print("Slow storage test begin")

# 1. write out `env` to stdout
env_vars = os.environ
print("Print env vars")
for env in env_vars:
    print(f"{env}: {env_vars[env]}")