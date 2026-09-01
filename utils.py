# Creating a function to round data to tabular values
def round_to_table_value(value, available_values):
    if value <= available_values[0]:
        return available_values[0]

    if value >= available_values[-1]:
        return available_values[-1]

    for i in range(len(available_values) - 1):
        if available_values[i] <= value <= available_values[i + 1]:
            if value - available_values[i] <= available_values[i + 1] - value:
                return available_values[i]
            return available_values[i + 1]

    return available_values[-1]
