# wowi

~~artificial intelligence~~
~~wisdom workers~~
**wo**rkman's **wi**sdom
Avoid to reinvent the wheels, handle general behaviors under Linux/shell......for daily development.


----

-   ```python
    countdown(
        seconds: int,
        print_content: Any = None,
        prefix_message: str = 'countdown') -> None:
    ```

    Wrapper for countdown, sleep, and display specified message.

    -   `seconds`: countdown seconds
    -   (deprecated) `print_content`: show number of countdown seconds
    -   `prefix_message`: prefix countdown message

    e.g.:   `countdown(3)`



-   ```python
    run_shell_cmd(
        cmd: str,
        live: bool = False,
        show_result: bool = True,
        show_cmd_newline: bool = True) -> Tuple[subprocess.Popen, str, str]:
    ```

    execute linux commands via python, then return `subprocess.Popen` object, STDOUT and STDERR.

    when call this function with enable `live` option, it will replace non-printable byte to `\xNN`

    -   `cmd`: command
    -   `live`: flush the buffer to STDOUT on the fly
    -   `show_result`: print STDOUT, STDERR and exit code after command executed
    -   `show_cmd_newline`: convert `\n` to `\\n ` before print command

    e.g.:
    -   `proc, _, __ = run_shell_cmd('/tmp/myScript.sh')`
    -   `proc, out, err = run_shell_cmd('tar zxvf test.tar.gz', live=True)`
    -   `run_shell_cmd('yum -y install tree')`



-   ```python
    live_as_shell_cmd(
        cmd: str) -> Tuple[subprocess.Popen, str, str]:
    ```

    execute commands via python, and show as linux output


-   ```python
    resolve_path(input_path: Union[str, pathlib.Path]) -> pathlib.Path:
    ```

    Convert string to pathlib.Path object and resolve it.

    -   `input_path`: path as string

    e.g.:
    -   `path = resolve_path('.')`
    -   `path = resolve_path('~det/Code')`
    -   `path = resolve_path('../../foobar/')`
