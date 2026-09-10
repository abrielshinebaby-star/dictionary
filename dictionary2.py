dictionary={"Maths":80,"Science":70,"English":90,"French":95,"History":100}
total_values=0
for value in dictionary.values():
    total_values=total_values+value
print(total_values)
number_of_values=len(dictionary.values())
print(total_values/number_of_values)