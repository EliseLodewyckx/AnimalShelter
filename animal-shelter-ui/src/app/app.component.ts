import { Component } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';

import { Animal, AnimalType, Sex } from './services/animal';
import { AnimalService } from './services/animal-shelter.service';
import { Prediction } from './services/prediction';
import { PredictionDialog } from './prediction-dialog/prediction-dialog.component';

@Component({
  selector: 'app-root',
  styleUrls: ['./app.component.scss'],
  templateUrl: 'app.component.html',
})
export class AppComponent {

  animal: Animal;
  loading: boolean;

  constructor(
    private animalService: AnimalService,
    private dialog: MatDialog) {
    this.animal = new Animal(AnimalType.Dog, Sex.Male, true, 5);
    this.loading = false;
  }

  predictFor(animal: Animal) {
    console.log(animal)
    this.loading = true;
    this.animalService
      .makePrediction(this.animal)
      .subscribe(
        prediction => this.processPrediction(prediction),
        error => this.handleError(error));
  }

  private processPrediction(prediction: Prediction) {
    console.log(prediction);
    this.loading = false;
    let dialogRef = this.dialog.open(PredictionDialog, {
      height: '200px',
      width: '250px',
      data: prediction
    })
    dialogRef.afterClosed().subscribe(result => result);
  }

  private handleError(error: any) {
    this.loading = false;
    console.error(error);
  }
}
