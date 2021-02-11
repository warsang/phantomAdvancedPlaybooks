def task4customFunc(current_container=None, results=None, **kwargs):
    """
    mytask4customfunc
    
    Args:
        current_container
        results
    
    Returns a JSON-serializable object that implements the configured data paths:
        my_out_custom_list
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import phantom.rules as phantom
    
    outputs = {}
      
    
    # Write your custom code here...
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
