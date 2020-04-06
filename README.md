# esp-atcoap-micropython
 [![Author](https://img.shields.io/badge/Author-HAIZAKURA-b68469?style=flat-square)](https://nya.run) [![License](https://img.shields.io/github/license/HAIZAKURA/esp-atcoap-micropython?style=flat-square)](./LICENSE)

 A CoAP over AT Lib for esp8266/esp32 with MicroPython.

## Usage

```python
from at_coap import AT_CoAP

# reveive message
def on_rev(rev_msg):
    print('receive:', rev_msg)
    # '_ERR_' for message sending failed

# uartid can only be 1 or 2 on esp32 / 0 on esp8266
coap = AT_CoAP(uartid=2, rxpin=16, txpin=17, callback=on_rev)

# send message
coap.send('123')
```

## Notice

**Only tested on ESP32 with QUECTEL BC28 NB-IoT module.**

**Only implements basic transceiver function and error handling function.**

## Author

**esp-atcoap-micropython** © [HAIZAKURA](https://nya.run), Released under the [MIT](./LICENSE) License.

> [Personal Website](https://nya.run) · GitHub [@HAIZAKURA](https://github.com/HAIZAKURA) · Twitter [@haizakura_0v0](https://twitter.com/haizakura_0v0) · Telegram [@haizakura](https://t.me/haizakura)