#!/bin/bash
cd ./github/Heroku

source venv/bin/activate

python3 send.py

date >> ./123.txt



# Install any necessary dependencies using pip
#pip install package1 package2 package3

# Execute your Python script or command here
#python your_script.py

# Deactivate the virtual environment after script execution
#deactivate
