from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI(title='Open Table Project')
templates = Jinja2Templates(directory='templates')

@app.get('/', response_class=HTMLResponse)
async def home(request: Request): return templates.TemplateResponse(request=request, name='home.html', context={'title':'Home'})
@app.get('/programs', response_class=HTMLResponse)
async def programs(request: Request): return templates.TemplateResponse(request=request, name='programs.html', context={'title':'Programs'})
@app.get('/impact', response_class=HTMLResponse)
async def impact(request: Request): return templates.TemplateResponse(request=request, name='impact.html', context={'title':'Impact'})
@app.get('/get-involved', response_class=HTMLResponse)
async def get_involved(request: Request): return templates.TemplateResponse(request=request, name='get-involved.html', context={'title':'Get Involved'})
@app.get('/donate', response_class=HTMLResponse)
async def donate(request: Request): return templates.TemplateResponse(request=request, name='donate.html', context={'title':'Donate'})
