#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 11:23:59 2025

@author: home
"""

import random

class Animal:
    def __init__(self, animal_id):
        self.x = 1
        self.y = 1
        self.id = animal_id

    def move(self, p_min, p_max):
        pass

    def get_location(self):
        return (self.x, self.y)

class Cat(Animal):
    def __init__(self, animal_id):
        super().__init__(animal_id)
        self.strength = random.randint(1, 5)  # Cats have random strength

    def move(self, p_min, p_max):
        x_step = random.randint(-1, 1)
        new_x = self.x + x_step
        if p_min <= new_x <= p_max:
            self.x = new_x

        y_step = random.randint(-1, 1)
        new_y = self.y + y_step
        if p_min <= new_y <= p_max:
            self.y = new_y

    def __str__(self):
        return f"Cat(ID: {self.id}, Strength: {self.strength}, Location: {self.get_location()})"

class Dog(Animal):
    def __init__(self, animal_id):
        super().__init__(animal_id)
        self.strength = random.randint(3, 7)  # Dogs are generally stronger than Cats

    def fight(self, cat):
        print(f"Dog {self.id} (Strength: {self.strength}) fights Cat {cat.id} (Strength: {cat.strength})")
        if self.strength > cat.strength:
            print(f"Dog {self.id} wins and survives!")
            return self
        else:
            print(f"Dog {self.id} loses and turns into a Cat!")
            return Cat(self.id)  # Dog turns into a Cat with the same ID

    def __str__(self):
        return f"Dog(ID: {self.id}, Strength: {self.strength}, Location: {self.get_location()})"

# Simulation
def simulate_fight(dog_count=1, cat_count=1, grid_min=0, grid_max=10):
    dogs = [Dog(i) for i in range(dog_count)]
    cats = [Cat(i) for i in range(cat_count)]

    print("Initial Animals:")
    for dog in dogs:
        print(dog)
    for cat in cats:
        print(cat)

    # Simulate fights between Dogs and Cats
    for dog in dogs[:]:  # Iterate over a copy to allow modifications
        if cats:  # If there are Cats left to fight
            cat = random.choice(cats)
            result = dog.fight(cat)
            if isinstance(result, Cat):
                dogs.remove(dog)
                cats.append(result)
                print(f"New Cat added: {result}")
            cats.remove(cat)  # The Cat is defeated or wins
            
    print("\nRemaining Animals After Fights:")
    for dog in dogs:
        print(dog)
    for cat in cats:
        print(cat)

# Run the simulation
simulate_fight(dog_count=2, cat_count=3)