from os.path import exists

import yaml
import os

config_path = "conf"


def create_config_pipeline(name: str, config: dict) -> None:
    create_config(f"{config_path}/pipes", name, config)


def load_config_pipeline(name: str) -> dict:
    return load_config(f"{config_path}/pipes", name)


def create_config_general(config: dict) -> None:
    create_config(f"{config_path}", "general", config)


def load_config_general() -> dict:
    return load_config(f"{config_path}", "general")


def create_config(path: str, name: str, config: dict) -> None:
    os.makedirs(path, exist_ok=True, mode=0o777)
    with open(f"{path}/{name}.yml", 'w') as file:
        file.write(yaml.dump(config, sort_keys=False))


def load_config(path: str, name: str) -> dict:
    with open(f"{path}/{name}.yml", "r") as stream:
        return yaml.safe_load(stream)


def update_config(path: str, name: str, update: dict) -> None:
    conf = load_config(path, name)
    conf.update(update)
    create_config(path, name, conf)


# Example
create_config_pipeline("testpipe", {
    "source": {
        "type": "website",
        "url": "https://example.com",
    },
    "sink": {
        "type": "qanswer",
        "url": "https://qa.example.com",
        "token": "abc123",
    },
})

# Creates general config if not existent
if not exists(f"{config_path}/general.yml"):
    create_config_general(
        {
            "flask": {
                "TEMPLATES_AUTO_RELOAD": True,
            },
            "qanswer": {
                "username": "test",
                "password": "not_secure!!1"
            },
        })
