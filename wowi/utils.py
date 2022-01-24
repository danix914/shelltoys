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
                  live=False,
                  show_result=True):
    """Execute linux commands via subprocess.Popen

    Run commands via Popen, then return Popen object, STDOUT and STDERR.
    When call this function with enabled 'live' option,
    it will replace non-printable byte to '\\xNN'

        Usage example:

        proc, _, __ = run_shell_cmd('/tmp/myScript.sh')
        proc, out, err = run_shell_cmd('tar zxvf test.tar.gz', live=True)
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

    if live:
        # an UTF-8 encoded character has 1 to 4 byte(s)
        # first 5-bit defined number of byte the character used
        # (c < 128)(ASCII) 0xxx xxxx
        # (192 <= c < 224) 110x xxxx  10xx xxxx
        # (224 <= c < 240) 1110 xxxx  10xx xxxx  10xx xxxx
        # (240 <= c < 248) 1111 0xxx  10xx xxxx  10xx xxxx  10xx xxxx

        out = b''
        for bchar in iter(lambda: p.stdout.read(1), b''):
            out += bchar
            temp = 0b01111111
            bint = bchar[0]
            char = None
            for ele in range(-1, 4):
                if bint < 255 - temp:  # 128 -> 192 -> 224 -> 240 -> 248
                    if ele > 0:
                        otherbytes = p.stdout.read1(ele)
                        out += otherbytes
                        bchar += otherbytes
                    char = bchar.decode('utf8', 'backslashreplace')
                    break
                temp >>= 1  # 0x7f -> 0x3f -> 0x1f -> 0x0f -> 0x07
            if char is None:
                char = bchar.decode('utf8', 'backslashreplace')

            sys.stdout.write(char)
            # Python's standard out is buffered (meaning that it collects some of the data "written" to standard out before it writes it to the terminal).
            # Calling sys.stdout.flush() forces it to "flush" the buffer
            sys.stdout.flush()
        _, err = p.communicate()
    else:
        out, err = p.communicate()
    out = out.decode('utf8', 'backslashreplace')
    err = err.decode('utf8', 'backslashreplace')

    if show_result:
        print('\n=== result ===\nSTDOUT:\n{}\nSTDERR:\n{}'.format(out, err))
        print('=== Exit code: {} (command: `{}`) ===\n'.format(p.returncode, human_cmd))
    return (p, out, err)


def live_as_shell_cmd(cmd):
    """Execute command via Python and show as STDOUT
    """
    return run_shell_cmd(cmd, live=True, show_result=False, cmd_info=False)
