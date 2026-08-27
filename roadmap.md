# Middle Automation QA Roadmap

## EPIC: Middle Automation QA

**Goal:** перейти від простого написання автотестів до рівня Middle Automation QA: проєктувати automation framework, приймати технічні рішення, дебажити CI, працювати з API/DB та пояснювати архітектуру.

**Орієнтовна тривалість:** 3–4 місяці.

---

## STORY 1 — Playwright + Pytest Framework

1. Multiple pages / tabs
2. expect_page()
3. Popup handling
4. Alert / Confirm / Prompt
5. File upload
6. File download
7. Keyboard actions
8. Mouse actions
9. Hover
10. Drag & Drop
11. Iframes / frames
12. Network interception
13. Request / Response interception
14. wait_for_url()
15. wait_for_load_state()
16. Auto-waiting
17. Explicit waits
18. Fixtures architecture
19. Fixture scopes
20. Fixture dependencies
21. yield / teardown
22. Parametrization
23. Custom markers: smoke / regression / slow
24. pytest --collect-only
25. pytest -m
26. pytest -k
27. Pytest hooks
28. BasePage review
29. Page Object review
30. Refactor duplicated code
31. Reusable navigation methods

### Definition of Done
- Розуміти Browser / Context / Page.
- Вміти працювати з tabs, popups, iframe та files.
- Вміти працювати з network.
- Правильно використовувати waits.
- Вміти створювати fixtures.
- Вміти використовувати parametrization та markers.
- Пояснювати архітектуру власного POM.
- Аргументувати abstraction decisions.

---

## STORY 2 — API Automation

1. HTTP fundamentals
2. GET / POST / PUT / PATCH / DELETE
3. Headers
4. Cookies
5. Query parameters
6. Path parameters
7. JSON request body
8. Response validation
9. Status codes
10. Negative API testing
11. Authentication
12. Token management
13. API fixtures
14. Reusable API client
15. Pydantic response validation
16. API test data
17. API + UI scenarios
18. API error handling

### Definition of Done
- Створити API client.
- Створити pytest API tests.
- Реалізувати authentication.
- Реалізувати response validation.
- Реалізувати negative tests.
- Інтегрувати API tests з Allure та CI.

---

## STORY 3 — SQL + Database Testing

1. SELECT
2. WHERE
3. ORDER BY
4. GROUP BY
5. HAVING
6. INNER JOIN
7. LEFT JOIN
8. Multiple JOINs
9. Subqueries
10. CTE
11. Aggregations
12. INSERT / UPDATE / DELETE
13. Transactions
14. Indexes — basics
15. DB connection from Python
16. DB fixtures
17. Validate API result in DB
18. Validate UI result in DB

### Final practical scenario
`POST API -> Database -> SELECT -> UI -> Allure`

---

## STORY 4 — Framework Architecture & Refactoring

1. Review project structure
2. Define responsibilities of BasePage
3. Page Objects boundaries
4. Test layer vs page layer
5. Test data separation
6. Configuration management
7. Environment variables
8. API layer architecture
9. Utils / helpers
10. Dependency Injection
11. Composition vs inheritance
12. SOLID
13. DRY
14. KISS
15. YAGNI
16. Good abstraction vs overengineering
17. Refactor existing framework
18. Code review of own framework

### Definition of Done
Я можу пояснити, за що відповідає кожен layer / class / module і чому конкретне архітектурне рішення було прийнято.

---

## STORY 5 — CI/CD Advanced

1. GitHub Actions basics
2. Jobs
3. Steps
4. needs
5. Conditions
6. if: always()
7. Secrets
8. Caching
9. Artifacts
10. Matrix strategy
11. Scheduled runs
12. PR workflow
13. Smoke on PR
14. Regression on main
15. Nightly regression
16. Browser matrix
17. CI failure debugging
18. Allure history
19. Allure trends

### Final CI flow
`Pull Request -> Ruff -> Smoke -> Allure -> Merge`

`main -> Regression`

`Nightly -> Full Regression`

---

## STORY 6 — Docker

1. Docker concepts
2. Images
3. Containers
4. Dockerfile
5. Build image
6. Run container
7. Environment variables
8. Volumes
9. Networks
10. Docker Compose
11. Run pytest in container
12. Playwright in Docker
13. Docker + GitHub Actions

### Definition of Done
- Розуміти Image vs Container vs VM.
- Самостійно запускати automation framework у Docker.
- Інтегрувати Docker з CI.

---

## STORY 7 — Real-world Integrations

1. TestRail concepts
2. TestRail API
3. Map pytest -> TestRail case
4. Update test result automatically
5. Allure -> TestRail links
6. Jira concepts
7. Jira API basics
8. Link automation test -> issue
9. CI -> TestRail results
10. CI -> Allure
11. Secrets for integrations
12. Handle API failures

---

## STORY 8 — Middle QA Interview + System Thinking

1. Playwright interview questions
2. pytest interview questions
3. Python interview questions
4. API testing interview
5. SQL interview
6. CI/CD interview
7. Git interview
8. Automation architecture
9. Test Pyramid
10. Test strategy
11. Risk-based testing
12. Flaky tests
13. Debugging scenarios
14. Parallel execution problems
15. Test isolation
16. Framework design exercise
17. Mock interview
18. Presentation of GitHub project

---

# PARALLEL STORY — Python Advanced

1. OOP
2. Classes / inheritance
3. Composition
4. Decorators
5. Generators
6. Context managers
7. Exceptions
8. Dataclasses
9. Type hints
10. Protocol
11. Enum
12. property
13. classmethod / staticmethod
14. SOLID
15. Design Patterns
16. Dependency Injection
17. Clean Code

---

# PARALLEL STORY — Test Engineering

1. Test Pyramid
2. Test strategy
3. Test coverage
4. Equivalence Partitioning
5. Boundary Value Analysis
6. Negative testing
7. Risk-based testing
8. Test isolation
9. Test data management
10. Mocking vs Stubbing
11. Contract testing
12. Integration testing
13. E2E testing
14. Flaky tests
15. Test maintainability
16. Test execution optimization

---

# PARALLEL STORY — Git / Engineering Workflow

1. Branches
2. Commit
3. Push
4. Merge
5. Pull Request
6. Code Review
7. Rebase
8. Conflict resolution
9. Cherry-pick
10. Revert
11. Stash
12. Bisect

---

# Правило роботи над кожною Task

1. Теорія
2. Реалізація у власному repository
3. Локальний запуск
4. Перевірка / debugging
5. Allure, якщо це test-related task
6. CI
7. Аналіз результату
8. Коротко пояснити, чому рішення зроблено саме так

---

# Definition of Done — весь Roadmap

- Самостійно проєктувати automation framework.
- Пояснити архітектуру власного framework.
- Писати стабільні Playwright UI tests.
- Писати API automation.
- Перевіряти дані через SQL / DB.
- Працювати з pytest fixtures та parametrization.
- Працювати з CI/CD.
- Дебажити failures у CI.
- Працювати з Docker.
- Інтегрувати automation з Allure / TestRail / Jira.
- Розуміти test strategy та risk-based testing.
- Пояснювати технічні рішення на Middle QA interview.
- Захистити власний GitHub automation project як portfolio project.

## Головний принцип

Ми не просто «проходимо теми».

Кожна task повинна перетворюватися на практичний engineering skill:

`Тема -> Теорія -> Реалізація -> Refactoring -> Test -> CI -> Аналіз -> Пояснення рішення`

**Ціль: Python Automation QA -> Middle Automation QA.**
