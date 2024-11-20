import { Component, OnInit } from '@angular/core';
import { OlympicPredictService } from '../olympic-predict.service';
import { Prediction } from 'src/Models/Prediction';

@Component({
  selector: 'app-olympic-prediction',
  templateUrl: './olympic-prediction.component.html',
  styleUrls: ['./olympic-prediction.component.css']
})
export class OlympicPredictionComponent implements OnInit {


  sportsNames:string[];
  eventsMap = new Map<string, string[]>();

  choosedSportName:string;
  choosedEventSportName:string

  predictResult:Prediction[];
  constructor(public olympicPredictService: OlympicPredictService) { }


  ngOnInit(): void {
    this.getSports()
    this.getSportEvents()
  }


  getSports(){
    this.olympicPredictService.getSports().subscribe(sports => {
      console.log(sports)
      this.sportsNames = sports;
      return sports;
    })
  }


  getSportEvents():string[]{
    let eventsTmp:string[] = [];
    this.olympicPredictService.getSportEvents().subscribe(events => {
      eventsTmp = events;
      console.log(eventsTmp)
      this.assetSportEvents(eventsTmp)
      return eventsTmp;
    })
    return eventsTmp;

  }

  getMedalPrediction(event_name:string)
  {
    this.olympicPredictService.getOlympicPredict(event_name).subscribe(prediction => {
      this.predictResult = prediction;
      console.log(prediction)
      this.olympicPredictService.setPredictionData(prediction);
    })
  }

  


  assetSportEvents(events: string[]) {
  
    for (let i = 0; i < events.length; i++) {
      const sport = events[i].split(" ")[0]; // Nazwa sportu (pierwszy element w nazwie wydarzenia)
      
      // Jeśli sport nie istnieje w mapie, inicjalizuj pustą tablicę
      if (!this.eventsMap.has(sport)) {
        this.eventsMap.set(sport, []);
      }
  
      // Dodaj wydarzenie do odpowiedniej tablicy
      this.eventsMap.get(sport)?.push(events[i]);
    }
  
    console.log(this.eventsMap);
    console.log(this.eventsMap.keys)
  }
  
  predictionClear()
  {
    this.choosedSportName = '';
    this.choosedEventSportName = '';
    this.predictResult = [];
    this.olympicPredictService.isPredictionReleased = false;
      this.olympicPredictService.setBooleanValue(this.olympicPredictService.isPredictionReleased);
      console.log('Boolean value set to:',this.olympicPredictService.isPredictionReleased);
  }

}
