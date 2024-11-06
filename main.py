from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.gzip import GZipMiddleware

from _math.solver import do_math

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(GZipMiddleware)
templates = Jinja2Templates(directory="templates")


@app.get("/")
def main(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/calculus-1")
def calculus(request: Request):
    equation, rs = do_math()

    return templates.TemplateResponse(
        request=request,
        name="calculus.html",
        context={"equation": equation, "roots": rs},
    )
