import winrm

# Create the winrm session that will be used to add facts to a windows host.
def create_winrm_session(host, username, password):
    try:
        # Create a winrm connection with winrm.
        rm = winrm.Session(host, auth=(username, password))
        return rm
    except winrm.FEATURE_OPERATION_TIMEOUT:
        print('Error: Could not connect to {}.'.format(host))
        exit(code=1)
    except winrm.FEATURE_READ_TIMEOUT:
        print('Error: Could not connect to {}.'.format(host))
        exit(code=1)

def inject_win_facts(facts, host, username, password):
    cmd = ''
    rm = create_winrm_session(host, username, password)