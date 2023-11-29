from diagrams import Diagram, Cluster
from diagrams.onprem.container import Docker
from diagrams.onprem.database import PostgreSQL
from diagrams.onprem.inmemory import Redis
from diagrams.generic.network import Network

with Diagram("Docker Compose Architecture", show=False, direction="TB"):
    # Networks
    front_tier = Network("Front Tier Network")
    back_tier = Network("Back Tier Network")

    # Services
    with Cluster("Services"):
        vote = Docker("vote")
        result = Docker("result")
        worker = Docker("worker")
        redis = Redis("redis")
        db = PostgreSQL("db")

    # Connections and Networks
    vote >> front_tier >> result
    vote >> back_tier >> redis
    result >> back_tier >> db
    worker >> back_tier >> [redis, db]

# Generate the diagram
diagram_path = "./docker_compose_diagram.png"
diagram.render(diagram_path)
diagram_path