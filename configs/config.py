import yaml

to_config = "path/to/config"
with open(to_config, "r") as f:
    config = yaml.safe_load(f)