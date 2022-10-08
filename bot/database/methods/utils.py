from datetime import datetime, timezone


# returns date in TIMESTAMP format (for postgres) like that "TIMESTAMP '2022-10-02 06:23:14.959617+00:00'"
def get_timestamp_format_value(date: datetime) -> str:
    return "TIMESTAMP \'" + str(date) + "\'"


# returns date in TIMESTAMP format for now()
def get_timestamp_for_now() -> str:
    return "TIMESTAMP \'" + str(datetime.now(timezone.utc)) + "\'"
