import math
import numpy as np
import matplotlib.pyplot as plt
import utility as ut

types = ["i", "s", "d", "msw", "mww"]
probabilities = [0.35, 0.3, 0.3, 0.025, 0.025]

iteration = 0
kills = 0


def kill_streak(cockroachType, streak=0, backtrack=0):
    if cockroachType == "i":
        streak += 1
    elif cockroachType == "d":
        streak += 5
    elif cockroachType == "msw":
        streak += 50
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


fig, axes = plt.subplots()
axes.set_xlim(0, 1)
axes.set_ylim(0, 1)
currentRect = None

ratios = np.empty(100)

while iteration < 100:
    selectedType = np.random.choice(types, p=probabilities)
    kills = kill_streak(selectedType)
    ratio = kills / 250
    if ratio > 1:
        ratio = 1
    print(f"{selectedType}, {ratio}")
    ratios[iteration] = ratio
    if currentRect:
        currentRect.remove()
    currentRect = ut.draw_rectangle(axes, ratio)
    plt.show(block=False)
    plt.pause(0.05)
    iteration += 1

currentRect.remove()
averageRatio = np.mean(ratios)
print(averageRatio)
ut.draw_rectangle(axes, averageRatio)
plt.show(block=False)
plt.pause(30)










