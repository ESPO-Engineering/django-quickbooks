from django.dispatch import Signal

qbd_task_create = Signal()

customer_created = Signal()
customer_updated = Signal()
invoice_created = Signal()
invoice_updated = Signal()
realm_authenticated = Signal()
qbd_first_time_connected = Signal()

from django_quickbooks.signals.customer import *
from django_quickbooks.signals.invoice import *
from django_quickbooks.signals.qbd_task import *
