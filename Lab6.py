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

def undefined_0(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('undefined_0() called')

    parameters = []

    phantom.act(action="<undefined>", parameters=parameters, name="undefined_0")

    return

"""
httpsphabb09classsplunkcomrestpl
"""
def get_data_temp(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('get_data_temp() called')

    # collect data for 'get_data_temp' call
    formatted_data_1 = phantom.get_format_data(name='myurl__as_list')

    parameters = []
    
    # build parameters list for 'get_data_temp' call
    for formatted_part_1 in formatted_data_1:
        parameters.append({
            'location': formatted_part_1,
            'verify_certificate': "",
            'headers': "",
        })

    phantom.act(action="get data", parameters=parameters, app={ "name": 'HTTP' }, callback=format_1, reviewer="admin", name="get_data_temp")

    return

def format_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('format_1() called')
    
    template = """{0}"""

    # parameter list for template variable replacement
    parameters = [
        "get_data_temp:action_result.data.*.parsed_response_body",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="format_1")

    custom_function_0(container=container)

    return

def custom_function_0(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('custom_function_0() called')
    
    parameters = [{}]

    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################    

    # call custom function "", returns the custom_function_run_id
    phantom.custom_function(custom_function='', parameters=parameters, name='custom_function_0')

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

    undefined_0(container=container)

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