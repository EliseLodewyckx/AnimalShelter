export class Animal {
  animalType: AnimalType;
  sex: Sex;
  intact: boolean;
  age: number;
  // ...
}

export enum AnimalType {
  Cat,
  Dog
}

export enum Sex {
  Male,
  Female
}
