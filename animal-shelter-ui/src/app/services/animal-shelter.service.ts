import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

import { Animal } from './animal';
import { TwoClassPrediction } from './two-class-prediction';

@Injectable()
export class AnimalService {

    constructor(private http: HttpClient) {}

    makePrediction(animal: Animal): Observable<TwoClassPrediction> {
      return this.http.post<TwoClassPrediction>('http://localhost:5000/predict', animal, { responseType: 'text' as 'json' });
    }
}
