FROM python:3-alpine3.15
ENV flag="bi0s{FuZz1n9_15_fun}"
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD python ./main.py
EXPOSE 3000