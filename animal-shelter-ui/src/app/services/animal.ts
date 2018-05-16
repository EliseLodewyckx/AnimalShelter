export class Animal {
  animalType: AnimalType;
  sex: Sex;
  intact: boolean;
  age: number;
  mix: boolean;
  // ...

  constructor(
    animalType: AnimalType,
    sex: Sex,
    intact: boolean,
    age: number,
    mix: boolean) {
      this.animalType = animalType;
      this.sex = sex;
      this.intact = intact;
      this.age = age;
      this.mix = mix;
  }
}

export enum AnimalType {
  Cat = 'Cat',
  Dog = 'Dog'
}

export enum Sex {
  Male = 'Male',
  Female = 'Female'
}
