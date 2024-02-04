import math

import numpy
import scipy
from scipy.signal import find_peaks

from plot_data import plot_data
import parser_data

cleanTime = []


def count_steps(data):
    global cleanTime
    #print("Accelerometer data graph")

    cleanMag = moving_average(vector_magnitude(data), 100, data)
    '''
    ADD YOUR CODE HERE. This function counts the number of steps in data and returns the number of steps
    '''
    peaks, _ = find_peaks(cleanMag, distance=50)
    peaks = list(peaks)
    dataPeaks = []
    peakTime = []

    for x in peaks:
        dataPeaks.append(cleanMag[x])
        peakTime.append(data[x][0])


    num_steps = len(dataPeaks)

    timeSpan = abs(data[0][0] - data[len(data) - 1][0])

    num_steps = num_steps / timeSpan
    # plot_data(data, vector_magnitude(data), cleanMag, cleanTime, dataPeaks, peakTime)

    # return number of steps taken per second
    return num_steps


def vector_magnitude(data):
    magnitude = []

    for x in range(len(data)):
        magnitude.append(math.sqrt((data[x][1] ** 2 + (data[x][2]) ** 2) + (data[x][3] ** 2)))

    return magnitude


def moving_average(data, window, data2):
    global cleanTime
    cleanMag = []
    cleanTime = []
    for x in range(len(data) - window):
        average = 0

        for y in range(window):
            average += data[x + y]

        cleanMag.append(average / window)
        cleanTime.append(data2[x][0])

    return cleanMag


def main():
    number_of_steps_DataOne = []
    for x in range(1, 11):
        file_name = f"TA 1/window{x}.csv"  # Change to your file name
        data = parser_data.get_data(file_name)
        number_of_steps_DataOne.append(count_steps(data))

    number_of_steps_DataTwo = []
    for x in range(1, 11):
        file_name = f"TA 2/window{x}.csv"  # Change to your file name
        data = parser_data.get_data(file_name)
        number_of_steps_DataTwo.append(count_steps(data))

    number_of_steps_DataThree = []
    for x in range(1, 11):
        file_name = f"TA 3/window{x}.csv"  # Change to your file name
        data = parser_data.get_data(file_name)
        number_of_steps_DataThree.append(count_steps(data))

    averageOne = numpy.mean(number_of_steps_DataOne)
    averageTwo = numpy.mean(number_of_steps_DataTwo)
    averageThree = numpy.mean(number_of_steps_DataThree)

    threshold = .25
    for x in range(1, 10):
        file_name = f"test/test_window{x}.csv"  # Change to your file name
        data = parser_data.get_data(file_name)
        number_of_steps_test = count_steps(data)

        if (averageOne - threshold) < number_of_steps_test < (averageOne + threshold):
            print(x, "is for TA 1")
        elif (averageTwo - threshold) < number_of_steps_test:
            print(x, "is for TA 2")
        elif (averageThree - threshold) < number_of_steps_test < (averageThree + threshold):
            print(x, "is for TA 3")



if __name__ == "__main__":
    main()
