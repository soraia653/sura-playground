from dotenv import dotenv_values

config = dotenv_values("src/.env.dev")

user = config['ADMIN']
pw = config['PASSWORD']

print(f"{user}'s password is {pw}")
