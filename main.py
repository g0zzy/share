from fastapi import FastAPI
from daytona import Daytona

app = FastAPI()
daytona = Daytona()

@app.post("/run")
def run():
    # create fresh sandbox
    sandbox = daytona.create({
        "snapshot": "daytonaio/sandbox:0.6.0",
        "name": "lovable-run"
    })

    # run your pipeline (repo should already be available OR install here)
    sandbox.process.exec("python run_pipeline.py")

    # get result
    result = sandbox.fs.download_file("outputs/applications.json")

    return {"data": result}
