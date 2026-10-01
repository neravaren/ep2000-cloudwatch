import pytest

import ep20_api


class FakeSerial:
    """
    Serial port stub, returns the given response to read()
    """
    def __init__(self, response):
        self.response = response
        self.written = b''
        self.read_sizes = []

    def reset_input_buffer(self):
        pass

    def write(self, data):
        self.written += bytes(data)

    def read(self, size):
        self.read_sizes.append(size)
        return self.response[:size]


@pytest.fixture(autouse=True)
def no_sleep(monkeypatch):
    monkeypatch.setattr(ep20_api.time, 'sleep', lambda _: None)


def test_send_command_reads_full_response_in_one_call():
    connection = FakeSerial(bytes([0x0A, 0x03, 0x02, 0x12, 0x34, 0xAB, 0xCD]))
    result = ep20_api.send_command(connection, {'data': '0A 03 75 30', 'size': 7})
    assert connection.written == bytes([0x0A, 0x03, 0x75, 0x30])
    assert connection.read_sizes == [7]
    assert result == '0A 03 02 12 34 AB CD '


def test_send_command_raises_on_short_response():
    connection = FakeSerial(bytes([0x0A, 0x03]))
    with pytest.raises(TimeoutError, match='got 2 of 59 bytes'):
        ep20_api.send_command(connection, ep20_api.Commands.COMMAND_1)


def test_send_command_raises_on_no_response():
    connection = FakeSerial(b'')
    with pytest.raises(TimeoutError, match='got 0 of 25 bytes'):
        ep20_api.send_command(connection, ep20_api.Commands.COMMAND_2)
