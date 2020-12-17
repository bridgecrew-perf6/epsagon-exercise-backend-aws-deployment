import pandas as pd

def tag_query(tag: pd.Series, attr, value, operation) -> bool:
    """
    Query conditions in the tag column of the spans dataframe. Used internally in pandas.
    :param tag - a pandas series. a column of spans dataframe
    :param attr - key to query in tags
    :param value - value to query in tags
    :param operation - operation to match tags query

    return bool
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