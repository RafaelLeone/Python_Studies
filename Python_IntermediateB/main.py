import pandas
import os


# Get the absolute path to the directory containing the script.
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "quests.csv")
data = pandas.read_csv(file_path)

# Calculate data.
percentage = (data.Complete*100)/data.Total
formatted_percentage = percentage.apply(lambda x: f"{x:.2f}%")
print(formatted_percentage)

# Filter rows where "Quests" column.
selected_quests = ['Main', 'Side']
filtered_rows = data[data.Quests.isin(selected_quests)]
# Hide columns.
columns_to_drop = ['Found to do', 'Remaining', 'Remaining to find']
filtered_rows = filtered_rows.drop(columns=columns_to_drop)
print(filtered_rows)

# Add column.
data['Percentage'] = formatted_percentage
print(data)

# Delete data.
columns_to_drop.append('Percentage')
data = data.drop(columns=columns_to_drop)
data.to_csv('totk_tracker.csv', index=False)

new_data = pandas.read_csv('totk_tracker.csv')
print(new_data)
