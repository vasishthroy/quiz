FROM python:3
RUN mkdir -p ./src
WORKDIR ./src

COPY quiz.json .
COPY . .
CMD [ "python", "quiz.py" ]
# ENTRYPOINT [ "python3" ] 
