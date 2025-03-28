from fastapi import FastAPI, HTTPException, status, Response, Depends
from typing import Optional, Any
from models import Boss

app = FastAPI()

bosses = {
    1: {
        "name": "Godrick",
        "title": "The Grafted",
        "location": "Stormveil Castle",
        "drop": 15000,
        "shardbearer": True
    },
    2: {
        "name": "Rennala",
        "title": "Queen of the Full Moon",
        "location": "Academy of Raya Lucaria",
        "drop": 40000,
        "shardbearer": True
    },
    3: {
        "name": "Radahn",
        "title": "Starscourge",
        "location": "Caelid",
        "drop": 70000,
        "shardbearer": True
    },
    4: {
        "name": "Rykard",
        "title": "Lord of Blasphemy",
        "location": "Volcano Manor",
        "drop": 130000,
        "shardbearer": True
    },
    5: {
        "name": "Morgott",
        "title": "Omen King",
        "location": "Leyndell Royal Capital",
        "drop": 120000,
        "shardbearer": True
    }
}

@app.get("/bosses")
async def get_bosses():
    return bosses

@app.get("/bosses/{boss_id}")
async def get_boss(boss_id: int):
    try:
        boss = bosses[boss_id]
        return boss
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"nao existe boss com o ID {boss_id}")

