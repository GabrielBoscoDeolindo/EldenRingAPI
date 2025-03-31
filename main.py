from fastapi import FastAPI, HTTPException, status, Depends, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import List
from sqlmodel import Session, select, create_engine
from models import Boss, create_db_and_tables


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

async def lifespan(app: FastAPI):
    create_db_and_tables(engine)
    yield


app = FastAPI(lifespan=lifespan)
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_model=List[Boss])
async def get_bosses(request: Request, session: Session = Depends(get_session)):
    bosses = session.exec(select(Boss)).all()
    return templates.TemplateResponse("index.html", {"request": request, "bosses": bosses})


@app.get("/{boss_id}")
async def get_boss(request: Request, boss_id: int, session: Session = Depends(get_session)):
    boss = session.get(Boss, boss_id)
    if not boss:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe boss com o ID {boss_id}")
    return templates.TemplateResponse("boss.html", {"request": request, "boss": boss})

@app.post("/", response_model=Boss)
async def create_boss(boss: Boss, session: Session = Depends(get_session)):
    session.add(boss)
    session.commit()
    session.refresh(boss)
    return boss

@app.get("/{boss_id}", response_model=Boss)
async def get_boss(boss_id: int, session: Session = Depends(get_session)):
    boss = session.get(Boss, boss_id)
    if not boss:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe boss com o ID {boss_id}")
    return boss

    


