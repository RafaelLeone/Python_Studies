import pandas
import os


# Get the absolute path to the directory containing the script.
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "totk_tracker.csv")
data = pandas.read_csv(file_path)
print(data)

# Calculate data.
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
# Order the dictionary by values
sorted_dict = dict(sorted(data_dict.items(), key=lambda item: item[1]))
new_order = list(sorted_dict.keys())
result_data = data.reindex(new_order)

print(result_data)

# To do: Properly reorder and create new csv in this folder.
