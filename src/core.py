from module.EDF import Task, edf_scheduler
from module.visualize import print_schedule
from module.visualize import visualize_schedule

# Your tasks
# Task(name, release_time, execution_time, deadline)
task1 = Task("A", 0, 3, 5)
task2 = Task("B", 2, 5, 10)
task3 = Task("C", 4, 2, 7)
task4 = Task("D", 6, 4, 8)
task5 = Task("E", 7, 1, 3)
task6 = Task("F", 8, 3, 6)
task7 = Task("G", 10, 2, 4)
task8 = Task("H", 12, 4, 7)

tasks_list = [task1, task2, task3, task4, task5, task6, task7, task8]

# Running the EDF scheduler from EDF module
result_schedule = edf_scheduler(tasks_list)

print("Schedule: ", result_schedule)

# Printing the schedule using the visualize module
print_schedule(result_schedule)

# Visualizing the schedule using the visualize module
visualize_schedule(result_schedule)
