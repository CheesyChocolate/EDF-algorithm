def print_schedule(tasks_list):
    for task in tasks_list:
        print(f"Task: {task[0]}, Completion Time: {task[4] if len(task) > 4 else 'Not Completed'}")


def visualize_schedule(tasks):
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()

    for i, task in enumerate(tasks):
        task_name = task[0]
        arrival_time = task[1]
        execution_time = task[2]
        completion_time = task[4]

        ax.barh(task_name, width=completion_time - arrival_time, left=arrival_time, label=f'Task {task_name}', color='g')

    ax.set_xlabel('Time')
    ax.set_ylabel('Tasks')
    ax.set_title('Task Schedule Visualization')
    ax.legend()

    plt.show()
