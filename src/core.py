from module.EDF import edf_scheduler
from module.visualize import visualize_schedule

# 2D array: [task_name, arrival_time, execution_time, deadline, completion_time]
tasks_list = [
    ['A', 0, 3, 5],
    ['B', 2, 5, 10],
    ['C', 4, 2, 7],
    ['D', 5, 4, 12],
    ['E', 6, 2, 15],
    ['F', 7, 3, 20],
    ['G', 8, 2, 25],
    ['H', 9, 4, 30],
]


# Running the EDF scheduler from EDF module
edf_scheduler(tasks_list)

# Visualizing the schedule using the visualize module
visualize_schedule(tasks_list)
