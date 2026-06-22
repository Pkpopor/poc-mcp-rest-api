from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/api/sales")
def get_sales_data():
    # อ่านข้อมูลจาก CSV
    df = pd.read_csv("sample_sales_data.csv")
    # ส่งข้อมูลกลับไปเป็น JSON (List)
    return df.to_dict(orient="records")