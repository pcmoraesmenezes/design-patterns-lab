# Factory Design Pattern

Factory Method is a creational design pattern that lets us abstract-out the creation logic of specific class instances, so it provides a mechanism for creation of objects without exposing the instantiation logic to the client. 

It provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. It is used when the exact type of the object to be created is not known until runtime. The Factory Design Pattern is useful when you want to create objects without specifying the exact class of the object that will be created.

There are two main and crucial points in the Factory Method pattern:

1. Objects are created by calling a factory method, rather than by calling a constructor.

2. Objects are created through an abstraction not a concretion.

So, in the `Factory Method` pattern, we create objects without exposing the creation logic to the caller, and the caller refers to newly created object through a common interface.


It is also useful when you want to create objects that belong to a common superclass or interface, but the exact type of the object is not known until runtime. The Factory Design Pattern is often used in conjunction with other design patterns, such as the Singleton Pattern or the Abstract Factory Pattern.

Normally, we create objects using constructors. The question is: 
    
    Is this a good thing?

**No.** In fact this approach has some major architectural flaws:

- We have to know the exact class type of the object we want to create.

To understand why this is bad imagine the following scenario:

    Imagine if we wanted to create an app that used different types of shapes? Ones that we have not even created yet. How would we do that?

    We would have to create a new class for each shape we wanted to create. This would be a nightmare. We would have to modify the code every time we wanted to add a new shape. This is not good.


Let's look at other scenario:

1. Assume that you are creating a space-shooter game.

2. In this game you have different types of bullets that users could use.

    2.1 But, you do not know the exact type of bullet that the user will use.

    How to create them?

3. Additionally, you might in the future have new types of bullets that you want to add to the game.

```python

fb : FastBullet = FastBullet()
sb : SlowBullet = SlowBullet()
spb : SplashBullet = SplashBullet()

idk : IDontKnow = ?
```

In this case we have `idk` that ilustrates the problem. We do not know the exact type of bullet that we want to create.

The main problem with this approach is that our code is unnecessarily aware of the type of objects that it creates and thus it is strongly coupled with them.

If we make the Bullet an `abstract class` we can make it to be the parent class of all Bullets:

```python

class Bullet(ABC):
    pass


class FastBullet(Bullet):
    pass

class SlowBullet(Bullet):
    pass

class SplashBullet(Bullet):
    pass

```

This help us because now we can create Bullet instances based only on the `Bullet` interface/contract instead of the specific implementations. We then use the Factory Method design pattern as follows:

```python

class BulletFactory(ABC):
    @abstractmethod
    def create_bullet(self) -> Bullet:
        pass

class FastBulletFactory(BulletFactory):
    def create_bullet(self) -> Bullet:
        return FastBullet()

class SlowBulletFactory(BulletFactory):
    def create_bullet(self) -> Bullet:
        return SlowBullet()

class SplashBulletFactory(BulletFactory):
    def create_bullet(self) -> Bullet:
        return SplashBullet()
```

The great advantage is that the caller does not need to know how the factory creates the bullet. The caller only needs to know **HOW** to call the factory method with what initialization data.

We could even make this more generic, by using some type of `context data` to initialize the instance.

```python
class BulletFactory(ABC):
    @abstractmethod
    def create_bullet(self, context: dict) -> Bullet:
        pass

class FastBulletFactory(BulletFactory):
    def create_bullet(self, context: dict) -> Bullet:
        return FastBullet(context['speed'])


class SlowBulletFactory(BulletFactory):
    def create_bullet(self, context: dict) -> Bullet:
        return SlowBullet(context['speed'])


class SplashBulletFactory(BulletFactory):
    def create_bullet(self, context: dict) -> Bullet:
        return SplashBullet(context['speed'])
```

Other advantage is that we could cache objects in the factory for added performance. 

```python	

class BulletFactory(ABC):
    _cache = {}

    @abstractmethod
    def create_bullet(self, context: dict) -> Bullet:
        pass

class FastBulletFactory(BulletFactory):
    def create_bullet(self, context: dict) -> Bullet:
        if context['speed'] not in self._cache:
            self._cache[context['speed']] = FastBullet(context['speed'])
        return self._cache[context['speed']]

class SlowBulletFactory(BulletFactory):
    def create_bullet(self, context: dict) -> Bullet:
        if context['speed'] not in self._cache:
            self._cache[context['speed']] = SlowBullet(context['speed'])
        return self._cache[context['speed']]

class SplashBulletFactory(BulletFactory):
    def create_bullet(self, context: dict) -> Bullet:
        if context['speed'] not in self._cache:
            self._cache[context['speed']] = SplashBullet(context['speed'])
        return self._cache[context['speed']]
```


---

This pattern is often used with the following GoF patterns:

1. Strategy and Iterator design patterns are often used with Factory Method pattern to let collection subclasses return different types of iterators that are compatible with the collections.

2. `Factory Method` pattern can also be used in the `Object Pool` pattern when creating cached objects of different subtypes.

## When to use Factory Method pattern?

When a caller can't anticipate the types of objects it must create.

When you have many objects of a common type (like for example a `Shape` with subclasses such as `Circle`, `Square`, etc.) and you want to create them without exposing the creation logic to the caller.

When you want to create objects that belong to a common superclass or interface, but the exact type of the object is not known until runtime.

When you want to create objects that are expensive to create and you want to cache them for later use.

When you want to create objects that are complex and you want to simplify the creation process.

## Pros

- It allows sub-classes to choose the type of objects to create.

- Simple to implement and understand.

- Promotes loose-coupling by eliminating the need to bind application-specific classes into code. That means the code interacts only with the resultant interface or abstract class.

- Single Responsibility Principle. The Factory Method pattern follows the Single Responsibility Principle by allowing a class to delegate

- Open/Closed Principle. The Factory Method pattern follows the Open/Closed Principle by allowing a class to be open for extension but closed for modification. This means that a class can be extended without modifying the existing code. This allows for easier maintenance and updates to the system. It also allows for easier testing of the system.

## Cons

The greatest disadvantage of the Factory Method pattern is that it can expand the total number of classes in a system. Every concrete class also requires a concrete Createor class. Note: Parameterized Factory Method pattern can be used to reduce the number of classes in a system.


## Considerations

When you have many objects of a common type (for example `Shape`):

- Make all such object types (like for example `IShape`) follow the same interface or extend the same abstract class. This interface should declare methos that make sense in every `Shape`, but in a generalized way.

- Create a Factory with a static creation method which always returns the same common interface reference 
  (like for example `IShape`) but internally creates the specific object type (like for example `Circle`, `Square`, etc.) based on the input parameters.

- Let the Factory know wwhich instance you want, through some sort of a constant id for the specific object type. This can be accomplish through an enum or a list of constant which could be integers or strings.