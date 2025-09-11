from neo4j import GraphDatabase
from django.conf import settings
from datetime import datetime

def get_personalized_feed(username, limit=40):
    """
    Fetches posts for a developer's personalized feed based on who they follow.
    Returns a list of dictionaries with imgUrl, caption, datePosted (ISO string), and author info.
    """
    driver = GraphDatabase.driver(
        settings.NEO4J_URI,
        auth=(settings.NEO4J_USER, settings.NEO4J_PASSWORD)
    )

    query = """
    MATCH (d1:Developer {username: $username})-[:FOLLOWED]->(d2:Developer)-[r:POSTED]->(p:Post)
    RETURN p.id AS id, p.imgUrl AS imgUrl, p.caption AS caption, r.datePosted AS datePosted, d2.username AS author
    ORDER BY r.datePosted DESC
    LIMIT $limit
    """

    feed = []
    try:
        with driver.session() as session:
            result = session.run(query, username=username, limit=limit)
            for record in result:
                data = record.data()
                # Convert Neo4j DateTime to ISO string for JSON
                if 'datePosted' in data and hasattr(data['datePosted'], 'isoformat'):
                    data['datePosted'] = data['datePosted'].isoformat()
                feed.append(data)
    finally:
        driver.close()  # ensure driver closes

    return feed
