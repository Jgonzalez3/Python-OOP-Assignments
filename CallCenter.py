# pylint: disable=print-statement

import time, datetime

class Call(object):
    def __init__(self, unique_id, caller_name, caller_phone, reason_for_call):
        self.unique_id = unique_id
        self.caller_name = caller_name
        self.caller_phone = caller_phone
        self.time_of_call = datetime.datetime.now().strftime("%Y/%m/%d %I:%m:%S %p")
        self.reason_for_call = reason_for_call
    def Display(self):
        print "ID:", self.unique_id
        print "Caller:", self.caller_name
        print "Phone:", self.caller_phone
        print "Time of Call:", self.time_of_call
        print "Reason:", self.reason_for_call
        return self

class CallCenter(object):
    def __init__(self, calls):
        self.calls = calls
        print self.calls
        self.queue_size = len(calls)
    def Add(self, caller):
        self.caller = caller
        self.calls.append(caller)
        self.queue_size += 1
        print "Caller", caller
        return self
    def Remove(self):
        self.calls.remove(self.calls[0])
        self.queue_size -= 1
        return self
    def RemoveByPhone(self, caller_phone):
        for i in range(0, self.queue_size):
            if self.calls[i].caller_phone == caller_phone:
                call = i
                break
        self.calls.remove(self.calls[call])
        self.queue_size -= 1
    # def Sort(self):
    #     self.calls.sort()
    def Info(self):
        print "Queue Size", self.queue_size
        for caller in range(0,len(self.calls)):
            print caller
            print self.calls[caller].caller_name
            print self.calls[caller].caller_phone
            print self.calls[caller].time_of_call
        return self

call1 = Call(1, "John", "222-222-2222", "card not working")
call2 = Call(2, "Michael", "333-333-3333", "home mortgage")
call3 = Call(3, "John", "444-444-4444", "fraud")
call4 = Call(4, "Lu", "555-555-5555", "account balance")

boa = CallCenter([])
print "CallCenter Current", boa.Info()
print "CallCenter", boa.Add(call1).Add(call2).Add(call3).Add(call4).Remove().Info()
