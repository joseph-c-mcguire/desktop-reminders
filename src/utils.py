from pathlib import Path

import yaml


def read_yaml(path: Path) -> any:
    """Returns the contents of a yaml file, if it can't read it then it throws an exception.

    Args:
        path (Path): The path to the YAML config file.

    Returns:
        any
            The YAML file contents
    """
    # Open the file
    with open(path) as stream:
        try:
            # Load the contents, safely
            yaml_contents = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            # Throw an exception if it can't read the Path
            print(exc)
    return yaml_contents