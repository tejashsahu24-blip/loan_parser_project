@echo off

REM Create main project folder
mkdir loan_parser_project

REM Move into project folder
cd loan_parser_project

REM Create files
type nul > main.py
type nul > parser.py
type nul > schemas.py
type nul > requirements.txt

REM Create folders
mkdir agreements
mkdir output
mkdir venv

REM Create sample PDF files
type nul > agreements\loan1.pdf
type nul > agreements\loan2.pdf

REM Create sample JSON output file
type nul > output\loan1.json

echo.
echo Project structure created successfully!
pause