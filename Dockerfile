FROM python:3.12-alpine
WORKDIR /app
COPY app/ /app/
RUN echo "Building student app image"
EXPOSE 8080
CMD ["python", "app.py"]
