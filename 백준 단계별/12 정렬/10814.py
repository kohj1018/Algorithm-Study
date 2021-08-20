N = int(input())

user_list = []
for i in range(N):
    age, name = input().split()
    user_list.append([int(age), name, i])

user_list.sort(key=lambda user: (user[0], user[2]))

for user in user_list:
    print(user[0], user[1])
