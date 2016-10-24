import os


class InvalidProblemException(Exception):
    pass


def get_problem_from_cwd():
    try:
        problem = int(os.path.basename(os.getcwd()))

        if problem < 0:
            raise InvalidProblemException

        return problem
    except ValueError:
        raise InvalidProblemException


def find_source_code():
    return os.getcwd() + '/' + str(get_problem_from_cwd()) + ".cpp"


def color_red(str):
    return '\033[91m' + str + '\033[0m'


def color_green(str):
    return '\033[92m' + str + '\033[0m'


def pretty_date(time):
    from datetime import datetime
    now = datetime.now()
    diff = now - time
    second_diff = diff.seconds
    day_diff = diff.days

    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return "just now"
        if second_diff < 60:
            return "%d seconds ago" % (second_diff)
        if second_diff < 120:
            return "a minute ago"
        if second_diff < 3600:
            return "%s minutes ago" % (second_diff / 60)
        if second_diff < 7200:
            return "an hour ago"
        if second_diff < 86400:
            return "%d hours ago" % (second_diff / 3600)
    if day_diff == 1:
        return "Yesterday"
    if day_diff < 7:
        return "%d days ago" % day_diff
    if day_diff < 31:
        return "%d weeks ago" % (day_diff / 7)
    if day_diff < 365:
        return "%d months ago" % (day_diff / 30)
    return "%d years ago" % (day_diff / 365)