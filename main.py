import streamlit as st
import numpy as np
import pandas as pd

st.title("Streamlit 超入門")

st.write("dataflame")

df = pd.DataFrame({
    "１列目":[1, 2, 3, 4],
    "２列目":[2, 30, 4, 5]
})

st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as nu
import pandas as pd
```
"""