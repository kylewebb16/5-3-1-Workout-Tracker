def calculate_one_rep_max(weight, reps):
    # Brzycki formula: load × (36 / (37 - reps))
    one_rep_max = weight * (36 / (37 - reps))
    return one_rep_max


def calc_five_week(one_rep_max):
    one_rep_max = one_rep_max * 0.9
    # 2 warmup sets 40%, 50%, working sets 65%, 75%, 85%
    five_week_sets = []
    five_week_sets[0] = one_rep_max * 0.4
    five_week_sets[1] = one_rep_max * 0.5
    five_week_sets[2] = one_rep_max * 0.65
    five_week_sets[3] = one_rep_max * 0.75
    five_week_sets[4] = one_rep_max * 0.85
    
    return five_week_sets

def calc_three_week(one_rep_max):
    one_rep_max = one_rep_max * 0.9
    # 2 warmup sets 40%, 50%
    # working sets are 70%, 80%, 90%
    three_week_sets = []
    three_week_sets[0] = one_rep_max * 0.4
    three_week_sets[1] = one_rep_max * 0.5
    three_week_sets[2] = one_rep_max * 0.7
    three_week_sets[3] = one_rep_max * 0.8
    three_week_sets[4] = one_rep_max * 0.9
    
    return three_week_sets

def calc_max_week(one_rep_max):
    one_rep_max = one_rep_max * 0.9
    # 2 warmup sets 40%, 50%
    # working sets are 75%, 85%, 95%
    max_week_sets = []
    max_week_sets[0] = one_rep_max * 0.4
    max_week_sets[1] = one_rep_max * 0.5
    max_week_sets[2] = one_rep_max * 0.75
    max_week_sets[3] = one_rep_max * 0.85
    max_week_sets[4] = one_rep_max * 0.95
    
    return max_week_sets

def calc_deload_sets(one_rep_max):
    one_rep_max = one_rep_max * 0.9
    # 2 warmup sets are 40%, 40%
    # 3 working sets are 40%, 50%, 60%
    deload_week_sets = []
    deload_week_sets[0] = one_rep_max * 0.4
    deload_week_sets[1] = one_rep_max * 0.4
    deload_week_sets[2] = one_rep_max * 0.4
    deload_week_sets[3] = one_rep_max * 0.5
    deload_week_sets[4] = one_rep_max * 0.6
    
    return deload_week_sets

def update_upper_max(one_rep_max):
    one_rep_max = one_rep_max + 5
    return one_rep_max

def update_lower_max(one_rep_max):
    one_rep_max = one_rep_max + 10
    return one_rep_max