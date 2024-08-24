# 3rd Parth
from notifypy import Notify
from pathlib import Path
# Default python
import argparse
import time
from collections import defaultdict
# Local Imports
from src.utils import read_yaml
# Constants
CONFIG_PATH = Path("config.yaml") # The yaml configuration file

def main(config: Path = CONFIG_PATH) -> None:
    """Main function to run the messages provided in the YAML file.

    Args:
        CONFIG_PATH (Path): _description_
    """
    # Start the notify api
    notification = Notify()
    # Read in the yaml file with message configs
    multiple_messages = read_yaml(path=config)
    # Initialize a dictionary for keeping track of message counts
    counter = defaultdict(lambda : 0)
    # Run until one of the counter's breaks or otherwise go for ever
    while True:
        # Loop through each message 
        for message_id, message_contents in multiple_messages.items():
            # If one of the counters is met, break the loop and end
            if counter[message_id] == message_contents["max-number"]:
                break
            else:
                # Check the content for notification info.
                for key in message_contents:
                    if hasattr(notification, key):
                        setattr(notification, key, message_contents[key])
                # Send notification, increment counter and wait
                notification.send()
                counter[message_id] += 1
                time.sleep(message_contents["wait"])


if __name__ == "__main__":
    # CLI stuff
    parser = argparse.ArgumentParser(description = "A desktop notification thing!")
    parser.add_argument("-c", "--config", type=str, nargs=1, 
                        metavar="config",
                        default=CONFIG_PATH,
                        help="Enter the config file path"
                        )
    args = parser.parse_args()
    # Run the program
    main(config = Path(args.config))