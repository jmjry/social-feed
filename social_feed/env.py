import os

os.environ["DATABASE_URL"] = 'postgres://nszzpjxocijppg:0e28710dc1fbca41daddf3a90ac4dfd0'
os.environ["SECRET_KEY"] = "okjhgv9876"


def return_secret_key():
    return "okjhgv9876"
