class SpanFilter(object):
    def __init__(self, attr, value, operation = "eq", is_tag = False):
        assert operation in ["eq", 'gte', 'gt', 'lte', 'lt']
        self.operation = operation
        self.attr = attr
        self.value = value
        self.is_tag = is_tag