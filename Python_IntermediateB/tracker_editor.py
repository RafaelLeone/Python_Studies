import pandas
import os


# Get the absolute path to the directory containing the script.
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "totk_tracker.csv")
data = pandas.read_csv(file_path)

# Calculate data.
## Calculate All.
total_sum = data['Total'].sum()
complete_sum = data['Complete'].sum()
found_sum = data['Found'].sum()
all = {'Quests': 'All', 'Total': total_sum, 'Complete': complete_sum, 'Found': found_sum}
new_row = pandas.DataFrame([all])
data = pandas.concat([data, new_row], ignore_index=True)
print(data)
## Calculate percentage.
percentage = (data.Complete*100)/data.Total
formatted_percentage = percentage.apply(lambda x: f"{x:.2f}%")
data['Percentage'] = formatted_percentage
## Calculate Remaining.
remaining = data.Total - data.Complete
data['Remaining'] = remaining
## Calculate Remaining to find.
remaining_to_find = data.Total - data.Found
data['Remaining to find'] = remaining_to_find
## Calculate Found to do.
found_to_do = data.Remaining - data['Remaining to find']
data['Found to do'] = found_to_do

# Reorder.
data_dict = {index: float(row['Percentage'][:-1]) for (index, row) in data.iterrows()}
all_position = len(data_dict) - 1
# Order the dictionary by values
sorted_dict = dict(sorted(list(data_dict.items())[:-1], key=lambda item: item[1]))
new_order = list(sorted_dict.keys())
new_order.append(all_position)
result_data = data.reindex(new_order)

print(result_data)

file_path = os.path.join(script_dir, "totk_totals.csv")
result_data.to_csv(file_path, index=False)
