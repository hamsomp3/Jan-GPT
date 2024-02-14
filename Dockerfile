FROM python:3.11
RUN pip install uvicorn==0.27.1
RUN pip install chromadb==0.4.18 
RUN pip install fastapi==0.109.2
COPY server.py .
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
