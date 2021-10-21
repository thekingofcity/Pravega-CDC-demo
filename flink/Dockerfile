FROM flink:1.13.2-scala_2.12

MAINTAINER Pravega

EXPOSE 8081

COPY pravega-connectors-flink-1.13_2.12-0.10.0-291.ea7c049-SNAPSHOT.jar /opt/flink/lib/
COPY flink-conf.yaml /opt/flink/conf/
COPY init.sql /opt/flink/

WORKDIR /opt/flink

ENTRYPOINT ["tail", "-f", "/dev/null"]
