from collections import deque

class SmartPrinterQueue:

    def __init__(self):
        self.urgent_queue = deque()
        self.normal_queue = deque()

    def add_job(self, job_name, priority):
        if priority.upper() == "URGENT":
            self.urgent_queue.append(job_name)
        else:
            self.normal_queue.append(job_name)

    def print_jobs(self):
        print("Printing Order:")

        while self.urgent_queue:
            print("URGENT :", self.urgent_queue.popleft())

        while self.normal_queue:
            print("NORMAL  :", self.normal_queue.popleft())


# Driver Code
printer = SmartPrinterQueue()

# Static Input
printer.add_job("Invoice.pdf", "URGENT")
printer.add_job("Report.pdf", "NORMAL")
printer.add_job("SalarySlip.pdf", "URGENT")
printer.add_job("Resume.pdf", "NORMAL")
printer.add_job("Project.pdf", "NORMAL")

printer.print_jobs()