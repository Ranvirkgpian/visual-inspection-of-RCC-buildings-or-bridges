# RCC Visual Inspection Application

## Vibe Coding Assignment – Tutorial 1

A simple web-based application for recording and summarising visual inspection observations of a **G+2 RCC residential building**.

The application was developed using the Vibe Coding approach:

**Engineering Idea → Prompt → Initial Program → Testing → Modification → Improvement**

---

## Project Objective

The objective of this application is to provide a simple digital interface for systematically recording visible conditions observed during a visual inspection of an RCC structure.

The application allows the user to:

* Enter basic structure information
* Select the floor/location
* Select an RCC structural component
* Record the observation location
* Select the visible defect
* Classify severity/condition
* Add remarks
* Select a recommended action
* Record multiple observations
* View an overall condition summary
* Export observations as CSV
* Print or save the inspection information as PDF

---

## Structure Used

**Structure Type:** G+2 RCC Residential Building

The application includes common RCC components such as:

* Columns
* Beams
* Floor slabs
* Roof slab
* Staircase
* Balcony/projection
* Masonry wall/interface
* Foundation/plinth
* External RCC surfaces

---

## Defect Categories

The application provides the following visible defect categories:

* Cracks
* Spalling
* Exposed reinforcement
* Corrosion staining
* Dampness/leakage
* Honeycombing
* Deformation
* Surface deterioration
* No significant visible defect
* Other

---

## Condition Classification

Each observation can be classified as:

| Condition | Meaning                                                             |
| --------- | ------------------------------------------------------------------- |
| Good      | No significant visible deterioration                                |
| Minor     | Minor visible deterioration requiring monitoring                    |
| Moderate  | Deterioration requiring maintenance/inspection attention            |
| Severe    | Significant visible deterioration requiring professional assessment |

---

## Condition Index

The application provides a simple visual condition index to help prioritise recorded observations.

The scoring used is:

* Good = 0 penalty
* Minor = 1 penalty
* Moderate = 3 penalty
* Severe = 5 penalty

The displayed index is intended only as a **documentation and prioritisation aid**.

It is **not a structural safety assessment** and must not be interpreted as proof that a structure is safe or unsafe.

---

## Sample Inspection Cases

The application includes sample observations covering:

1. Minor cracking in a column
2. Moderate spalling in a beam
3. Moderate corrosion staining in a column
4. Severe dampness/leakage in a roof slab
5. Good condition staircase

These sample cases can be loaded using the **Load Sample Cases** button.

---

## How to Run

No installation is required.

### Method 1 – Local Computer

1. Download or clone this repository.
2. Open `index.html`.
3. The application will open in a web browser.
4. Enter inspection observations.
5. Use **Add Observation** to record each observation.

### Method 2 – GitHub Pages

The application can be hosted using GitHub Pages.

1. Upload `index.html` and `README.md` to a GitHub repository.
2. Open the repository.
3. Go to **Settings → Pages**.
4. Select the main branch as the deployment source.
5. Save the settings.
6. GitHub will provide a public website URL.

---

## Project Structure

```text
RCC-Visual-Inspection/
│
├── index.html
│
└── README.md
```

---

## Vibe Coding Workflow

```text
Engineering Problem
        ↓
Define Inspection Workflow
        ↓
Write AI Coding Prompt
        ↓
Generate Initial Web Application
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
Deploy Using GitHub Pages
```

---

## Important Limitation

This application is designed for **visual inspection documentation**.

It does not:

* Perform structural analysis
* Calculate structural capacity
* Diagnose structural failure
* Replace an engineer's professional assessment
* Automatically determine structural safety
* Replace detailed inspection or NDT

Where serious deterioration is observed, a qualified structural professional should carry out the appropriate detailed assessment.

---

## Technologies Used

* HTML5
* CSS3
* JavaScript
* Browser-based local application
* GitHub Pages for deployment

No external libraries are required.

---

## Future Improvements

Possible future versions could include:

* Inspection photographs
* Image upload
* Defect location mapping
* Component-wise statistics
* Inspection history
* Search and filtering
* Automatic report generation
* Database storage using Supabase
* User authentication
* Computer-vision-based defect detection
* PDF inspection report generation

---

## Author

**Student Project – AIML / Civil Engineering**

### Project Type

**Vibe Coding Assignment – Visual Inspection of RCC Structure**
