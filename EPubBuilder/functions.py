import os


TEMPLATE_FOLDER = "./templates"


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

    try:
        xml_template_file = os.path.join(TEMPLATE_FOLDER, 'container.xml')
        with open(xml_template_file, 'r') as xml_file:
            xml_content = xml_file.read()

        container_file_path = os.path.join(folder, "container.xml")
        with open(container_file_path, "w") as container_file:
            container_file.write(xml_content.strip())

        return True
    except Exception as e:
        return e


def make_opf_file(folder: str, title: str) -> str:

    opf_template_file = os.path.join(TEMPLATE_FOLDER, 'title.opf')
    with open(opf_template_file, 'r') as opf_f:
        template_content = opf_f.read()

    opf_content = template_content.replace("{{title}}", title)

    opf_file = os.path.join(folder, title + ".opf")
    with open(opf_file, "w") as f:
        f.write(opf_content.strip())

    return opf_file
