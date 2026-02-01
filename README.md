# Candidate Assessment Report



<br>

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

![](C:\Users\DELL\AppData\Roaming\marktext\images\2026-01-28-20-49-56-image.png)

<br>

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

![](C:\Users\DELL\AppData\Roaming\marktext\images\2026-01-28-21-18-31-image.png)

<br>

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

![](C:\Users\DELL\AppData\Roaming\marktext\images\2026-01-28-21-29-06-image.png)

<br>

<br>

## PART 4: INTERACTIVE FRONTEND INTERFACE

- **How to run**

Go to the `part4_frontend` directory and click the html file.

- **Design**

Assign `checkbox` and `number input` for input data and connect them with js variable using id. Update the recommendation information after judgment logic.

- **Result**

<img src="file:///C:/Users/DELL/AppData/Roaming/marktext/images/2026-01-28-21-33-26-image.png" title="" alt="" width="313"><img title="" src="file:///C:/Users/DELL/AppData/Roaming/marktext/images/2026-01-28-21-35-38-image.png" alt="" width="264">

<img title="" src="file:///C:/Users/DELL/AppData/Roaming/marktext/images/2026-01-28-21-34-11-image.png" alt="" width="306"><img title="" src="file:///C:/Users/DELL/AppData/Roaming/marktext/images/2026-01-28-21-34-49-image.png" alt="" width="291">
