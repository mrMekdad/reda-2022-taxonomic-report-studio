"""Core workflow for Taxonomic Report Studio by Red@."""

PROJECT_NAME = "Taxonomic Report Studio"
DOMAIN_THEME = "bioinformatics"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
