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
