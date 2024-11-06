from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.gzip import GZipMiddleware

from _math.generator import FuncGenerator

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(GZipMiddleware)
templates = Jinja2Templates(directory="templates")


@app.get("/")
def main(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/calculus-1")
def calculus(request: Request):
    func_generator = FuncGenerator()
    roots, poly_latex, derivative = func_generator.generate_polynomial_equation(4)

    return templates.TemplateResponse(
        request=request,
        name="calculus.html",
        context={"equation": poly_latex, "roots": roots, "derivative": derivative},
    )
