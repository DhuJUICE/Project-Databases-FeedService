from neo4j import GraphDatabase
from django.conf import settings

# Initialize Neo4j driver using Django settings
driver = GraphDatabase.driver(
    settings.NEO4J_URI,
    auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
)

def create_developer_node(dev_id, first_name, last_name, email, username):
    """
    Creates a Developer node in Neo4j.
    """
    with driver.session() as session:
        session.run(
            """
            CREATE (d:Developer {
                id: $id,
                first_name: $first_name,
                last_name: $last_name,
                email: $email,
                username: $username
            })
            """,
            id=dev_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username
        )
