#  tgcalls - a Python binding for C++ library by Telegram
#  pytgcalls - a library connecting the Python binding with MTProto
#  Copyright (C) 2020-2021 Il`ya (Marshal) <https://github.com/MarshalX>
#
#  This file is part of tgcalls and pytgcalls.
#
#  tgcalls and pytgcalls is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  tgcalls and pytgcalls is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License v3
#  along with tgcalls. If not, see <http://www.gnu.org/licenses/>.
import logging

from pytgcalls.group_call_factory import GroupCallFactory
from pytgcalls.implementation.group_call_file import GroupCallFileAction
from pytgcalls.implementation.group_call_native import GroupCallNativeAction

# backward compatibility below. Dont use it in new projects

from pytgcalls.mtproto.pyrogram_bridge import PyrogramBridge


logger = logging.getLogger(__name__)


def backward_compatibility_helper(group_call_type, client, *args, **kwargs):
    logger.warning(
        'You use deprecated import from backward compatibility suite. '
        'Please update you code. Backward compatibility will be deleted at any time! '
        'For more info visit https://github.com/MarshalX/tgcalls/discussions/101'
    )

    clazz = GroupCallFactory.GROUP_CALL_CLASS_TO_TYPE.get(group_call_type)
    wrapped_client = PyrogramBridge(client)

    return clazz(wrapped_client, *args, **kwargs)


def GroupCall(client, *args, **kwargs):
    return backward_compatibility_helper(GroupCallFactory.GROUP_CALL_TYPE.FILE, client, *args, **kwargs)


def GroupCallDevice(client, *args, **kwargs):
    return backward_compatibility_helper(GroupCallFactory.GROUP_CALL_TYPE.DEVICE, client, *args, **kwargs)


def GroupCallRaw(client, *args, **kwargs):
    return backward_compatibility_helper(GroupCallFactory.GROUP_CALL_TYPE.RAW, client, *args, **kwargs)


__all__ = [
    'GroupCallFactory',
    'GroupCallFileAction',
    'GroupCallNativeAction',
    # below backward compatibility
    'GroupCall',
    'GroupCallDevice',
    'GroupCallRaw',
]
__version__ = '1.0.0dev'
__pdoc__ = {
    'Action': False,
    'Dispatcher': False,
    'DispatcherMixin': False,
    'GroupCallDispatcherMixin': False,
    'GroupCallNativeAction': False,
    'GroupCallNativeDispatcherMixin': False,
    'GroupCallNative': False,
}
