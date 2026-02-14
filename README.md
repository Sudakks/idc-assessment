# Candidate Assessment Report



## PART 1: DEVELOPMENT ENVIRONMENT SETUP

- **How to build and run this Docker**

```bash
cd part1_docker
docker build -t env-test .
docker run --rm env-test
```

- **Dependencies**

```bash
pandas
requests
flask
```

- **Successful setup messages**

<img width="839" height="129" alt="image" src="https://github.com/user-attachments/assets/2c8600b3-75a4-4858-833d-c7c349dd196d" />

<br>

## PART 2: HEALTHCARE DATA INTEGRATION FRAMEWORK

- **How to run**

```bash
cd part2_data_integration
python example_usage.py
```

- **Design**

I wrap the data request and result formatting into one class, `OpenFDAClient`. Users can change the drug name in example_usage.py to get the reactions for different drugs and change the data resources (`base_url`) in this class. No extra details to take care of.  The output will be written into `sample_output.txt`.

- **Extensibility**

To support EMR data, the input should be extended to consume standardized formats. Then it could be added by replacing the file-based input with an API-driven data source, while reusing the same validation and processing logic once the data is normalized.

- **Results**

<img width="675" height="230" alt="image" src="https://github.com/user-attachments/assets/395aae40-e16c-476b-a48b-737f2e544a26" />

<br>

## PART 3: CLINICAL API ENDPOINT

- **How to run**

```bash
cd part3_api
pip install -r requirements.txt
python -m uvicorn app:app --reload #start the server
python test_api.py #test the endpoint
```

- **Design**

I chose `FastAPI` and use `BaseModel` to validate the input data. I created 2 classes `RiskAssessmentRequest` and `RiskAssessmentResponse` for standard input and output.

- **Dependencies**

```bash
fastapi
uvicorn
```

- **Results**
With 3 test cases

<img width="887" height="210" alt="image" src="https://github.com/user-attachments/assets/74ef56c8-6938-4719-ae2a-0875e745c313" />


<br>

## PART 4: INTERACTIVE FRONTEND INTERFACE

- **How to run**

Go to the `part4_frontend` directory and click the html file.

- **Design**

Assign `checkbox` and `number input` for input data and connect them with js variable using id. Update the recommendation information after judgment logic.

- **Result**

<img width="906" height="755" alt="image" src="https://github.com/user-attachments/assets/5f379b72-e917-45d5-ae7f-4ed3fc10be3c" />


## Followup Questions

1. **API Update**
Have fixed the bugs and logic in app.py, here is the results for 3 test cases.
<img width="887" height="210" alt="image" src="https://github.com/user-attachments/assets/74ef56c8-6938-4719-ae2a-0875e745c313" />

2. **OpenFDA Module**
- Explain why the current rate limit handling would not properly detect HTTP 429.


I found the pending logic is wrong. I put the `response.status_code == 429` behind the `response.status_code != 200`. If `response.status_code == 429` holds, `response.status_code != 200` should definitely hold. Then it won't go into that logic branch.
- Briefly describe how you would correct it.


Put `response.status_code == 429` as the first pending logic. I have updated it in this repo.

3. **Short Questions**
- What is the difference between HTTP 400 and HTTP 422 in FastAPI?


For HTTP 422, the request was received and parsed correctly, but the data inside violates the rules predefined in the Pydantic models. For HTTP 400, the server can’t even read the request, because the syntax of the request is invalid

- What limitation does an in-memory cache have in a multi-worker deployment?


Each worker will have their own in-memory cache, therefore, a single request will execute in each worker and waste memory.  The cache can’t sync among different workers.


