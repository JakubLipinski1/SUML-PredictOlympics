import { TestBed } from '@angular/core/testing';

import { OlympicPredictService } from './olympic-predict.service';

describe('OlympicPredictService', () => {
  let service: OlympicPredictService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(OlympicPredictService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
