import { Component } from '@angular/core';
import { Http, Response } from '@angular/http';
import 'rxjs/add/operator/map';
import { UserService } from './services/user.service';
import { AnimalService } from './services/animal-shelter.service';
import { FeaturesAnimal } from './models/features-animal';


@Component({
  selector: 'app-root',
  styleUrls: ['./app.component.css'],
  template: `
  <h1>
    {{title}}
  </h1>

  <div>
    <button
    (click) = predict()> Make prediction </button>
  </div>

  <div *ngIf= predictionNotUndefined()>
    The prediction is:
    {{prediction}}
  </div>
`,
})
export class AppComponent {
  title = 'Animal Shelter';
  users;
  prediction: Number;
  featuresAnimal: FeaturesAnimal;

  constructor(private userService: UserService,
    private animalShelterService: AnimalService) {
    this.users = userService.getUsers();
    this.featuresAnimal = {
      feature1: 2,
      feature2: 1
    };
  }

  predict() {
    this.animalShelterService.makePrediction()
      .subscribe(response => {
        this.prediction = response.json();
        console.log('prediction ' + this.prediction);
      });

    console.log(this.prediction);
  }

  predictionNotUndefined() {
    return this.prediction !== undefined;
  }
}
