import multiprocessing

from drone import Drone, DroneCommandProcessor
from controller import run_flight_sequence


def run_drone_process(command_queue, response_queue):
    drone = Drone("drone01")
    processor = DroneCommandProcessor(drone, command_queue, response_queue)
    processor.run()


if __name__ == "__main__":
    command_queue = multiprocessing.Queue()
    response_queue = multiprocessing.Queue()

    drone_process = multiprocessing.Process(
        target=run_drone_process,
        args=(command_queue, response_queue))
    drone_process.start()

    run_flight_sequence(command_queue, response_queue)

    command_queue.put(None)
    drone_process.join()
