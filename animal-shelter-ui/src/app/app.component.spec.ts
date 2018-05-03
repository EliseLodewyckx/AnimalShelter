import { TestBed, async } from '@angular/core/testing';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/observable/of';
import { Response, ResponseOptions } from '@angular/http';
import { AppComponent } from './app.component';

let component: AppComponent;
let animalService;

describe('AppComponent', () => {
  beforeEach(async(() => {
    animalService = jasmine.createSpyObj('AnimalService', ['makePrediction']);
    component = new AppComponent(animalService);
  }));

  it(`.predict should call AnimalService`, async(() => {
    const options = new ResponseOptions({
      body: '{"name":"Jeff"}'
    });
    const res = new Response(options);
    animalService.makePrediction.and.returnValue(Observable.of(res));
    component.predict();
    expect(animalService.makePrediction).toHaveBeenCalled();
  }));

  it('.predictionNotUndefined should return false when prediction undefined', async(() => {
    component.prediction = undefined;
    expect(component.predictionNotUndefined()).toBe(false);
  }));

  it('.predictionNotUndefined should return true when prediction not undefined', async(() => {
    component.prediction = 5;
    expect(component.predictionNotUndefined()).toBe(true);
  }));
});
