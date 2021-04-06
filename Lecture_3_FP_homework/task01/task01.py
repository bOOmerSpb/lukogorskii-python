# Using functional approach, generators, currying,
# implement functions that writes IP list of redirected requests (code 304) into another file
# separate pure_func from functions that change state (io_func)
# write negative test "test_myfunc_negative"
# Set pytest as default runner
# https://stackoverflow.com/questions/6397063/how-do-i-configure-pycharm-to-run-py-test-tests
# hit Ctrl+Shift+F10 or RMB on the file to run tests
import re


def io_func(logfile_path, result_file_path):
    def gen_line(file_path):
        with open(file_path, "r") as data:
            for line in data:
                yield data.readline()

    with open(result_file_path, "w") as result:
        lineg = gen_line(logfile_path)
        [result.write(pure_func(line) + "\n") for line in lineg if pure_func(line) is not None]


def pure_func(file_line):
    # pattern = re.compile(r'.*HTTP/1.1\" 304.*')
    pattern = re.compile(r'.*HTTP *.* 304.*')
    if file_line.find("304") > 13:
        return file_line.split("-")[0].strip()
    return None


def test_myfunc_positive():
    line = '218.30.103.62 - - [17/May/2015:11:05:17 +0000] "GET /projects/xdotool/xdotool.xhtml \
    HTTP/1.1" 304 - "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"'
    assert pure_func(line) == "218.30.103.62"


def test_myfunc_negative():
    line = '218.30.304.62 - - [17/May/2015:11:05:17 +0000] "GET /projects/xdotool/xdotool.xhtml \
    HTTP/1.1" 200 - "-" "Sogou web spider/4.0(+http://www.sogou.com/docs/help/webmasters.htm#07)"'
    print(pure_func(line) == "218.30.304.62")


io_func("apache_log", "result.txt")
