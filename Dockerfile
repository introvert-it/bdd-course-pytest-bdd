FROM python:3

WORKDIR /jenkins

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
