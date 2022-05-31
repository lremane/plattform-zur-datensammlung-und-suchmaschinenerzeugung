import yaml
import os

config_path = "config"


def create_config_pipeline(name: str, config: dict) -> None:
    create_config(f"{config_path}/pipes", name, config)


def load_config_pipeline(name: str) -> dict:
    return load_config(f"{config_path}/pipes", name)


def create_config_general(config: dict) -> None:
    create_config(f"{config_path}", "general", config)


def load_config_general() -> dict:
    return load_config(f"{config_path}", "general")


def create_config(path: str, name: str, config: dict) -> None:
    os.makedirs(path, exist_ok=True)
    with open(f"{path}/{name}.yaml", 'w') as file:
        file.write(yaml.dump(config))


def load_config(path: str, name: str) -> dict:
    with open(f"{path}/{name}.yaml", "r") as stream:
        return yaml.safe_load(stream)


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

create_config_general({
    "webserver": {
        "port": 8080,
    },
    "theme": "dark",
})

print(load_config_general())