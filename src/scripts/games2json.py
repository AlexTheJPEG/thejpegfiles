import json
import re

def get_wordle():
    print("Paste Wordle results exactly, then press Enter: ")
    wordle = []
    first_line_match = re.match(r"Wordle (\S*) (\S)/6", input())
    wordle_number, wordle_guesses = first_line_match.groups()
    wordle_number = int(wordle_number.replace(",", ""))
    wordle_guessed = wordle_guesses != "X"
    wordle_guesses = int(wordle_guesses) if wordle_guessed else 6
    _ = input()
    for _ in range(wordle_guesses):
        wordle.append(input())
    return {
        "number": wordle_number,
        "guesses": wordle_guesses if wordle_guessed else "X",
        "game": wordle,
    }


def get_connections():
    print("Paste Connections results exactly, then press Enter: ")
    connections = []
    _ = input()
    connections_number = int(input().split("#")[1])
    connections_full_rows, connections_mistakes = 0, 0
    while connections_full_rows != 4 and connections_mistakes != 4:
        connections.append((row := input()))
        if all(r == row[0] for r in row):
            connections_full_rows += 1
        else:
            connections_mistakes += 1
    return {
        "number": connections_number,
        "mistakes": connections_mistakes,
        "game": connections,
    }


def get_strands():
    print("Paste Strands results exactly, then press Enter *twice*: ")
    strands = []
    strands_number = int(input().split("#")[1])
    strands_theme = input()
    strands_hints = 0
    while (row := input()) != "":
        strands.append(row)
        strands_hints += row.count("💡")
    return {
        "number": strands_number,
        "theme": strands_theme,
        "hints": strands_hints,
        "game": strands,
    }

wordle_results = get_wordle()
connections_results = get_connections()
strands_results = get_strands()

games_json = json.dumps({
    "wordle": wordle_results,
    "connections": connections_results,
    "strands": strands_results,
}, ensure_ascii=False)
print(games_json)


