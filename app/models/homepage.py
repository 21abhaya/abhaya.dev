from sqlalchemy import Table, Column, String, Integer, DateTime
from sqlalchemy.orm import registry

mapper_registry = registry()

homepage = Table(
    "homepage",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("content", String(255)),
    Column("created_at", DateTime, default=datetime.now),
    Column("updated_at", DateTime, default=datetime.now)
)

class Homepage:
    pass 

mapper_registry.map_imperatively(Homepage, homepage)
