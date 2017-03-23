#!/usr/bin/env python
# _*_ coding: utf-8 _*_

class Animal(object):
	def run(self):
		print('animal is running...')

class Dog(Animal):
	def run(self):
		print('dog is running...')

class Cat(Animal):
	def run(self):
		print('cat is running...')

def run_twice(animal):
	animal.run()
	animal.run()

a = Animal()
d = Dog()
c = Cat()

print('a is animal ?',isinstance(a,Animal))
print('a is Dog ?',isinstance(a,Dog))
print('a is Cat ?',isinstance(a,Cat))

print('d is animal ?',isinstance(d,Animal))
print('d is dog ?',isinstance(d,Dog))
print('d is cat ?',isinstance(d,Cat))

run_twice(c)