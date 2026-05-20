import xml.etree.ElementTree as ET

class ReadXML:

    @staticmethod
    def get_offer_data(path):
        tree = ET.parse(path)
        root = tree.getroot()

        offers = []
        for offer in root.findall("offer"):
            data = {child.tag: child.text for child in offer}
            offers.append(data)

        return offers