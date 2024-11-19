import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { TestGetComponent } from './test-get/test-get.component';
import { FormsModule } from '@angular/forms';
import {HttpClientModule} from '@angular/common/http';
import { OlympicPredictionComponent } from './olympic-prediction/olympic-prediction.component';
import { PredictionChartComponent } from './prediction-chart/prediction-chart.component';

@NgModule({
  declarations: [
    AppComponent,
    TestGetComponent,
    OlympicPredictionComponent,
    PredictionChartComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
