class User:
    def __init__(self, user_id='codetree', level=10):
        self.id = user_id
        self.level = level

users = [User(), User(*input().split())]

for user in users:
    print(f'user {user.id} lv {user.level}')