from approvaltests.file_approver import FileApprover


def pytest_sessionstart():
    FileApprover.approved_files = [] 