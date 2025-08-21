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


def make_opf_file(folder: str, title: str) -> str:

    opf_content = """
    <?xml version="1.0"?>
    <package
    version="3.0"
    xml:lang="en"
    xmlns="http://www.idpf.org/2007/opf"
    unique-identifier="pub-id">

   <metadata
       xmlns:dc="http://purl.org/dc/elements/1.1/">

      <dc:identifier
          id="pub-id">
         urn:uuid:B9B412F2-CAAD-4A44-B91F-A375068478A0
      </dc:identifier>

      <dc:language>
         en
      </dc:language>

      <dc:title>
         Book Title
      </dc:title>

      <dc:creator
          id="creator">
         Creator Name
      </dc:creator>

      <meta
          property="dcterms:modified">
         2000-03-24T00:00:00Z
      </meta>

      <dc:publisher>
         Book Publisher
      </dc:publisher>

      <dc:date>
         2000-01-31
      </dc:date>

      <meta
          property="dcterms:dateCopyrighted">
         9999-01-01
      </meta>

      <dc:identifier
          id="isbn13">
         urn:isbn:9780741014559
      </dc:identifier>

      <dc:identifier
          id="isbn10">
         0-7410-1455-6
      </dc:identifier>
   </metadata>

   <manifest>
      <item id="r4915"
          href="book.html"
          media-type="application/xhtml+xml"/>
      <item id="r7184"
          href="images/cover.png"
          media-type="image/png"/>
      <item id="nav"
          href="nav.html"
          media-type="application/xhtml+xml"
          properties="nav"/>
   </manifest>

   <spine>
      <itemref
          idref="r4915"/>
   </spine>
</package>
    """

    opf_file = os.path.join(folder, title + ".opf")
    with open(opf_file, "w") as f:
        f.write(opf_content.strip())
