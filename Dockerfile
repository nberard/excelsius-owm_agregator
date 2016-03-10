FROM ubuntu:latest
#setup locale for root user to handle special chars
RUN locale-gen fr_FR.UTF-8
ENV LANG fr_FR.UTF-8
ENV LANGUAGE fr_FR:fr
ENV LC_ALL fr_FR.UTF-8
#copy it to environment file so that cron uses it
RUN echo "LANG=$LANG" >> /etc/environment
#update and install python
RUN apt-get update
RUN apt-get install -y python3 python3-pip
COPY . /opt/owm_agregator
WORKDIR /opt/owm_agregator
#install python requirements
RUN pip3 install -r requirements.txt
#setup crontab
ADD crontab /etc/cron.d/owm_agregator-cron
RUN chmod 0644 /etc/cron.d/owm_agregator-cron
RUN touch /var/log/cron.log
CMD cron && tail -f /var/log/cron.log