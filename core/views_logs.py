from __future__ import unicode_literals
import models


def logger(ticket, user, action, destiny):
    new_log_row = models.Logs.objects.create(log_ticket = ticket, log_user=user, log_action=action, log_destiny=str(destiny))
    new_log_row.save()
    return new_log_row
