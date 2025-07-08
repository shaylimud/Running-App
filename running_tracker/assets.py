import importlib.resources


def load_logo_b64():
    """Return base64-encoded logo image."""
    return importlib.resources.files(__package__).joinpath("logo.b64").read_text().strip()

