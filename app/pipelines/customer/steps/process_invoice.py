from pipelines.core.base import Step
from pipelines.core.task import TaskContext
import logging


class ProcessInvoice(Step):
    def process(self, task_context: TaskContext) -> TaskContext:
        self._get_invoice(task_context)
        return task_context

    def _get_invoice(self, task_context: TaskContext):
        logging.info("Billing intent detected. Invoice service should be called.")
        task_context.steps[self.step_name] = {"invoice_retrieved": True}
