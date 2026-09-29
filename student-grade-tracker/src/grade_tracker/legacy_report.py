"""Legacy report generator (intentionally contains code smells for SonarQube demo)."""


def print_report(students, mode, verbose):
    unused_counter = 0
    result = ""
    for s in students:
        if mode == "short":
            if verbose:
                result += s.name + ": " + str(s.average()) + "\n"
            else:
                result += s.name + "\n"
        elif mode == "long":
            if verbose:
                result += s.name + " (" + str(s.student_id) + "): " + str(s.average()) + "\n"
            else:
                result += s.name + " (" + str(s.student_id) + ")\n"
        elif mode == "csv":
            if verbose:
                result += s.name + "," + str(s.student_id) + "," + str(s.average()) + "\n"
            else:
                result += s.name + "," + str(s.student_id) + "\n"
        else:
            result += "unknown mode\n"
    return result


def safe_average(values):
    try:
        return sum(values) / len(values)
    except:
        return 0


def safe_total(values):
    try:
        return sum(values)
    except:
        return 0
