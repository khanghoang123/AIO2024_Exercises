import torch
import torch.nn as nn
from abc import ABC, abstractmethod


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        return x_exp/sum(torch.exp(x))


class softmax_stable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        c = torch.max(x)
        x_exp = torch.exp(x-c)
        return x_exp/sum(torch.exp(x-c))


class Person(ABC):
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(
            f'Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}')


class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(
            f'Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}')


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist

    def describe(self):
        print(
            f'Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}')


class Ward:
    def __init__(self, name):
        self.name = name
        self.list_person = list()

    def add_person(self, person: Person):
        self.list_person.append(person)

    def describe(self):
        print('Ward Name: ', self.name)
        for x in self.list_person:
            x.describe()

    def count_doctor(self):
        count = 0
        for x in self.list_person:
            if isinstance(x, Doctor):
                count += 1
        return count

    def sort_age(self):
        self.list_person.sort(key=lambda x: x.yob, reverse=True)

    def compute_average(self):
        total = 0
        count = 0
        for x in self.list_person:
            if isinstance(x, Teacher):
                total += x.yob
                count += 1
        return total/count

class StackOverflow(Exception):
    pass
class StackUnderflow(Exception):   
    pass
class MyStack:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__stack = []

    def is_empty(self):
        return len(self.__stack) == 0

    def is_full(self):
        return len(self.__stack) == self.__capacity

    def pop(self):
        if self.is_empty():
            raise StackUnderflow('Underflow')
        return self.__stack.pop()

    def push(self, value):
        if self.is_full():
            raise StackOverflow('Overflow')
        return self.__stack.append(value)

    def top(self):
        if self.is_empty():
            return 'Stack is empty'
        return self.__stack[-1]


class Queue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__queue = []

    def is_empty(self):
        return len(self.__queue) == 0

    def is_full(self):
        return len(self.__queue) == self.__capacity

    def enqueue(self, value):
        if self.is_full():
            raise StackOverflow('Overflow')
        self.__queue.append(value)

    def dequeue(self):
        if self.is_empty():
            raise StackUnderflow('Underflow')
        return self.__queue.pop(0)

    def front(self):
        if self.is_empty():
            return 'Queue is empty'
        return self.__queue[0]


if __name__ == '__main__':
    # Bai 1:
    data = torch.Tensor([1, 2, 3])
    softmax = Softmax()
    output = softmax(data)
    print(output)

    softmax_stable = softmax_stable()
    output = softmax_stable(data)
    print(output)

    # Bai 2:

    # a
    student1 = Student(name="studentA", yob=2010, grade="7")
    student1.describe()

    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    teacher1.describe()

    doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
    doctor1.describe()

    # b
    print()
    teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
    doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
    ward1 = Ward(name="Ward1")
    ward1.add_person(student1)
    ward1.add_person(teacher1)
    ward1.add_person(teacher2)
    ward1.add_person(doctor1)
    ward1.add_person(doctor2)
    ward1.describe()

    # c
    print(f'\nNumber of doctors: {ward1.count_doctor()}')

    # d
    print('\nAfter sorting Age of Ward1 people')
    ward1.sort_age()
    ward1.describe()

    # e
    print(f'\nAverage year of birth (teachers): {ward1.compute_average()}')

    # Bai 3:
    stack1 = MyStack(capacity=5)
    stack1.push(1)
    stack1.push(2)
    print(stack1.is_full())
    print(stack1.top())
    print(stack1.pop())
    print(stack1.top())
    print(stack1.pop())
    print(stack1.is_empty())

    # Bai 4:
    queue1 = Queue(capacity=5)
    queue1.enqueue(1)
    queue1.enqueue(2)
    print(queue1.is_full())
    print(queue1.front())
    print(queue1.dequeue())
    print(queue1.front())
    print(queue1.dequeue())
    print(queue1.is_empty())
