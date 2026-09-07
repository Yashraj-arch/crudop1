from fastapi import FastAPI
from routes import employee_router, salary_router

app = FastAPI(title="emp mng api")

app.include_router(employee_router)
app.include_router(salary_router)


@app.get("/")
def root():
    return {"message": "api is running"}


