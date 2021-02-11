"""
Notable Events Playbook
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'myquerystring' block
    myquerystring(container=container)

    return

def run_query_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('run_query_1() called')

    # collect data for 'run_query_1' call
    formatted_data_1 = phantom.get_format_data(name='myquerystring')

    parameters = []
    
    # build parameters list for 'run_query_1' call
    parameters.append({
        'command': "savedsearch",
        'query': formatted_data_1,
        'display': "",
        'parse_only': "",
    })

    phantom.act(action="run query", parameters=parameters, assets=['mysplunkinstance'], callback=Output_formatted, name="run_query_1")

    return

def myquerystring(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('myquerystring() called')
    
    template = """myphantomlab4search server={0}"""

    # parameter list for template variable replacement
    parameters = [
        "artifact:*.cef.hostname",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="myquerystring")

    run_query_1(container=container)

    return

def add_comment_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('add_comment_1() called')

    formatted_data_1 = phantom.get_format_data(name='Output_formatted__as_list')

    phantom.comment(container=container, comment=formatted_data_1)

    return

def Output_formatted(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Output_formatted() called')
    
    template = """This is the total number of peer servers returned by the search {0}"""

    # parameter list for template variable replacement
    parameters = [
        "myquerystring:formatted_data.*",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="Output_formatted")

    add_comment_1(container=container)

    return

def on_finish(container, summary):
    phantom.debug('on_finish() called')
    # This function is called after all actions are completed.
    # summary of all the action and/or all details of actions
    # can be collected here.

    # summary_json = phantom.get_summary()
    # if 'result' in summary_json:
        # for action_result in summary_json['result']:
            # if 'action_run_id' in action_result:
                # action_results = phantom.get_action_results(action_run_id=action_result['action_run_id'], result_data=False, flatten=False)
                # phantom.debug(action_results)

    return