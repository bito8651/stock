import pandas as pd
import matplotlib.pyplot as plt


def read_csv(file):
    # converters那邊是告訴它Adj Close那列我要讀取成float，否則它預設會是字串
    df = pd.read_csv(file)
    df = df['Adj Close'].astype('float')  # 我只要Adj Close那列的資料
    return df.tolist()  # 轉換為python內建的list物件


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


def clac_profit(data, signal):
    pos = 0  # 持有方向
    entry = 0  # 進場價
    trades = 0  # 裝著每筆交易的損益
    for i in range(len(data)):
        if signal[i] == 1:
            if pos == 0:  # 表示目前沒有持股
                entry = data[i]  # 單純進場，紀錄成本價即可
            elif pos == -1:  # 原本持有空單，現在遇到買進訊號
                # 因為要將空單出場，換成多單
                # 要先計算此單出場的獲利
                profit = entry - data[i]  # 空單的獲利是 成本價 - 現在價格
                total  += profit
                entry = data[i]
            pos = 1  # 將持有方向設為1
        elif signal[i] == -1:
            if pos == 0:  # 表示目前沒有持股
                entry = data[i]  #那就只是單純進場，紀錄成本價即可
            elif pos == 1:  # 原本持有多單，現在遇到賣出訊號
                profit = data[i] - entry  # 空單的獲利是 成本價 - 現在價格
                total += profit
                entry = data[i]
            pos = -1  # 把持有方向設為1 

    return total * 1000  # 放大一千倍是因為每次交易都是一張股票(1000股)


def main():
    data = read_csv('data/2330.csv')
    signal = three_days(data)
    total = clac_profit(data, signal)
    print(total)

main()