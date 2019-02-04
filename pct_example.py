import pandas as pd
f = pd.Series([10, 20, 85])

print(f.pct_change()*100)