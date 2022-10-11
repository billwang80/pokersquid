import logging
import time
from typing import Any, Optional

from .channel import MessageFormatError, ChannelError, MessageTimeout, Channel
from .player import Player

class PlayerServer(Player):
  def __init__(self, channel: Channel, logger, *args, **kwargs):
    Player.__init__(self, *args, **kwargs)
    self._channel: Channel = channel
    self._connected: bool = True
    self._logger = logger if logger else logging
  
  def disconnect(self):
    if self._connected:
      self.send_message({"message_type": "disconect"})
      self._channel.close()
      self._connected = False

  @property
  def channel(self) -> Channel:
    return self._channel

  @property
  def connected(self) -> bool:
    return self._connected

  def update_channel(self, new_player):
    self.disconect()
    self._channel = new_player.channel
    self._connected = new_player.connected

  def ping(self) -> bool:
    try:
      self.try_send_message({"message_type": "ping"})
      message = self.receive_message(timeout_epoch=time.time() + 2)
      MessageFormatError.validate_message_type(message, expected="pong")
      return True
    except ChannelError:
      return False

  def send_message(self, message: Any):
    return self._channel.send_message(message)

  def receive_message(self, timeout_epoch: Optional[float] = None) -> Any:
    message = self._channel.receive_message(timeout_epoch)
    if "message_type" in message and message["message_type"] == "disconnect":
      raise ChannelError("Client disconnected")
    return message