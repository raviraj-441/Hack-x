from fastapi import FastAPI
from routers import auth, user, menu, order, gamification

app = FastAPI(title="Café Gamified Ordering API")

# Include our routers with prefixes and tags
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(menu.router, prefix="/menu", tags=["menu"])
app.include_router(order.router, prefix="/orders", tags=["orders"])
app.include_router(gamification.router, prefix="/gamification", tags=["gamification"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
