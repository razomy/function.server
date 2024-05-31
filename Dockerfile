FROM python:3.12.3-slim

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ENV PORT 8000
EXPOSE 8000

COPY . .

RUN chmod +x ./main.sh
CMD ./main.sh
