import os

from .Builder import Builder


builder = Builder("../tests/epubs")
container_name = builder.make_container_folder("first_epub")
