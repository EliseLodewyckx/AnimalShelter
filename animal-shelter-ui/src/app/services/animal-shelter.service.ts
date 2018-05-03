import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import { Headers, RequestOptions } from '@angular/http';
import { Observable } from 'rxjs/Rx';


@Injectable()
export class AnimalService {
    private animalShelterUrl = 'http://localhost:5000/predict';
    constructor(private http: Http) { }

    makePrediction(): Observable<Response> {
        const headers = new Headers({ 'Content-Type': 'application/json' });
        const options = new RequestOptions({ headers: headers });
        const content = { feature1: 2, feature2: 2 };
        return this.http.post(this.animalShelterUrl, content, options);
    }
}
