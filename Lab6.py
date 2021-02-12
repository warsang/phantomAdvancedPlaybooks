"""
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'action_0' block
    action_0(container=container)

    return

def action_0(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('action_0() called')

    parameters = []

    phantom.act(action="<undefined>", parameters=parameters, name="action_0")

    return

def httpsphabb09classsplunkcomrestpl(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('httpsphabb09classsplunkcomrestpl() called')

    # collect data for 'httpsphabb09classsplunkcomrestpl' call

    parameters = []
    
    # build parameters list for 'httpsphabb09classsplunkcomrestpl' call
    parameters.append({
        'location': "rest/playbook_run/1481/log?filter_message_contains=%22temp_%22",
        'verify_certificate': False,
        'headers': "",
    })

    phantom.act(action="get data", parameters=parameters, assets=['something'], name="httpsphabb09classsplunkcomrestpl")

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