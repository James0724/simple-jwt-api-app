FROM public.ecr.aws/sam/build-python3.7:latest
WORKDIR /app
ADD . .
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "main:APP"]
