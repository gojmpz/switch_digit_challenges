import re
from typing import Optional, List


def switch_test(rows: List[str]) -> None:
    def get_transformers() -> List[List[int]]:
        r = range(1, 5)
        res = []
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
                        res.append([a1, a2, a3, a4])
        return res

    def transform(pattern: List[int], transformer: List[int]) -> List[int]:
        output = []
        for item in transformer:
            output.append(pattern[item - 1])
        return output

    def find_solutions(transformers: List[List[Optional[List[int]]]], target: List[int]) -> List[List[int]]:
        input_pattern = [1, 2, 3, 4]
        viable_results = [[[None], input_pattern]]
        v = []
        for row in transformers:
            # print(viable_results)
            for ix, p in enumerate(viable_results):
                for t in row:
                    if t is None:
                        for t_iter in get_transformers():
                            history = p[0].copy()
                            history.append(t_iter)
                            v.append([history, transform(p[1], t_iter)])
                    else:
                        history = p[0].copy()
                        history.append(t)
                        v.append([history, transform(p[1], t)])
            if len(v) > 0:
                viable_results = v
                v = []
        ret = []
        # print(viable_results)

        for result in viable_results:
            if result[1] == target:
                ret.append(result[0])
        return ret

    def extract_transformers(pattern: str) -> List[List[Optional[int]]]:
        def format_(p: str) -> List[int]:
            return [int(_) for _ in p]

        splited = pattern.split(' ')
        transformers = []
        for item in splited:
            if item == '0':
                transformers.append(None)
                continue
            transformers.append(format_(item))
        return transformers

    rows = [re.sub(" +", " ", row).strip() for row in rows]
    transformers = []
    for row in rows:
        if len(row) > 0:
            transformers.append(extract_transformers(row))
    solutions = find_solutions(transformers[:-1], transformers[len(transformers) - 1][0])

    max_tr = [' ' for _ in range(max([len(t) for t in transformers]))]
    for solution in solutions:
        print(f"\nsolution")
        for chain, tr in zip(solution[1:], transformers[:-1]):
            s = ''.join([str(s) for s in chain])
            output = max_tr.copy()
            if tr[0] is not None:
                for ix, transformer in enumerate(tr):
                    if len(tr) == 1 and len(max_tr) > 1:
                        ix += 1
                    tr = ''.join([str(s) for s in transformer])
                    if tr == s:
                        output[ix] = '▓'
                    else:
                        output[ix] = '░'
            print(''.join(output) + f' {s}')


def solve_switch_test() -> None:
    labels = ['row', 'row', 'row', 'row']
    inp = []
    for label in labels:
        var = input(f"\n{label}: ")
        if var == 'quit':
            exit()
        var = re.sub("[^0-9 ]", "", var)
        inp.append(var)
    print(inp)
    if len(''.join(inp)) == 0:
        return
    switch_test(inp)


if __name__ == '__main__':
    while True:
        try:
            solve_switch_test()
        except Exception as e:
            print(f"Exception occurred: {e}")
