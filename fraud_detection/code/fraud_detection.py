import matplotlib.pyplot as plot
import csv
import numpy as np
import random
import sys
file = open(sys.argv[1], "r")
#file = open("ElectionUSA2012.csv", "r")
outfile = open("retrievedData.txt", "w")
outfile2 = open("myAnswer.txt", "w")
nominees=[]
x=[]
states = []
NomineesDict = {}
firstnine = []
percentages = []
percentagesstr = []
oo =sys.argv[2].split(',')
#------------------------------------------returns a list which contains all vote for each nominees
def retrieveData(x,y):
    a = []
    for i in y:
        input_file = csv.DictReader(open(str(x)))
        NomineesDict[str(i)] = [int(d[i]) for d in input_file if str(i) in d]
        a.extend(NomineesDict[str(i)])
    return a
#print(retrieveData(sys.argv[1], oo))    # sys.argv[1], sys.argv[2]
outfile.write(str(retrieveData(sys.argv[1], oo)))
firstlist = retrieveData(sys.argv[1], oo)
#------------------------------------------percentage calculations
for i in oo:
    firstnine.append(NomineesDict[str(i)])
for i in firstnine:
    p = sum(i) / sum(retrieveData(sys.argv[1], oo)) *100
    q = float("%.3F" % p)
    percentages.append(q)
for i in percentages:
    r = "{}%".format(i)
    percentagesstr.append(r)
#-------------------------------------------plotting
def DispBarPlot():
    for line in file.readlines():
        operands = line.rstrip('\n').split(',')
        #print(operands)
        nominees.append(operands)
        x=nominees[1:]
    #print("x", x)
    for i in x:
        states.append(i[0])
    #print(states)
    temp=[]
    temp2=[]
    colons={}
    y = oo
    for i in NomineesDict.keys():
        toplam = sum(NomineesDict[i])
        colons[str(i)] = sum(NomineesDict[i])
        temp.append(colons[str(i)])
    for i in y:
        if sorted(temp)[-1] == colons[i]:
            t=i
        elif sorted(temp)[-2] == colons[i]:
            u=i
    #print(t)
    #print(u)
    values = NomineesDict[t]
    zınk = NomineesDict[u]
    #print(zınk)
    #print(values)
    barw = 0.2
    x_pos = index = np.arange(len(states))
    #x_pos = [x for x in range(len(states))]

    plot.bar(x_pos, zınk,width=barw, label=str(u), color="r")
    plot.bar(x_pos + barw, values, width=barw, label=str(t), color="b")
    plot.xticks(x_pos + barw, states)
    plot.xlim((0, len(states)))
    plot.xticks(size='small', rotation=90)
    #plt.subplots(nrows=2, ncols=2)    #grafik outputunda 4 tane kare cıkarıyor
    plot.ylabel("Vote Count")
    plot.xlabel("States")
    plot.legend()
    plot.tight_layout()
    plot.savefig('ComparativeVotes.pdf', bbox_inches=None)
    #plot.show()
    plot.close()
def compareVoteonBar():
    po = oo
    x_pos = index = np.arange(len(percentages))
    for i in po:
        if po.index(i) == 0:
            plot.bar(x_pos, percentages, label=i, color='r', align="center")
        elif po.index(i) == 1:
            plot.bar(x_pos, percentages, label=i, color='b', align="center")
        elif po.index(i) == 2:
            plot.bar(x_pos, percentages, label=i, color='y', align="center")
        elif po.index(i) == 3:
            plot.bar(x_pos, percentages, label=i, color='c', align="center")
    plot.bar(x_pos, percentages, color='r' + 'b' + 'y' + 'c', align="center")
    plot.xticks(x_pos, percentagesstr)
    plot.xlabel('Nominees')
    plot.ylabel('Vote Percentages')
    plot.legend()
    plot.savefig('CompVotePercs.pdf')
    #plot.show()
    plot.close()
#-----------------------------------------
onestens = []
def obtainHistogram(x):
    for i in x :
        if len(str(i)) == 1:
            x[x.index(i)]='0'+str(i)
    digits = []
    for i in x :
        i = str(i)
        digits.append(i[-2])
        digits.append(i[-1])
    freqq = []
    for i in range(10):
        freqq.append(digits.count(str(i))/(2*len(x)))
    return freqq
freq = obtainHistogram(retrieveData(sys.argv[1], oo))
#print(teller)
def plotHistogram():
    xx = freq
    x_axis = [i for i in range(10)]
    idealline = [0.1 for i in range(10)]
    plot.plot(x_axis, idealline, '--', linewidth=1, color='g', label='Mean')
    plot.plot(x_axis, freq, color='r', label='Digit Dist.')
    plot.xlabel('Digits')
    plot.ylabel('Distribution')
    plot.title('Histogram of least sign. digits')
    plot.legend()
    plot.savefig('Histogram.pdf')
    #plot.show()
    plot.close()
def plotHistogramWithSample():
    x_axis = [i for i in range(10)]
    idealline = [0.1 for i in range(10)]
    random1 = obtainHistogram([random.randint(0, 100) for i in range(10)])
    random2 = obtainHistogram([random.randint(0, 100) for i in range(50)])
    random3 = obtainHistogram([random.randint(0, 100) for i in range(100)])
    random4 = obtainHistogram([random.randint(0, 100) for i in range(1000)])
    random5 = obtainHistogram([random.randint(0, 100) for i in range(10000)])
    #print(random1)------------------ sample 1 with numbers that randomly generated
    plot.plot(x_axis, idealline, '--', linewidth=1, color='g', label='Mean')
    plot.plot(x_axis, random1, linewidth=1, color='r', label='Digit Dist.')
    plot.title('Histogram of least sign. digits - Sample:1')
    plot.xlabel('Digits')
    plot.ylabel('Distribution')
    plot.legend(loc='upper left')
    plot.savefig('HistogramofSample1.pdf')
    plot.close()
    #plot.show()--------------------- sample 2 with numbers that randomly generated
    plot.plot(x_axis, idealline, '--', linewidth=1, color='g', label='Mean')
    plot.plot(x_axis, random2, linewidth=1, color='b', label='Digit Dist.')
    plot.title('Histogram of least sign. digits - Sample:2')
    plot.xlabel('Digits')
    plot.ylabel('Distribution')
    plot.legend(loc='upper left')
    plot.savefig('HistogramofSample2.pdf')
    plot.close()
    #plot.show()--------------------- sample 3 with numbers that randomly generated
    plot.plot(x_axis, idealline, '--', linewidth=1, color='g', label='Mean')
    plot.plot(x_axis, random3, linewidth=1, color='y', label='Digit Dist.')
    plot.title('Histogram of least sign. digits - Sample:3')
    plot.xlabel('Digits')
    plot.ylabel('Distribution')
    plot.legend(loc='upper left')
    plot.savefig('HistogramofSample3.pdf')
    plot.close()
    #plot.show()--------------------- sample 4 with numbers that randomly generated
    plot.plot(x_axis, idealline, '--', linewidth=1, color='g', label='Mean')
    plot.plot(x_axis, random4, linewidth=1, color='c', label='Digit Dist.')
    plot.title('Histogram of least sign. digits - Sample:4')
    plot.xlabel('Digits')
    plot.ylabel('Distribution')
    plot.legend(loc='upper left')
    plot.savefig('HistogramofSample4.pdf')
    plot.close()
    #plot.show()--------------------- sample 5 with numbers that randomly generated
    plot.plot(x_axis, idealline, '--', linewidth=1, color='g', label='Mean')
    plot.plot(x_axis, random5, linewidth=1, color='m', label='Digit Dist.')
    plot.title('Histogram of least sign. digits - Sample:5')
    plot.xlabel('Digits')
    plot.ylabel('Distribution')
    plot.legend(loc='upper left')
    plot.savefig('HistogramofSample5.pdf')
    plot.close()
    #plot.show()----------------------
def calculateMSE(x,y):
    total=0
    for i in range(len(x)):
        total = total + (x[i] - y[i])**2
    return total
idealline1 = [0.1 for i in range(len(freq))]
currentMSE = calculateMSE(freq, idealline1)
#print(retrieveData("ElectionUSA2012.csv", ["Obama", "Romney", "Johnson", "Stein"]))

ddd = []
def compareMSEs():
    total1111 = 0
    total2222 = 0
    for i in range(10000):
        a = [random.randint(0,101) for i in range(len(firstlist))]
        t1 = obtainHistogram(a)
        t2 = calculateMSE(t1, idealline1)
        if t2 >= currentMSE:
            total1111 += 1
        else:
            total2222 += 1
    ddd.append(total1111)
    ddd.append(total2222)
    return ddd
kkk = compareMSEs()
print("MSE value of 2012 USA Election is {}".format(currentMSE))
outfile2.write("MSE value of 2012 USA Election is {}\n".format(currentMSE))
print("The number of MSE of random samples which are larger than or equal to USA election MSE is {}".format(kkk[0]))
outfile2.write("The number of MSE of random samples which are larger than or equal to USA election MSE is {}\n".format(kkk[0]))
print("The number of MSE of random samples which are smaller than USA election MSE is {}".format(kkk[1]))
outfile2.write("The number of MSE of random samples which are smaller than USA election MSE is {}\n".format(kkk[1]))
print("2012 USA election rejection level p is {}".format(kkk[1]/10000))
outfile2.write("2012 USA election rejection level p is {}\n".format(kkk[1]/10000))
if kkk[0]/10000 < 0.05:
    print("Finding: We reject the null hypothesis at the p= {} level".format(kkk[1]/10000))
    outfile2.write("Finding: We reject the null hypothesis at the p= {} level".format(kkk[1]/10000))
    #to reject the null hypothesis you first need to obtain p value which is smaller than significance level(0.05)
    #buradan anladigim, eger null hypothesisi reddetmek istiyorsak ilk once p valuemiz 0.05'ten kücük olmali
else:
    print("Finding: There is no statistical evidence to reject null hypothesis")
    outfile2.write("Finding: There is no statistical evidence to reject null hypothesis")
DispBarPlot()
compareVoteonBar()
plotHistogram()
plotHistogramWithSample()
file.close()
outfile.close()
outfile2.close()











