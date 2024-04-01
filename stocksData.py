import json

import easyquotation
quotation = easyquotation.use('tencent')
quotation.market_snapshot(prefix=True)
a = quotation.real('00700')
a1 = quotation.stocks(['00700', '162411'])
a2 = quotation.stocks(['sh00001', 'sh00001'], prefix=True)
print(a)
print(a1)
print(a2)
# b = json.dumps(a)
# b1 = json.dumps(a1)
# b2 = json.dumps(a2)
# print(json.dumps(a))
# print(json.dumps(a1))
# print(json.dumps(a2))
# print(b.name)
