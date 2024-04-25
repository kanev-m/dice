from dice import Dice
from plotly.graph_objs import Bar, Layout
from plotly import offline

dice_1 = Dice()
dice_2 = Dice()

results = []
frequencies = []

for roll_num in range(10000):
    result = dice_1.roll() + dice_2.roll()
    results.append(result)

# анализ результатов
max_result = dice_1.num_sides + dice_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# визуализация результатов
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dice 1000 items',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='2_d6.html')