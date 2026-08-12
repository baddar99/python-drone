# drone-python

Small toy project to play around with a drone control setup, without needing an actual drone (or a broker/MQTT/certs to set up).

The controller and the drone run as two separate processes and talk over a couple of `multiprocessing.Queue`s — one for commands going out, one for acks coming back. `Drone` itself doesn't do anything real, it just prints what it would be doing (take off, move around, rotate, land, etc.), so you can use it to try out the command flow.

## Running it

```
python main.py
```

You'll see the drone process print each action as it runs, and the controller print the ack for each one it gets back.

## Layout

`commands.py` just has the command name strings so both sides agree on them. `drone.py` has the `Drone` class and the processor that runs in its process. `controller.py` fires off a hardcoded sequence of commands (take off, move up, a couple of rotations, land) and waits for the last ack. `main.py` wires the two together.

Started out as an MQTT-based thing (drone subscribed to a topic, controller published commands to it) but ripped that out in favor of just using multiprocessing directly — simpler to run and doesn't need a broker or certs lying around.
