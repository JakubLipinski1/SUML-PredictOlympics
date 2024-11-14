import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/internal/Observable';
import { HttpClient } from '@angular/common/http';
import { Test } from 'src/Model/Test';

@Injectable({
  providedIn: 'root'
})
export class TestService {

  constructor(private http: HttpClient) { }

  getTasks(): Observable<Test[]> {
    return this.http.get<Test[]>('http://127.0.0.1:5000/elementy');
  }
  
}
