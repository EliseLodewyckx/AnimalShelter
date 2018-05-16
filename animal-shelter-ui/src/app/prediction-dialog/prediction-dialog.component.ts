import { Component, Inject } from '@angular/core';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';

import { Prediction } from '../services/prediction';

@Component({
  selector: 'prediction-dialog',
  templateUrl: './prediction-dialog.component.html',
  styleUrls: ['./prediction-dialog.component.scss']
})
export class PredictionDialog {

  constructor(
    public dialogRef: MatDialogRef<PredictionDialog>,
    @Inject(MAT_DIALOG_DATA) public prediction: Prediction) { }

  mapToIcon(prediction) {
    return new Map<Prediction, string>([
      [Prediction.Adoption, 'accessibility_new'],
      [Prediction.Died, 'cloud_queue'],
      [Prediction.Euthanasia, 'trending_down'],
      [Prediction.ReturnToOwner, '360'],
      [Prediction.Transfer, 'directions_bus']]).get(prediction);
  }

  removeUnderscores(string: string) {
    return string.replace(/_/g,' ');
  }

  close() {
    this.dialogRef.close();
  }
}
