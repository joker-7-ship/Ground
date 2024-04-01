import efinance as ef
stock_code = '00700'
freq = 1
df = ef.stock.get_quote_history(stock_code)
print(df)
df.to_csv(f'{stock_code}.csv', encoding='utf-8-sig', index=None)
print(f'股票:{stock_code}的行情数据已存储到文件：{stock_code}.csv中！')

