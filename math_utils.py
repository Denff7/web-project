import numpy as np


def average(grades):
    return np.average(grades)


def min_max(grades):
    min_grade = min(grades)
    max_grade = max(grades)
    return min_grade, max_grade  # Правильно



def count_above_average(grades):
    avg = average(grades)
    above_avg = [grade for grade in grades if grade > avg]
    return len(above_avg)