import { Component, OnInit, Inject } from '@angular/core';
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
    @Inject(MAT_DIALOG_DATA) public prediction: Prediction) {}

  onNoClick(): void {
    this.dialogRef.close();
  }
}
