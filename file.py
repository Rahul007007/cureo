#Datastructure
class LogInputs:
    def __init__(self, timestamp, log_type, severity):
        self.timestamp = timestamp
        self.log_type = log_type
        self.severity = severity

class LogManipulation:
    def __init__(self):
        self.logs = []
    
    def log_submit(self, timestamp, log_type, severity):    #1: Submit a new log
        self.logs.append(LogInputs(timestamp, log_type, severity))
        return "No output\n"
    
    def compute(self, values):  #2,3,4: Compute stats
        if not values:
            return "Min: 0.0, Max: 0.0, Mean: 0.0\n"
        log_severity = [val for val in values]
        return f"Min: {round(min(log_severity),6)}, Max: {round(max(log_severity),6)}, Mean: {round(sum(log_severity)/len(log_severity),6)}\n"
    
    def compute_for_log_type(self, log_type):   #2: Compute stats for a log type
        values = [log.severity for log in self.logs if log.log_type == log_type]
        return self.compute(values)
    
    def compute_for_before_timestamp(self, timestamp):  #3: Compute stats for logs before a timestamp
        values = [log.severity for log in self.logs if log.timestamp < timestamp]
        return self.compute(values)
    
    def compute_for_after_timestamp(self, timestamp):   #3: Compute stats for logs after a timestamp
        values = [log.severity for log in self.logs if log.timestamp > timestamp]
        return self.compute(values)
    
    def compute_for_before_log_type(self, log_type, timestamp): #4: Compute stats for logs before a timestamp for a log type
        values = [log.severity for log in self.logs if log.timestamp < timestamp and log.log_type == log_type]
        return self.compute(values)
    
    def compute_for_after_log_type(self, log_type, timestamp):  #4: Compute stats for logs after a timestamp for a log type
        values = [log.severity for log in self.logs if log.timestamp > timestamp and log.log_type == log_type]
        return self.compute(values)
    
logmp = LogManipulation()


def main():
    with open('input.txt', 'r') as infile, open('output.txt', 'w') as outfile:
        errors = infile.readlines()
        for i in errors:

            split_arr = i.split()
            cmd = split_arr[0]

            if cmd =='1':   #1: Submit a new log
                timestamp, log_type, severity = split_arr[1].split(';')
                outfile.write(logmp.log_submit(int(timestamp), log_type, float(severity)))

            elif cmd == '2':    #2: Compute stats for a log type
                log_type = split_arr[1]
                outfile.write(logmp.compute_for_log_type(log_type))

            elif cmd == '3':    #3: Compute stats for logs before/after a timestamp
                timestamp = int(split_arr[-1])
                if split_arr[1].startswith("BEFORE"):
                    outfile.write(logmp.compute_for_before_timestamp(timestamp))
                else:
                    outfile.write(logmp.compute_for_after_timestamp(timestamp))
                    
            elif cmd == '4':   #4: Compute stats for logs before/after a timestamp for a log type
                log_type, timestamp = split_arr[-2], int(split_arr[-1])
                if split_arr[1].startswith("BEFORE"):
                    outfile.write(logmp.compute_for_before_log_type(log_type, timestamp))
                else:
                    outfile.write(logmp.compute_for_after_log_type(log_type, timestamp))
if __name__ == '__main__':
    main()

    