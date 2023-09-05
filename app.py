from db_helper import DatabaseWrapper
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

import uvicorn
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/criteria_search/search_api_e", response_class=HTMLResponse)
async def search_api_e_c(request: Request):
    return templates.TemplateResponse("criteria_search_api.html", {"request": request})


@app.get("/criteria_search/search_mashup_e", response_class=HTMLResponse)
async def search_mashup_e_c(request: Request):
    return templates.TemplateResponse("criteria_search_mashup.html", {"request": request})


@app.get("/keyword_search/search_api_e", response_class=HTMLResponse)
async def search_api_e_k(request: Request):
    return templates.TemplateResponse("keyword_search_api.html", {"request": request})


@app.get("/keyword_search/search_mashup_e", response_class=HTMLResponse)
async def search_mashup_e_k(request: Request):
    return templates.TemplateResponse("keyword_search_mashup.html", {"request": request})


@app.get("/keyword_search/search_api")
async def search_api_by_keyword(request: Request):

    database_wrapper = DatabaseWrapper()
    search_string = request.query_params.get("user_input")
    output_df = database_wrapper.search_apis_by_keywords(search_string)
    table_data = output_df.to_html(index=False)
    return templates.TemplateResponse("search_results.html", {"request": request, "table": table_data})


@app.get("/keyword_search/search_mashup")
async def search_mashup_by_keyword(request: Request):
    database_wrapper = DatabaseWrapper()
    search_string = request.query_params.get("user_input")
    output_df = database_wrapper.search_mashup_by_keywords(search_string)
    table_data = output_df.to_html(index=False)
    return templates.TemplateResponse("search_results.html", {"request": request, "table": table_data})


@app.get("/criteria_search/search_api")
async def search_api_by_criteria(request: Request):
    database_wrapper = DatabaseWrapper()
    output_df = database_wrapper.search_apis_by_criteria(request.query_params.items())
    table_data = output_df.to_html(index=False, classes="table")
    return templates.TemplateResponse("search_results.html", {"request": request, "table": table_data})


@app.get("/criteria_search/search_mashup")
async def search_mashup_by_criteria(request: Request):
    database_wrapper = DatabaseWrapper()
    output_df = database_wrapper.search_mashup_by_criteria(request.query_params)
    table_data = output_df.to_html(index=False, classes="table")
    return templates.TemplateResponse("search_results.html", {"request": request, "table": table_data})

if __name__ == '__main__':
    uvicorn.run(app)
