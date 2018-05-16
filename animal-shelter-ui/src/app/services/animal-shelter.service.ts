import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Headers, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs';
import { Prediction } from './prediction';
import { Animal } from './animal';


@Injectable()
export class AnimalService {

    constructor(private http: HttpClient) {}

    makePrediction(animal: Animal): Observable<Prediction> {
        return this.http.post<Prediction>('http://10.161.128.81:5000/predict', animal);
    }
}
