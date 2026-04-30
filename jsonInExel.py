import pandas as pd
import json
import re

with open('db.json', 'r', encoding='utf-8') as f:
    content = f.read()
    fixed_content = content.replace('\\', '\\\\')
    data = json.loads(fixed_content)

df = pd.DataFrame.from_dict(data, orient='index')
df.reset_index(inplace=True)
df.rename(columns={'index': 'file'}, inplace=True)
def clean_for_excel(val):
    if isinstance(val, str):
        return re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F]', '', val)
    return val

df = df.map(clean_for_excel)
df.to_excel('statistics.xlsx', index=False, engine='openpyxl')
print("сделано")