class Agent:
    def __init__(self, code_name, score):
        self.name = code_name
        self.score = int(score)

agent_name, min_score = '', 101
for _ in range(5):
    agent = Agent(*input().split())
    if agent.score < min_score:
        min_score = agent.score
        agent_name = agent.name

print(agent_name, min_score)