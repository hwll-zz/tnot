'''

TERMINALNOTIFIER.

:author: Jake Hwll
:license: MIT

'''

import os
import subprocess

from tnot import *

valid_sounds = [
    'Basso', 'Blow', 'Bottle', 'Frog', 'Funk', 
    'Glass', 'Hero', 'Morse', 'Ping', 'Pop', 
    'Purr', 'Sosumi', 'Submarine', 'Tink'
]

def notify(
        title: str,
        message: str,
        subtitle: str=None,
        icon: str=None,
        sound: str=None,
        custom_sound: str=None,
        activate: str=None,
        group: str=None,
        execute: str=None,
        content_image: str=None,
        dnd_skip: bool=False,
        url: str=None,
        ):
    '''

    Runs a terminal command to access the terminal-notifier at a commandline level.

    REQUIRED.
    * title - A title of the broadcast, the top-line.
    * message - A message of the broadcast, the bottom-line.

    OPTIONAL.

    * subtitle - A subtitle, shown below the title. The mid-line.
    * icon - An image to be displayed alongside the notification.
    * sound - A sound to be played, must be valid in dictionary.
    * custom_sound - A sound to be played, bypasses invalid dictionary.
    * activate - An application to be opened, via plist id. i.e com.apple.Terminal
    * execute - A terminal command to be executed upon opening application.
    * group - The group ID of the sent notification.
    * dnd_skip - Whether or not we should check for `Do Not Disturb`.
    * content_image - An image in which you want to display with the notification.
    * url - A url to open in the users browser upon clicking notification.
    '''

    s, a, r, g, ex, dnd, img= ("",)*7
    t = '-title {!r}'.format(title)

    if subtitle is not None:
        s = '-subtitle {!r}'.format(subtitle)

    m = '-message {!r}'.format(message)
    i = '-appIcon {!r}'.format(icon)

    if sound is not None and custom_sound is not None:
        raise exc.InvalidSound('Too many sound effects, cannot distinguish which to use.')
        return

    if sound is not None:
        if sound not in valid_sounds:
            raise exc.InvalidSound('Invalid sound effect, use --custom_sound to bypass this.')
            return

        a = '-sound {!r}'.format(sound)

    if custom_sound is not None:
        a = '-sound {!r}'.format(sound)

    if activate is not None:
        r = '-activate {!r}'.format(activate)

    if execute is not None:
        ex = '-execute {!r}'.format(execute)

    if group is not None:
        g = '-group {!r}'.format(group)

    if dnd_skip is True:
        dnd = '-ignoreDnD'

    if content_image is not None:
        img = '-contentImage {!r}'.format(content_image)

    if url is not None:
        url = '-open {!r}'.format(url)

    values = [m, t, s, a, ex, r, dnd, img, url, g, i]

    for value in values:
        if value is None:
            values.remove(value)

    os.system('terminal-notifier {}'.format(' '.join(values)))


def remove(id: str, output: bool=True):
    '''

    Runs a command to remove a specific notification from terminal.

    REQUIRED.
    * id - The id of the content to be removed.

    OPTIONAL.
    * output - Whether output should be sent or not.

    '''

    r = '-remove {!r}'.format(id)

    o = ("",)*1

    if output is False:
        o = '>/dev/null'

    os.system('terminal-notifier {}'.format(' '.join([r, o])))


def list(id: str):
    '''

    Lists out as a string the current notifications.

    REQUIRED.
    * id - The id of the content to be removed.

    '''

    r = '-list {!r}'.format(id)

    test = os.system('terminal-notifier {}'.format(' '.join([r])))
