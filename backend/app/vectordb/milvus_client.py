from pymilvus import connections


def connect_to_milvus():

    connections.connect(
        alias="default",
        host="localhost",
        port="19530"
    )

    print("Milvus Connected Successfully")