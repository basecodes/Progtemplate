
from engine.reader import directory_reader, file_reader, json_reader, csv_reader, file_name, xml_reader, yaml_reader
from engine.template import Template
from engine.writer import file_writer


class Engine:
    def __init__(self):
        self.templates = dict()
        self.objects = dict()

    def read_template(self, path):
        paths = directory_reader(path, "template")
        for path in paths:
            name = file_name(path)
            txt = file_reader(path)
            template = Template()
            template.parse_body(txt)
            self.templates[name] = template

    def read_data(self, path):
        json_paths = directory_reader(path, "json")
        for p in json_paths:
            name = file_name(p)
            json = json_reader(p)
            self.objects[name] = json

        csv_paths = directory_reader(path, "csv")
        for p in csv_paths:
            name = file_name(p)
            csv = csv_reader(p)
            self.objects[name] = csv

        xml_paths = directory_reader(path, "xml")
        for p in xml_paths:
            name = file_name(p)
            xml = xml_reader(p)
            self.objects[name] = xml

        yaml_paths = directory_reader(path, "yaml")
        for p in yaml_paths:
            name = file_name(p)
            yaml = yaml_reader(p)
            self.objects[name] = yaml

    def export(self, path):
        for k, vs in self.objects.items():
            template = self.templates[k]
            txt = template.handle_body(vs)
            file_writer(path + "/" + k + "." + template.suffix, txt)


