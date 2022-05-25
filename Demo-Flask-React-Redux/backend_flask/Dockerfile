FROM  python:3.10.0-slim
RUN python -m pip install --upgrade pip
ENV PYTHONNUNBUFFERED=1
# WORKDIR /
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


ENV PORT = 5000
EXPOSE 5000
COPY . .
CMD [ "python", "app.py" ] 