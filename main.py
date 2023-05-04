from fastapi import FastAPI
import pandas as pd
import uvicorn

df = pd.read_csv('./data/services2019.csv')

app = FastAPI()

@app.get("/")
async def home():
    return {"this is a API service for MN CPT code details"}

@app.route('/preview', methods=["GET"])
def preview():
    top10rows = df.head(1)
    result = top10rows.to_json(orient="records")
    return result

@app.route('/cpt/<value>', methods=['GET'])
def icdcode(value):
    print('value: ', value)
    filtered = df[df['svc_code'] == value]
    if len(filtered) <= 0:
        return 'There is nothing here'
    else: 
        return filtered.to_json(orient="records")

@app.route('/icd/<value>/sex/<value2>')
def icdcode2(value, value2):
    filtered = df[df['svc_code'] == value]
    filtered2 = filtered[filtered['sex'] == value2]
    if len(filtered2) <= 0:
        return 'There is nothing here'
    else: 
        return filtered2.to_json(orient="records")  

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 