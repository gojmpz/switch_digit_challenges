import re
from typing import Callable, Optional, List


def elementary_algebra(result: int) -> None:
    def solve(f: Callable, result: int) -> Optional[List[int]]:
        r = range(1, 10)
        for a1 in r:
            for a2 in r:
                if a2 == a1:
                    continue
                for a3 in r:
                    if a3 == a2 or a3 == a1:
                        continue
                    for a4 in r:
                        if a4 == a3 or a4 == a2 or a4 == a1:
                            continue
                        if f([a1, a2, a3, a4]) == result:
                            return [a1, a2, a3, a4]
        return None
    funcs = {
        lambda a: a[0] * a[1]: lambda a: f"{a[1]} * {a[0]} = {result}",
        1: None,
        lambda a: a[0] + a[1] + a[2]: lambda a: f"{a[0]} + {a[1]} + {a[2]} = {result}",
        lambda a: a[0] - a[1] + a[2]: lambda a: f"{a[0]} - {a[1]} + {a[2]} = {result}",
        lambda a: a[0] - a[1] - a[2]: lambda a: f"{a[0]} - {a[1]} - {a[2]} = {result}",
        2: None,
        lambda a: a[0] + a[1] + a[2] + a[3]: lambda a: f"{a[0]} + {a[1]} + {a[2]} + {a[3]} = {result}",
        lambda a: a[0] + a[1] - a[2] + a[3]: lambda a: f"{a[0]} + {a[1]} - {a[2]} + {a[3]} = {result}",
        lambda a: a[0] + a[1] - a[2] - a[3]: lambda a: f"{a[0]} + {a[1]} - {a[2]} - {a[3]} = {result}",
        3: None,
        lambda a: a[0] * a[1] + a[2]: lambda a: f"{a[1]} * {a[0]} + {a[2]} = {result}",
        lambda a: a[0] * a[1] - a[2]: lambda a: f"{a[1]} * {a[0]} - {a[2]} = {result}",
        4: None,
        lambda a: a[0] * a[1] + a[2] + a[3]: lambda a: f"{a[1]} * {a[0]} + {a[2]} + {a[3]} = {result}",
        lambda a: a[0] * a[1] - a[2] + a[3]: lambda a: f"{a[1]} * {a[0]} - {a[2]} + {a[3]} = {result}",
        lambda a: a[0] * a[1] - a[2] - a[3]: lambda a: f"{a[1]} * {a[0]} - {a[2]} - {a[3]} = {result}",
        5: None,
        lambda a: a[0] * a[1] * a[2]: lambda a: f"{a[0]} * {a[1]} * {a[2]} = {result}",
        lambda a: a[0] * a[1] * a[2] + a[3]: lambda a: f"{a[2]} * {a[1]} * {a[0]} + {a[3]} = {result}",
        lambda a: a[0] * a[1] * a[2] - a[3]: lambda a: f"{a[2]} * {a[1]} * {a[0]} - {a[3]} = {result}",
    }
    blank = False
    for f, r in funcs.items():
        if r is None:
            if not blank:
                print('')
                blank = True
            continue
        solution = solve(f, result)
        if solution:
            print(r(solution))
            blank = False


def solve_numeracy_test() -> None:
    var = input("\nNumber: ")
    if var == 'quit':
        exit()
    var = re.sub("[^0-9]", "", var)
    if len(var) == 0:
        return
    elementary_algebra(int(var))


if __name__ == '__main__':
    while True:
        try:
            solve_numeracy_test()
        except Exception as e:
            print(f"Exception occurred: {e}")
