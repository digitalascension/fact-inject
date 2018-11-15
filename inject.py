#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import argparse, sys

from fact_inject import windows, nix


class FactInject:
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Add facts to multiple nodes at once',
            usage='''inject.py <command> -h [<hosts>] -j [<fact_file.json>]
        Inject commands:
           win    Inject Facter facts on a windows host.
           nix    Inject Facter facts on a *nix host.
        ''')
        parser.add_argument('command', help='Subcommand to run')
        # parse_args defaults to [1:] for args, but you need to
        # exclude the rest of the args too, or validation will fail
        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)
        # use dispatch pattern to invoke method with same name
        getattr(self, args.command)()

    def win(self):
        parser = argparse.ArgumentParser(
            description='Builds krnl environment')
        # NOT prefixing the argument with -- means it's not optional
        parser.add_argument('-t', help='Kernel version that will be pulled')
        parser.add_argument('-t', help='Kernel version that will be pulled')
        args = parser.parse_args(sys.argv[2:])

        print(args)

    def nix(self):
        parser = argparse.ArgumentParser(
            description='Pulls a kernel'
        )
        parser.add_argument('-t', help='Kernel version that will be pulled')
        parser.add_argument('-t', help='Kernel version that will be pulled')
        args = parser.parse_args(sys.argv[2:])

        print(args)

def command_message():
    print('Usage: krnl COMMAND\n')
    print('A distributed kernel management system\n')
    print('Options:')
    print('build    Builds krnl environment')
    print('pull    Pulls a kernel')
    print('list    Lists all pulled kernels\n')
    print("Run 'krnl COMMAND -h' for more information on a command.")
    exit(code=1)


if __name__ == '__main__':
    FactInject()