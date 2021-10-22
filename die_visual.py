from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die = Die()

#Make some rolls, and store the results in a list
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

#Prints the result of each roll

#print(results)
#Analize the results
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#print(frequencies)
x_values = list(range(1,die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title= 'Results of Rolling One D6 100 Times', xaxis=x_axis_config, yaxis= y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename = 'D6.html')
