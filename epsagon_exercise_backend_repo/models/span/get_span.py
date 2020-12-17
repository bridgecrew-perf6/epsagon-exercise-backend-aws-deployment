from models.span.filter.filter import SpanFilter
import pandas as pd
from .constants import operations
from .query_methods import tag_query
import typing

def get_span(*param_filters: tuple) -> typing.List[dict]:
    """
    Get spans from file with applied filters
    :params *filters - filters of tuple(attr, value, operation, is_tag) to apply to dataframe

    returns List of span dicts
    """
    inital_spans_df = _load_spans_from_file()
    updated_spans_df = _update_initial_spans_dataframe(inital_spans_df)
    return _filter_spans(updated_spans_df, *param_filters)

def _load_spans_from_file(local_filepath: str = "./spans.json") -> pd.DataFrame:
    """
    Loads spans objects from json file, prefering local filepath.
    :param local_filepath - path string

    returns pandas.DataFrame
    """
    try:
        spans_df = pd.read_json(local_filepath)
    except Exception as e:
        spans_df = pd.read_json(
            "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/95a4b69e-773f-499a-abd8-528e7d4ea273/spans.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201214%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201214T204525Z&X-Amz-Expires=86400&X-Amz-Signature=3fb4ca2cc308a1800d8e8191dcaf31622708ae4101d25a356a41f46668801f0d&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22spans.json%22")

    return spans_df

def _update_initial_spans_dataframe(spans_df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds endTime column to dataframe, changes spanId column type to string
    :param spans_df - initial spans_df to update

    returns pandas.DataFrame
    """
    end_time_column = spans_df.apply(lambda row: row.startTime + row.duration, axis=1)
    spans = spans_df.assign(endTime=end_time_column.values)
    spans["spanId"] = spans["spanId"].astype(str)
    return spans

def _filter_spans(spans_df: pd.DataFrame, *param_filters: tuple) -> typing.List[dict]:
    """
    Applies filters on a dataframe.
    :param spans_df - spans dataframe to filter
    :params *filters - filters of tuple(attr, value, operation, is_tag) to apply to dataframe

    returns List of span dicts
    """
    filters = []
    for param_filter in param_filters:
        assert len(param_filter) == 4
        filters.append(SpanFilter(attr=param_filter[0], value=param_filter[1], operation=param_filter[2], is_tag=param_filter[3]))

    for filt in filters:
        if type(filt) != SpanFilter:
            raise TypeError("Filter has to be of type SpanFilter")
        if not filt.is_tag and filt.attr not in list(spans_df.columns):
            raise ValueError("Attr has to be a tag or one of: {}".format(spans_df.columns))

    for filt in filters:
        if filt.is_tag:
            return spans_df[spans_df['tags'].apply(lambda x: tag_query(x, filt.attr, filt.value, filt.operation))]
        else:
            if type(filt.value) == str:
                filt.value = '"{}"'.format(filt.value)
            query = '{} {} {}'.format(filt.attr, operations[filt.operation], filt.value)
            # print("QUERY: {}".format(query))
            spans_df = spans_df.query(query)
    return spans_df.to_dict(orient="records")
