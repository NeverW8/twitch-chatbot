from datetime import datetime, timezone


def calculate_time(stream_started):
    local_time_utc = datetime.utcnow().replace(tzinfo=timezone.utc)

    # Previous Unix timestamp
    prev_unix_timestamp = local_time_utc.timestamp()

    # Convert string to datetime object
    string_to_datetime = datetime.strptime(
        stream_started, "%Y-%m-%dT%H:%M:%SZ"
    ).replace(tzinfo=timezone.utc)

    # Convert stream_started time to Unix timestamp
    streamer_unix_timestamp = string_to_datetime.timestamp()

    # Calculate difference in seconds
    difference_seconds = streamer_unix_timestamp - prev_unix_timestamp

    # Convert difference to hours and minutes
    difference_hours = int(difference_seconds // 3600)
    difference_minutes = int((difference_seconds % 3600) // 60)

    print(
        difference_hours,
        difference_minutes,
    )

    a_day = 24
    a_hour = 60
    remaining_time = a_day - abs(difference_hours), a_hour - abs(difference_minutes)
    uptime = abs(difference_hours), abs(difference_minutes)

    return remaining_time, uptime
