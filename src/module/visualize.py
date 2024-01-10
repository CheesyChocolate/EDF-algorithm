def print_schedule(schedule):
    print("Scheduled Tasks:")
    for task, start_time in schedule:
        print(f"Task {task} starts at time {start_time}")


import matplotlib.pyplot as plt

def visualize_schedule(schedule):
    fig, ax = plt.subplots()

    y_ticks = []
    task_labels = []

    for i, (task_name, start_time) in enumerate(schedule):
        ax.barh(i, start_time, color='b', align='center')
        task_labels.append(f'Task {task_name}')

    ax.set_yticks(range(len(schedule)))
    ax.set_yticklabels(task_labels)
    ax.set_xlabel('Time')
    ax.set_ylabel('Tasks')
    ax.set_title('EDF Scheduler Visualization')

    plt.show()
