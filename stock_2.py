def three_days(data):
    output = []
    for i in range(len(data)):
        if i < 3:
            output.append(0)
        elif data[i] > data[i-1] > data[i-2] > data[i-3]:
            output.append(1)
        elif data[i] < data[i-1] < data[i-2] < data[i-3]:
            output.append(-1)
        else:
            output.append(0)
    return output



def retrive_data():
    data = []
    data2 = []
    stock_adj_close =[]
    csvfilename = 'data/2330.csv'
    with open(csvfilename, 'r', ) as f:
        for column in f:
            s = column.strip().split(',')
            data.append(s[5])  # 只把要使用的AdjClose加入list
            del data[0]  # delete the title 'Adj Close'

        for item in data:
            stock_adj_close = data2.append(float(item))
    return stock_adj_close


def main():
    retrive_data()
main()
