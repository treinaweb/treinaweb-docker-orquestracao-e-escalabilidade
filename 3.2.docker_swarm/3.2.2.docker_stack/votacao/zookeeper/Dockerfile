FROM centos

# Set default path
WORKDIR /opt

# Install wget
RUN yum install -y wget

# Install Java
RUN curl -L -C - -b "oraclelicense=accept-securebackup-cookie" -O 'http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.tar.gz' && \
  tar -xvzf jdk-8u131-linux-x64.tar.gz && \
  rm -f jdk-8u131-linux-x64.tar.gz && \
  mkdir /usr/jdk && \
  mv jdk1.8.0_131 /usr/jdk

# Set Java environment 
ENV JAVA_HOME /usr/jdk/jdk1.8.0_131 
ENV PATH=$PATH:$JAVA_HOME/bin

# Install Zookeeper
RUN wget https://www-eu.apache.org/dist/zookeeper/zookeeper-3.4.14/zookeeper-3.4.14.tar.gz && \
  tar -xvzf zookeeper-3.4.14.tar.gz && \
  cd zookeeper-3.4.14 && \
  mkdir data && \
  echo -e "tickTime=2000 \ndataDir=/path/to/zookeeper/data \nclientPort=2181 \ninitLimit=5 \nsyncLimit=2" >> conf/zoo.cfg

# Start Zookeeper
CMD ["/opt/zookeeper-3.4.14/bin/zkServer.sh", "start-foreground"]
