import sys


def main():
    for question in questions:
        try:
            print(pokemon_list[int(question)])
        except:
            print(pokedex[question])


if __name__ == "__main__":
    input = sys.stdin.readline
    n, m = map(int, input().split())
    pokemon_list = [0]
    pokedex = {}
    number = 1
    for _ in range(n):
        pokemon = input().rstrip()
        pokemon_list.append(pokemon)
        pokedex[pokemon] = number
        number += 1
    questions = [input().rstrip() for _ in range(m)]
    
    main()
    