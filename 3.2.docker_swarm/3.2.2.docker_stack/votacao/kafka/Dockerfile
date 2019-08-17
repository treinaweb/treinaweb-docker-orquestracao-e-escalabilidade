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
RUN wget http://archive.apache.org/dist/kafka/0.9.0.0/kafka_2.11-0.9.0.0.tgz && \
  tar -xvzf kafka_2.11-0.9.0.0.tgz && \
  rm kafka_2.11-0.9.0.0.tgz && \
  sed -i 's/zookeeper.connect=localhost:2181/zookeeper.connect=zookeeper01:2181/g' /opt/kafka_2.11-0.9.0.0/config/server.properties

# Start Kafka
CMD ["/opt/kafka_2.11-0.9.0.0/bin/kafka-server-start.sh", "/opt/kafka_2.11-0.9.0.0/config/server.properties"]
