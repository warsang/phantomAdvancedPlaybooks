def get_playbook_run_ids(request1_body=None, **kwargs):
    """
    Function 2 get playbook run ids
    
    Args:
        request1_body (CEF type: *)
    
    Returns a JSON-serializable object that implements the configured data paths:
        my_output (CEF type: *): hello
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    
    for element in request1_body:
        phantom.debug(element)
    
    # Write your custom code here...
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
