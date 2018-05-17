import { Component } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';

import { Animal, AnimalType, Sex } from './services/animal';
import { AnimalService } from './services/animal-shelter.service';
import { TwoClassPrediction } from './services/two-class-prediction';
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
    this.animal = new Animal(AnimalType.Dog, Sex.Male, true, 5, false);
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

  private processPrediction(prediction: TwoClassPrediction) {
    console.log(prediction);
    console.log(this.mapResultToNewLabel(prediction))
    this.loading = false;
    let dialogRef = this.dialog.open(PredictionDialog, {
      width: '400px',
      data: this.mapResultToNewLabel(prediction)
    })
    dialogRef.afterClosed()
      .subscribe(result => result);
  }

  private handleError(error: any) {
    this.loading = false;
    console.error(error);
  }

  private mapResultToNewLabel(result) {
    if (result === "Alive") {
      return "No attention needed"
    } else {
      return "Extra attention required"
    }
  }
}
