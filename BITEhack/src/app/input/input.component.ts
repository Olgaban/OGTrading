import { Component, OnInit } from '@angular/core';
import { Form, NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { CurrenciesService } from '../services/currencies.service';

@Component({
  selector: 'app-input',
  templateUrl: './input.component.html',
  styleUrls: ['./input.component.css']
})
export class InputComponent implements OnInit {
  currencies: String[] = ["btc", 'eth', 'doge', 'huj']

  constructor(public currService: CurrenciesService,
    private router: Router) { }

  ngOnInit(): void {
    this.currService.getCurrencies().subscribe(
      (currs: string[]) => {
        this.currencies = currs;
      }
    )
  }

  onStartCurrencyChange(event: any) {
    let target = event.target;
    this.currService.startCurrency = target.value
  }

  onTargetCurrencyChange(event: any) {
    let target = event.target;
    this.currService.targetCurrency = target.value
  }

  onSubmit(form: NgForm) {
    if(! form.valid) { 
      return
    }
    // this.currService.sendCurrencies();
    this.router.navigate(["/sequence"]);
  }
}
