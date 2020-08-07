FROM python:3.8-rc
LABEL MAINTAINER=Lu
COPY voice_backend /voice_backend
RUN pip install --upgrade pip; \
	pip install requests jieba django
EXPOSE 8000
WORKDIR /voice_backend
CMD ["python", "manage.py", "runserver", "0:8000"]
