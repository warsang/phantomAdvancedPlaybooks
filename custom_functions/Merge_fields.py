def Merge_fields(hostname=None, my_dest_src_param=None, current_container=None, **kwargs):
    """
    I used this to normalize cef fields from different formated entries into one
    
    Args:
        hostname: my_hostname
        my_dest_src_param: my_dest_src_param
        current_container (CEF type: phantom container id): current_container=None
    
    Returns a JSON-serializable object that implements the configured data paths:
        
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
    update_container = phantom.get_container(current_container)
    phantom.debug(hostname)
    phantom.debug(my_dest_src_param)
    if hostname:
        phantom.update(update_container, {'hostname':hostname})
    else:
        phantom.update(update_container, {'hostname':my_dest_src_param})

    # Write your custom code here...
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
