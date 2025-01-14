"""
poorly performing, poorly written module

"""

import datetime
import csv
import time
import timeit
import cProfile
import line_profiler
import atexit
profile = line_profiler.LineProfiler()
atexit.register(profile.print_stats)


@profile
def analyze(filename):
    start = datetime.datetime.now()
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        new_ones = []
        [new_ones.append((list(row)[5], list(row)[0])) for row in reader if list(row)[5] > '00/00/2012']

        year_count = {
            "2013": 0,
            "2014": 0,
            "2015": 0,
            "2016": 0,
            "2017": 0,
            "2018": 0
        }

        for new in new_ones:
            if new[0][6:] == '2013':
                year_count["2013"] += 1
            elif new[0][6:] == '2014':
                year_count["2014"] += 1
            elif new[0][6:] == '2015':
                year_count["2015"] += 1
            elif new[0][6:] == '2016':
                year_count["2016"] += 1
            elif new[0][6:] == '2017':
                year_count["2017"] += 1
            elif new[0][6:] == '2018':
                year_count["2017"] += 1

        print(year_count)

    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        found = 0

        for line in reader:
            # lrow = list(line)
            if "ao" in line[6]:
                found += 1

        print(f"'ao' was found {found} times")
        end = datetime.datetime.now()

    return start, end, year_count, found


@profile
def main():
    filename = "data/exercise.csv"
    # t0 = time.time()
    analyze(filename)
    # t1 = time.time()
    # print(t1-t0)


if __name__ == "__main__":
    main()
