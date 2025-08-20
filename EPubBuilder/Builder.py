import os

from .functions import make_mimetype_file


class Builder:

    def __init__(self, store_folder: str = ""):
        self.store_folder = store_folder

    def make_container_folder(self, name: str = "") -> str:
        """
        Creates a container folder for the EPUB structure.

        """
        container_name = os.path.join(self.store_folder, name)
        os.makedirs(container_name, exist_ok=True)

        make_mimetype_file(container_name)
        return container_name
