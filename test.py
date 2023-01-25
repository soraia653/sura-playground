from dotenv import dotenv_values

config = dotenv_values("src/.env.prod")

user = config['ADMIN']
pw = config['PASSWORD']

print(f"{user}'s password is {pw}")
