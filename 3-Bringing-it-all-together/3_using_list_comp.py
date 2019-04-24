""" Using a list comprehension
This time, you're going to use the lists2dict() function you defined in the last exercise to turn a bunch of lists into a list of dictionaries with the help of a list comprehension.

The lists2dict() function has already been preloaded, together with a couple of lists, feature_names and row_lists. feature_names contains the header names of the World Bank dataset and row_lists is a list of lists, where each sublist is a list of actual values of a row from the dataset.

Your goal is to use a list comprehension to generate a list of dicts, where the keys are the header names and the values are the row entries. """

""" Instructions
70 XP
Instructions
70 XP
Inspect the contents of row_lists by printing the first two lists in row_lists.
Create a list comprehension that generates a dictionary using lists2dict() for each sublist in row_lists. The keys are from the feature_names list and the values are the row entries in row_lists. Use sublist as your iterator variable and assign the resulting list of dictionaries to list_of_dicts.
Look at the first two dictionaries in list_of_dicts by printing them out.
Show Answer (-70 XP)
Hint
To access the yth element of a list x, do: x[y].
The output expression should be a call to lists2dict(), with feature_names as the first argument and sublist as the second argument. Make sure you iterate over the list of lists row_lists.
You can access the elements of a list of dictionaries the same way as you would any other list. """

# Print the first two lists in row_lists
print(row_lists[0])
print(row_lists[1])

# Turn list of lists into list of dicts: list_of_dicts
list_of_dicts = [lists2dict(feature_names,sublist) for sublist in row_lists]

# Print the first two dictionaries in list_of_dicts
print(list_of_dicts[0])
print(list_of_dicts[1])