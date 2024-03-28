def custom_strftime(t):
    return t.strftime('{S} %b, %Y - %H:%M:%S').replace('{S}', str(t.day) + ('th' if 10 <= t.day <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(t.day % 10, 'th')))