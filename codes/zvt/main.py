from zvt.domain import *

# 国内
Stock.record_data(provider="em")
df = Stock.query_data(provider="em", index='code')
print(df)

# 美股
# Stockus

# 港股
# Stockhk

# 预测

from zvt.domain import Stock, Stock1dHfqKdata
from zvt.ml import MaStockMLMachine

Stock.record_data(provider="em")
entity_ids = ["stock_sz_000001", "stock_sh_601318"]
Stock1dHfqKdata.record_data(provider="em", entity_ids=entity_ids)
machine = MaStockMLMachine(entity_ids=["stock_sz_000001"], data_provider="em")
machine.train()
machine.predict()
machine.draw_result(entity_id="stock_sz_000001")
