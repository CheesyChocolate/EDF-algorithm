def edf_scheduler(tasks):
    current_time = 0
    tasks.sort(key=lambda x: x[3])  # Sort tasks based on deadlines

    for task in tasks:
        if task[1] > current_time:
            current_time = task[1]

        task_completion_time = current_time + task[2]
        task.append(task_completion_time)
        current_time = task_completion_time

    return tasks
