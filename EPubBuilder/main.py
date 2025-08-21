import os

from Builder import Builder


os.sep = "/"

builder = Builder("tests/epubs")
container_name = builder.make_container_folder("first_epub")
print(container_name)
