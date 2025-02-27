from pathlib import Path
from typing import List, Tuple

type Salary = Tuple[int, int]
type Cats = List[dict]


def total_salary(path: str) -> Salary:
    splitted = path.split(".")

    if splitted[-1] != "txt":
        raise ValueError("You need to specify txt file")

    total = 0
    average = 0

    with open(path, "r") as file:
        lines = file.read().split("\n")
        for line in lines:
            guy, salary = line.split(",")
            total += int(salary)
            average += int(salary)
        average = int(average / len(lines))

    return total, average


def get_cats_info(path: str) -> Cats:
    formatted_cats = []
    with open(path, "r") as file:
        lines = file.read().split("\n")
        for line in lines:
            cat_id, name, age = line.split(",")
            formatted_cats.append({"id": cat_id, "name": name, "age": age})

    return formatted_cats


def walk_tree(path: str, indent: str = ""):
    converted_path = Path(path).expanduser().resolve()

    if not converted_path.is_dir():
        print(f"Error: {converted_path} is not directory.")
        return

    visited = set()

    if converted_path in visited:
        return

    visited.add(converted_path)

    print(f"{indent}📂 {converted_path.name}")

    items = sorted(converted_path.iterdir())

    for item in items:
        if item.is_dir():
            walk_tree(str(item), "   ")
        else:
            print(f"{indent}   📜 {item.name}")
