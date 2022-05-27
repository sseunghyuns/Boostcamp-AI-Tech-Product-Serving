from fastapi import FastAPI
import uvicorn

app = FastAPI()

fake_itmes = [{'item_name': 'baz'}, {'item_name': 'bar'}, {'item_name': 'boo'}]

@app.get("/items/")
def read_items(skip: int=0, limit: int=10):
    return fake_itmes[skip:limit]

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
