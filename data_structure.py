import time

class QUEUE:
    def __init__(self):
        self.queue = []
        self.id_counter = 1

    def Enqueue(self, name, people, vip, remarks):
        booking = {
        "id": self.id_counter,
        "name": name,
        "people": people,
        "vip": vip,
        "remarks": remarks,
        "time": time.time()
        }
        if vip:
            self.queue.insert(0, booking)  # Add VIP bookings to the front
        else:
            self.queue.append(booking)  # Add regular bookings to the back
        self.id_counter += 1




    def Dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        return None

    def Cancel(self, booking_id):
        for i, booking in enumerate(self.queue):
            if booking["id"] == booking_id:
                del self.queue[i]
                return True
        return False

    def Print_test(self):
        return self.queue
