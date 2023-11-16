"""
Meta bot implementation to coordinate between different GPTs
"""


"""
  new_message:
    message:            last message a user sent
    previous_messages:  collection of all previous messages. the meta-bot should select 
                        which of these are relevant for the current query.
"""


def new_message(message, previous_messages):
    return "The first thing to focus on is [probably real long answer, can be html formatted]..."
