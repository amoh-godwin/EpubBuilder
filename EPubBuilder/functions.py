import os


def make_mimetype_file(folder: str) -> str:
    """
    Creates a mimetype file in the specified folder.
    The mimetype file is required for EPUB files.
    """
    mimetype_path = os.path.join(folder, "mimetype")
    with open(mimetype_path, "w") as mimetype_file:
        mimetype_file.write("application/epub+zip")
    return mimetype_path


def make_container_xml(folder: str) -> bool:
    """
    Creates a container.xml file in the specified folder.
    This file is part of the EPUB structure.
    """
    xml_content = """
    <?xml version="1.0"?>\n
    <container\n
        version="1.0"\n
        xmlns="urn:oasis:names:tc:opendocument:xmlns:container">\n
    <rootfiles>\n
        <rootfile />\n
    </rootfiles>\n
    </container>\n
    """
    try:
        container_file_path = os.path.join(folder, "container.xml")
        with open(container_file_path, "w") as container_file:
            container_file.write(xml_content.strip())
        return True
    except Exception as e:
        return e
