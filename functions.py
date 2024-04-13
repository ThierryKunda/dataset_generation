import random, csv
from datetime import datetime

from typing import Callable


def get_random_from_list(data: list[str|tuple[str, int]]) -> str:
    if isinstance(data[0], tuple):
        all_values = [vw[0] for vw in data]
        all_weights = [vw[1] for vw in data]
        return random.choices(all_values, all_weights)[0]
    key_number = random.randint(0, len(data)-1)
    return data[key_number]

def get_random_key(data: dict[str]) -> str:
    key_number = random.randint(0, len(data)-1)
    return list(data.keys())[key_number]

def get_weighted_key_from_keyname(list_of_keys: list[tuple[str, int]], keyname: str) -> tuple[str, int]:
    for wk in list_of_keys:
        if wk[0] == keyname:
            return wk
    raise ValueError("Not found in the list ")

def get_random_weighted_key(data: dict[str|tuple[str, int]]) -> str:
    all_weighted_keys = list(data.keys())
    if isinstance(all_weighted_keys[0], str):
        return get_random_key(data)
    all_keys = [wk[0] for wk in all_weighted_keys]
    all_weights = [wk[1] for wk in all_weighted_keys]
    res = random.choices(all_keys, all_weights)[0]
    return get_weighted_key_from_keyname(all_weighted_keys, res)

def get_values_from_method(data: dict[str|tuple[str, int]] | list[str], next_key_method: Callable[[dict], list]) -> list:
    # Affectation directe de la valeur de manière aléatoire
    if isinstance(data, list):
        return [get_random_from_list(data)]
    # Affectation d'une clé de manière aléatoire si data est un dictionnaire
    key = next_key_method(data)
    value = data[key]
    formatted_key = key[0] if isinstance(key, tuple) else key
    if isinstance(value, list):
        return [formatted_key, get_random_from_list(value)]
    return [formatted_key] + get_values_from_method(value, next_key_method)

def generate_sample(data: dict, sample_size: int = 50):
    res = []
    for _ in range(sample_size):
        res.append(get_values_from_method(data, get_random_weighted_key))
    return res

def merge_nth_row(columns: list[list[str]], nth: int) -> list[list[str]]:
    res = []
    for col in columns:
        res += col[nth]
    return res

def generate_random_time(date_start: str, date_end: str) -> str:
    date_start = datetime.strptime(date_start, "%d/%m/%Y")
    date_end = datetime.strptime(date_end, "%d/%m/%Y")
    date_start_ts, date_end_ts = date_start.timestamp(), date_end.timestamp()
    rand_ts = random.uniform(date_start_ts, date_end_ts)
    res = datetime.fromtimestamp(rand_ts)
    return res.strftime("%d/%m/%Y")

def add_rand_dates_for_rows(rows: list[list[str]], date_start: str, date_end: str):
    res = []
    for row in rows:
        res.append([generate_random_time(date_start, date_end)] + row)
    return res

def merge_sample(columns: list[list[str]], max_index: int, header: list[str] | None = None, date_start: str = "28/04/2008", date_end: str = "11/04/2024") -> list[list[str]]:
    # res = [header] if header else []
    res = []
    for nth in range(max_index):
        res.append(merge_nth_row(columns, nth))
    res = add_rand_dates_for_rows(res, date_start, date_end)
    # print(res[0])
    return [header] + res if header else res

def generate_dataset(possible_values: list[dict[str]], rows_amount: int = 50, header: list[str] | None = None) -> list[str]:
    samples = [generate_sample(values, rows_amount) for values in possible_values]
    return merge_sample(samples, rows_amount, header)

def to_csv_file(dataset: list[list[str]], path: str, separator: str = ";"):
    with open(path, 'w', newline='', encoding="utf8") as csvfile:
        writer = csv.writer(csvfile, delimiter=separator)
        writer.writerows(dataset)