import math
from statistics import mean
import matplotlib.pyplot as plt

def poisson_dist(k, lambda_):
    poisson= ((math.e**(-lambda_)) * lambda_**k) / math.factorial(k)
    return poisson

def prob(avg1: float, avg2: float, n: [], goals: int) -> {}:

    # The first team's name
    name1=n[0]
    # The second team's name
    name2=n[1]

    # Stores a list of goals and a list of probabilities for each team
    goal_p={
        f'{name1}': {
            'goals': [],
            'p': []
        },
        f'{name2}': {
            'goals': [],
            'p': []
        }
    }

    # Check the probability for every goal in range 0-6
    if goals in range(0,7):
        for i in range(goals + 1):
            team_1_odds = poisson_dist(i, avg1)
            team_2_odds = poisson_dist(i, avg2)
            goal_p[f'{name1}']['goals'].append(i)
            goal_p[f'{name1}']['p'].append(round(team_1_odds,3))
            goal_p[f'{name2}']['goals'].append(i)
            goal_p[f'{name2}']['p'].append(round(team_2_odds,3))
    else:
        print('Invalid number of goals.')

    return goal_p

def prob_dist(avg1: float, avg2: float, n: [], goals: int):
    teams_goals_odds=prob(avg1, avg2, n, goals)
    colors=['green', 'red']
    avgs=[avg1, avg2]

    fig,axes=plt.subplots(1,2,figsize=(10,5))

    for i in range(0,2):
        axes[i].bar(teams_goals_odds[f'{n[i]}']['goals'], teams_goals_odds[f'{n[i]}']['p'], color=colors[i],
                    label=f'Average goals: {avgs[i]:.2f}')
        axes[i].set_title(f'{n[i]}', fontsize=14)
        axes[i].set_xlabel('Number of goals', fontsize=12)
        axes[i].set_ylabel('Probability', fontsize=12)
        axes[i].set_xticks(teams_goals_odds[f'{n[i]}']['goals'])
        axes[i].grid(axis='y', linestyle='--', alpha=0.7)
        axes[i].legend()

    plt.show()