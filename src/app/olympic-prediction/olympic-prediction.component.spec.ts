import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OlympicPredictionComponent } from './olympic-prediction.component';

describe('OlympicPredictionComponent', () => {
  let component: OlympicPredictionComponent;
  let fixture: ComponentFixture<OlympicPredictionComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OlympicPredictionComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(OlympicPredictionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
