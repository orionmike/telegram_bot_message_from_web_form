import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from bot_message.router import router as router_message
from config import ABS_PATH

app = FastAPI()

app.include_router(router_message)
app.mount("/static", StaticFiles(directory=f"{ABS_PATH}/static"), name="static")

templates = Jinja2Templates(directory=f"{ABS_PATH}/templates")


@app.get('/', response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        "form/form.html.jinja",
        {
            'request': request,
        })


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=80, log_level="info", reload=True)
