
from line_notify import LineNotify
from twse import get_twse_trade


# f = open('token.txt', 'r')
# token = f.readline().strip()
notify = LineNotify("Sy9rJxszlzspDGHBZsarWuA1NuDqSLo6dWkZ09dwxat")

def send_data():
    result = get_twse_trade()
    print(result)
    print("-------------")

    if result[0] == 404:
        notify.send(result[1])
        pass
    elif result[0] == 200:
        notify.send(result[1] + "三大法人買賣金額統計表", image_path='./resources/'+result[1]+'.png')
        return result[0]
    else:
        pass

if __name__ == '__main__':
    send_data()

