import matplotlib.pyplot as plt
import numpy as np
def plot_gantt_chart(tasks):
    fig, ax = plt.subplots()

    # Set y-axis limits and labels
    ax.set_ylim(0, len(tasks))
    ax.set_yticks(range(len(tasks)))
    ax.set_yticklabels([f'T{i}' for i in range(1, len(tasks) + 1)])

    # Set x-axis limits and labels
    min_time = min(task[0][0] for task in tasks)
    max_time = max(task[-1][1] for task in tasks)
    ax.set_xlim(min_time, max_time)
    ax.set_xlabel('Time')
    ax.set_xticks(np.arange(0,29,1))

    # Define colors for each task
    colors = ['#f4eb97', '#89ddf4','grey', '#e8b7b7']
  # Adding 'gray' for idle state

    # Merge all task intervals into a single list
    all_intervals = [interval for task in tasks for interval in task]

    # Sort the intervals by start time
    all_intervals.sort(key=lambda interval: interval[0])

    # Calculate idle intervals
    idle_intervals = []
    previous_end = min_time
    for interval in all_intervals:
        start, end = interval
        if start > previous_end:
            idle_intervals.append([previous_end, start])
        previous_end = max(previous_end, end)

    # Plot the tasks
    for i, task in enumerate(tasks):
        for start, end in task:
            duration = end - start
            ax.barh(i, duration, left=start, height=0.5, align='center', color=colors[i])

    # Plot the idle intervals
    for interval in idle_intervals:
        start, end = interval
        duration = end - start
        ax.barh(len(tasks), duration, left=start, height=0.5, align='center', color=colors[-1])

    # Display the chart
    plt.grid(True)
    plt.show()

# Define the task data
tasks = [
    [[0, 1.5], [4, 5.5], [8.5, 10], [12, 13.5], [16, 17.5], [20, 21.5], [24, 25.5]],
 [[1.5, 4], [8, 8.5], [10.5, 12], [13.5, 15.0], [21.5, 24], [25.5, 26.0]],
 [[5.5, 8], [10, 10.5], [15.0, 16], [17.5, 19.5], [26.0, 28]],
]



# Plot the Gantt chart
plot_gantt_chart(tasks)
