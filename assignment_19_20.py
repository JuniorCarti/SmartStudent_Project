#Assignment a) HealthProfile Class (Single Responsibility Principle)

class HealthProfile:
    def __init__(self, name, age, weight_kg, height_cm, gender, activity_level):
        self.name = name
        self.age = age
        self.weight_kg = weight_kg
        self.height_cm = height_cm
        self.gender = gender.lower()
        self.activity_level = activity_level.lower()
    
    def get_bmi(self):
        """Calculate Body Mass Index"""
        height_m = self.height_cm / 100
        return round(self.weight_kg / (height_m ** 2), 2)
    
    def get_bmr(self):
        """Calculate Basal Metabolic Rate using Mifflin-St Jeor Equation"""
        if self.gender == 'male':
            bmr = 10 * self.weight_kg + 6.25 * self.height_cm - 5 * self.age + 5
        else:  # female
            bmr = 10 * self.weight_kg + 6.25 * self.height_cm - 5 * self.age - 161
        return round(bmr)
    
    def __str__(self):
        return f"{self.name} ({self.age}y, {self.gender}): {self.weight_kg}kg, {self.height_cm}cm"

# Example usage
profile = HealthProfile("Alice", 30, 65, 170, "female", "moderate")
print(f"BMI: {profile.get_bmi()}")
print(f"BMR: {profile.get_bmr()} calories/day")



#The HealthProfile class adheres to SRP 
# by focusing solely on storing health data and calculating basic metrics. 
# It doesn't handle workout routines, calorie calculations for specific activities, 
# or dietary planning. This separation allows the class to have a single reason to change - 
# modifications to health metric formulas or data storage. 
# Other classes can depend on HealthProfile for raw data while implementing their own specialized logic. 
# For example, a WorkoutPlanner class could use HealthProfile's BMR to calculate calorie needs, 
# and a NutritionCalculator could use the same data for meal planning. 
# This design prevents the HealthProfile from becoming a "god object" 
# and makes the system more maintainable. Changes to workout logic won't affect health metrics, and vice versa.



#Assignment b) Extendable CalorieCalculator (Open/Closed Principle)

from abc import ABC, abstractmethod

class CalorieCalculator(ABC):
    @abstractmethod
    def calculate(self, minutes):
        pass

class Walking(CalorieCalculator):
    def calculate(self, minutes):
        return round(minutes * 4.5)  # 4.5 calories per minute

class Running(CalorieCalculator):
    def calculate(self, minutes):
        return round(minutes * 10.0)  # 10 calories per minute

class Swimming(CalorieCalculator):
    def calculate(self, minutes):
        return round(minutes * 7.0)  # 7 calories per minute

class Cycling(CalorieCalculator):
    def calculate(self, minutes):
        return round(minutes * 8.0)  # 8 calories per minute

class ActivityPlanner:
    def __init__(self):
        self.activities = {
            'walking': Walking(),
            'running': Running(),
            'swimming': Swimming(),
            'cycling': Cycling()
        }
    
    def calculate_total_calories(self, activity_minutes):
        total = 0
        for activity, minutes in activity_minutes.items():
            if activity in self.activities:
                total += self.activities[activity].calculate(minutes)
        return total

# Example usage
planner = ActivityPlanner()
workout = {'walking': 30, 'running': 20}
print(f"Total calories: {planner.calculate_total_calories(workout)}")


#The CalorieCalculator system follows OCP by using abstraction and inheritance. The base abstract class defines the interface, and concrete implementations handle specific calculations. To add new activities like "Dancing" or "Yoga", I simply create new subclasses without modifying existing code. The ActivityPlanner uses polymorphism - it works with any CalorieCalculator subclass through the common interface. This design is closed for modification (existing classes don't change) but open for extension (new activities can be added). The system doesn't need switch statements or if-else chains to handle different activity types. Each activity encapsulates its own calculation logic, making the system more maintainable and testable. New features can be added by extending rather than modifying, reducing the risk of introducing bugs in existing functionality.


#Assignment c) Workout Devices Simulation (LSP & ISP)

from abc import ABC, abstractmethod

class WorkoutDevice(ABC):
    @abstractmethod
    def start_tracking(self):
        pass
    
    @abstractmethod
    def stop_tracking(self):
        pass
    
    @abstractmethod
    def get_data(self):
        pass

class SmartWatch(WorkoutDevice):
    def start_tracking(self):
        print("SmartWatch: Tracking started")
        return True
    
    def stop_tracking(self):
        print("SmartWatch: Tracking stopped")
        return {"time": 3600, "steps": 5000, "distance": 4.2, "heart_rate": 120}
    
    def get_data(self):
        return self.stop_tracking()

class SmartShoe(WorkoutDevice):
    def start_tracking(self):
        print("SmartShoe: Tracking started")
        return True
    
    def stop_tracking(self):
        print("SmartShoe: Tracking stopped")
        return {"time": 3600, "steps": 8000, "distance": 6.5}
    
    def get_data(self):
        return self.stop_tracking()

class HeartRateBand(WorkoutDevice):
    def start_tracking(self):
        print("HeartRateBand: Tracking started")
        return True
    
    def stop_tracking(self):
        print("HeartRateBand: Tracking stopped")
        return {"time": 3600, "heart_rate": 135, "calories": 420}
    
    def get_data(self):
        data = self.stop_tracking()
        data.setdefault('steps', 0)  # Graceful degradation
        data.setdefault('distance', 0)
        return data

def test_devices():
    devices = [SmartWatch(), SmartShoe(), HeartRateBand()]
    
    for device in devices:
        print(f"\nTesting {device.__class__.__name__}:")
        device.start_tracking()
        data = device.get_data()
        print(f"Data: {data}")

test_devices()

#The design follows Liskov Substitution Principle by ensuring all device subclasses can replace the base WorkoutDevice without breaking functionality. Each implements the complete interface while providing sensible defaults for missing features (like HeartRateBand returning 0 for steps). Interface Segregation is achieved by keeping the interface minimal - only essential methods for tracking. If devices had vastly different capabilities, I might create smaller interfaces like StepTracker and HeartRateMonitor, but the current design balances simplicity with functionality. Devices gracefully handle missing data through default values rather than raising errors, maintaining substitutability. This allows the system to work with any workout device that implements the core tracking methods, whether it's a simple pedometer or advanced smartwatch. The design avoids forcing devices to implement unused methods while ensuring they can all be used interchangeably in the fitness application.


#Assignment d) Fitness Tracker with Dependency Inversion

import datetime
from abc import ABC, abstractmethod
import json
import csv

class Workout(ABC):
    @abstractmethod
    def __init__(self, start, end, calories=None):
        self.start = start
        self.end = end
        self.calories = calories
    
    def get_duration(self):
        return self.end - self.start
    
    @abstractmethod
    def get_calories(self):
        pass
    
    def __eq__(self, other):
        return (self.get_duration() == other.get_duration() and 
                self.kind == other.kind)

class RunningWorkout(Workout):
    def __init__(self, start, end, distance_km=None, calories=None):
        super().__init__(start, end, calories)
        self.distance = distance_km
        self.icon = '🏃‍♂️'
        self.kind = 'Running'
    
    def get_calories(self):
        if self.calories:
            return self.calories
        # Estimate: 60 calories per km
        return self.distance * 60 if self.distance else 0

class BikeWorkout(Workout):
    def __init__(self, start, end, distance_km=None, calories=None):
        super().__init__(start, end, calories)
        self.distance = distance_km
        self.icon = '🚴🏽‍♂️'
        self.kind = 'Cycling'
    
    def get_calories(self):
        if self.calories:
            return self.calories
        return self.get_duration().total_seconds() / 3600 * 300

class WorkoutPlanner:
    def __init__(self, workout_types):
        self.workout_types = workout_types
    
    def create_workout(self):
        print("Available workout types:")
        for i, (name, cls) in enumerate(self.workout_types.items(), 1):
            print(f"{i}. {name}")
        
        choice = int(input("Choose workout type: ")) - 1
        workout_name = list(self.workout_types.keys())[choice]
        workout_class = self.workout_types[workout_name]
        
        start = input("Start time (YYYY-MM-DD HH:MM): ")
        end = input("End time (YYYY-MM-DD HH:MM): ")
        distance = input("Distance (km, optional): ")
        
        start_dt = datetime.datetime.strptime(start, "%Y-%m-%d %H:%M")
        end_dt = datetime.datetime.strptime(end, "%Y-%m-%d %H:%M")
        
        if distance:
            workout = workout_class(start_dt, end_dt, float(distance))
        else:
            workout = workout_class(start_dt, end_dt)
        
        return workout

def save_to_json(workouts, filename):
    data = []
    for workout in workouts:
        data.append({
            'kind': workout.kind,
            'start': workout.start.isoformat(),
            'end': workout.end.isoformat(),
            'duration': workout.get_duration().total_seconds(),
            'calories': workout.get_calories()
        })
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

# Example usage
if __name__ == "__main__":
    workout_types = {
        'Running': RunningWorkout,
        'Cycling': BikeWorkout
    }
    
    planner = WorkoutPlanner(workout_types)
    workouts = []
    
    while True:
        workout = planner.create_workout()
        workouts.append(workout)
        
        print(f"\nWorkout created: {workout.icon} {workout.kind}")
        print(f"Duration: {workout.get_duration()}")
        print(f"Calories: {workout.get_calories():.0f}")
        
        cont = input("\nCreate another workout? (y/n): ")
        if cont.lower() != 'y':
            break
    
    save_to_json(workouts, 'workouts.json')
    print("Workouts saved to workouts.json")

#The system follows Dependency Inversion Principle by depending on abstractions rather than concretions. WorkoutPlanner doesn't depend on specific workout classes but on the abstract Workout interface and a dictionary of available types. This allows adding new workout types without modifying the planner. The save_to_json function also depends on the abstract interface, not concrete classes. This decoupling makes the system extensible - new workout types can be added by registering them in the workout_types dictionary. The planner remains unchanged, demonstrating that high-level modules don't depend on low-level modules but both depend on abstractions. This design facilitates testing and maintenance.
