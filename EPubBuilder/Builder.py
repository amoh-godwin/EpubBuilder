import os

from functions import make_mimetype_file


class Builder:

    def __init__(self, store_folder: str = ""):
        self.store_folder = store_folder
        self.epub_container: str = ""
        self.meta_inf_folder: str = ""

    def make_container_folder(self, name: str = ""):
        """
        Creates a container folder for the EPUB structure.

        """
        container_name = os.path.join(self.store_folder, name)
        os.makedirs(container_name, exist_ok=True)

        make_mimetype_file(container_name)
        self.epub_container = container_name

    def make_meta_inf_folder(self, container_name: str):
        """
        Creates the META-INF folder inside the EPUB container.
        """
        meta_inf_folder = os.path.join(container_name, "META-INF")
        os.makedirs(meta_inf_folder, exist_ok=True)
        self.meta_inf_folder = meta_inf_folder
