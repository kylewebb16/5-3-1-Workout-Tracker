def calculate_one_rep_max(weight, reps):
    # Brzycki formula: load × (36 / (37 - reps))
    one_rep_max = weight * (36 / (37 - reps))
    return one_rep_max

class Exercise():
    def __init__(self, one_rep_max: int) -> None:
        self.one_rep_max = one_rep_max
    
    def calc_five_week(self):
        working_max = self.one_rep_max * 0.9
        # 2 warmup sets 40%, 50%, working sets 65%, 75%, 85%
        percents_five_week = [0.4, 0.5, 0.65, 0.75, 0.85]
        five_week_sets = [round(percent * working_max) for percent in percents_five_week]
        return five_week_sets
    
    def calc_three_week(self):
        working_max = self.one_rep_max * 0.9
        # 2 warmup sets 40%, 50%
        # working sets are 70%, 80%, 90%
        percent_deload_week = [0.4, 0.5, 0.7, 0.8, 0.9]
        three_week_sets = [round(percent * working_max) for percent in percent_deload_week]
        return three_week_sets

    def calc_max_week(self):
        working_max = self.one_rep_max * 0.9
        # 2 warmup sets 40%, 50%
        # working sets are 75%, 85%, 95%
        percent_max_week = [0.4, 0.5, 0.75, 0.85, 0.95]
        max_week_sets = [round(percent * working_max) for percent in percent_max_week]
        return max_week_sets

    def calc_deload_sets(self):
        working_max = self.one_rep_max * 0.9
        # 2 warmup sets are 40%, 40%
        # 3 working sets are 40%, 50%, 60%
        percent_deload_week = [0.4, 0.5, 0.5, 0.6, 0.7]
        deload_week_sets = [round(percent * working_max) for percent in percent_deload_week]
        return deload_week_sets

    def update_ORM(self):
        self.one_rep_max = self.one_rep_max + 5
    
class Squat(Exercise):
    pass

class Deadlift(Exercise):
    pass

class BenchPress(Exercise):
    def update_ORM(self):
        self.one_rep_max = self.one_rep_max + 5

class OverheadPress(Exercise):
    def update_ORM(self):
        self.one_rep_max = self.one_rep_max + 5