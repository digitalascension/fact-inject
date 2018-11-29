import paramiko

# Create the winrm session that will be used to add facts to a windows host.
# This is a helper function.
def create_ssh_session(host, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    return ssh

# Generate all of the environment variables that will be used to create the bash
# script that wil inject linux environment variables.
def create_nix_facter_vars(facts):
    vars = []
    for item in facts.keys():
        vars.append('{0}={1}'.format(item, facts[item]))
    return vars

# Add the generated facts to the remote linux hosts.
def inject_facts(facts, host, username, password):
    cmd = ''
    # Create an ssh connection with paramiko.
    ssh = create_ssh_session(host, username, password)
    try:
        ssh.connect(hostname=host, username=username, password=password)
    except paramiko.SSHException:
        print('Error: Could not connect to {}.'.format(host))
        exit(code=1)

    for item in facts.keys():
        cmd += 'echo export {0}={1} >> ~/.bash_profile;source ~/.bash_profile;'.format(item, facts[item])
    print(cmd)
    # Now append the facts to the /home/<user>/.profile.
    stdin, stdout, stderr = ssh.exec_command(command=cmd, timeout=15)
    stdin.close()
    print(stdout.read().decode('ascii').strip("\n"))
    if stdout != 0:
        print('Error: Facts could not be added to the host.')
    else:
        print('Info: Facts were successfully added.')
    cmd = 'source ~/.profile'
    output = ssh.exec_command(command=cmd, timeout=15)
    if output != 0:
        print('Error: Profile could not be sourced.')
    else:
        print('Info: Profile was successfully sourced.')
    ssh.close()
