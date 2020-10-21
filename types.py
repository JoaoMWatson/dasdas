from typing import Mapping


def soma(num1: int = 0, num2: int = 0) -> int:
    return num1 + num2


returno = soma(2, 2)
print(returno)

results: Mapping[str, int] = {
    "result 1": soma(1, 0),
    "result 2": soma(23232, 12131212)
}
retorno2 = results['result 2']
print(results['result 1'])
print(retorno2)
