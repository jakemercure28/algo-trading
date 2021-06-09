import sys

stockPrice = (59,55,62,63,49,48,48,49,46,47,44,48,47,47,46,46,49,48,46,44,45,46,43,35,39,42
,43,41,39,38,39,40,40,41,37,36,35,35,36,38,33,35,34,37,38,53,54,52,48,47,48,57,56,58,42,45,39,
41,47,47,46,49,48,41,41,42,43,43,46,45,48,40,51,43,52,51,47,48,44,45,42,43,49,41,53,42,43,56,59,71,102,68,
54,55,53,54,52,49,42,43,42,53,52,58,53,49,51,55,58,71,121,130,89,72,77,73,78,72,83,83,84,93,92,92,92,91,90,
90,96,69,66,62,62,63,61,67,69,71,72,73,72,72,72,78,73,78,75,76,76,76,77,79,82,84,89,93,91,99,102,155,166,121,100,92,92,93,96,91,62,63,61,67,102,143,155,166,121,100,92,92,93,96,91
,62,63,61,67,102,143,155,166,121,100,92,92,93,92,91,62,63,61,67,102,143,155,166,121,100,92,92,93,96,91,
90,87,86,67,77,74,74,78,74,71,71,67,67,64,63,68,67,64,64,61,42,41,36,36,33,37,36,31,27,27,26,26,27,26,25,
24,25,26,25,24,23,24,25,23,24,25,26,23,23,23,24,23,23,22,21,21,24,22,21,23,22,21,21)

movingAvgs = []

#ALGO accounts
cash = 10000
stockQuantity = 0
stockEquity = 0

#HODL accounts
cash2 = 10000
stockQuantity2 = 0
stockEquity2 = 0
HODL = 0

#Calculate moving AVGs over time period
day = 0
for itr in (stockPrice):
    try:
        movingAvg = (stockPrice[day-2] + stockPrice[day-1] + stockPrice[day]) / 3
        movingAvgs.append(movingAvg)
    except:
        continue

    day+=1


#BUY HOLD trading
stockQuantity2 = 16 # this applies to starting price of 59 only

stockEquity2 += stockQuantity2 * stockPrice[0]
cash2 -= stockEquity2

cash2 += stockQuantity2 * stockPrice[day-1]
stockEquity2 = 0
stockQuantity2 = 0


#ALGO tradig
day = 0
for itr in (stockPrice):

# next step, create dynamic threshold for determining order size


### large order, high fluctuation in price
    #buy order
    if (movingAvgs[day] > stockPrice[day] and movingAvgs[day] / stockPrice[day] > 1.25):
        if(cash* 100 >= stockPrice[day]):
            cash -= 100 * stockPrice[day]
            stockQuantity += 100
            stockEquity = stockQuantity * stockPrice[day]

    #sell order
    if (movingAvgs[day] < stockPrice[day] and movingAvgs[day] / stockPrice[day] < .8):
        if(stockQuantity > 100):
            cash += stockPrice[day] * 100
            stockQuantity -= 100
            stockEquity = stockPrice[day] * stockQuantity


### single order, small fluctuation in price
    #buy order
    if movingAvgs[day] > stockPrice[day]:
        if(cash >= stockPrice[day]):
            cash -= stockPrice[day]
            stockQuantity += 1
            stockEquity = stockQuantity * stockPrice[day]

    #sell order
    if movingAvgs[day] < stockPrice[day]:
        if(stockQuantity > 1):
            cash += stockPrice[day]
            stockQuantity -= 1
            stockEquity = stockPrice[day] * stockQuantity

    day+=1 # cycle though each day

#ALGO trading results
print('Cash:',cash)
print('Stock quan:', stockQuantity)
print('Stock equity:', stockEquity)
print('Algo Total:', cash + stockEquity)

#HODL trading results
print()
print('Cash 2:', cash2)
print('Stock quan 2:', stockQuantity2)
print('Stock equity 2:', stockEquity2)
print('HODL Total:', cash2 + stockEquity2)