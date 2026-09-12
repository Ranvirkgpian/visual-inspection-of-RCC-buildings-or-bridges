# RCC Visual Inspection Dashboard

## AIML/SIS Tutorial 1 – Vibe Coding Assignment

A Python-based web application for recording and summarising visual inspection observations of RCC structures.

## Technology Used

* Python
* Streamlit
* Pandas

## Features

* Structure information entry
* RCC building/bridge selection
* Floor/level selection
* Component selection
* Defect classification
* Severity/condition classification
* Recommended action
* Inspection remarks
* Multiple observations
* Sample test cases
* Visual condition index
* Inspection summary
* CSV export

## Project Structure

```text
RCC-Visual-Inspection/
│
├── app.py
├── requirements.txt
└── README.md
```

## How to Run Locally

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

The application will open in the browser.

## Inspection Workflow

```text
Engineering Problem
        ↓
Define Inspection Workflow
        ↓
Write AI Coding Prompt
        ↓
Generate Initial Python Application
        ↓
Test With Sample Observations
        ↓
Identify Improvements
        ↓
Add Condition Classification
        ↓
Add Summary & Recommendations
        ↓
Add CSV Export
        ↓
Final Testing
        ↓
Deploy Web Application
```

## Sample Test Cases

### Case 1 – Minor Crack

* Floor: Ground Floor
* Component: Column
* Location: Grid A-2 east face
* Defect: Cracks
* Severity: Minor
* Action: Routine Monitoring

### Case 2 – Moderate Spalling

* Floor: First Floor
* Component: Beam
* Location: Grid B-3 soffit
* Defect: Spalling
* Severity: Moderate
* Action: Repair / Maintenance Attention

### Case 3 – Corrosion Staining

* Floor: Second Floor
* Component: Column
* Location: Grid C-1 external face
* Defect: Corrosion Staining
* Severity: Moderate
* Action: Detailed Inspection / NDT Recommended

### Case 4 – Severe Leakage

* Floor: Roof
* Component: Roof Slab
* Location: NW corner
* Defect: Dampness/Leakage
* Severity: Severe
* Action: Urgent Professional Assessment

### Case 5 – Good Condition

* Floor: Ground Floor
* Component: Staircase
* Location: Central stair flight
* Defect: No Significant Visible Defect
* Severity: Good
* Action: Routine Monitoring

## Visual Condition Index

The application uses the following documentation-oriented penalty system:

| Condition | Penalty |
| --------- | ------: |
| Good      |       0 |
| Minor     |       1 |
| Moderate  |       3 |
| Severe    |       5 |

The index is calculated as:

```text
Visual Condition Index
= 100 − (Average Penalty × 20)
```

The value is limited between 0 and 100.

**Important:** This index is only a documentation/prioritisation aid. It is not a structural safety assessment.

## Vibe Coding Approach

The application was developed by converting the engineering inspection workflow into a structured software requirement and then iteratively improving the generated Python application.

The development process included:

1. Understanding the RCC visual inspection problem.
2. Defining required inspection fields.
3. Creating the initial Python/Streamlit application.
4. Testing the application using sample observations.
5. Adding condition classification.
6. Adding summary statistics.
7. Adding recommendations.
8. Adding CSV export.
9. Testing the final workflow.

## Limitations

This application is intended for educational demonstration and preliminary visual inspection documentation.

It does not replace:

* Structural engineering assessment
* Non-destructive testing
* Detailed condition surveys
* Structural analysis
* Professional engineering judgement

## Future Improvements

Possible future versions could include:

* Uploading inspection photographs
* Automatic crack detection using computer vision
* Defect location mapping
* Inspection history
* Search and filtering
* Statistical dashboards
* PDF report generation
* Database storage using Supabase
* User authentication
* AI-assisted defect classification

## Author

**Ranvir Kumar**

AIML/SIS Tutorial 1 – Vibe Coding Assignment
