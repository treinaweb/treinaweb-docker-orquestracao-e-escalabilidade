yum install -y wget

wget --no-cookies --no-check-certificate --header "Cookie: oraclelicense=accept-securebackup-cookie" https://download.oracle.com/otn-pub/java/jdk/12.0.2+10/e482c34c86bd4bf8b56c0b35558996b9/jdk-12.0.2_linux-x64_bin.rpm

rpm -Uvh jdk-12.0.2_linux-x64_bin.rpm

export JAVA_HOME=/usr/java/jdk-12.0.2
export PATH=$PATH:$JAVA_HOME/bin

wget https://www-us.apache.org/dist/zookeeper/zookeeper-3.5.5/apache-zookeeper-3.5.5.tar.gz

tar -xvzf apache-zookeeper-3.5.5.tar.gz 
cd apache-zookeeper-3.5.5
mkdir data

echo -e "tickTime=2000 \ndataDir=/path/to/zookeeper/data \nclientPort=2181 \ninitLimit=5 \nsyncLimit=2" >> conf/zoo.cfg

bin/zkServer.sh start
