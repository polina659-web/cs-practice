from collections import Counter

def parse_event(line: str) -> dict:
    line = line.strip()
    if not line:
        raise ValueError("Пустая строка")

    parts = line.split(maxsplit=2)
    if len(parts) < 3:
        raise ValueError("Некорректная строка: недостаточно частей")

    time_str, level, message = parts
    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}

    if level not in valid_levels:
        raise ValueError(f"Неизвестный уровень: {level}")

    return {"time": time_str, "level": level, "message": message}


def count_levels(lines) -> dict:
    counts = {}

    for line in lines:
        line = line.strip()
        if not line:
            continue

        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            counts["BROKEN"] = counts.get("BROKEN", 0) + 1

    return counts


def top_errors(lines, n: int) -> list[list]:
    error_messages = []

    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            event = parse_event(line)
            if event["level"] == "ERROR":
                error_messages.append(event["message"])
        except ValueError:
            continue

    counter = Counter(error_messages)
    sorted_items = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    top_n = sorted_items[:n]

    return [[msg, count] for msg, count in top_n]


def format_report(counts: dict, errors: list[list]) -> str:
    report_lines = ["Отчёт по журналу", ""]

    for level in sorted(counts.keys()):
        count = counts[level]
        report_lines.append(f"{level}: {count}")

    report_lines.append("")
    report_lines.append("Частые ошибки:")

    for msg, count in errors:
        report_lines.append(f"- {msg} — {count}")

    return "\n".join(report_lines) + "\n"
