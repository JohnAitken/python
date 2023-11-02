import re

with open('work_attendance.txt', "r") as f, open("outfile.txt", "w") as outfile:
    for line in f:
        if line.strip():
            outfile.write(line)

results = []

with open('outfile.txt', 'r') as o:
    results = [line[-9:].strip() for line in o]

mornings = [x[:-2].rstrip() for x in results if x.endswith("AM")]
afternoons = [x[:-2].rstrip() for x in results if x.endswith("PM")]

def time_to_seconds(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60

mornings_seconds = [time_to_seconds(time) for time in mornings]
afternoons_seconds = [time_to_seconds(time) for time in afternoons]

mornings_average = sum(mornings_seconds) / len(mornings_seconds) if mornings_seconds else 0
afternoons_average = sum(afternoons_seconds) / len(afternoons_seconds) if afternoons_seconds else 0

morn_hr, morn_min = divmod(mornings_average, 3600)
aft_hr, aft_min = divmod(afternoons_average, 3600)
morn_min = morn_min // 60
aft_min = aft_min // 60

morn_min_str = f"{morn_min:02}"
aft_min_str = f"{aft_min:02}"

print(f'Average start time: {morn_hr}:{morn_min_str} AM')
print(f'Average quit time: {aft_hr}:{aft_min_str} PM')
