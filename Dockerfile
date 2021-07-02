FROM centos

RUN yum update -y
RUN yum install python36 -y 

RUN mkdir /app

COPY . /app

WORKDIR /app

CMD ["python3", "agent.py"]
