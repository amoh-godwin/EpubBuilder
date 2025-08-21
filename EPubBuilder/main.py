import os

from Builder import Builder


os.sep = "/"

builder = Builder("../tests/epubs")
builder.make_container_folder("first_epub")
