class SecretMission:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time

secret_mission = SecretMission(*input().split())
print(f'secret code : {secret_mission.code}')
print(f'meeting point : {secret_mission.place}')
print(f'time : {secret_mission.time}')