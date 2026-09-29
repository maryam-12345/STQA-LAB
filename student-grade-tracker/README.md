# Student Grade Tracker

A small Python project built for a Software Testing & Quality Assurance assignment.
It manages student scores, converts them to letter grades / GPA, and computes class statistics.

## Structure
```
src/grade_tracker/
    student.py         # Student model (validation, scores, average)
    calculator.py      # Letter grade, GPA, class average, top student
    legacy_report.py   # Intentionally smelly code for SonarQube to flag
tests/                 # pytest unit tests
sonar-project.properties
.github/workflows/sonarqube.yml
```

## Run tests
```bash
pip install -r requirements.txt
pytest --cov=src --cov-report=xml --junitxml=test-results.xml
```

## Analyze with SonarQube (local)
1. Start SonarQube: `docker run -d --name sonarqube -p 9000:9000 sonarqube:community`
2. Open http://localhost:9000 (login `admin` / `admin`, then change the password).
3. Create a project with key `student-grade-tracker` and generate a token.
4. Run the tests (above) to produce `coverage.xml`.
5. Run the scanner:
```bash
sonar-scanner -Dsonar.host.url=http://localhost:9000 -Dsonar.token=YOUR_TOKEN
```
Or with Docker:
```bash
docker run --rm --network host -v "$PWD:/usr/src" sonarsource/sonar-scanner-cli \
  -Dsonar.host.url=http://localhost:9000 -Dsonar.token=YOUR_TOKEN
```

## Notes
`legacy_report.py` deliberately contains code smells (high cognitive complexity, duplicated
logic, bare `except`, unused variable) and has no tests. Screenshot the SonarQube results
"before", refactor and add tests, then re-scan for an "after" comparison.
