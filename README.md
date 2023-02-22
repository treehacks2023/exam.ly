# Exam.ly

## About
Ever had a professor who never gave any practice exams, or are you a TA who has to spend hours coming up with and writing tests? We are here for you. As students, we have always faced the constant issues of finding material to study for and practice for upcoming exams.

Exam.ly accepts PDFs of any course content, articles, or information of any kind, and generates an entirely new set of problems to test your knowledge, using GPT-3.

## Running
1. run `pip -r install requirements.txt`
2. create `.env` file based on `.env-example`
3. run `app.py`

## Tech-stack
- Flask
- GPT3

## Acknowledgements
- GPT3 API does not accept queries above certain treshold, meaning not all queries are going to work (~4000 tokens max)
- The following repo is TreeHacks 2023 submission.
