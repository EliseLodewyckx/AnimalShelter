import { Component } from '@angular/core';

import { AnimalService } from './services/animal-shelter.service';
import { Animal } from './services/animal';

@Component({
  selector: 'app-root',
  styleUrls: ['./app.component.scss'],
  templateUrl: 'app.component.html',
})
export class AppComponent {

  animal: Animal;

  constructor(private animalService: AnimalService) {}

  predict() {
    this.animalService
      .makePrediction(this.animal)
      .subscribe(response => {
        // this.prediction = response;
        console.log('Prediction ' + response);
      });
  }
}
