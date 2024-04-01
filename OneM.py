import efinance as ef
import time
from datetime import datetime
# stock_code = '微软'
# freq = '1'
# df = ef.stock.get_quote_history(stock_code)
# df.to_csv(f'{stock_code}.csv', encoding='utf-8-sig, index=None')
# print(f'股票:{stock_code}的行情数据已存储到文件：{stock_code}.csv中！')
stock_code = '600518'
freq = 1
status = {stock_code: 0}
while 1:
    df = ef.stock.get_quote_history(stock_code,klt=freq)
    now = str(datetime.today()).split('.')[0]
    df.to_csv(f'{stock_code}.csv', encoding='utf-8-sig', index=None)
    print(f'已在{now}，将股票:{stock_code}的行情数据已存储到文件：{stock_code}.csv中！')
    if len(df) == status[stock_code]:
        print(f'{stock_code}已收盘')
        break
    status[stock_code] = len(stock_code)
    print('暂停60秒')
    time.sleep(60)
    print('-'*10)
print('全部股票已收盘')

