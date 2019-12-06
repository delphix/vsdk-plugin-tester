import datetime
import os
import time
from ansible.plugins.callback.default import CallbackModule as CallbackModule_default


class CallbackModule(CallbackModule_default):
    """
    A plugin for timing tasks
    """

    CALLBACK_VERSION = 2.0
    CALLBACK_TYPE = 'stdout'
    CALLBACK_NAME = 'delphix_tests'

    def __init__(self):
        super(CallbackModule, self).__init__()
        self.start = ""
        self.stop = ""
        self.listtask = []

    def v2_runner_on_ok(self, result):
        print "Runner on OK 2"
        task = result._task.name
        self.stop = "OK"
        self.listtask.append((task, self.stop))

    # def v2_runner_on_failure(self, result):
    #     print "Runner on NOK 2"
    #     self.stop = "NOK"
    #     self.listtask.append((self.start, self.stop))

    def v2_runner_on_failed(self, result, ignore_errors=False):

        task = result._task.name
        self.listtask.append((task, "DUPA"))

    def v2_playbook_on_task_start(self, task, is_conditional):
        pass

    def v2_playbook_on_stats(self, stats):
        for i in self.listtask:
            print i

    # def playbook_on_task_start(self, name, is_conditional):
    #     """
    #     Logs the start of each task
    #     """

    #     if os.getenv("ANSIBLE_PROFILE_DISABLE") is not None:
    #         return

    #     if self.current is not None:
    #         # Record the running time of the last executed task
    #         self.stats[self.current] = time.time() - self.stats[self.current]

    #     # Record the start time of the current task
    #     self.current = name
    #     self.stats[self.current] = time.time()


    # def playbook_on_stats(self, stats):
    #     """
    #     Prints the timings
    #     """

    #     if os.getenv("ANSIBLE_PROFILE_DISABLE") is not None:
    #         return

    #     # Record the timing of the very last task
    #     if self.current is not None:
    #         self.stats[self.current] = time.time() - self.stats[self.current]

    #     # Sort the tasks by their running time
    #     results = sorted(
    #         self.stats.items(),
    #         key=lambda value: value[1],
    #         reverse=True,
    #     )

    #     # Just keep the top 10
    #     results = results[:10]

    #     # Print the timings
    #     for name, elapsed in results:
    #         print(
    #             "{0:-<70}{1:->9}".format(
    #                 '{0} '.format(name),
    #                 ' {0:.02f}s'.format(elapsed),
    #             )
    #         )

    #     total_seconds = sum([x[1] for x in self.stats.items()])
    #     print("\nPlaybook finished: {0}, {1} total tasks.  {2} elapsed. \n".format(
    #             time.asctime(),
    #             len(self.stats.items()),
    #             datetime.timedelta(seconds=(int(total_seconds)))
    #             )
    #       )
