def add_log_info(values):
    return values['return_data'], values['pos'], values['new_val']


def remove_log_info(values):
    return values['return_data'], values['pos1'], values.get('pos2', values['pos1'] + 1)
