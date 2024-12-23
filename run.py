# run.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="10.150.150.177",
        port=8000,
        reload=True
    )
