from fastapi import FastAPI
from daytona import Daytona

app = FastAPI()
daytona = Daytona()

@app.get("/run")
def run():
    # connect to existing running sandbox
    sandbox = daytona.get("autoapply")

    # run your pipeline (repo should already be available OR install here)
    sandbox.process.exec("python run_pipeline.py")

    # get result
    result = sandbox.fs.download_file("outputs/applications.json")

    return {"data": result}
