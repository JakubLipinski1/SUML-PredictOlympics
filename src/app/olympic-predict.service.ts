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

  constructor(private http: HttpClient) { }


  getSports(): Observable<string[]> {
    return this.http.get<string[]>('http://127.0.0.1:5000/sports');
  }

  getSportEvents(): Observable<string[]> {
    return this.http.get<string[]>('http://127.0.0.1:5000/sport/events');
  }
  
  getOlympicPredict(event_name:string):Observable<Prediction[]>{

    this.isPredictionReleased = true;
    return this.http.get<Prediction[]>('http://127.0.0.1:5000/predict?event_name='+event_name)
    
  }


  setPredictionData(data: any): void {
    this.predictionData.next(data); // Ustawienie nowych danych
  }

  getPredictionData(): any {
    return this.predictionData.getValue(); // Pobranie aktualnej wartości
  }
  
}
