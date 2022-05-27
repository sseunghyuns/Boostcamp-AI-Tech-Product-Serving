from typing import Optional
from fastapi import FastAPI
import uvicorn

app = FastAPI()

fake_itmes = [{'item_name': 'baz'}, {'item_name': 'bar'}, {'item_name': 'boo'}]

@app.get('/items/{item_id}')
def read_items(item_id: str, q: Optional[str] = None):
    if q: 
        return {'item_id': item_id, "q":q}
    return {"item_id": item_id}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
