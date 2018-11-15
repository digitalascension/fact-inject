# Fact Inject
A tool to inject facter facts remotely.

### Usage
Inject uses JSON key-value pairs to add Facter environment variables to the target hosts.

To add facts to a Linux host, run the following command:
```bash
$ inject nix --host testhost.com --file path/to/jsonfile
```

To add facts to a Windows host, run the following command:
```bash
$ inject win --host testwin.com --file path/to/jsonfile
```

I am currently working on adding a configuration file for username and password.

### Contributing
If you would like to contribute to this project, make a pull request! I would love to have help
from the community.

### Created By
Luke Brady, 2018