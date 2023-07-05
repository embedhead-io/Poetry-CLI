#!/bin/bash

# Define the default location of the CLI script
DEFAULT_CLI_DIRECTORY="~/poetry_cli"

# Read the CLI directory from the user
echo "Please enter the directory of your Poetry CLI script (leave empty for default): "
read CLI_DIRECTORY

# Use the default directory if the user input is empty
if [ -z "$CLI_DIRECTORY" ]
then
  CLI_DIRECTORY=$DEFAULT_CLI_DIRECTORY
fi

# Use the Python 3 interpreter to run the cli.py file
python3 $CLI_DIRECTORY/cli.py