import logging
from pipelines.core.task import TaskContext
from pipelines.core.base import Step


class GetAppointment(Step):
    """Step for getting an IT support appointment."""

    def process(self, task_context: TaskContext) -> TaskContext:
        logging.info(
            "IT Support intent detected. Appointment service should be called."
        )
        return task_context
