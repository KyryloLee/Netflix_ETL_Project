class BaseTable():
    def __init__(self, connector):
        self.table_name = 'BaseTable'
        self.create_table = None
        self.cursor = connector.cursor()
        connector.excecute(self.create_table))
        return self

    def insert(self, data, columns):
        try:
