from typing import TextIO


def run_command(iter_obj: TextIO, query: str) -> list:
    query_items = query.split('|')
    for item in query_items:
        cmd_value = item.split(':')
        command = cmd_value[0]
        value = cmd_value[1]
        result = map(lambda v: v.strip(), iter_obj)
        if command == "filter":
            value = value
            result = filter(lambda v, text=value: text in v, result)
        if command == 'map':
            column_id = int(value)
            result = map(lambda v, idx=column_id: v.split(" ")[idx], result)
        if command == 'unique':
            result = set(result)
        if command == 'sort':
            order = value
            if order == 'desc':
                result = sorted(result, reverse=True)
            else:
                result = sorted(result)
        if command == 'limit':
            quantity = int(value)
            result = list(result)[:quantity]
        return result
