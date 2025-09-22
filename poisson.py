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
    team1=n[0]
    team2=n[1]

    fig,axes=plt.subplots(1,2,figsize=(10,5))

    # Team 1 probability distribution
    axes[0].bar(teams_goals_odds[f'{team1}']['goals'], teams_goals_odds[f'{team1}']['p'], color='green',
                label=f'Average goals: {avg1:.2f}')
    axes[0].set_title(f'{team1}: Poisson Distribution', fontsize=14)
    axes[0].set_xlabel('Number of goals', fontsize=12)
    axes[0].set_ylabel('Probability', fontsize=12)
    axes[0].set_xticks(teams_goals_odds[f'{team1}']['goals'])
    axes[0].grid(axis='y', linestyle='--', alpha=0.7)
    axes[0].legend()

    # Team 2 probability distribution
    axes[1].bar(teams_goals_odds[f'{team2}']['goals'], teams_goals_odds[f'{team2}']['p'], color='red',
                label=f'Average goals: {avg2:.2f}')
    axes[1].set_title(f'{team2}: Poisson Distribution', fontsize=14)
    axes[1].set_xlabel('Number of goals', fontsize=12)
    axes[1].set_xlabel('Probability', fontsize=12)
    axes[1].set_xticks(teams_goals_odds[f'{team2}']['goals'])
    axes[1].grid(axis='y', linestyle='--', alpha=0.7)
    axes[1].legend()

    plt.show()