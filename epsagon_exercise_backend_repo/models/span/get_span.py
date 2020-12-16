from models.span.filter.filter import SpanFilter
import pandas as pd

try:
    spans = pd.read_json("./../../spans.json")
except Exception as e:
    spans = pd.read_json("https://s3.us-west-2.amazonaws.com/secure.notion-static.com/95a4b69e-773f-499a-abd8-528e7d4ea273/spans.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201214T204525Z&X-Amz-Expires=86400&X-Amz-Signature=3fb4ca2cc308a1800d8e8191dcaf31622708ae4101d25a356a41f46668801f0d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22spans.json%22")

end_time_column = spans.apply(lambda row: row.startTime + row.duration, axis=1)
spans = spans.assign(endTime=end_time_column.values)
spans["spanId"] = spans["spanId"].astype(str)

operations = {
    "eq": "==",
    "gte": ">=",
    "gt": ">",
    "lte": "<=",
    "lt": "<"
}

def get_span_by_filters(*args):
    """
    expect args to be a list of tuples: [(attr, value, operation, is_tag)]
    """
    filters = []
    for arg in args:
        assert len(arg) == 4
        filters.append(SpanFilter(attr=arg[0], value=arg[1], operation=arg[2], is_tag=arg[3]))

    queried = _get_span_by_filters(*filters)
    return queried.to_dict(orient="records")

def _get_span_by_filters(*filters):
    for filt in filters:
        if type(filt) != SpanFilter:
            raise TypeError("Filter has to be of type SpanFilter")
        if not filt.is_tag and filt.attr not in list(spans.columns):
            raise ValueError("Attr has to be a tag or one of: {}".format(spans.columns))

    for filt in filters:
        if filt.is_tag:
            return spans[spans['tags'].apply(lambda x: query_tag(x, filt.attr, filt.value, filt.operation))]
        else:
            if type(filt.value) == str:
                filt.value = '"{}"'.format(filt.value)
            query = '{} {} {}'.format(filt.attr, operations[filt.operation], filt.value)
            print("QUERY: {}".format(query))
            return spans.query(query)

    return spans

def query_tag(tag, attr, value, operation):
    """
    tag is a list of dicts
    """
    try:
        for dic in tag:
            keys = list(dic.keys())
            valueColumn = [key for key in keys if key != "key"][0]
            if operation == "eq":
                if dic["key"] == attr and dic[valueColumn] == value:
                    return True
            elif operation == "gte":
                if dic["key"] == attr and dic[valueColumn] >= value:
                    return True
            elif operation == "gt":
                if dic["key"] == attr and dic[valueColumn] > value:
                    return True
            elif operation == "lte":
                if dic["key"] == attr and dic[valueColumn] <= value:
                    return True
            elif operation == "lt":
                if dic["key"] == attr and dic[valueColumn] < value:
                    return True
        else:
            return False
    except TypeError as e:
        raise ValueError('operation {} is not supported for attribute {}'.format(operation, attr))
