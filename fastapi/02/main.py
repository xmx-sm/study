

import uvicorn

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json

app = FastAPI()

# 挂载静态文件目录，用于存放 HTML、CSS 和 JavaScript 文件
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    # 示例数据
    data = {
        "labels": ["January", "February", "March", "April", "May", "June", "July"],
        "datasets": [
            {
                "label": "Dataset 1",
                "backgroundColor": "rgba(75,192,192,0.2)",
                "borderColor": "rgba(75,192,192,1)",
                "data": [65, 59, 80, 81, 56, 55, 40],
                "fill": False,
            },
            {
                "label": "Dataset 2",
                "backgroundColor": "rgba(153, 102, 255, 0.2)",
                "borderColor": "rgba(153, 102, 255, 1)",
                "data": [28, 48, 40, 19, 86, 27, 90],
                "fill": False,
            },
            # // 可以添加更多的数据集...
        ]
    }
    return templates.TemplateResponse("index.html", {"request": request, "data": json.dumps(data)})

if __name__ == "__main__":
    uvicorn.run(app,host="127.0.0.1",port=8000)