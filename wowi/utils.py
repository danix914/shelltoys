import subprocess
import sys
import time


def countdown(seconds, prefix_message='countdown'):
    """Wrapper for countdown, sleep, and display specified message.

        Usage example:

        countdown(10)
    """
    print(f'wait {seconds} second(s)...')
    count = 0
    while count < seconds:
        delta = seconds - count
        print(f'{prefix_message}: {delta:>6}', end='\r')
        sys.stdout.flush()
        time.sleep(1)
        count += 1
    print()


def run_shell_cmd(cmd,
                  *,
                  show_cmd_newline=True,
                  cmd_info=True,
                  show_result=True):
    """Execute linux commands via subprocess.Popen

    Run commands via Popen, then return Popen object, STDOUT and STDERR.

        Usage example:

        proc, _, __ = run_shell_cmd('/tmp/myScript.sh')
        run_shell_cmd('yum -y install tree')
    """
    if show_cmd_newline:
        human_cmd = cmd.replace('\n', '\\n ')  # add a space for readability
    else:
        human_cmd = cmd
    if cmd_info:
        print('running command: `{human_cmd}`\n'
              '  please wait a minute...')
    p = subprocess.Popen(cmd, shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    out = out.decode('utf8', 'backslashreplace')
    err = err.decode('utf8', 'backslashreplace')

    if show_result:
        print('\n=== result ===\nSTDOUT:\n{}\nSTDERR:\n{}'.format(out, err))
        print('=== Exit code: {} (command: `{}`) ===\n'.format(p.returncode, human_cmd))
    return (p, out, err)
