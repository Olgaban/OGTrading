import { Component, OnInit } from '@angular/core';
import { CurrenciesService } from '../services/currencies.service';

@Component({
  selector: 'app-output',
  templateUrl: './output.component.html',
  styleUrls: ['./output.component.css']
})
export class OutputComponent implements OnInit {

  constructor(public currService: CurrenciesService) { }

  ngOnInit(): void {
  }

}
