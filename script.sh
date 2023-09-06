#0 15 * * 1-5 /github/Heroku/script.sh


source /home/jason/github/Heroku/venv/bin/activate

python3 /home/jason/github/Heroku/send.py
