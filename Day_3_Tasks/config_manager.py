# Description: Reads, writes, and manipulates application state configurations using underlying JSON file streams.

import json

def save_config(data: dict, filename: str) -> None:
    with open(filename, mode='w') as file:
        json.dump(data, file, indent=4)

def load_config(filename: str) -> dict:
    with open(filename, mode='r') as file:
        return json.load(file)

def update_config(filename: str, key: str, value) -> None:
    data = load_config(filename)
    data[key] = value
    save_config(data, filename)

if __name__ == "__main__":
    # json.dump() directly serializes a dictionary into an open writeable text file object.
    # json.dumps() converts a dictionary into a standard Python string string object instead of a file stream.
    
    config_file = "config.json"
    initial_config = {
        "model": "ResNet50",
        "learning_rate": 0.001,
        "epochs": 10
    }

    save_config(initial_config, config_file)
    print(load_config(config_file))

    update_config(config_file, "epochs", 20)
    print(load_config(config_file))