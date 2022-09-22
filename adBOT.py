import argparse
import datetime
import rpyc
from rpyc.utils.server import ThreadedServer
import subprocess

date_time = datetime.datetime.now()


class MonitorService(rpyc.Service):
    def on_connect(self, connection):
        print('\nConnected on {}'.format(date_time))

    def on_disconnect(self, connection):
        print('Disconnected on {}\n'.format(date_time))

    def exposed_run_command(self, command):
        try:
            output = subprocess.check_output(command, shell=True)
            print(output)
        except subprocess.CalledProcessError as Error:
            print(Error.returncode)
            print(Error.output)


def main():
    parser = argparse.ArgumentParser(description='Active Directory BOT')
    parser.add_argument('-port', type=int, help="Enter custom port number")
    args = parser.parse_args()
    port = args.port
    if not port:
        port = 19961
    t = ThreadedServer(MonitorService, port=port)
    t.start()


if __name__ == "__main__":
    main()
