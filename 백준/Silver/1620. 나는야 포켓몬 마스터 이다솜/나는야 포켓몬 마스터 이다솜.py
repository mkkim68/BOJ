import sys
input = sys.stdin.readline

N, M = map(int, input().split())
pokemon = {}
pokemon_by_int = {}
for i in range(1, N+1):
    name = str(input())[:-1]
    pokemon[i] = name
    pokemon_by_int[name] = i

for _ in range(M):
    problem = str(input())[:-1]
    if problem.isdecimal():
        print(pokemon[int(problem)])
    else:
        print(pokemon_by_int[problem])
