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

    # call 'List_merge_input' block
    List_merge_input(container=container)

    return

def run_savedsearch(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('run_savedsearch() called')
        
    #phantom.debug('Action: {0} {1}'.format(action['name'], ('SUCCEEDED' if success else 'FAILED')))
    
    # collect data for 'run_savedsearch' call
    formatted_data_1 = phantom.get_format_data(name='myquerystring')

    parameters = []
    
    # build parameters list for 'run_savedsearch' call
    parameters.append({
        'query': formatted_data_1,
        'command': "savedsearch",
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
        "list_filtered_final:custom_function_result.data.*.item",
    ]

    phantom.format(container=container, template=template, parameters=parameters, name="myquerystring")

    run_savedsearch(container=container)

    return

def Add_Comment_2_case(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Add_Comment_2_case() called')

    formatted_data_1 = phantom.get_format_data(name='Output_formatted__as_list')

    phantom.comment(container=container, comment=formatted_data_1)
    Buildcontainerlist(container=container)

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
                    'owner': "",
                    'status': "in progress",
                    'comment': formatted_part_1,
                    'urgency': "",
                    'event_ids': container_item[0],
                    'integer_status': "",
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
def Buildcontainerlist(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('Buildcontainerlist() called')
    
    action_results_data_0 = phantom.collect2(container=container, datapath=['run_savedsearch:action_result.data.*.peer', 'run_savedsearch:action_result.data.*.count', 'run_savedsearch:action_result.data.*.priority', 'run_savedsearch:action_result.parameter.context.artifact_id'], action_results=results )
    container_property_0 = [
        [
            container.get("id.*"),
        ],
    ]

    parameters = []

    action_results_data_0_0 = [item[0] for item in action_results_data_0]
    action_results_data_0_1 = [item[1] for item in action_results_data_0]
    action_results_data_0_2 = [item[2] for item in action_results_data_0]
    container_property_0_0 = [item[0] for item in container_property_0]

    parameters.append({
        'peer': action_results_data_0_0,
        'count': action_results_data_0_1,
        'priority': action_results_data_0_2,
        'current_container': container_property_0_0,
    })
    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################    

    # call custom function "mainPhantomPlaybooksAdvanced/task4customFunc", returns the custom_function_run_id
    phantom.custom_function(custom_function='mainPhantomPlaybooksAdvanced/task4customFunc', parameters=parameters, name='Buildcontainerlist', callback=cf_mainPhantomPlaybooksAdvanced_list_2_containers_1)

    return

def cf_mainPhantomPlaybooksAdvanced_list_2_containers_1(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('cf_mainPhantomPlaybooksAdvanced_list_2_containers_1() called')
    
    custom_function_result_0 = phantom.collect2(container=container, datapath=['Buildcontainerlist:custom_function_result.data.results_list'], action_results=results )
    container_property_0 = [
        [
            container.get("label"),
        ],
    ]

    parameters = []

    container_property_0_0 = [item[0] for item in container_property_0]
    custom_function_result_0_0 = [item[0] for item in custom_function_result_0]

    parameters.append({
        'container_label': container_property_0_0,
        'to_be_containerized': custom_function_result_0_0,
    })
    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################    

    # call custom function "mainPhantomPlaybooksAdvanced/list_2_containers", returns the custom_function_run_id
    phantom.custom_function(custom_function='mainPhantomPlaybooksAdvanced/list_2_containers', parameters=parameters, name='cf_mainPhantomPlaybooksAdvanced_list_2_containers_1')

    return

"""
List to merge the inputs
"""
def List_merge_input(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('List_merge_input() called')
    
    container_data_0 = phantom.collect2(container=container, datapath=['artifact:*.cef.destinationHostName', 'artifact:*.cef.hostname', 'artifact:*.id'])

    parameters = []

    container_data_0_0 = [item[0] for item in container_data_0]
    container_data_0_1 = [item[1] for item in container_data_0]

    parameters.append({
        'input_1': container_data_0_0,
        'input_2': container_data_0_1,
        'input_3': None,
        'input_4': None,
        'input_5': None,
        'input_6': None,
        'input_7': None,
        'input_8': None,
        'input_9': None,
        'input_10': None,
    })
    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################    

    # call custom function "community/list_merge", returns the custom_function_run_id
    phantom.custom_function(custom_function='community/list_merge', parameters=parameters, name='List_merge_input', callback=list_filtered_final)

    return

"""
list_filtered_final
"""
def list_filtered_final(action=None, success=None, container=None, results=None, handle=None, filtered_artifacts=None, filtered_results=None, custom_function=None, **kwargs):
    phantom.debug('list_filtered_final() called')
    
    custom_function_result_0 = phantom.collect2(container=container, datapath=['List_merge_input:custom_function_result.data.*.item'], action_results=results )

    parameters = []

    custom_function_result_0_0 = [item[0] for item in custom_function_result_0]

    parameters.append({
        'input_list': custom_function_result_0_0,
    })
    ################################################################################
    ## Custom Code Start
    ################################################################################

    # Write your custom code here...

    ################################################################################
    ## Custom Code End
    ################################################################################    

    # call custom function "community/list_drop_none", returns the custom_function_run_id
    phantom.custom_function(custom_function='community/list_drop_none', parameters=parameters, name='list_filtered_final', callback=myquerystring)

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