import sys
from logstats import count_levels, top_errors, format_report, parse_event

def main():
    filename = sys.stdin.readline().strip()
    if not filename:
        return

    total_parsed = 0
    error_count = 0
    broken_count = 0

    with open(filename, encoding="utf-8") as log:
        for line in log:
            line = line.strip()
            if not line:
                continue
            try:
                event = parse_event(line)
                total_parsed += 1
                if event["level"] == "ERROR":
                    error_count += 1
            except ValueError:
                broken_count += 1

    print(total_parsed)
    print(error_count)
    print(broken_count)

    with open(filename, encoding="utf-8") as log:
        counts = count_levels(log)

    with open(filename, encoding="utf-8") as log:
        errors = top_errors(log, 5)

    report = format_report(counts, errors)

    with open("report.txt", "w", encoding="utf-8") as f:
        f.write(report)


if __name__ == "__main__":
    main()
