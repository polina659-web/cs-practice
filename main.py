from stats import read_valid, average_by_city, warmest_city
import sys

if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    valid_records = read_valid(lines)

    num_parsed = len(valid_records)
    num_skipped = len(lines) - num_parsed

    if num_parsed == 0:
        print(0)
        print(0)
        print(0.0)
    else:
        avgs = average_by_city(valid_records)
        warmest = warmest_city(valid_records)

        print(num_parsed)
        print(num_skipped)
        print(f"{avgs[warmest]:.1f}")
