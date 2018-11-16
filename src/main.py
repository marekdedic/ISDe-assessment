from matplotlib import pyplot

from data_utils import load
from data_stats import CDataStatsNoPreprocess, CDataStatsTrimmed, CDataStatsFrame

x, y = load('data/mnist.csv')

stats = [CDataStatsNoPreprocess(), CDataStatsTrimmed(30), CDataStatsFrame(28, 28, 5)]
names = ['original', 'trimmed', 'framed']
output = ''

for i in range(3):
    digit = x[i]
    pyplot.figure(figsize = (12, 12))
    pyplot.subplot(2, 2, 1)
    pyplot.imshow(digit.reshape(28, 28))
    pyplot.title('The ' + str(i + 1) + '. digit')
    for j in range(len(stats)):
        pyplot.subplot(2, 2, j + 2)
        stat = stats[j]
        stat.histogram(digit)
        pyplot.title('Histogram, ' + names[j])
        output += 'The mean of the ' + str(i + 1) + '. digit, ' + names[j] + ': ' + str(stat.mean(digit)) + '\n'
    pyplot.savefig('digit' + str(i) + '.pdf', dpi = 1000)

for j in range(len(stats)):
    stat = stats[j]
    output += 'The global mean, ' + names[j] + ': ' + str(stat.dataset_mean(x)) + '\n'

file = open("output.txt", "w")
file.write(output)
file.close()
