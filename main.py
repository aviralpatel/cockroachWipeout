import math
import numpy as np
import matplotlib.pyplot as plt

types = ["i", "s", "d", "msw", "mww"]
probabilities = [0.45, 0.3, 0.2, 0.025, 0.025]

selectedType = np.random.choice(types, p=probabilities)


def kill_streak(cockroachType, streak=0, backtrack=0):
    if cockroachType == "i":
        streak += 1
    elif cockroachType == "d":
        streak += 5
    elif cockroachType == "msw":
        streak += 3
    elif cockroachType == "mww":
        streak = 10000000000
    elif cockroachType == "s":
        meetingTypes = ["s", "d", "msw", "mww"]
        meetingProbabilities = [0.1, 0.54, 0.35, 0.01]
        if backtrack == 0:
            streak += 1
            backtrack += 1
            friendLst = np.random.choice(meetingTypes, size=3, p=meetingProbabilities)
            # print(friendLst)
            for cockroach in friendLst:
                streak = kill_streak(cockroach, streak, backtrack)
        elif backtrack == 1:
            streak += 1
            backtrack += 1
            toss = np.random.randint(0, 2)
            if toss == 1:
                Size = 3
            elif toss == 0:
                Size = 2
            friendLst = np.random.choice(meetingTypes, size=Size, p=meetingProbabilities)
            # print(friendLst)
            for cockroach in friendLst:
                streak = kill_streak(cockroach, streak, backtrack)
        elif backtrack == 2:
            streak += 1
            Size = np.random.choice([1, 2, 3], p=[0.45, 0.35, 0.2])
            friendLst = np.random.choice(meetingTypes, size=Size, p=meetingProbabilities)
            # print(friendLst)
            for cockroach in friendLst:
                streak = kill_streak(cockroach, streak, backtrack)
    return streak


y = kill_streak(selectedType)
print(math.log(y) + 1)






