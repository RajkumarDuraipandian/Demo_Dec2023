from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53

with Diagram("AWS-Clustered Web Services", show=False):
    dns = Route53("dns") # domain name system / Amazon route 53
    lb = ELB("lb") # Elastic load balancing

    with Cluster("Services"): # Amazon Elastic container service
        svc_group = [ECS("web1"),
                     ECS("web2"),
                     ECS("web3")]

    with Cluster("DB Cluster"): # Relational database one for admin write previlage and other one with read only option [Kind of distributed availability group]
        db_primary = RDS("userdb-write")
        db_primary - [RDS("userdb-ro")]

    memcached = ElastiCache("memcached") # Amazon ElastiCache

    dns >> lb >> svc_group
    svc_group >> db_primary
    svc_group >> memcached