"""
abcd123
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'myurl' block
    myurl(container=container)

    return

"""
httpsphabb09classsplunkcomrestpl
"""
def get_data_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_data_1() called')

    # collect data for 'get_data_1' call
    formatted_data_1 = phantom.get_format_data(name='myurl__as_list')

    parameters = []
    
    # build parameters list for 'get_data_1' call
    for formatted_part_1 in formatted_data_1:
        parameters.append({
            'location': formatted_part_1,
            'verify_certificate': False,
            'headers': "",
        })

    phantom.act(action="get data", parameters=parameters, assets=['something'], callback=format_1, reviewer="admin", name="get_data_1")

    return

def format_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_1() called')
    
    template = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "get_data_1:action_result.data.*.parsed_response_body",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_1")

    return

"""
myurl
"""
def myurl(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('myurl() called')
    
    template = """/rest/container/{0}"""

    # parameter list for template variable replacement
    parameters = [
        "container:id",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="myurl")

    get_data_1(container=container)

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