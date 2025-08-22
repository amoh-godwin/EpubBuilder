import os

import functions


class Builder:

    def __init__(self, store_folder: str = ""):
        self.store_folder = store_folder
        self.epub_container: str = ""
        self.meta_inf_folder: str = ""
        self.opf_name: str = "EPUB"
        self.opf_container = ""

        # Book details
        self.title: str = "BookTitle"

    def make_container_folder(self, name: str = ""):
        """
        Creates a container folder for the EPUB structure.
        """
        container_name = os.path.join(self.store_folder, name)
        os.makedirs(container_name, exist_ok=True)

        functions.make_mimetype_file(container_name)
        self.epub_container = container_name

    def make_meta_inf_folder(self, container_name: str):
        """
        Creates the META-INF folder inside the EPUB container.
        """
        meta_inf_folder = os.path.join(container_name, "META-INF")
        os.makedirs(meta_inf_folder, exist_ok=True)
        self.meta_inf_folder = meta_inf_folder
        functions.make_container_xml(meta_inf_folder)

    def make_opf_file(self):
        opf_container = os.path.join(self.epub_container, self.opf_name)
        os.makedirs(opf_container, exist_ok=True)
        functions.make_opf_file(opf_container, self.title)
        self.opf_container = opf_container

    def create_template_html(self):
        functions.copy_template_html(self.opf_container)
