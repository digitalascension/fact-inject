import paramiko


def inject_facts(facts, host, username, password):
    cmd = ''
    # Create an ssh connection with paramiko.
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=username, password=password)

    for item in facts.keys():
        cmd += 'echo export {0}={1} >> ~/.profile;'.format(item, facts[item])
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
