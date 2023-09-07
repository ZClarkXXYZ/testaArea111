import matplotlib.pyplot as plt

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("Hello World")


def testFunct2C(): #function for Lab 1 2.C
    listX = [1,2,3,4]
    listY = [1,4,9,16]
    plt.plot(listX, listY, 'gs')
    plt.axis([0, 6, 0, 20])
    plt.show()

def plotFunct2F(): #function for Lab 1 2. and also 3
    x_chord = 8
    y_chord = 2.6
    #plt.plot(x_chord, y_chord, 'kd') #Single chord plotting


    m_slope = 3
    b_intercept = 5
    chords = 6
    chordListY = []
    chordListX = []
    for chord in range(chords):
        chordListX.append(x_chord + x_chord*chord)
        chordListY.append(y_chord + y_chord*m_slope*chord + b_intercept)

    plt.plot(chordListX, chordListY)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

plotFunct2F()