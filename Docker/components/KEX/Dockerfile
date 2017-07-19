FROM python:2.7
MAINTAINER D.Thatmann d.thatmann@tu-berlin.de
RUN apt -y update && apt install -y python-pip maven libffi-dev git unzip pwgen vim && pip install flask_mail flask_oidc Flask-SQLAlchemy==1.0 Flask-Login flask-bootstrap flask-user requests Flask-OAuthlib beautifulsoup4 cssutils html5lib
RUN mkdir Entrance-PJ 
WORKDIR /Entrance-PJ
RUN git clone https://github.com/SNET-Entrance/Entrance-KEX 
WORKDIR /Entrance-PJ/Entrance-KEX/src
RUN python setup.py install && python setup-database.py install
#ENTRYPOINT ["python"] 
CMD ["python", "./run.py"]
expose 20001

#ADD ./scripts/start.sh /start.sh
#RUN chmod 755 /start.sh
#CMD ["/bin/bash", "/start.sh"]
