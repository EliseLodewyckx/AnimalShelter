import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { MatSelectModule } from '@angular/material/select';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { MatSliderModule } from '@angular/material/slider';
import { MatButtonModule } from '@angular/material/button';
import { MatProgressBarModule } from '@angular/material/progress-bar';
import { MatDialogModule } from '@angular/material/dialog';

import { AppComponent } from './app.component';
import { AnimalService } from './services/animal-shelter.service';
import { PredictionDialog } from './prediction-dialog/prediction-dialog.component';

@NgModule({
  declarations: [
    AppComponent,
    PredictionDialog
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    HttpClientModule,
    FormsModule,
    MatSelectModule,
    MatCheckboxModule,
    MatSliderModule,
    MatButtonModule,
    MatProgressBarModule,
    MatDialogModule
  ],
  entryComponents: [
    PredictionDialog
  ],
  providers: [AnimalService],
  bootstrap: [AppComponent]
})
export class AppModule { }
