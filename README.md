# QA Analyst Technical Assessment

**Candidate:** Manuel Magayanes
**Language Used:** Python
**Completion Date:** 10/14/25

## Part 1: Functional Programming
- **Time Spent:** ~5 minutes
- **Approach:** Create a new array that would have all non-duplicate values. Then iterate through all the values in the given array and insert them into the new array if that value isn't already in the new array.

## Part 2: API Testing  
- **Time Spent:** ~15 minutes
- **Approach:** Used the requests library to make each of the desired requests. Used the json library to both display each endpoint's response and to make the POST request for the second endpoint. The data for the second endpoint's request is obtained from the user via the input() function. The necessary data for that request was determined from the given website which is the given base url.

## How to Run
### Part 1

### Go to the folder for Part 1
Go to the folder for Part 1:
```bash
cd qa-analyst-assessment/part1-functional
```

Run the Part 1 Python file:
```bash
python3 solution.py
```

### Part 2
Go to the folder for Part 2:
```bash
cd qa-analyst-assessment/part2-api-testing
```

Then create and enter the following Python virtual environment:
```bash
python3 -m venv part2venv
# Mac/Linux
source part2venv/bin/activate
# Windows
part2venv/Scripts/activate
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

Run the Part 2 Python file. You will be asked to input a Title, Body, and User ID:
```bash
python3 solution.py
```


