import random

actions = ["go", "stop", "slow"]
reward = 0

for episode in range(10):
    action = random.choice(actions)
    if action == "go":
        reward += 10
    else:
        reward -= 5

print("Total Reward:", reward)
