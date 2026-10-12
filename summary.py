with open("demo_logs.log","r") as file:
    for line in file:
        if "ERROR" in line
            with open("error_logs.log","a") as error_file:
                error_file.write(line)
        elif "WARNING" in line:
            with open("warning_logs.log","a") as warning_file:
                warning_file.write(line)
        elif "INFO" in line:
            with open("info_logs.log","a") as info_file:
                info_file.write(line)
        elif "DEBUG" in line:
            with open("debug_logs.log","a") as debug_file:
                debug_file.write(line)
        elif "CRITICAL" in line:
            with open("critical_logs.log","a") as critical_file:
                critical_file.write(line)
        elif "FATAL" in line:
            with open("fatal_logs.log","a") as fatal_file:
                fatal_file.write(line)
        elif "TRACE" in line:
            with open("trace_logs.log","a") as trace_file:
                trace_file.write(line)
        elif "NOTICE" in line:
            with open("notice_logs.log","a") as notice_file:
                notice_file.write(line)
        elif "ALERT" in line:
            with open("alert_logs.log","a") as alert_file:
                alert_file.write(line)
        else:
            with open("other_logs.log","a") as other_file:
                other_file.write(line)