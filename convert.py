def convert_output(output):
    converted_output = []
    task_execution = []
    for item in output:
        if isinstance(item, list):
            task_execution.append([item[0], item[1]])
        else:
            converted_output.append(task_execution)
            task_execution = []
    if task_execution:
        converted_output.append(task_execution)
    return converted_output
output = [
    [0, 1.5], [4, 5.5], [8.5, 10], [12, 13.5], [16, 17.5], [20, 21.5], [24, 25.5],
    [1.5, 4], [8, 8.5], [10.5, 12], [13.5, 15.0], [21.5, 24], [25.5, 26.0],
    [5.5, 8], [10, 10.5], [15.0, 16], [17.5, 19.5], [26.0, 28]
]

converted_output = convert_output(output)

print(converted_output)
