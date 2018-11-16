from matplotlib import pyplot

from data_utils import load
from data_stats import CDataStatsNoPreprocess, CDataStatsTrimmed, CDataStatsFrame

x, y = load('data/mnist.csv')

noPreprocess = CDataStatsNoPreprocess()
trimmed = CDataStatsTrimmed(30)
frame = CDataStatsFrame(28, 28, 5)

for i in range(3):
    for stat in [frame]:
        pyplot.imshow(x[i].reshape(28, 28))
        pyplot.title('The ' + str(i + 1) + '. digit')
        pyplot.show()
        stat.histogram(x[i])
        pyplot.title('Histogram for the ' + str(i + 1) + '. digit')
        pyplot.show()
        print(stat.mean(x[i]))
