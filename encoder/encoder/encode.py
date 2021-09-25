#module to encode url with sepcial charc during api call
class Encode():

    def __init__(self):
        pass
    
    def encoded(self, data):
        encodedata = {"!": "%21", "\"": "%22",  "#": "%23", "$": "%24",  "%": "%25", "&": "%26", "'": "%27", "(": "%28", ")": "%29", "*": "%2A", "+": "%2B", ",": "%2C", "-": "%2D", ".": "%2E",  "/": "%2F"}
        output = "".join([encodedata.get(d, d) for d in data])
        return output
    
    def encodewithtemplate(self, template, data):
        output = "".join([template.get(d, d) for d in data])
        return output