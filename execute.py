
from engine.engine import Engine

if __name__ == '__main__':
    engine = Engine()
    engine.read_template("./templates")
    engine.read_data("./data")
    engine.export("./publish")
    print("-------------> Finish!")

