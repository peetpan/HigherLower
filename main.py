import art
import random
import game_data

print(art.logo)
num = random.choice(game_data.data)
score = 0
flag = True
A = random.choice(game_data.data)
B = random.choice(game_data.data)
while flag:
    print(f'Compare A: {A["name"]}, a {A["description"]}, from {A["country"]}')
    print('\t', art.vs)
    print(f'Compare B: {B["name"]}, a {B["description"]}, from {B["country"]}')
    ans = input("Who has more followers? Type \'A\' or \'B\'")
    if (
            ans == 'A' and A["follower_count"] > B["follower_count"]
    ) or (
            ans == 'B' and B["follower_count"] > A["follower_count"]
    ):
        score += 1
        A = B
        B = random.choice(game_data.data)
        print(f'You\'re correct! Current score: {score}\n')
    else:
        flag = False
        print(f'Sorry, that\'s wrong. Final Score: {score}')
