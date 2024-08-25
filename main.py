import os
import uuid
import requests
import datetime
from dotenv import load_dotenv
import telegram_message as tm


if __name__ == '__main__':
    load_dotenv()
    _LANGSMITH_API_KEY:str = os.getenv('LANGCHAIN_API_KEY')


    run_id = str(uuid.uuid4())

    res = requests.post(
        f"{os.environ['LANGCHAIN_ENDPOINT']}/runs",
        json={
            "id": run_id,
            "name": "MyFirstRun",
            "run_type": "chain",
            "start_time": datetime.datetime.now(datetime.UTC).isoformat(),
            "inputs": {"text": "Foo"},
        },
        headers={"x-api-key": _LANGSMITH_API_KEY},
    )

    # ... do some work ...

    requests.patch(
        f"{os.environ['LANGCHAIN_ENDPOINT']}/runs/{run_id}",
        json={
            "outputs": {"my_output": "Bar"},
            "end_time": datetime.datetime.now(datetime.UTC).isoformat(),
        },
        headers={"x-api-key": _LANGSMITH_API_KEY},
    )

