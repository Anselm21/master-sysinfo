This script responds to 'dashbord' (ui) requests with data, gathered from servers with 'sysinfo' script installed.

Install:
git clone
virtualenv venv
pip install -r requirements.txt
Setup:
Create file 'config.py' and fill it with clusters info (see example in config.example.py)
Run:
python main.py