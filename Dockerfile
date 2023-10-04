FROM python:3.11
# RUN python -m venv .
# RUN source ./bin/activate.fish
WORKDIR /code
COPY . .
RUN python -m pip install --no-cache-dir -r requirements.txt
EXPOSE 8000