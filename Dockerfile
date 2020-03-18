FROM python:3
COPY . /
RUN pip install pytest allure-pytest
CMD ["pytest", "--clean-alluredir", "--alluredir=/allure_report", "/test_gmail.py" , "-s",  "-v"]