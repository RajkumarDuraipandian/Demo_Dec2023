# Demo_Dec2023
Installation
It requires Python 3.6 or higher, check your Python version first.

It uses Graphviz to render the diagram, so you need to install Graphviz to use diagrams. After installing graphviz (or already have it), install the diagrams.

macOS users can download the Graphviz via brew install graphviz if you're using Homebrew. Similarly, Windows users with Chocolatey installed can run choco install graphviz.

**using pip (pip3)**
$ pip install diagrams

**using pipenv**
$ pipenv install diagrams

**using poetry**
$ poetry add diagrams

Clustered Web Services
from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53

with Diagram("Clustered Web Services", show=False):
    dns = Route53("dns")
    lb = ELB("lb")

    with Cluster("Services"):
        svc_group = [ECS("web1"),
                     ECS("web2"),
                     ECS("web3")]

    with Cluster("DB Cluster"):
        db_primary = RDS("userdb")
        db_primary - [RDS("userdb ro")]

    memcached = ElastiCache("memcached")

    dns >> lb >> svc_group
    svc_group >> db_primary
    svc_group >> memcached

   

 **Reference**  https://diagrams.mingrammer.com/docs/getting-started/installation
