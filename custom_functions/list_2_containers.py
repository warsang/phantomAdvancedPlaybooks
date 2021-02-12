def list_2_containers(to_be_containerized=None, container_label=None, **kwargs):
    """
    Creates containers from a list
    
    Args:
        to_be_containerized (CEF type: *)
        container_label
    
    Returns a JSON-serializable object that implements the configured data paths:
        new_container_ids
    """
    ############################ Custom Code Goes Below This Line #################################
    import json
    import re
    import phantom.rules as phantom
    
    outputs = {}
       
    
    # Write your custom code here...
    new_container_ids = []
    temp_peer_track = []
    phantom.debug("hello")
    phantom.debug(container_label)
    for item in to_be_containerized:
        phantom.debug(item)
        (peer, priority, count) = item
        if peer not in temp_peer_track:
            if 'critical' in priority:
                priority = "high"
            temp_peer_track.append(peer)
            sta, msg, cid = phantom.create_container(name="Malware Peer found: %s" % peer, label=container_label)
            if re.match("^\d+\.\d+\.\d+\.\d+$", peer) is not None:
                phantom.add_artifact(container=cid, raw_data={}, cef_data={"destinationAddress": peer}, label=container_label, name="Malware IP Peer: %s" % peer, severity=priority, artifact_type="host")
            else:
                phantom.add_artifact(container=cid, raw_data={}, cef_data={"destinationHostName": peer}, label=container_label, name="Malware Hostname Peer: %s" % peer, severity=priority, artifact_type="host")
            new_container_ids.append(cid)
        
    outputs = {"new_container_ids": new_container_ids}
    
    # Return a JSON-serializable object
    assert json.dumps(outputs)  # Will raise an exception if the :outputs: object is not JSON-serializable
    return outputs
