from fastapi import FastAPI
import pandas as pd
import uvicorn

df = pd.read_csv('./data/services2019.csv')

app = FastAPI()

@app.get('/')
def home():
    return {"this is a API service for MN CPT code details"}

@app.get('/preview')
async def preview():
    top30rows = df.head(30)
    result = top30rows.to_json(orient="records")
    return result 

@app.get('/sex/{value}')
async def cptcode(value):
    print ('value: ', value)
    filtered = df[df['sex'] == value]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else: 
        return filtered.to_json(orient="records")

@app.get('/sex/{value}/county_code/{value2}')
async def cptcode2(value, value2):
    print ('value: ', value)
    filtered = df[df['sex'] == value]
    filtered2 = filtered[filtered['county_code'] == value2]
    if len(filtered2) <= 0:
        return 'There is nothing here'
    else: 
        return filtered2.to_json(orient="records")  

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 