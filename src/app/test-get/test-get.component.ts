import { Component, OnInit } from '@angular/core';
import { TestService } from '../test.service';
import { Test } from 'src/Model/Test';

@Component({
  selector: 'app-test-get',
  templateUrl: './test-get.component.html',
  styleUrls: ['./test-get.component.css']
})
export class TestGetComponent implements OnInit {

  constructor(private testService: TestService) { }


  ngOnInit(): void {
  }


  
  testSendGet(){
    this.testService.getTasks().subscribe(test => {
      console.log(test)
    })
  }
}
