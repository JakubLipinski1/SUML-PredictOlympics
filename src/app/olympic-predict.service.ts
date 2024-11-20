import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/internal/Observable';
import { HttpClient } from '@angular/common/http';
import { Prediction } from 'src/Models/Prediction';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class OlympicPredictService {

  private predictionData = new BehaviorSubject<any>(null);
  predictionData$ = this.predictionData.asObservable(); 
  public isPredictionReleased = false;
  private isPredictionReleasedData = new BehaviorSubject<boolean>(false);
  isPredictionReleasedData$ = this.isPredictionReleasedData.asObservable();
  constructor(private http: HttpClient) { }

  setBooleanValue(value: boolean): void {
    this.isPredictionReleasedData.next(value);
  }

  getSports(): Observable<string[]> {
    return this.http.get<string[]>('https://jaklip3322-4bbe782f-f250-4f67-91e9-ac673bf58fdb.socketxp.com/sports');
  }

  getSportEvents(): Observable<string[]> {
    return this.http.get<string[]>('https://jaklip3322-4bbe782f-f250-4f67-91e9-ac673bf58fdb.socketxp.com/sport/events');
  }
  
  getOlympicPredict(event_name:string):Observable<Prediction[]>{

    this.isPredictionReleased = true;
    return this.http.get<Prediction[]>('https://jaklip3322-4bbe782f-f250-4f67-91e9-ac673bf58fdb.socketxp.com/predict?event_name='+event_name)
    
  }


  setPredictionData(data: any): void {
    this.predictionData.next(data); // Ustawienie nowych danych
  }

  getPredictionData(): any {
    return this.predictionData.getValue(); // Pobranie aktualnej wartości
  }
  
}
