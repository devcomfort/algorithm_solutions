from typing import Union
import re


def printify(name: str, cnt: Union[int, str], max_len: int = 20):
    return f"{name}{' ' * (max_len - len(str(cnt)) - len(name))}{cnt}"


print(
    printify("Animal", "Count"),
    "-"*20,
    sep="\n"
)

print(
    '\n'.join(
        list(
            map(
                lambda v: printify(
                    *re.sub(r"\s+", " ", v).split()),
                """
                    Chickens      100
                    Clydesdales     5
                    Cows           40
                    Goats          22
                    Steers          2
                """
                .strip()
                .split('\n')
            )
        )
    ))
