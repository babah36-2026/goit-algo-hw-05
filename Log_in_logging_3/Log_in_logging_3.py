import sys

def parse_log_line(line: str) -> dict:
    date, time, level, message = line.strip().split(" ", 3)

    return {
        "date": date,
        "time": time,
        "level": level,
        "message": message
    }


def load_logs(file_path: str) -> list:
    logs = []

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            logs.append(parse_log_line(line))

    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["level"] == level.upper()]

def count_logs_by_level(logs: list) -> dict:
    counts = {}

    for log in logs:
        level = log["level"]

        if level in counts:
            counts[level] += 1
        else:
            counts[level] = 1

    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")

    for level, count in counts.items():
        print(f"{level:<17}| {count}")

if len(sys.argv) < 2:
    print("Вкажіть шлях до лог-файлу.")
    sys.exit()

file_path = sys.argv[1]

try:
    logs = load_logs(file_path)

except FileNotFoundError:
    print("Файл не знайдено.")
    sys.exit()

except ValueError:
    print("Помилка в структурі log-файлу.")
    sys.exit()

counts = count_logs_by_level(logs)
display_log_counts(counts)

if len(sys.argv) > 2:
    level = sys.argv[2]
    filtered_logs = filter_logs_by_level(logs, level)

    print(f"\nДеталі логів для рівня '{level.upper()}':")

    for log in filtered_logs:
        print(f'{log["date"]} {log["time"]} - {log["message"]}')




