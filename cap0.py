# %%
users = [
    {'id': 0, 'user': 'Hero'},
    {'id': 1, 'user': 'Dunn'},
    {'id': 2, 'user': 'Sue'},
    {'id': 3, 'user': 'Chi'},
    {'id': 4, 'user': 'Thor'},
    {'id': 5, 'user': 'Clive'},
    {'id': 6, 'user': 'Hicks'},
    {'id': 7, 'user': 'Devin'},
    {'id': 8, 'user': 'Kate'},
    {'id': 9, 'user': 'Klein'}
]

friendship_pairs = [
    (0,1), (0,2), (1,2), (1,3), (2,3), (3,4), (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)
]


# %%
# incializar uma lista vazia para cada id de usuario
friendships = {user['id']: [] for user in users}
friendships

# %%
# loop para preenchimento de pares amigos
for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)

friendships

# %%
# calculando a media de conexoes

def number_of_friends(user):
    """Quantos Amigos tem o _user_?"""
    user_id = user["id"]
    friends_ids = friendships[user_id]
    return len(friends_ids)

total_connections = sum(number_of_friends(user) for user in users)
total_connections

# %%
num_users = len(users)
print(num_users)

avg_connections = total_connections / num_users
avg_connections


# %%
num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]
num_friends_by_id.sort(key=lambda id_and_friends: id_and_friends[1], reverse=True)

num_friends_by_id



# %%
# friend for a friend
def foaf_ids_bad(user):
    return [foaf_id
            for friend_id in friendships[user['id']]
            for foaf_id in friendships[friend_id]
            ]

foaf_ids_bad(users[0])


# %%
from collections import Counter

def friends_of_friend(user):
    user_id = user['id']
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id
        and foaf_id not in friendships[user_id]
    )

print(friends_of_friend(users[3]))

# %%
