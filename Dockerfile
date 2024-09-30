FROM apache/airflow:2.10.2
COPY requirments.txt .
RUN pip install -r requirments.txt