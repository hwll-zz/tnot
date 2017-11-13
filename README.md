# tnot

A very bare-bones terminal-notifier wrapper for notifying in Python. Contains basic features in order to help you wrap your head around the API. Basically generates and runs the terminal command for you so that you can worry less and work faster.

## Installation

Install using [pip]() with..

```sh
pip install tnot
```

## Examples

Send a notification displaying some basic information.

```py
import tnot.tnot as tnot

tnot.notify(
       title='A Real Notification',
       message='Hello, this is me, notifying you!')
```

### Arguments

```py
'''
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
```

