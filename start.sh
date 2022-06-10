echo "Cloning Repo...."
git clone https://github.com/CyniteOfficial/cynitesecretbot /MessageSearchBot
cd /MessageSearchBot
pip3 install -r requirements.txt
echo "Starting Bot...."
python3 main.py
