from math_utils import average, min_max, count_above_average

grades = [85, 92, 78, 90, 66, 74, 88, 95]

print("Список оцінок:", grades)
print("Середня оцінка:", average(grades))
print("Мінімум і максимум:", min_max(grades))
print("Кількість оцінок вище середнього:", count_above_average(grades))