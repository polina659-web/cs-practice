import json
import re

_INT_RE = re.compile(r"^-?\d+$")
_FLOAT_RE = re.compile(r"^-?\d+\.\d+$")


def _parse_value(raw: str):
    value = raw.strip()
    if value.lower() in ("true", "yes"):
        return True
    if value.lower() in ("false", "no"):
        return False
    if _INT_RE.match(value):
        return int(value)
    if _FLOAT_RE.match(value):
        return float(value)
    return value


def csv_to_records(text: str) -> list[dict]:
    lines = [line for line in text.split("\n") if line.strip()]
    if not lines:
        return []
    headers = [h.strip() for h in lines[0].split(",")]
    records = []
    for line in lines[1:]:
        values = [v.strip() for v in line.split(",")]
        records.append(dict(zip(headers, values)))
    return records


def parse_settings(lines: list[str]) -> dict:
    settings = {}
    current_key = None
    for line in lines:
        line = line.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        stripped = line.strip()
        if stripped.startswith("- "):
            if current_key is not None:
                settings[current_key].append(_parse_value(stripped[2:]))
            continue
        if ":" in stripped:
            key, _, value = stripped.partition(":")
            key = key.strip()
            if value.strip():
                settings[key] = _parse_value(value)
                current_key = None
            else:
                settings[key] = []
                current_key = key
    return settings


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    result = []
    for row in rows:
        value = row.get(key)
        if value in extra:
            merged = dict(extra[value])
            merged.update(row)
            result.append(merged)
        else:
            result.append(dict(row))
    return result


def records_to_json(records: list[dict]) -> str:
    return json.dumps(records, ensure_ascii=False, indent=2, sort_keys=True)
