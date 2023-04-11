from fastapi import FastAPI

app = FastAPI(
    title="Social Network"
)


@app.get("/")
async def greeting_init():
    return "Hi!"
