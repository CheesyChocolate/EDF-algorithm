class Task:
    def __init__(self, name, arrival_time, execution_time, deadline):
        self.name = name
        self.arrival_time = arrival_time
        self.execution_time = execution_time
        self.deadline = deadline

    def __str__(self):
        return f"Task {self.name}: Arrival={self.arrival_time}, Execution={self.execution_time}, Deadline={self.deadline}"


def edf_scheduler(tasks):
    current_time = 0
    tasks.sort(key=lambda x: x.deadline)  # Sort tasks based on deadlines
    schedule = []

    while tasks:
        available_tasks = [task for task in tasks if task.arrival_time <= current_time]
        if not available_tasks:  # If no tasks are available at current time
            current_time += 1
            continue

        selected_task = min(available_tasks, key=lambda x: x.deadline)
        tasks.remove(selected_task)
        schedule.append((selected_task.name, current_time))
        current_time += selected_task.execution_time

    return schedule
