from collections import deque


def detect_first_time_marker(doc):

    with open(doc) as f:
        datastream_buffer = list(f.read())
        queue = deque(datastream_buffer[:4], maxlen=4)
        counter = 4
        for letter in datastream_buffer[4:]:
            if len(queue) == len(set(queue)):
                return "".join(list(queue)), counter
            queue.append(letter)
            counter += 1


if __name__ == "__main__":

    doc = "./Day6_input.txt"

    marker, counter = detect_first_time_marker(doc)

    print(f"marker : {marker}")
    print(f"counter : {counter}")
