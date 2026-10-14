def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Expected exactly 3 fields separated by ';'")

    city, temp_str, date = parts
    city = city.strip()
    date = date.strip()

    if not city or not date:
        raise ValueError("City or date field is empty")

    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Temperature is not a valid number: {temp_str}")

    return {"city": city, "temperature": temp, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    valid_records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            continue
    return valid_records


def average_by_city(records: list[dict]) -> dict:
    sums = {}
    counts = {}

    for r in records:
        city = r["city"]
        t = r["temperature"]
        sums[city] = sums.get(city, 0.0) + t
        counts[city] = counts.get(city, 0) + 1

    averages = {}
    for city in sums:
        averages[city] = round(sums[city] / counts[city], 1)

    return averages


def warmest_city(records: list[dict]) -> str:
    if not records:
        return ""

    avgs = average_by_city(records)
    max_avg = max(avgs.values())
    candidates = [city for city, avg in avgs.items() if avg == max_avg]
    return min(candidates)
