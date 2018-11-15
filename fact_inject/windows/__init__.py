import winrm

# Create the winrm session that will be used to add facts to a windows host.
# This is a helper function.
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

# Generate all of the environment variables that will be used to create the powershell
# script that wil inject windows environment variables.
def create_win_facter_vars(facts):
    vars = []
    for item in facts.keys():
        vars.append('$env:{0}="{1}"'.format(item, facts[item]))
    return vars

# Add Facter facts to windows as environment variables.
def inject_win_facts(facts, host, username, password):
    cmd = ''
    rm = create_winrm_session(host, username, password)