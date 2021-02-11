"""
Notable Events Playbook
"""

import phantom.rules as phantom
import json
from datetime import datetime, timedelta
def on_start(container):
    phantom.debug('on_start() called')
    
    # call 'Event_Comment' block
    Event_Comment(container=container)

    # call 'myquerystring' block
    myquerystring(container=container)

    return

def run_savedsearch(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('run_savedsearch() called')

    # collect data for 'run_savedsearch' call
    formatted_data_1 = phantom.get_format_data(name='myquerystring')

    parameters = []
    
    # build parameters list for 'run_savedsearch' call
    parameters.append({
        'command': "savedsearch",
        'query': formatted_data_1,
        'display': "",
        'parse_only': "",
    })

    phantom.act(action="run query", parameters=parameters, assets=['mysplunkinstance'], callback=Output_formatted, name="run_savedsearch")

    return

def myquerystring(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('myquerystring() called')
    
    template = """myphantomlab4search server={0}"""

    # parameter list for template variable replacement
    parameters = [
        "artifact:*.cef.hostname",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="myquerystring")

    run_savedsearch(container=container)

    return

def Add_Comment_2_case(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Add_Comment_2_case() called')

    formatted_data_1 = phantom.get_format_data(name='Output_formatted__as_list')

    phantom.comment(container=container, comment=formatted_data_1)
    MyPhantomcustomfunction(container=container)

    return

def Output_formatted(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Output_formatted() called')
    
    template = """This is the total number of peer servers returned by the search {0}"""

    # parameter list for template variable replacement
    parameters = [
        "run_savedsearch:action_result.summary.total_events",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="Output_formatted")

    Add_Comment_2_case(container=container)

    return

def update_event_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('update_event_1() called')

    # collect data for 'update_event_1' call
    container_data = phantom.collect2(container=container, datapath=['artifact:*.cef.event_id', 'artifact:*.id'])
    formatted_data_1 = phantom.get_format_data(name='Event_Comment__as_list')

    parameters = []
    
    # build parameters list for 'update_event_1' call
    for container_item in container_data:
        for formatted_part_1 in formatted_data_1:
            if container_item[0]:
                parameters.append({
                    'event_ids': container_item[0],
                    'owner': "",
                    'status': "in progress",
                    'integer_status': "",
                    'urgency': "",
                    'comment': formatted_part_1,
                    'wait_for_confirmation': "",
                    # context (artifact id) is added to associate results with the artifact
                    'context': {'artifact_id': container_item[1]},
                })

    phantom.act(action="update event", parameters=parameters, assets=['mysplunkinstance'], name="update_event_1")

    return

def Event_Comment(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Event_Comment() called')
    
    template = """We're working on this event. Check status here: {0}"""

    # parameter list for template variable replacement
    parameters = [
        "container:url",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="Event_Comment")

    update_event_1(container=container)

    return

"""
MyPhantomcustomfunction
"""
def MyPhantomcustomfunction(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('MyPhantomcustomfunction() called')
    
    action_results_data_0 = phantom.collect2(container=container, datapath=['run_savedsearch:action_result.message', 'run_savedsearch:action_result.parameter.context.artifact_id'], action_results=results )
    container_property_0 = [
        [
            container.get("id"),
        ],
    ]

    parameters = []

    action_results_data_0_0 = [item[0] for item in action_results_data_0]

    for item0 in container_property_0:
        parameters.append({
            'current_container': item0[0],
            'results': action_results_data_0_0,
        })
    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################    

    # call custom function "mainPhantomPlaybooksAdvanced/task4customFunc", returns the custom_function_run_id
    phantom.custom_function(custom_function='mainPhantomPlaybooksAdvanced/task4customFunc', parameters=parameters, name='MyPhantomcustomfunction')

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