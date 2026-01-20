from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def greet():
    return ("Hello, welcome to the application!")

@app.get("/health")
def health_check():
    return {"status": "ok"}