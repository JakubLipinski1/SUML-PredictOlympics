import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Chart, ChartConfiguration, ChartType, registerables } from 'chart.js';
import { OlympicPredictService } from '../olympic-predict.service';

Chart.register(...registerables);
@Component({
  selector: 'app-prediction-chart',
  templateUrl: './prediction-chart.component.html',
  styleUrls: ['./prediction-chart.component.css']
})
export class PredictionChartComponent implements OnInit {
  constructor(public olympicPredictService: OlympicPredictService) {}

  sportName:string;

  ngOnInit(): void {

    this.olympicPredictService.isPredictionReleasedData$.subscribe(value => {
      console.log('Boolean value changed to:', value);
      // Wywołaj funkcję, gdy wartość zmieni się na `false`
      if (!value && this.chartInstance) {
        this.chartInstance.destroy()
      }
    });

    // Nasłuchiwanie na zmiany w danych predykcji
    this.olympicPredictService.predictionData$.subscribe(data => {
      if(this.chartInstance)
        {
          this.chartInstance.destroy()
        }
      if (data) {
        this.renderChart(data);
      }
    });
  }

  chartInstance: Chart | null = null; // Przechowywanie instancji wykresu

  renderChart(data: any[]): void {
    const labels: string[] = [];
    const goldData: number[] = [];
    const silverData: number[] = [];
    const bronzeData: number[] = [];
  
    // Zbierz wszystkie drużyny do "labels"
    data.forEach(medal => {
      medal.top_teams.forEach((team: any) => {
        if (!labels.includes(team.team)) {
          labels.push(team.team);
        }
      });
    });
  
    // Zainicjalizuj wartości zerowe dla wszystkich drużyn w każdej kategorii
    labels.forEach(() => {
      goldData.push(0);
      silverData.push(0);
      bronzeData.push(0);
    });
  
    // Wypełnij dane
    data.forEach(medal => {
      this.sportName = medal.event_name;
      medal.top_teams.forEach((team: any) => {
        const teamIndex = labels.indexOf(team.team);
        const probability = parseFloat(team.probability.replace('%', ''));
        if (medal.medal_type === 'gold') {
          goldData[teamIndex] = probability;
        } else if (medal.medal_type === 'silver') {
          silverData[teamIndex] = probability;
        } else if (medal.medal_type === 'bronze') {
          bronzeData[teamIndex] = probability;
        }
      });
    });
  
    const ctx = document.getElementById('medalChart') as HTMLCanvasElement;
  
    // Zniszcz poprzedni wykres, jeśli istnieje
    if (this.chartInstance) {
      this.chartInstance.destroy();
    }
  
    // Utwórz nowy wykres
    this.chartInstance = new Chart(ctx, {
      type: 'bar' as ChartType,
      data: {
        labels: labels,
        datasets: [
          {
            label: 'Gold',
            data: goldData,
            backgroundColor: 'rgba(255, 215, 0, 0.6)',
            borderColor: 'rgba(255, 215, 0, 1)',
            borderWidth: 1
          },
          {
            label: 'Silver',
            data: silverData,
            backgroundColor: 'rgba(192, 192, 192, 0.6)',
            borderColor: 'rgba(192, 192, 192, 1)',
            borderWidth: 1
          },
          {
            label: 'Bronze',
            data: bronzeData,
            backgroundColor: 'rgba(205, 127, 50, 0.6)',
            borderColor: 'rgba(205, 127, 50, 1)',
            borderWidth: 1
          }
        ]
      },
      options: {
        responsive: true,
        plugins: {
          legend: {
            position: 'top'
          },
          title: {
            display: true,
            text: 'Medal Prediction - '+this.sportName
          }
        },
        scales: {
          x: {
            title: {
              display: true,
              text: 'Countries'
            }
          },
          y: {
            beginAtZero: true,
            title: {
              display: true,
              text: 'Probability (%)'
            }
          }
        }
      }
    });
  }
}