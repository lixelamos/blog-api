from fastapi import FastAPI, APIRouter, HTTPException
from starlette.responses import HTMLResponse

from routes import router

app = FastAPI()

# Include routers
app.include_router(router)

# Route to display all available routes
@app.get("/", response_class=HTMLResponse)
async def main_page():
    route_info = "<h1>Available Routes:</h1>"
    for route in app.routes:
        route_info += f"<p><strong>{route.path}</strong>: {route.methods}</p>"
    return route_info

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
