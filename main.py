import calculate_lifts as prgm

weight = 300
reps = 2
one_rep_max = prgm.calculate_one_rep_max(weight, reps)
bench = prgm.BenchPress(one_rep_max)
three_week_bench = bench.calc_three_week()

for i in range(5):
    print("Set {}: 5 reps of {} \n".format(i + 1, three_week_bench[i]))
