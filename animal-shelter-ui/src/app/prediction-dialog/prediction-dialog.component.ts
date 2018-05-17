import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';

import { TwoClassPrediction } from '../services/two-class-prediction';

@Component({
  selector: 'prediction-dialog',
  templateUrl: './prediction-dialog.component.html',
  styleUrls: ['./prediction-dialog.component.scss']
})
export class PredictionDialog {

  constructor(
    public dialogRef: MatDialogRef<PredictionDialog>,
    @Inject(MAT_DIALOG_DATA) public prediction: TwoClassPrediction) { }

  mapToIcon(prediction) {
    return new Map<TwoClassPrediction, string>([
      [TwoClassPrediction.Alive, 'accessibility_new'],
      [TwoClassPrediction.Dead, 'cloud_queue']])
      .get(prediction);
  }

  removeUnderscores(string: string) {
    return string.replace(/_/g,' ');
  }

  close() {
    this.dialogRef.close();
  }
}
