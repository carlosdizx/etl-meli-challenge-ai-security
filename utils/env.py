import tomli
from pathlib import Path

secrets_path = Path(__file__).resolve().parents[1] / 'secrets.toml'

with open(secrets_path, 'rb') as f:
    secrets = tomli.load(f)


def get_secrets() -> dict:
    return secrets
