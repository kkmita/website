import copy
import inspect
from typing import Dict, Optional, List


def caller_name() -> str:
    """
    `inspect.stack() returns a list of frame records
    for the caller’s stack. This function extracts the name
    of the outer function
    :return:
    """
    _stack = inspect.stack()
    return _stack[1].function


def set_active(tabs: List[Dict[str, str]], view_name: str):
    _tabs = copy.deepcopy(tabs)
    for tab in _tabs:
        if view_name in tab['href']:
            tab['active'] = 'active'

    _tabs[0]['view_name'] = view_name
    _tabs[1]['view_name'] = view_name
    return _tabs
