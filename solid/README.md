# SOLID Principles

## Single Responsibility Principle (SRP)

A class should have one, and only one, reason to change. This means that a class should only have one job or responsibility. If a class has more than one responsibility, it becomes coupled, and changes to one responsibility may affect the other responsibilities.

Let's take a look at an example:

```python

class TodoList:
    def __init__(self):
        self.todos = []

    def add_todo(self, todo):
        self.todos.append(todo)

    def remove_todo(self, todo):
        self.todos.remove(todo)

    def get_todos(self):
        return self.todos

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for todo in self.todos:
                f.write(f"{todo}\n")

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            self.todos = [line.strip() for line in f.readlines()]
```
In this example, the `TodoList` class has multiple responsibilities: managing the list of todos and saving/loading the list to/from a file. This violates the Single Responsibility Principle.

Also, this violates SRP, which states that a class should have only one reason to change. If we need to change the way we save or load todos, we would have to modify the `TodoList` class, which could lead to bugs in the todo management functionality.



To fix this, we can create a separate class for file operations:

```python

class TodoList:
    def __init__(self):
        self.todos = []

    def add_todo(self, todo):
        self.todos.append(todo)

    def remove_todo(self, todo):
        self.todos.remove(todo)

    def get_todos(self):
        return self.todos


class TodoFileManager:
    @staticmethod
    def save_to_file(todos, filename):
        with open(filename,
                    'w') as f:
                for todo in todos:
                    f.write(f"{todo}\n")

    @staticmethod
    def load_from_file(filename):
        with open(filename,
                    'r') as f:
                return [line.strip() for line in f.readlines()]
```

Now, the `TodoList` class is responsible only for managing the list of todos, while the `TodoFileManager` class is responsible for saving and loading the list to/from a file. This adheres to the Single Responsibility Principle.

## Open/Closed Principle (OCP)
The Open/Closed Principle states that software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. This means that we should be able to add new functionality to a class without changing its existing code.
This can be achieved through inheritance or interfaces. Let's take a look at an example:

```python

class AreaCalculator:
    def calculate_area(self, shape):
        if isinstance(shape, Circle):
            return 3.14 * shape.radius ** 2
        elif isinstance(shape, Rectangle):
            return shape.width * shape.height


class Circle:
    def __init__(self, radius):
        self.radius = radius


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


```

This code calculates the area of different shapes using conditional statements inside the `AreaCalculator` class. If we want to add a new shape, we would have to modify the `AreaCalculator` class, which violates the Open/Closed Principle.

To fix this, we can use polymorphism and interfaces:

```python

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class AreaCalculator:
    def calculate_area(self, shape):
        return shape.area()
```
In this example, we created a `Shape` interface with an `area` method. Each shape class (e.g., `Circle`, `Rectangle`) implements the `area` method. The `AreaCalculator` class can now calculate the area of any shape without needing to modify its code. This adheres to the Open/Closed Principle.


## Liskov Substitution Principle (LSP)

The Liskov Substitution Principle states that objects of a superclass should be replaceable with objects of a subclass without affecting the correctness of the program. This means that if a class is a subclass of another class, it should be able to be used in place of the superclass without causing any issues.

Let's take a look at an example:

```python

class Bird:
    def fly(self):
        print("I can fly!")

class Penguin(Bird):
    def fly(self):
        print("I can't fly!")
```

In this example, the `Penguin` class is a subclass of the `Bird` class. However, it violates the Liskov Substitution Principle because it cannot fly. If we try to use a `Penguin` object in place of a `Bird` object, it will not behave as expected. Plus the `fly` method in the `Penguin` class is overriding the `fly` method in the `Bird` class, but it is not providing the same functionality. This violates the Liskov Substitution Principle.

This generates inconsistency in the code, as we expect all birds to be able to fly.

To fix this, we can create a separate interface for flying birds:

```python

from abc import ABC, abstractmethod
class Bird(ABC):
    @abstractmethod
    def fly(self):
        pass

class FlyingBird(Bird):
    def fly(self):
        print("I can fly!")


class NonFlyingBird(Bird):
    def fly(self):
        print("I can't fly!")

class Penguin(Bird):
    pass

```

In this example, we created a `Bird` interface with a `fly` method. The `FlyingBird` class implements the `fly` method, while the `NonFlyingBird` class does not. The `Penguin` class is now a subclass of the `Bird` class but does not implement the `fly` method. This adheres to the Liskov Substitution Principle because we can now use any bird object in place of a `Bird` object without causing any issues.

## Interface Segregation Principle (ISP)
The Interface Segregation Principle states that no client should be forced to depend on methods it does not use. This means that we should create small, specific interfaces rather than large, general-purpose interfaces. This allows clients to only implement the methods they need.

Let's take a look at an example:

```python

class IMultiFunctionalDevice:
    def print(self):
        pass

    def scan(self):
        pass

    def fax(self):
        pass
    
    def copy(self):
        pass


class Printer(IMultiFunctionalDevice):
    def print(self):
        print("Printing...")

class Scanner(IMultiFunctionalDevice):
    def scan(self):
        print("Scanning...")

class FaxMachine(IMultiFunctionalDevice):
    def fax(self):
        print("Faxing...")
```

In this example, we have a large interface `IMultiFunctionalDevice` that has multiple methods. The `Printer`, `Scanner`, and `FaxMachine` classes implement this interface, but they only need to implement the methods they use. This violates the Interface Segregation Principle because the classes are forced to implement methods they do not use.
To fix this, we can create smaller, more specific interfaces:

```python

from abc import ABC, abstractmethod
class IPrinter(ABC):
    @abstractmethod
    def print(self):
        pass

class IScanner(ABC):
    @abstractmethod
    def scan(self):
        pass

class IFaxMachine(ABC):
    @abstractmethod
    def fax(self):
        pass

class Printer(IPrinter):
    def print(self):
        print("Printing...")

class Scanner(IScanner):
    def scan(self):
        print("Scanning...")

class FaxMachine(IFaxMachine):
    def fax(self):
        print("Faxing...")
```
In this example, we created smaller interfaces for each functionality. The `Printer`, `Scanner`, and `FaxMachine` classes now implement only the interfaces they need. This adheres to the Interface Segregation Principle because the classes are not forced to implement methods they do not use.

## Dependency Inversion Principle (DIP)

The Dependency Inversion Principle states that high-level modules should not depend on low-level modules. Both should depend on abstractions. This means that we should depend on interfaces rather than concrete implementations. This allows us to change the implementation without affecting the high-level module.

Let's take a look at an example:

```python

class EmailService:
    def send_email(self, message):
        print(f"Sending email: {message}")

class SmsService:
    def send_sms(self, message):
        print(f"Sending SMS: {message}")

class NotificationService:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SmsService()

    def send_notification(self, message, receiver, method):
        if method == "email":
            self.email_service.send_email(message)
        elif method == "sms":
            self.sms_service.send_sms(message)

```

In the initial code, the `NotificationService` class depends on the concrete implementations of `EmailService` and `SmsService`. This violates the Dependency Inversion Principle because if we want to change the implementation of the email or SMS service, we would have to modify the `NotificationService` class.

Both should depend on abstractions. This allows us to change the implementation without affecting the high-level module. A direct dependency on concatre classes makes the `NotificationService` less flexible and harder to change or extend. For example, if we want to add a new notification method (e.g., push notifications), we would have to modify the `NotificationService` class, which could lead to bugs in the existing code.


To fix this, we can create an interface for the notification service:

```python

from abc import ABC, abstractmethod

class IMessageService(ABC):
    @abstractmethod
    def send(self, message, receiver):
        pass

    
class EmailService(IMessageService):
    def send(self, message, receiver):
        print(f"Sending email to {receiver}: {message}")

    
class SmsService(IMessageService):
    def send(self, message, receiver):
        print(f"Sending SMS to {receiver}: {message}")


class NotificationService:
    def __init__(self, message_service: IMessageService):
        self.message_service = message_service

    def send_notification(self, message, receiver):
        self.message_service.send(message, receiver)

    
```