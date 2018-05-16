import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

import { Animal } from './animal';
import { Prediction } from './prediction';

@Injectable()
export class AnimalService {

    constructor(private http: HttpClient) {}

    makePrediction(animal: Animal): Observable<Prediction> {
      return this.http.post<Prediction>('http://10.161.128.81:5000/predict', animal, { responseType: 'text' as 'json' });
    }
}
