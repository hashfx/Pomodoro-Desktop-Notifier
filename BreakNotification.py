# python -m pip install plyer
from plyer import notification

notification.notify(
    title='TIME TO TAKE BREAK',
    message='Remove Ear-Phones.-----Focus @ 20_20_20-----Relax',
    app_icon= None,  # e.g. 'C:\\icon_32x32.ico'
    timeout=10,  # seconds
)
